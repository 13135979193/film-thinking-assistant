# 解说漫自动化：安装与使用

将剧本核对、角色与空间分析、场景/道具生成、图片入Excel和交付检查串起来的 Codex skill。中文名 **解说漫自动化**，技术调用名 `$narrated-drama-automation`。

## 其他电脑安装

### 下载安装器

- Mac：[下载双击安装文件](https://github.com/13135979193/film-thinking-assistant/raw/refs/heads/main/install-narrated-drama.command)。保存后双击运行；若浏览器没有保留执行权限，让Codex运行该文件即可。系统若要求确认来源，按实际提示处理，不需要关闭系统保护。
- Windows：[下载PowerShell安装脚本](https://github.com/13135979193/film-thinking-assistant/raw/refs/heads/main/install-narrated-drama.ps1)。在PowerShell运行，或交给Codex执行；如策略不允许脚本，改用下面的一句话安装，不需要更改安全策略。此脚本尚未在Windows实机验证。

安装器会下载公开仓库，只安装解说漫自动化；已有版本先备份。默认装入用户Codex技能目录，尊重 `CODEX_HOME`。不安装图像工具，也不改原影视助手；需要接入时用下面的安装口令。Mac安装器已在临时目录实测安装与更新备份。

### 一句话安装（各平台推荐）

[打开技能安装地址](https://github.com/13135979193/film-thinking-assistant/tree/main/skills/narrated-drama-automation)

在另一台电脑的 Codex 中复制发送下面这一句即可，不需要逐个复制文件：

```text
使用 $skill-installer 安装 https://github.com/13135979193/film-thinking-assistant/tree/main/skills/narrated-drama-automation ，保留全部 references、scripts 和 agents 文件。安装后验证技能。如果本机已有影视助手，将“解说漫自动化”加入它的任务路由；保留其他功能，不覆盖我的原有技能。
```

这是“一句话安装”：GitHub网页本身不会替另一台电脑执行安装。需要目标电脑已装 Codex、可以访问GitHub。装好后新开一轮对话再调用；若未识别，重新打开Codex。图片生成需要该电脑可用的图像工具，Excel编辑需要相应表格能力；安装流程不会附送工具额度、API密钥或本项目图片。

如果已安装同名技能，需要更新，请让Codex先备份旧目录，再安装最新版本，保留项目文件。不要直接覆盖自定义改动。

## 开始使用

附上原始剧本（DOCX/PDF/文本均可）和已有Excel，没有表则先拆解。发送：

```text
解说漫自动化。先完整核对剧本与资产表，列出原文事实和推断。先分析第一个场景属于谁、年代国家、人物身份与适配建筑风格，给我提示词并生成一张正面场景图。先看样，不批量生成。
```

样图认可后：

```text
以我认可的这张图为质量基准，继续完成其余场景。空间宽阔但不空荡，布局有细节，门默认关闭，保持剧本身份与年代国家。逐张检查，出问题就修改，全部完成后按编号嵌入Excel的场景表，调整图片尺寸与行高，再打包原图和提示词。
```

只做道具：

```text
解说漫自动化，只制作核对后的道具表。纯白背景，物体完整，画幅适应尺寸；原文没说旧就做全新；包和表原文无指定则做豪华有设计感的原创款；床、椅子、门不用单独生成。文件文字按原文且排版美观。逐张检查后按编号嵌入Excel。
```

仅写提示词：`解说漫自动化，只写S003的场景提示词，不生图。`

继续旧项目：附上最新Excel、`manifest.json`、认可的参考图和对应提示词，再说 `解说漫自动化，从项目记录继续剩余资产。` 安装技能不会自动带走旧电脑上的项目资料。

## 实际工作顺序

1. 全文核对：保持原编号，补遗漏、纠冲突，区分原文明示、推断、美术补充。
2. 设计分析：空间归属和人物身份先于风格；国家年代先于材质配色；不把有钱等同满屋金色，不把男性房间等同蓝灰黑。
3. 参考与定样：需要时上网看真实图片，代表样图实际检查，认可后记录基准。
4. 批量制作：逐资产保存真实图片、提示词和版本；看图修改，不能只检查工具是否成功。
5. 图片入表：编号一一对应，等比缩放、行高适配，保留其他工作表与已有图片。
6. 检查交付：清单、图片、表格与ZIP一致；待核与失败明确列出。

同一场景换角度、换日夜时保留空间关系。宽阔豪华等要求服务于具体剧本；小公寓、医院不会全部套成豪宅。认可的配色只在当前项目沿用。

## 内置检查脚本（可选）

Python 3.9及以上，无第三方依赖。让Codex在已安装技能的 `scripts/asset_manifest.py` 执行，路径由当前电脑确定：

```sh
python3 scripts/asset_manifest.py init ./项目目录
python3 scripts/asset_manifest.py audit ./项目目录/manifest.json
python3 scripts/asset_manifest.py package ./项目目录/manifest.json ./交付.zip
```

`init` 创建空清单，不覆盖旧项目。清单格式与字段见 [道具与交付](skills/narrated-drama-automation/references/delivery.md)。`audit` 检查编号、来源、图片头部尺寸和提示词文件；`package` 在所有非排除项已检查后打包原图与提示词。图片完整解码、审美、文字准确性和Excel嵌图需另行验证，脚本不会代替这些工作。

## 交付与限制

建议保留：带图片Excel、最终图片、提示词、清单、索引与ZIP。批量生成受当前账号工具、额度与可用时间限制；工具失败必须报缺口，不能虚报完成。技能不自动生成视频，不自动对外发布项目，不会永久记住其他电脑未提供的资料。

Codex官方技能说明：[Build skills](https://learn.chatgpt.com/docs/build-skills)。本仓库流程技能可以单独安装；原有影视思维助手仍在 [原技能目录](skills/film-thinking-assistant)。
