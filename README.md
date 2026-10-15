# 影视思维助手

## 新增：解说漫自动化

从剧本核对到场景/道具设计、图像生成、按编号嵌入Excel和检查打包的一套工作流，可独立安装，也可作为影视助手的任务入口。

**[安装地址](https://github.com/13135979193/film-thinking-assistant/tree/main/skills/narrated-drama-automation) · [完整使用教程](NARRATED-DRAMA-GUIDE.md)**

[Mac双击安装文件](https://github.com/13135979193/film-thinking-assistant/raw/refs/heads/main/install-narrated-drama.command) · [Windows安装脚本](https://github.com/13135979193/film-thinking-assistant/raw/refs/heads/main/install-narrated-drama.ps1)（Windows脚本尚未实机验证）

把下面一句发给另一台电脑的Codex：

```text
使用 $skill-installer 安装 https://github.com/13135979193/film-thinking-assistant/tree/main/skills/narrated-drama-automation ，保留全部附带文件。如果本机已有影视助手，将“解说漫自动化”加入它的任务路由，不覆盖其他功能。
```

安装后新开一轮，输入 **解说漫自动化** 并附上剧本和资产表即可。网页不会自行执行本机安装；实际生图使用目标电脑自己的可用工具与额度。此发布不包含私人剧本或项目图片。

---

一个可安装的 Codex skill，将已记录的影视判断、纠错经验、光影与空间知识用于当前任务。

## 安装

**安装链接：[https://github.com/13135979193/film-thinking-assistant/tree/main/skills/film-thinking-assistant](https://github.com/13135979193/film-thinking-assistant/tree/main/skills/film-thinking-assistant)**

把这一句连同链接发给 Codex：

> 使用 $skill-installer 安装 https://github.com/13135979193/film-thinking-assistant/tree/main/skills/film-thinking-assistant ，完整保留 references 资料。安装完成后告诉我如何调用。

安装后新开一轮对话，输入“使用影视思维助手，处理这次场景任务”，或使用 `$film-thinking-assistant`。无需手动复制每个知识文件。

## 直接看记录

- [20个具体反馈：日期、指正、前后变化和规则对应](skills/film-thinking-assistant/references/feedback-evidence.md)
- [30条判断原则](skills/film-thinking-assistant/references/judgment-principles.md)
- [20个纠偏案例](skills/film-thinking-assistant/references/correction-cases.md)
- [光影原则](skills/film-thinking-assistant/references/lighting-principles.md)、[光影诊断](skills/film-thinking-assistant/references/lighting-diagnosis.md)
- [空间原则](skills/film-thinking-assistant/references/space-principles.md)、[建筑图谱](skills/film-thinking-assistant/references/space-atlas.md)

当前版本0.2.0。知识与案例是已保存记录的蒸馏，记录内引语未对原聊天逐字核验；实际图像执行仍使用使用者自己的生成工具。当前使用者要求优先于作者的历史偏好。来源和验证范围见技能内说明。
