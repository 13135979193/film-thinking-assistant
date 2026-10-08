# 影视思维助手 · Codex 技能包

版本：0.2.0；整理日期：2026-10-08。

这是一个 skill。入口是 SKILL.md，判断经验、纠错案例、光影和空间知识放在 references 中，使用时按任务读取。下载者只需安装整个 film-thinking-assistant 文件夹，不必分别安装这些知识模块。

## 直接看蒸馏了什么

- [20 个具体反馈记录：指正、前后变化、保留项与对应规则](references/feedback-evidence.md)。记录内引用、作者转述和规则要求分别标明；没有冒称这是原聊天全文。
- [30 条判断原则](references/judgment-principles.md)：下一次任务怎样判断与取舍。
- [20 个纠偏案例](references/correction-cases.md)：常见失败及适用范围。
- [光影知识](references/lighting-principles.md)与[空间知识图谱](references/space-atlas.md)。

GitHub 链接安装时，Codex 应下载整个技能目录并保留 references，而不只保存 SKILL.md。安装链接为 [https://github.com/13135979193/film-thinking-assistant/tree/main/skills/film-thinking-assistant](https://github.com/13135979193/film-thinking-assistant/tree/main/skills/film-thinking-assistant)；安装后新开一轮对话，使用 $film-thinking-assistant 或说“使用影视思维助手”。

## 下载 ZIP 后在 Codex 使用

1. 解压并保留完整的 film-thinking-assistant 文件夹，包含 SKILL.md、references 和 agents；不要只复制入口文件。
2. 在同事用于影视工作的项目目录中创建 .agents/skills，把完整文件夹放进去。最终结构为：项目目录/.agents/skills/film-thinking-assistant/SKILL.md。
3. 在 Codex 中打开该项目，开始聊天，输入下面的例子。若技能尚未出现，重启 Codex 并检查 Skills 列表。

示例：

> 使用 $film-thinking-assistant，帮我设计这个剧本中的学校食堂。按原文确认年代、地域和容量，给完整中文提示词。

> 使用 $film-thinking-assistant，把这个已认可的客厅改成夜晚。保留布局和材质，只调整有依据的光源。

> 使用 $film-thinking-assistant，按这个房间的固定门窗和家具做真反打，先检查机位与世界方位，给完整提示词。

> 使用 $film-thinking-assistant，提炼我这次纠正的判断理由，记录到当前项目，不修改共享技能。

发布到 GitHub 后，也可在 Codex 中调用内置 $skill-installer，并提供真实仓库位置及本 skill 子目录进行个人安装。具体安装位置以同事当前版本的安装器为准。项目内安装方式与技能机制见 [官方说明](https://learn.chatgpt.com/docs/build-skills)。

## 使用习惯

提供当前剧本、参考图或已认可布局，并说清要提示词、实际图像还是资产表。可以直接用自然语言，不必选模块编号。当前项目要求优先于作者的历史偏好；写实、3D 漫场景及其他风格不会被强行统一。

本包包括设计与诊断知识。实际生图、修图和办公文件制作仍使用同事自己的 Codex 可用工具。没有生成工具时可以给提示词；没生成的图不会被说成已经完成。

来源覆盖、案例状态与验证范围见 [来源与范围](references/source-and-scope.md)。
