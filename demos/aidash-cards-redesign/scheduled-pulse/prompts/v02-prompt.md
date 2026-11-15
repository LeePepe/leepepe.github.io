# v02 · 极光六舱检视台 (topology-bento-glass-pods)

## 1. Visual Metaphor, Palette & Anti-Clone Spatial Lock

这是一块极光环境中的六舱调度仪：每件任务像一只带磨砂边框的浅抽屉，选中舱体把报告送到下方横贯工作面的检视托盘。光线来自任务状态的局部晕圈，不来自全屏彩色壁纸。两列三行矩形舱是主体，底部检视台是唯一细节出口；禁止用纸袋竖列加几块透明背景冒充 Bento。负责本稿的 Writer 仅独立手写 scheduled-pulse/v02.html，不派 Agent、不生产其他变体，也不以代码生成器批量拼 HTML/CSS。

设计身份选择 web/macOS、VS-006 Aurora 观测、CL-007 的冷极光支系；X 保持就地三键，Y 是 2×3 overview 与单一 bottom detail，Z 则环境底光→实色字面→浮动磨砂边沿。候选 AppTheme 原点为 Dark #0B101E / Light #EEF3FA；舱内可读面 #182238 / #FFFFFF，深浅正文 #EAF1FF / #17263F，辅助字 #B0BDD2 / #566780。非状态装饰只用低饱和冰蓝 #95ABD5，不沿用黄铜矿纸、Linear 石墨或航电白蓝英雄的令牌。

反克隆不是把 radius 从12改成20：bento-pod-grid 必须同时可见六件宽至少480px的舱，bottom-inspection-stage 始终在下方，不在选中舱内插入长报告。所有专属选择器使用 aurora-/pod-/inspection- 语汇，不能拿别稿的布局混入；除 content 与规定 data-* 外，跨候选 CSS class/rule 交集目标 <15%。没有第三列，没有42/58分割，没有异常上方英雄重排。

## 2. Single P0 Focus, Semantic Status Colors & Initial Showcase State

本页唯一 P0 是「选一舱，把它的执行证据平稳送到检视台」。首屏左上每日简报 05:00 点亮，底台默认打开其回执，让两主题初始截图都能同时看到六舱正面与完整报告。状态识别、次数及周期是 P1 常见信息；悬停摘要是 P2 非阻断预览；阶段和日志属于 P3，仅存在于下台，不另外加总览报表、导航页面或故障统计。

每舱必须用同一套语义原色照亮自己的灯点、边沿一角与状态徽章：#10B981 ● 成功 (1.8s) 覆盖简报、学习推荐和我的 PR 巡检；#F59E0B ▲ 耗时偏高 (14.2s) 专属数仓脉搏；#F43F5E ✕ 失败 (exit 1) 专属特定人 PR 审查；#06B6D4 ● 运行中用于 Linear @bot 桥接；按暂停后改成 #64748B ⏸ 已暂停。文字不依赖晕光对比，状态字形与汉字常驻，色弱用户也能分辨。

六舱阅读顺序为 row1 简报/学习，row2 数仓/桥接，row3 我的巡检/特定人审查。只给当前舱一条明亮上边沿，不把失败舱的红色换成选中冰蓝。运行青光周期2.4s、亮度幅度不超过15%，其他环境光静止。成功三舱一律展示 R5 的1.8s；这次不继承 R4 中学习2.4s与巡检0.9s。

## 3. Hover Brief Preview ([data-hover-brief]) & Click-to-Pull-Out Drawer ([data-report-panel]) Contract

舱 face 被 pointerenter、:hover 或 focus-within 命中时，以 -4px 垂直位移和略加强的接触影回应；不放大舱格，不调整网格行高。每件 [data-job-row] 内预置的 [data-hover-brief] 位于最后20px的浅槽，从 opacity 0 / translateY(5px) 浮到 opacity 1 / translateY(0)。底部三键在槽上方独立占位，预览不能遮住按钮。光学框可以透明，摘要文字底必须带不透明度≥.90的实色衬板。

六条 in-pod 简句按自己的语气分别写「简报已送达 · 3 题 → TIA-448」「学习题单成稿 → TIA-431」「入仓段 9.1s · 慢轮已结束 → TIA-448」「提交仍在运行 · 最近回执 TIA-448」「PR #311 检查已归档」「exit 1 · PR #308 尚未提交评审」。短句只取一个产出和一个结论；禁止 hover 才显示 Title、运行次数或状态，也不能把六条都写成同一条通用成功文案。移入卡内按钮仍保留预览，离开整个舱延迟120ms消隐。

