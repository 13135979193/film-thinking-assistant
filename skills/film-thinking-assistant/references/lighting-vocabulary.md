# 光影词汇：把判断变成生成指令

本页只保留常用功能词与可组合句式，不作为完整摄影术语表。先用 [光影原则](lighting-principles.md) 决定关系；已有参考图先按 [诊断方法](lighting-diagnosis.md) 找证据。默认遵循当前技能的交付语言，用户要求中文时直接用中文，不强制中英双份。

## 选词先有坐标

`camera-left/right` 指当前摄影机看到的左右，`front/side/rear` 描述来源相对主体与观察方向的位置。组合成“相机左前上方”“主体右后方高位”比单写“左光”明确。反打与多角度同时写房间固定来源，例如东墙窗，而不是要求每张图都保持相机左光。

角度、米数、尺寸与色温只有在用户给定、真实测量或作为明确设计设定时才使用。反推图先用较高／较低、大面／小面、近／远等相对关系；报告中用“推测”标未知，不把推测数值包装成原始参数。生成指令可以选定一套设计，不必把一长串不确定猜测交给模型。

## 按功能挑常用词

| 本次需要表达的判断 | 英文用语 | 应补充的关系 |
| --- | --- | --- |
| 主要塑形方向 | `directional key` | 从哪一侧、高低、照亮哪一面 |
| 大面方向光 | `large diffused source` | 由窗帘、扩散面或反射面形成；实际亮面与主体的关系 |
| 清楚投影 | `hard directional light` | 来源与遮挡体；影落在哪个面、向哪里延伸 |
| 柔和影边 | `soft-edged cast shadows` | 有效大源与遮挡距离，仍保留方向 |
| 有限暗部细节 | `restrained reflected fill` | 哪面墙、桌面或地面带回少量光 |
| 暗侧形体 | `negative fill on the shadow side` | 减少哪一侧反射，关键眼睛或动作仍可读 |
| 克制边缘光 | `subtle rear-side separation` | 有依据的后侧来源和要分开的边缘 |
| 局部画内来源 | `visible practical light` | 灯位、出光方向、照到的桌面／人物／邻墙 |
| 画外补足 | `matching off-frame augmentation` | 让增补仍可被画内窗或灯的方向与颜色解释 |
| 溢光限制 | `controlled spill` | 保留受光区，保护不应照亮的墙、背景或镜头 |
| 近亮远暗 | `falloff into the deeper room` | 近处来源到主体与背景的相对距离和遮挡 |
| 物体接地 | `localized contact shadows` | 实际接触点与适当强度，不形成整圈黑描边 |
| 漫反射暗侧 | `soft wall bounce` | 反弹墙的颜色和实际受亮区域 |
| 材料反光 | `view-dependent specular reflections` | 光源、相机与材质粗糙度；不统一所有材料的亮斑 |
| 前后景区分 | `separation in brightness and depth` | 哪层负责主体，哪层允许亮或暗 |
| 混合光分区 | `localized warm light against cooler ambient light` | 暖／冷各自来源与覆盖，不染全图 |
| 保留重要亮部 | `controlled highlight brightness` | 哪个窗、灯罩或反射需要形状／纹理 |
| 有体积的 3D 媒介 | `modeled volumes with restrained indirect light` | 透视、材质与接触关系，不靠强 AO 和塑料高光 |

`key/fill/rim` 是功能词；没有对应需求就不写。`high key` 用于明亮、浅阴影且仍有主次的目标，`low key` 用于大面积暗部与选择性可见；二者不等于全白或欠曝。`catchlight` 说明眼中反射，不意味着必须新增眼神灯。`gobo` 需要真实的遮片与投影路径，不用于解释凭空贴在墙上的纹理。

## 用四个模块写完整关系

第一模块写媒介、空间与保留对象；第二模块写主导来源及到达路径；第三模块只加入必要的反射、遮挡和背景；第四模块写本次关键验收条件。短任务通常一段就够，不强制把每种附件、每层光、每个色温写全。

```text
[Medium and scene, with the established camera and layout].
[Source] reaches [important surface] from [defined position] through [opening or modifier],
producing [cast-shadow direction and edge quality on a named receiving surface].
[Only the needed bounce, spill control, local practical, and background relationship].
[Required readable detail and the changes that must stay within scope].
```

方括号是写作槽位，交付前全部换成具体描述。不要把“柔光、大面积、高对比、无阴影、硬窗影”并列堆进去；若软环境与硬直射共存，分别说明各自路径。近大源可柔和却快速衰减，远大源可较均匀，不能写成“柔光所以全室同亮”。

## 可按任务选择的原创句式

### 窗侧日景：保留空间自然层次

适用：窗为主要来源的客厅、主厅、教室或无人环境资产。先决定直射太阳是否存在，再选硬影或漫射版本。下面选择漫射版本，没有另加一束窗格太阳光。

