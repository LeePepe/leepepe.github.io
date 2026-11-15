# v01 · 晨笺双袋 (topology-pocket-folio-stack)

## 1. Visual Metaphor & Archetype Lock
把定时脉搏做成一册放在桌面的双层文件袋：上袋装分钟工作的薄纸，下袋存晨间交付的厚笺，右侧圆形验印与底部抽出的回单属于同一册。锁定 desktop / macOS 26；VS-002 瑞士触感账本，CL-008 的靛蓝识别色落在暖纸上，组件 CP-002、仪表 DV-003、物理过渡 MI-006。X＝一个选中任务在自己的纸条内展开；Y＝快慢两袋纵向分层、回执下藏；Z＝后纸、当前纸、前袋唇、控制浮层四级。SWWallet 提供叠卡关系，Things 3 提供安静文字密度，CleanShot X 提供紧凑工具感，Alcove 仅借鉴凹口收纳。候选 AppTheme 名为 R3-PocketFolio；这是探索坐标，不冻结全产品主题。

## 2. Single P0 Focus & Initial Showcase State
首屏停在「每日批处理 2」下袋，唯一 P0 是个人数仓晨报行内的最新执行结果。该行已抽出 40px，显示 04:01 完成；右侧印章中心为 5/5，下方写「阶段通过」，不是五个任务的健康比例。上袋三张纸只露任务名、节律和最近完成时间，下袋的每日学习推荐露出 04:15 / 已投递 3 题。时钟固定 11月15日 04:15。receipt-tray 默认只露 40px 拉手与「执行回执」字样，五阶段和三题正文藏在袋内。每个任务名称只在所属纸条出现一次，不在冠栏、印章和回单再打印全名。

## 3. P1 / P2 Progressive Folding & Permanent DOM Contract
P1 留给两个袋口的节律标题和环的一个阶段提示，P2 是当前行的操作与回执正文。所有五个 job-row、快慢两页、五个 SVG circle 段及包含晨报记录和学习投递的 receipt-sheet 必须在初始 HTML 解析时存在；收起只改变位置和 inert / aria-hidden，不卸载节点。两页始终并列存在，选中纸条展开，其余纸条收为 40px。点击环段同步照亮原有对应阶段行，开启回单时将行内阶段说明让位，避免同一套明细两份并排。事件只更新 class、dataset、CSS 变量和既有文本叶；禁止 innerHTML、outerHTML、replaceChildren、insertAdjacentHTML。快袋选择与慢袋选择共用一个 selectedJobId；再次点击或 Esc 将纸条归袋，焦点回到原按钮。

## 4. Measured Layout & 1280x800 Viewport Geometry
在 1280x800 内将主册定为 x=100、y=88、1080x624px，外部未占用面积 34.19%，明确超过 >=22% whitespace。主册内边距 24px，content 为 1032x576：pulse-crown 高40，间隔16，dual-pocket-well 高408，间隔16，receipt-tray 高96。well 内为 816px 纸袋区 +24px 空气 +192px 印章湾；两袋各196px、间距16，收起条40px，展开条最多108px。回单展开会把 well 变为232px、tray 变为272px，保持总高576；此时只露纸头：快袋132px＝24px组标题+3×36px任务头，慢袋84px＝24px组标题+2×30px任务头，两袋间16px，原行操作正文归袋。动作途中用固定外框内的 transform 而非推高 main。回单正文左右两栏 460/460px、间隙24，每段/题行32px；名称列允许两行，数据列不省略。袋唇凹口半径14px、深14px，纸角16px，容器角26px。控制默认32px高，环段可用36x36px透明命中面，任何命中区域 >=28x28px；SF Pro 文本13/15/20px，中心读数32px。将可见叶子与焦点描边留在24px内边距内，禁止用 body overflow:hidden 掩盖超界，所有状态要求 0px unintended scroll overflow。

## 5. Dual-Theme Surface Polarity & Liquid Glass / Paper-Pocket Craft
R3-PocketFolio 的 Light 语义值：desk #F4F1EB、well #EAE7E1、paper #FFFEFB、ink #242B36、muted #5D6570、accent #4E59B9、success #286349、warning #8A570C、focus #0A65CF；Dark 对应 #10151F、#1B2432、#2A3546、#F2F5FB、#BCC6D6、#B7BEFF、#9FDDB7、#F0C780、#85BBFF。纸与袋都是不透明实面，暗色前纸比内井亮，不做灰色透明罩。袋口用独立前唇 Shape/clip-path 切出中心内凹半圆，唇边叠 0.5px inner specular highlight：Light #FFFFFFCC / Dark #FFFFFF24；环境阴影三停为 Light 0 1px 2px #1B27300A, 0 8px 18px #1B273010, 0 22px 42px #1B273014，Dark 用 #00000018/#00000024/#00000030。遮挡次序必须能看见后纸上缘而不遮字。仅冠栏的节律控制可有功能玻璃：IOR 1.5、bevel 10px、blur 8px、saturation 140%、rim 0.5px，不叠玻璃、不做色散花纹；Safari 或 reduced-transparency 使用 well 实色替代。所有时刻、5/5、3 题、14s 用 tabular-nums，按钮白字配深 accent，Dark 按钮用 desk 深字。