每舱的 button[data-row-trigger] 负责主体选择，独立 nav 中三枚动作按钮不嵌进这个 button。点击另一舱，六个事先写好的 [data-report-panel] 在同一 bottom-inspection-stage 内交叉过渡；再次点击当前舱把台面收回到20px的空托盘唇，六舱与底台外框位置保持不动。下台从 translateY(18px) 拉回0，内容 opacity 切换；不能用 fixed overlay 覆盖第三行，也不能把报告 append 到每张磁贴。

检视台保留 summary/outputs/stages/logs 四个报告块。胶囊 TIA-448、TIA-431、PR #311、PR #308 根据关联任务显示，指向该台内初始已存在的 #inspection-<job>-<receipt> 说明节点并移交焦点；上游没有给外部 URL 时不猜 GitHub repo 或 Linear workspace。未选中的报告 inert 且 aria-hidden，仍留在原 DOM；链接、撤销和动作 click 都 stopPropagation，选中与操作互不干扰。Esc 收托盘并把焦点送还发起舱。

## 4. Measured 1280x800 Viewport Geometry & Spatial Bounding Boxes

以1280×800内页作唯一测量坐标：aurora-hud-bar 在 (64,40,1152,40)；bento-pod-grid 在 (64,96,1152,400)；bottom-inspection-stage 在 (64,510,1152,250)；aurora-undo-strip 在 (64,768,1152,28)。二列宽568、列缝16，三行高128、行缝8，算式 2×568+16=1152 与 3×128+2×8=400。不因选择下台而压缩网格；灯影最大8px不能越进按钮目标。

六个舱左坐标为64或648，顶坐标依行96/232/368，外框568×128；扣16px左右内边得到536px可用。舱面标题行 y+16..38、周期行 y+40..58，下方动作/计数带 y+64..96，摘要槽 y+100..120。标题区最大340px，右上状态区176px，中间20px留白；次数在底带左侧最多300px，右侧动作组宽220，间隔16。动作64/72/60×32，间距8×2，总212，可完全靠右；计数可折为累计/今日两行，但所有数字保留。

下台内边16px，标题带24px、摘要24px、间隙8px；主体从 y582 到744，高162。左区宽552、右区552、中隔16，和为1120；左边五段每行24px，标签164、数值52、剩余轨道336，顶部34px产出胶囊行后剩120px正好容下五段。右边摘要补充最多42px、终端高度88px、来源说明32px；2–3行日志11px/18px不被裁掉。下台标题与总论不增加第三个报表容器。

采用22px HUD标题、14px舱名、12px正文/数字、11px日志四档，CJK 不降至9px去救布局。短摘要固定单行；按声明短文在536px宽下排版，不用 ellipsis。报告段落可自然折行，字体增大时只下台主体 scroll，不让 document 横向溢出。所有 capsule 和动作目标≥28×28；底栏高度28保证撤销可点而不与 viewport 外部设备壳碰撞。

## 5. Dual-Theme Surface Polarity & Tactile Drawer Lip Craft

玻璃只在舱的装饰外套和底台上沿采样环境底层，字面与日志底板保持实色。Dark 的壳层 rgba(204,222,255,.08)、实字面 #182238；Light 壳层 rgba(255,255,255,.62)、字面 #FFFFFF。壳 blur 18px、saturate(125%)，6px光学斜边，用四角柔和 radial 高光暗示 Fresnel，不加折射条纹。状态晕从本舱中心偏左上展开到80px半径、alpha最多.13；六团光不混成一片彩泥。