```text
An unoccupied interior with the established camera, architecture, and furniture layout.
Diffuse daylight enters through the large window on camera-left, reaching the near wall,
seating area, and floor from the same direction. Cast shadows extend away from the window
with soft transitions. Pale walls return a small amount of light into the deeper room.
Keep the entry and circulation path readable, with localized differences in brightness
rather than uniform illumination. Preserve the existing materials and room proportions.
```

中文关系：窗侧照到近处，再由浅墙带回少量光；深处仍有层次。若改为直射，单独写太阳方位、窗框遮挡和落影区域，不能只把 `diffuse` 换成 `hard` 而保留矛盾的软影描述。

### 人物窗光：可读表情而不填平

适用：采访或肖像。脸型和头部转动优先，不强制伦勃朗三角和某个固定角度；下例选择前侧略高的大窗关系。

```text
A portrait with the subject and camera position unchanged. A large diffused window
slightly above eye level on camera-left shapes the near side of the face. Preserve
the nose and cheek shadow transitions; let a pale wall return restrained light into
the shadow side so both eyes remain readable. Keep natural skin texture and separate
the dark hair from the lighter background without adding a bright outline.
```

若本次就要隐藏表情，可删除“双眼可读”的目标；若光位与人物转向不支持亮面，不要用额外眼神白点掩盖错误。

### 桌灯夜景：以已有暖来源主导

适用：桌边工作、卧室谈话、餐桌或夜间道具画面。下例没有默认加入蓝月光；窗外可按场景设为城市灯光、暗环境或另一个明确来源。

```text
Keep the room, camera, table, and lamp positions unchanged. The shaded table lamp is
the main local source, lighting the nearby tabletop and the side of the subject facing
it. Matching off-frame augmentation follows the lamp's direction and warm color,
making the relevant face and hand gesture readable while the rest of the room stays
subdued. Keep the lampshade's form visible and the tabletop reflection restrained.
Let the unlit areas retain just enough reflected light to describe the room.
```

火光版本先确认火源相对人脸的高度和规模，再写暖光影响下脸、手与邻近表面、局部亮度轻微变化。不可把所有烛光、壁炉和篝火统一成强顶光、同等衰减或快速闪烁。

### 直射外景：太阳与环境反弹共存

适用：庭院、街道、校园、建筑表面。方位和影长是本例选定的创作设定，不是所有外景默认。

```text
Low afternoon sunlight reaches the courtyard from camera-left, casting long shadows
across the paving away from the sun. Cooler skylight and restrained bounce from the
pale paving keep the shaded surfaces visible without erasing the direct-light pattern.
Match window, railing, and tree shadows to the same solar direction and their actual
receiving surfaces. Preserve material differences and avoid identical glossy highlights
on stone, glass, and painted metal.
```

低太阳仍可能因遮挡无直射；如果是阴天，改成大天空来源与浅影关系，去掉固定长硬影。雨路反光需有湿面、可见或画外亮源及观察角，不凭“夜景”自动铺满倒影。

## 变体与局部修复句式

### 同一空间换角度

```text
Keep the window and light sources at their established positions in the room.
For the new camera angle, recompute the visible lit faces, cast shadows, and specular
reflections from those same sources. Preserve the architecture, furniture positions,
materials, and time of day; do not move the light sources to retain the previous
screen-left appearance.
```

它描述连续性目标，不保证生成工具能从单张图推断未见空间。新角度涉及未知结构时先限定可推断范围，必要时使用额外参考，不编造已确定的背面布局。

### 一项主错误的修复

```text
Preserve the camera, architecture, object positions, and accepted visual style.
Use the existing left-side window as the dominant source. Correct the chair and table
cast shadows on the floor to follow that direction, restore localized contact shadows
at the legs, and soften the unsupported bright edge on the opposite side. Keep the
deeper room subdued, with only restrained bounce from the existing pale wall.
```

实际修复前仍要看原图是否支持左窗为主来源；不能把示例左窗强加给任意图。若只需修颜色，不追加投影变化；若需要保持已经认可的高光，就明确保留并解释相容路径。

## 不要让术语替代判断

- `cinematic, dramatic, beautiful, ultra realistic` 可表达风格意图，但删掉后仍应读出来源、落点和主次；它们不能替代光路。
- `deep contact shadows` 容易变成重黑边，通常写局部接触关系及适当强度更稳。
- `no fill, fully readable shadow side` 若没有说明反弹或其他来源，目标可能自相矛盾。
- `soft window light with razor-sharp window-frame shadows` 需要另一个直射分量；没有就改成一致的软影。
- `one key, no conflicting reflections` 不意味着金属高光必须位于人物亮侧；反射先按视角和材料检查。
- `physically accurate` 是目标，不能作为真实模拟或一次渲染成功的证明。给出清楚关系后仍须检查实际结果。

源面积、距离、遮挡、反射和颜色没有必要全部塞进每条指令。保留对本次结果影响最大的关系与保护条件；模型出现错光时按实际错误重写，避免不断追加互相矛盾的“质量词”。
