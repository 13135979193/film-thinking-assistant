#!/bin/bash
# macOS: download, then double-click. Optional first argument: skills directory.
set -euo pipefail
skill_name='narrated-drama-automation'
skills_root="${1:-${CODEX_HOME:-$HOME/.codex}/skills}"
download_dir="$(mktemp -d)"
stage=''
cleanup() { rm -rf "$download_dir"; if [ -n "$stage" ] && [ -d "$stage" ]; then rm -rf "$stage"; fi; }
trap cleanup EXIT
mkdir -p "$skills_root"
printf '正在下载：解说漫自动化\n'
curl --fail --location --retry 2 --connect-timeout 15 --max-time 120 \
  'https://codeload.github.com/13135979193/film-thinking-assistant/zip/refs/heads/main' \
  --output "$download_dir/repository.zip"
unzip -q "$download_dir/repository.zip" -d "$download_dir"
source_dir="$download_dir/film-thinking-assistant-main/skills/$skill_name"
test -f "$source_dir/SKILL.md"
stage="$(mktemp -d "$skills_root/.narrated-drama-install.XXXXXX")"
cp -R "$source_dir/." "$stage/"
target="$skills_root/$skill_name"
if [ -e "$target" ]; then
  backup_root="${skills_root%/}.backups"
  mkdir -p "$backup_root"
  backup="$backup_root/$skill_name.$(date +%Y%m%d-%H%M%S).$$"
  mv "$target" "$backup"
  printf '旧版已备份：%s\n' "$backup"
fi
mv "$stage" "$target"
stage=''
printf '\n安装成功：%s\n新开Codex对话，输入“解说漫自动化”并提供剧本即可。\n' "$target"
printf '如需接入原影视助手，告诉Codex：把解说漫自动化加入我的影视助手任务路由，保留其他功能。\n'