下台边沿可比舱壳更厚2px，托盘净内容不再做 backdrop-filter；玻璃永远不采样另一层玻璃。WebKit 没有复杂折射时使用静态 radial specular rim 与 inset 0 1px 0 rgba(255,255,255,.15)，不依赖 url(#filter) shader；reduced-transparency 时整个壳切换 #22304B / #E0E8F4 实色，层次依靠接触影和1px内高光继续成立。

每只 pod 上缘留一条2px抽屉唇，前方短而细的拉手是24×3px的低对比形状，不是假窗口交通灯。hover 只让壳微离底面，文字不折射、不同图层不互相毛玻璃。局部白亮片面积≤舱面的8%，避免整个透明候选比状态更抢眼。暗台 shadow 0 10px 28px rgba(0,0,0,.25)，浅台换蓝灰 .09；实色标题至少4.5:1、状态灯和focus轮廓至少3:1。

舱灯、暂停、回转、删除使用手写 inline SVG 24 viewBox/1.6px stroke、圆角连接，图标16px配全称按钮。色点照明可用规定原色，小字号状态文字在 Light 用同色深墨、Dark 用相应浅墨，不能把 #F59E0B 的亮黄字直接放白底。不是为 Light 把 Dark 白字 opacity 降低；两套表面极性独立定义。

## 6. Apple Native Spring Physics & 3-Button Permanent DOM Micro-Interactions

轨道曲线指定 cubic-bezier(0.22, 1.35, 0.36, 1)，舱抬起220ms、托盘抽出480ms、跨舱报告460ms。台面轮廓不变，内容移入才有弹性；高度折回20px唇使用无超调曲线，但预挂载内容滑动保留同一 spring 质感。快速点第三舱不排队播放第一舱的过时结果，以最新 selectedJob 为准。reduced-motion 将所有 y位移去掉、过渡≤60ms，停止环境脉冲而保持 running 徽章。

暂停键 [data-action="toggle-pause"] 改 enabled flag、灰灯和「继续」文字，保存最近执行结果而非把结果删掉；继续回到已结算的结果。一次运行可以与暂停排程并存：暂停后 Rerun 仍临时展示青色运行，完成后面上回 ⏸ 已暂停，同时回执内容更新。恢复 enabled 不重建组件、不重置计数，也不能用灰灯掩盖历史失败。

重跑键 [data-action="rerun"] 立即有运行回声，单个 job 的 inFlight 锁禁止连续点击重复提交；完成一次累计/今日各+1、耗时仅更新既有 Text.data/nodeValue，不设置父 Element.textContent，也不用 innerHTML 创建新日志。状态结果按本文声明的任务分支：健康1.8s、数仓14.2s偏高、审查exit1；这只是本页的受控反馈，不发实际调度、远程 API、文件或数仓写入。删除与 token 世代号配合，旧回调不可复活已删除舱。

删除键 [data-action="delete"] 先在舱底的预置确认层显示「确认删除」与取消，确认后该舱外格保持原568×128，内舱只缩回留下安静空槽；article 本身 inert，视觉空槽属于原grid cell，不把伙伴舱移位。底 undo-strip 的六个 [data-action="restore"] 控件原本就存在，按删除的 job 显示，支持连续删除多件再逐件恢复；恢复时原位置、次数、暂停状态不变。控制层和触发面是兄弟、事件隔离，删后focus到恢复，恢复focus回原舱；所有隐藏报告/确认层可见性与键盘 inert 同步。只允许属性与原 Text.data/nodeValue 改写，父 Element.textContent、remove/replaceChildren/innerHTML 以及替换 Text 节点都不可以，removedElements = 0 覆盖整个 main。

## 7. Production Data Inventory & Exact DOM Topology

数据沿来源分清：R5 三份主简报规定六任务、色义和四架构；旧 r4/domain §2 只供周期及次数库存，R5 明示的三个1.8s覆盖其旧耗时。这里编排的是 handoff 快照和明确的报告内容，不是测得的实时数仓数据；没有增加 L1–L5、ROI 或私有日志读取。aidash-metrics capability probe 拒收 scheduled_pulse，意味着不能以 Skills inspector 为本页数字作 readiness 背书。将来的生产 reader 要读取上游真实来源、窗口/覆盖/新鲜度，空回执应「暂无回执」而非零；此阶段不接这个 seam。

舱库存用分组文字完整落入首次 HTML：daily-brief 为「每日简报 05:00 / 每天 05:00 · 下次 12h 后 / 累计 142 次 · 今日 1 次」；daily-learning 为「每日学习推荐 04:15 / 每天 04:15 · 下次 11h 后 / 累计 98 次 · 今日 1 次」；这两舱均 ● 成功 (1.8s)，尾随暂停、Rerun、删除，不以 hover 替代任何一项字段。

第二排静态对象：aidata-pulse 的 Title「AIData 数仓脉搏 04:00」，周期「每天 04:00 · 下次 11h 后」，计数「累计 186 次 · 今日 1 次」，初徽章 ▲ 耗时偏高 (14.2s)；linear-bot-bridge 的 Title「Linear @bot 桥接」，周期「每 1m · 刚刚 16:45」，计数「累计 4,280 次 · 今日 184 次」，初徽章 ● 运行中。同样三键右对齐，状态并非从次数推导。

第三排资产：my-pr-patrol 展示「我的 PR 巡检」「每 5m · 2m 前」「累计 860 次 · 今日 36 次」以及 ● 成功 (1.8s)；target-pr-review 展示「特定人 PR 审查」「每 5m · 4m 前」「累计 312 次 · 今日 12 次」以及 ✕ 失败 (exit 1)。Title 中时间仍保留，不能凭已有周期列擅自删掉05:00/04:15/04:00。

所有台内报告有五个槽位标题 ① 个人源采集、② L2-L3 入仓、③ Retro-ROI、④ 学习寻题、⑤ Brief 投递；对应非晨间任务加实际阶段名，说明这是任务阶段映射，不宣称 PR 在做入仓/寻题。五色按青、靛、紫、琥珀、翡翠，fail槽红、running槽青、pending槽灰且文字说明，条长依据本报告已完成阶段的最大耗时，不用 min-height 冒充未知计时。

底台要为六件手写各自数据：简报 summary「采集与入仓已完成，三题进入晨间投递回执」，outputs TIA-448/TIA-431，秒数[0.3,0.5,0.4,0.3,0.3]；学习 summary「三题候选已去重匹配并送达」，TIA-431，候选/去重/匹配/整理/送达秒数[0.3,0.2,0.5,0.4,0.4]；数仓 summary「本轮完成，L2-L3 9.1s需要关注」，TIA-448，秒数[1.2,9.1,1.8,1.3,0.8]。条上的单位和值、总计1.8/14.2必须一致。

后面三件：桥接 report「路由已结束，当前提交仍运行」，TIA-448明确为上次已提交产出，消息读取.1/去重.1/路由.2s、提交运行中、确认未开始，不写完成时间；我的巡检 report「PR #311 的检查结论已保存」，PR #311，PR读取/检查/对比/保存/通知.4/.3/.4/.3/.4s；特定人 report「PR #308 审查退出码1，未形成新评审」，PR #308，读取.2/diff.3/执行.6s失败，评审和通知未执行。红舱不能虚构凭据过期、权限拒绝等根因。

高亮终端用预挂载 span 展示2–4行短尾：简报 `05:00:01.8 INFO delivered TIA-448`，学习 `04:15:01.8 INFO matched=3 sent`，数仓 `04:00:10.3 WARN L2-L3=9.1s` 后接 `04:00:14.2 INFO pulse committed`，桥接 `16:45:00.4 INFO commit pending`，巡检 `16:43:01.8 INFO PR311 checks stored`，审查 `16:41:01.1 ERROR review exit=1`。时间与标识可辨，INFO青、WARN金、ERROR红，日志文本不会带凭据或真实个人消息。

```text
main.topology-bento-glass-pods
└─ section.content
   ├─ nav.aurora-hud-bar
   ├─ section.bento-pod-grid
   │  ├─ article.glass-pod-card[data-job-row][data-job="daily-brief"]
   │  │  ├─ div.pod-optical-shell (光学装饰)
   │  │  ├─ button.pod-signal-face[data-row-trigger][aria-controls="inspection-daily-brief"]
   │  │  ├─ nav.pod-capsule-actions (toggle-pause / rerun / delete)
   │  │  ├─ p.pod-frosted-brief[data-hover-brief]
   │  │  └─ div.pod-delete-confirmation (确认/取消，首屏挂载)
   │  └─ article.glass-pod-card[data-job-row] ×5，按两列三行手写
   ├─ aside.bottom-inspection-stage
   │  ├─ div.inspection-docking-rim
   │  └─ article.inspection-receipt[data-report-panel] ×6
   │     ├─ header.inspection-verdict (summary)
   │     ├─ section.inspection-measure-bay (outputs / stages)
   │     └─ section.inspection-console-bay (logs / 产出来源说明)
   └─ footer.aurora-undo-strip (六枚 restore 常驻入口)
```

## 8. Explicit Anti-Patterns & Verification Targets

不能玻璃套玻璃、用模糊包整张文字层、放 caustic 条纹或夸张彩虹折射。不得画六个竖向同款列表再用 CSS grid 包一下；舱体确有独立灯角、抽屉唇和底部短纸，下台确实横跨1152px。不能生成 v05..v10、沙盒标语、原始 l10n keys、调试select、内页画廊控制器、Ruler/Active/Matte 验证栏。统计、导航或新产品能力不在本次任务中。

浏览器验收要测出六个568×128矩形及二列三行坐标；单击每舱时网格 bbox 保持，报告可见区 y510..760且不压第三排；hover短条为非零高度且 opacity>0，按钮各≥28px，状态字与4,280计数没有 …。两主题都需真实 WebKit 1280×800 PNG，初始简报报告完整、失败切换有红条与 ERROR、运行中不伪装完成，未知外部输出只走本页合法来源锚点。

对永久DOM做全main节点身份与MutationObserver双检，removedElements = 0；六份report、所有确认层和恢复键始终是初始对象。验证停止冒泡、暂停恢复、paused rerun、双击不双加、删除在途回调失效及多舱撤销。键盘 Tab、Enter/Space、Esc可完成同一流程，光学fallback/reduced-motion不丢信息；最终阶段再作Visual Traceback。本Stage1只提供可实现的设计决策，不能拿静态Markdown充当已通过渲染、Owner冻结或线上发布。