## 6. Apple Native Spring Physics & Micro-Interactions
晨笺的纸条选中向上抽40px，回单沿 Y 轴升起176px；两个动作均采用 cubic-bezier(0.22, 1.35, 0.36, 1)，480ms，背纸依次用20ms差错位但不延迟可用性。悬停只令命中的纸头 peek translateY(-6px)，移开回原位，hover 不抢选中权。环由五个常驻 circle 构成，viewBox 0 0 160 160、cx/cy=80、r=56、stroke=6、pathLength=100；每段 stroke-dasharray="16 84"，stroke-dashoffset 为0/-20/-40/-60/-80，整环旋转-90°，stroke-linecap="round"。hover/键盘焦点增亮该段，不改变5/5；点击打开并聚焦对应阶段。立即运行只对当前 job 生效，按钮旁已有 aria-live 先显示已排队，再运行中，最后刚刚完成 · 耗时 14s；调度在内存里推进，不连接宿主或 Linear，重复触发在完成前 disabled，切换纸条不会把结果写给另一任务。prefers-reduced-motion: reduce 时去掉弹性超调、peek和错峰，120ms opacity 或直接定位；信息、点击与键盘完全保留。

## 7. Production Data Inventory & Exact DOM Topology
双袋资料按以下位置绑定，ID 不作为界面标题：

| 纸袋 / 标识 | 唯一名称 | 频率 | 最近记录 |
|---|---|---|---|
| 上袋 · linear-bot-bridge | Linear @bot 桥接 | 每 1 分钟 | 04:14 完成 |
| 上袋 · my-pr-supervisor | 我的 PR | 每 5 分钟 | 04:10 完成 |
| 上袋 · pr-auto-review | PR 自动审查 | 每 5 分钟 | 04:10 完成 |
| 下袋 · aidata-digest | 个人数仓晨报 | 每日 04:00 | 04:01 · 5/5 阶段通过 |
| 下袋 · daily-learning | 每日学习推荐 | 每日 04:15 | 04:15 · 已投递 3 题 |

回单左栏按 collect → ① 个人源采集、normalize_merge → ② L2-L3 入仓、retro_roi → ③ Retro-ROI、learning_topics → ④ 学习寻题、digest_push → ⑤ Brief 投递排列，每项状态通过，不编造独立耗时。右栏标题「学习投递 · Linear TIA · 3/3」包含三条拟真题目：如何让增量入仓保持幂等？；怎样区分 Cache 命中率与上下文占比？；如何用证据区分实现缺陷与规格缺口？。这些是给离线选型的固定题目输入，不声称读取了线上 issue，UI 不显示这句交接说明，也不生成假 TIA 编号或外链。每日学习不是五阶段管线。

采用如下父子轮廓，不把指定子节点塞进统一模板。图标用24x24 currentColor inline SVG、1.6px圆角笔画，圆印章附可读 caption 与阶段按钮名。

```html
<main class="scheduled-card topology-pocket-folio-stack">
  <section class="content">
    <header class="pulse-crown"><h1></h1><time></time></header>
    <div class="dual-pocket-well">
      <article class="pocket-sheet fast-folio"><h2></h2><div class="job-row" data-job="linear-bot-bridge"></div><div class="job-row" data-job="my-pr-supervisor"></div><div class="job-row" data-job="pr-auto-review"></div></article>
      <article class="pocket-sheet daily-folio"><h2></h2><div class="job-row" data-job="aidata-digest"></div><div class="job-row" data-job="daily-learning"></div></article>
      <aside class="ring-seal-bay"><svg class="five-stage-ring"></svg><output></output><p class="stage-caption"></p></aside>
    </div>
    <footer class="receipt-tray"><button class="receipt-handle"></button><article class="receipt-sheet"><ol class="digest-stage-lines"></ol><ol class="linear-question-lines"></ol></article></footer>
  </section>
</main>
```

## 8. Explicit Anti-Patterns & Verification Targets
此册不允许 .caustic-veil、.ruler、Active/Matte bars、<select> 测试开关、沙盒免责文案、五点 orbital 星图，以及 innerHTML 节点替换。拒绝把两个袋做成五个等重瓷砖，或以纯透明磨砂替代纸唇；底部 tray 是卡内回单，不是 macOS 浮动导航。外层 chooser 独占主题、窗口红黄绿、画廊选择，卡内不加这些控件。

Writer 必验四个交互状态，每个都取 Light/Dark 1280x800 截图：S0 初始晨报下袋 / 5/5 / 回单收起；S1 点上袋我的 PR 后只有该纸抽出，日批双标题仍可读；S2 展开回单并点③，左五段与右三题完整、对应段高亮；S3 对当前任务运行，记录已排队→运行中→完成并用 Esc 归袋。保存各状态中所有 Interactive Element 对象身份，节点数和引用不得改变；验证键盘、inert 的隐藏内容不获焦、Reduce Motion、对比度 >=4.5:1、零数字省略、零原始本地化 key 与 0px 意外横纵滚动。截图与像素验证由 Stage 2 提供，本 Prompt 不冒充已渲染验收。
