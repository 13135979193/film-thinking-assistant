#!/usr/bin/env python3
"""Portable manifest integrity checks; never a substitute for visual review."""
import argparse
import csv
import io
import json
from pathlib import Path
import struct
import sys
import zipfile

STATES = {'pending', 'generated', 'needs_revision', 'checked', 'user_approved', 'excluded', 'failed'}
FINAL = {'checked', 'user_approved'}


def dimensions(path):
    with path.open('rb') as handle:
        header = handle.read(24)
        if header[:8] == b'\x89PNG\r\n\x1a\n' and header[12:16] == b'IHDR':
            return struct.unpack('>II', header[16:24])
        if header[:2] != b'\xff\xd8':
            raise ValueError('只支持真实PNG/JPEG，请另用图片库验证其他格式')
        handle.seek(2)
        while True:
            prefix = handle.read(1)
            if not prefix:
                break
            if prefix != b'\xff':
                continue
            marker = handle.read(1)
            while marker == b'\xff':
                marker = handle.read(1)
            if not marker or marker in (b'\xd9', b'\xda'):
                break
            if marker[0] in (0x01, *range(0xD0, 0xD9)):
                continue
            length = struct.unpack('>H', handle.read(2))[0]
            if length < 2:
                raise ValueError('JPEG段长度错误')
            if marker[0] in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
                _, height, width = struct.unpack('>BHH', handle.read(5))
                return width, height
            handle.seek(length - 2, 1)
    raise ValueError('缺少有效图片尺寸')


def load_manifest(path):
    data = json.loads(path.read_text(encoding='utf-8'))
    if not isinstance(data, dict) or not isinstance(data.get('assets'), list):
        raise ValueError('清单必须包含assets数组')
    return data


def check(path, require_final=False):
    data = load_manifest(path)
    errors, rows, seen = [], [], set()
    if not data['assets']:
        errors.append('资产清单为空，尚未完成拆解')
    for number, item in enumerate(data['assets'], 1):
        if not isinstance(item, dict):
            errors.append(f'第{number}项不是对象')
            continue
        ident = item.get('image_id')
        if not isinstance(ident, str) or not ident.strip() or any(c not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_' for c in ident):
            errors.append(f'第{number}项image_id仅可使用字母数字连字符下划线')
            continue
        if ident in seen:
            errors.append(f'{ident}: 重复图片编号')
        seen.add(ident)
        for key in ('source_id', 'category', 'source'):
            if not isinstance(item.get(key), str) or not item[key].strip():
                errors.append(f'{ident}: 缺少{key}')
        status = item.get('status')
        if status not in STATES:
            errors.append(f'{ident}: 未知状态')
        if status == 'excluded':
            continue
        if require_final and status not in FINAL:
            errors.append(f'{ident}: 尚未检查通过({status})')
        if status in FINAL and not str(item.get('review', '')).strip():
            errors.append(f'{ident}: 缺少人工检查记录review')
        if status not in {'generated', *FINAL}:
            continue
        resolved = {}
        for key in ('image_path', 'prompt_path'):
            value = item.get(key)
            if not isinstance(value, str) or not value:
                errors.append(f'{ident}: 缺少{key}')
                continue
            target = (path.parent / value).resolve()
            # Only package files from this project, never arbitrary host files.
            if not target.is_relative_to(path.parent.resolve()) or not target.is_file() or target.stat().st_size == 0:
                errors.append(f'{ident}: 文件缺失、为空或位于项目外: {key}')
                continue
            resolved[key] = target
        if 'image_path' in resolved:
            try:
                width, height = dimensions(resolved['image_path'])
                if width <= 0 or height <= 0:
                    raise ValueError('尺寸必须为正数')
            except (ValueError, OSError, struct.error) as exc:
                errors.append(f'{ident}: {exc}')
        rows.append((item, resolved))
    return data, rows, errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    subs = parser.add_subparsers(dest='command', required=True)
    init = subs.add_parser('init')
    init.add_argument('directory', type=Path)
    for name in ('audit', 'package'):
        command = subs.add_parser(name)
        command.add_argument('manifest', type=Path)
        if name == 'package':
            command.add_argument('output', type=Path)
    args = parser.parse_args()
    if args.command == 'init':
        args.directory.mkdir(parents=True, exist_ok=True)
        path = args.directory / 'manifest.json'
        if path.exists():
            parser.error('清单已存在，不覆盖')
        for directory in ('images', 'prompts'):
            (args.directory / directory).mkdir(exist_ok=True)
        path.write_text(json.dumps({'schema_version': 1, 'project': args.directory.name, 'design_baseline': {}, 'assets': []}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        print(path)
        return 0
    data, rows, errors = check(args.manifest, args.command == 'package')
    if errors:
        for message in errors:
            print(message, file=sys.stderr)
        return 1
    if args.command == 'audit':
        print(f'结构检查通过：{len(data["assets"])}项；审美和完整解码需另行检查')
        return 0
    if args.output.exists():
        parser.error('输出已存在，不覆盖')
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fields = ['image_id', 'source_id', 'category', 'source', 'status', 'image_path', 'prompt_path', 'review']
    sheet = io.StringIO(newline='')
    writer = csv.DictWriter(sheet, fields, extrasaction='ignore')
    writer.writeheader()
    packaged = json.loads(json.dumps(data))
    by_id = {item['image_id']: item for item in packaged['assets']}
    with zipfile.ZipFile(args.output, 'x', compression=zipfile.ZIP_DEFLATED) as archive:
        for item, paths in rows:
            target = by_id[item['image_id']]
            for key, folder in (('image_path', 'images'), ('prompt_path', 'prompts')):
                suffix = paths[key].suffix.lower() if key == 'image_path' else '.txt'
                relative = f'{folder}/{item["image_id"]}{suffix}'
                archive.write(paths[key], relative)
                target[key] = relative
            writer.writerow(target)
        archive.writestr('manifest.json', json.dumps(packaged, ensure_ascii=False, indent=2))
        archive.writestr('assets.csv', '\ufeff' + sheet.getvalue())
    print(f'已打包{len(rows)}张检查通过的图片及提示词：{args.output}')
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (ValueError, OSError, KeyError) as error:
        print(str(error), file=sys.stderr)
        sys.exit(1)
