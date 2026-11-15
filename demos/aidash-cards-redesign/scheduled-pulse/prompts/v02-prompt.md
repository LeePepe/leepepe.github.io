# v02 · 雾面浮条 (topology-liquid-glass-rows)

## 1. Visual Metaphor & Archetype Lock

参考 macOS 浮动工具条的光泽，但把六条任务做成平行、独立的 Floating Liquid Glass Row Strips：一条清晰的磨砂横条，下方解开半透明托盘。坐标锁 macOS / VS-004 / CL-004 cool-sage remix，X 保持五字段横读，Y 每次只解开一个报告，Z 为同级玻璃条和不透明读数岛。AppTheme=FogStrip；探索材质、组件与运动，不设计额外导航。Owner 明确要求本案 glass rows，作为当前候选例外，不推广为生产内容全面玻璃化。

美感靠条间12px空气和连续柔亮外缘，不靠背景花纹。字体选择 SF Pro 14px任务名、13px内容、12px日志、21px标题；数值仅启用 tabular-nums。按钮内 inline SVG 24×24 / stroke1.6 / round cap，暂停、重跑、删除图标各16px，保留文字；禁止用emoji充当玻璃控制件。参考路线为浮动glass strip，其次System Settings状态药丸、再其次原生popover磨砂边；不要混成桌面天气小组件。

## 2. Single P0 Focus & Initial Showcase State

打开即展示 AIData 数仓脉搏 04:00 的报告托盘，P0 是解释14.2s为何偏高；运行中桥接只保留小蓝色徽章，不抢第二个主角。工具条写「定时任务」及「点击任务展开汇报」，无状态大仪表。六条任务从每日简报排至特定人PR，初始无删除、无暂停。

首屏状态严格为 daily-brief「● 成功 (1.8s)」、daily-learning「● 成功 (2.4s)」、aidata-pulse「▲ 耗时偏高 (14.2s)」、linear-bot-bridge「● 运行中」、my-pr-patrol「● 成功 (0.9s)」、target-pr-review「✕ 失败 (exit 1)」。每条右端均有 暂停 / Rerun / 删除；失败行仍可暂停，不初始写继续。

## 3. P1 / P2 Progressive Folding & Permanent DOM Contract

P1 是不折叠的六条横条，P2 是选中条的结论、产出、阶段和日志；没有详情页或右侧inspectors。initial HTML 静态包含6个 li、6个 frosted tray及undo-toast-rail中6个恢复按钮，所有报告内容已存在。设置 data-open、data-paused、data-deleted 改表现；关闭托盘用常驻grid壳 0fr，打开1fr，inner min-height:0；removedElements = 0，zero innerHTML rebuild，禁止 JS 创建/销毁HTML片段。

仅有一个托盘可以占高度，点击另一行交换 open 标记，点击自身关闭。删除将原li高度与其占用间距一起归零，不移除节点；恢复轨就地出现「已删除…」和「撤销删除」。六个恢复入口按删除队列中最后一条显示，不堆出新toast节点。恢复放回原位置，保留该任务计数与暂停状态，不抢当前托盘；若删除当时的打开条，则保持无报告选中。使用已有文本节点更新徽章/计数，不能用父元素 textContent 丢失icon。

## 4. Measured Layout & 1280x800 Viewport Geometry

1280x800 内 main x24/y24、1232×752，padding24，content1184×704。glass-toolbar-strip48，下面16px留白；glass-row-stack占600（6×56 + 5×12间距 + 一个204px托盘）；再12px和undo rail28，总704。展开托盘跟随所属li增加204px，不能绝对定位盖住后续任务。外框由chooser提供，本页不重复系统标题栏；初始无滚动条，0px unintended overflow。

每strip左右18px后剩1148；五列宽242、224、214、186、218，gap16×4=64，合计1148。①②③④左对齐，⑤右对齐；三个动作宽60/70/56、高32、gap8，总202。行触发面①–④至少914×56，不要只让小chevron可点。产出标签至少32×28，恢复入口高28，所有hit targets >= 28x28px。最宽运行次数含4,280及184完整显示，不能用…；五列从不因某一行打开而改变尺寸。

204px托盘内padding16：24px报告标题，8px间隔，140px内容；内容grid为左400px结论与32px高输出链接，右720px阶段/日志，gap32（内宽1152）。五条直线阶段每行18px共90px，后接6px间距及44px两行日志。阶段标签13px，日志12px/20px；如果系统CJK字体稍宽，摘要允许两行，禁止整体缩放或横向挤压尾操作。

## 5. Dual-Theme Surface Polarity & Material Craft

FogStrip Light tokens：canvas #EAF0EE，glass tint #F8FCFAE6，opaque island #F5F9F7，ink #172822，muted #51655C，rim #FFFFFFCC，hover #FFFFFFF2，open #F4FCF8F2，tray #EDF6F0EB，accent/focus #176447。Dark tokens：canvas #14201B，tint #263B32E6，island #24362D，ink #F1FAF5，muted #B1C8BC，rim #D6F6E033，hover #304B3FF2，open #2D483AF2，tray #21382DEB，accent #9CD7B4。下投影light 0 4px 14px #173B2512，dark 0 5px 16px #06120D44；扩展托盘radius0 0 14px 14px，不做叠加白线。

徽章Light success=#245C3C/#E4F1E6、running=#205C89/#E4F0FB、warning=#795214/#FFF0D4、failed=#992C3B/#FCE8EE、paused=#52645B/#E8EFEB；Dark success=#A7DEB8/#233F2E、running=#AFD6FF/#223F56、warning=#F4D08A/#493A20、failed=#FFB0BF/#4B2A36、paused=#BFCEC4/#34483D。玻璃上每块徽章用不透明底，文字对比不得交给桌面壁纸决定。

光学限定 backdrop-filter:blur(20px) saturate(125%)，IOR概念1.45、rim1px、bevel8px、displacement0；不加载SVG折射滤镜，WebKit fallback是上述实心island色与柔边，不声称实现Snell物理。所有玻璃壳只采样实心canvas：row面与report面是上下相邻的兄弟paint区域，无玻璃父壳；toolbar也不铺在条上。保留内容读数的opaque岛，防glass sampling glass。reduced transparency / 不支持backdrop时改完全不透明，行排列及颜色语义不变；data-theme覆盖系统外观，不放主题切换器到本页。

## 6. Apple Native Spring Physics & Row/Button Micro-Interactions

解开托盘以500ms cubic-bezier(0.22, 1.35, 0.36, 1)驱动高度与translateY(-8px)->0；只在内层移动，glass backdrop固定，避免模糊采样抖动。收起同500ms，内容淡出160ms，不提前display:none。行hover外缘亮度变化120ms，不放大条宽；尾按钮press translateY(1px)90ms，释放150ms。prefers-reduced-motion时高度直接切换1ms、零位移/闪烁，running仍显示静态蓝点与文字。

行监听只处理非控制区的点击；toggle-pause、rerun、delete的handler均 event.stopPropagation()，restore与output links也隔离。暂停缓存previous badge，继续回到缓存状态；按Rerun立刻● 运行中，固定本页反馈完成后累计/今日各增1并写新耗时。每job有pending token防双击计数，暂停中的一次运行只更新报告、排程徽章回⏸ 已暂停；删除使未提交token失效，恢复不补执行。无需网络请求或宿主任务启动。

每条glass-summary-trigger有role=button、tabindex0、aria-controls指向独有tray；glass-face仅role=group；Enter/Space仅由自身target触发，三按钮用原生button独立键盘行为。收起tray用inert防隐形Tab；删除焦点移至可见恢复button，撤销后回对应strip。aria-live只播报本次状态文本，避免每次展开把完整日志朗读一遍。

glass-summary-trigger的可聚焦面占五列grid的1/5范围，内部subgrid沿用前四宽度；第5列action是它的兄弟，不嵌进button角色。旧引擎以§4四列宽+16px gap实现等价grid；所有返回strip的focus均落trigger。每轮Rerun在1000ms后交付本页新读数：简报成功1.6s、学习成功2.1s、数仓偏高12.8s、桥接成功0.6s、巡检成功0.8s、审查仍失败exit 1（执行1.0s）。完成阶段同比例调整到新总耗时，bridge改五条0.1、0.1、0.2、0.1、0.1s并注明提交确认结束，review后两条仍未执行；更新原有日志和结论而非追加报告。失败也属于一次已执行计数。latestResult始终存最新结算，paused仅叠加排程显示，避免继续把旧失败/旧running缓存拿回。

## 7. Production Data Inventory & Exact DOM Topology

横条01 data-job=daily-brief：①每日简报 05:00；②每天 05:00 · 下次 12h 后；③累计 142 次 · 今日 1 次；④● 成功 (1.8s)；⑤暂停、Rerun、删除。

横条02 data-job=daily-learning：①每日学习推荐 04:15；②每天 04:15 · 下次 11h 后；③累计 98 次 · 今日 1 次；④● 成功 (2.4s)；⑤暂停、Rerun、删除。

横条03 data-job=aidata-pulse：①AIData 数仓脉搏 04:00；②每天 04:00 · 下次 11h 后；③累计 186 次 · 今日 1 次；④▲ 耗时偏高 (14.2s)；⑤暂停、Rerun、删除。

横条04 data-job=linear-bot-bridge：①Linear @bot 桥接；②每 1m · 刚刚 16:45；③累计 4,280 次 · 今日 184 次；④● 运行中；⑤暂停、Rerun、删除。

横条05 data-job=my-pr-patrol：①我的 PR 巡检；②每 5m · 2m 前；③累计 860 次 · 今日 36 次；④● 成功 (0.9s)；⑤暂停、Rerun、删除。

横条06 data-job=target-pr-review：①特定人 PR 审查；②每 5m · 4m 前；③累计 312 次 · 今日 12 次；④✕ 失败 (exit 1)；⑤暂停、Rerun、删除。

每个tray强制四块：执行结论摘要、产出单据/PR、各子阶段耗时条、关键日志尾部。默认展开aidata-pulse填「04:00 脉搏完成，入仓阶段9.1s，占用本轮主要耗时。」；产出TIA-448；阶段 ① 个人源采集1.2s / ② L2-L3 入仓9.1s / ③ Retro-ROI1.8s / ④ 学习寻题1.3s / ⑤ Brief 投递0.8s；日志 `[04:00:10.3] WARN L2-L3 latency=9.1s`、`[04:00:14.2] INFO pulse receipt TIA-448`。条长按9.1s最大值，不画健康百分比环。

另五个完整托盘的数据分别为：简报「五阶段通过，晨间简报已送达」/ TIA-448与TIA-431 / ① 个人源采集0.3s、② L2-L3 入仓0.5s、③ Retro-ROI0.4s、④ 学习寻题0.3s、⑤ Brief 投递0.3s / `[05:00:01] INFO stages=5`、`[05:00:01.8] INFO briefing sent`；学习「三道推荐已放入Linear收件箱」/ TIA-431 / 收集0.4s、去重0.3s、匹配0.7s、编排0.5s、投递0.5s / `[04:15:01] INFO selected=3`、`[04:15:02.4] INFO delivered`；桥接「@bot路由进行中，尚未完成提交」/ TIA-448标注上次产出 / 读消息0.1s、去重0.1s、路由0.2s、提交进行中、确认未开始 / `[16:45:00] INFO routing`、`[16:45:00.4] INFO submit pending`；巡检「PR #311 的检查状态已归档」/ PR #311 / 读取0.2s、检查0.2s、差异0.1s、归档0.2s、通知0.2s / `[16:43:00] INFO checks read`、`[16:43:00.9] INFO patrol saved`；审查「PR #308 执行退出，评审没有提交」/ PR #308 / PR0.2s、diff0.3s、审查0.6s失败、提交未执行、通知未执行 / `[16:41:00.5] INFO review started`、`[16:41:01.1] ERROR exit=1`。进行中和未执行项不伪填耗时，不把最近产出伪装本次已完成。

链接保留可点标签，未有可信外部地址时绑定本报告内常驻产出说明锚点 #v02-output-{job}-{id}，滚动/聚焦到对应说明；不虚构PR所属仓库，不新开详情屏。六报告的heading均为「最后一次执行汇报 (Execution Report)」。下方为必须静态落实的父子结构，×6说明须在HTML中展开为六个li，而非前端动态克隆：

```html
<main class="fog-strip-panel topology-liquid-glass-rows">
  <section class="content">
    <nav class="glass-toolbar-strip"><h1></h1><span></span></nav>
    <ol class="glass-row-stack">
      <li class="glass-job-strip" data-job-row data-job="daily-brief">
        <div class="glass-face" role="group"><div class="glass-summary-trigger" role="button"><span data-col="title"></span><time data-col="schedule"></time><span data-col="counts"></span><span data-col="status"></span></div><div data-col="actions"><button data-action="toggle-pause"></button><button data-action="rerun"></button><button data-action="delete"></button></div></div>
        <section class="frosted-report-tray"><div class="tray-clip"><h2></h2><div class="tray-readout-island"><p data-report-block="summary"></p><nav data-report-block="outputs"></nav><ol data-report-block="stages"></ol><pre data-report-block="logs"></pre></div></div></section>
      </li>
      <!-- 另五个glass-job-strip永久兄弟节点，依域顺序填入全部字段和报告 -->
    </ol>
    <aside class="undo-toast-rail" aria-live="polite"><p></p><div class="undo-button-bank"><button data-action="restore" data-job="daily-brief"></button><!-- 另五枚恢复按钮 --></div></aside>
  </section>
</main>
```

## 8. Explicit Anti-Patterns & Verification Targets

雾面案排除 two-page split、5-segment ring gauge、orbital layout，绝不把六条玻璃横条摆成漂浮星系。不得出现 .caustic-veil / .ruler / Active-Matte / <select>测试控制 / sandbox disclaimers；禁止hero、fold-panel、secondary直接挂content，禁止innerHTML replacement和任何节点detach。没有背景斑马、连续流光、玻璃套玻璃，也不隐藏删除键。

Stage 2 对1280x800双主题逐项证据：六行五列对齐、默认第三托盘可完整阅读；六条切换均保持单展开，四块报告均存在；所有按钮click/keyboard不连带展开；Rerun计数恰增1、删除/撤销保持Element identity。全根MutationObserver必须removedElements=0，scrollWidth-clientWidth=0、文字不截断、links及三尾键>=28×28。截图与真实渲染检查属于Coding/Reviewer，Stage 1不得把此清单写成已通过的测试。
