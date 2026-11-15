# v04 · 精准运行台账 (topology-compact-pro-table)

## 1. Visual Metaphor & Archetype Lock

以 Linear / Raycast 的精密列表作为主路由，Flighty 的tabular读数作为次参考，System Settings作为按钮可读性兜底。锁定 macOS、VS-007、CL-008，AppTheme=PrecisionTable，四个维度是component、layout-navigation、typography-copy、motion-interaction。X五列对齐、Y inline master-detail sub-row、Z实心工作表配浅下沉详情；这是单屏列表，而非具有查询器和筛选器的新产品。

一个规整的表头和紧凑行使任务结果最快可扫描。任务字体SF Pro/PingFang SC 14px 500、内容13px、SF Mono12px读数、标题20px；不画巨大数字。status chips保留符号与短句；tail是ghost-pill，16px inline SVG（24×24 viewBox、stroke1.5、currentColor）配文字。只用1px行间线，不把每个cell做独立盒子。

## 2. Single P0 Focus & Initial Showcase State

P0=查看一次成功PR巡检的交付，默认 my-pr-patrol（第五条）展开240px master-detail subrow。初始六行均可见，标题「定时任务」，辅助文字「点击行查看最后一次执行汇报」。表头精确为任务名称、运行周期、累计/今日次数、最近状态、操作，不能用表头再展示任务数据。

启动固定badge序列为：daily-brief ● 成功 (1.8s)，daily-learning ● 成功 (2.4s)，aidata-pulse ▲ 耗时偏高 (14.2s)，linear-bot-bridge ● 运行中，my-pr-patrol ● 成功 (0.9s)，target-pr-review ✕ 失败 (exit 1)。全体active、无删除；右侧首键初始都是暂停。paused作为实际可切换状态实现，不把失败行预设为paused。

## 3. P1 / P2 Progressive Folding & Permanent DOM Contract

P1 的52px summary rows永久展示五列；P2 的summary/outputs/stages/logs只随单选subrow露出。initial HTML必须已有6个 pro-row-group、6个 subrow-report和footer的6个undo按钮，报告内容不依赖首次点击才加载。用data-open与aria-expanded驱动高度grid0fr/1fr，内层min-height:0；选择其他行收旧开新，选中行再次点击归零，不打开另一个panel。

删除将pro-row-group data-deleted设为true，零高度/inert但仍在文档中；footer说明被删除任务，露出对应的「撤销删除」。恢复依据固定job id而非当前DOM index，回原顺序，保留已发生的计数与暂停，subrow关闭，不抢其他打开行。Rerun、状态变更只写已有Text.data，不覆盖按钮icon或报告子元素；整个会话removedElements = 0、zero innerHTML rebuild，禁止模板克隆和remove/replaceChildren。

## 4. Measured Layout & 1280x800 Viewport Geometry

精确1280x800：main x32/y24为1216×752、padding24，content1168×704。pro-table-header48 + gap12 + pro-table-head-row32 + pro-table-rows552（6×52+240）+ gap24 + footer36 = 704。默认第五条下的报告与第六条均在首屏完整露出，不能让详情遮挡底行；初始scrollWidth=clientWidth、scrollHeight不超800，0px unintended overflow。macOS外框不在本页重画。

header row与每个group header采用相同grid、padding16和gap16；有效1136px=244+220+206+170+232+4×16。前四列左对齐，所有数字tabular，尾列right alignment。ghost-pill宽60/72/58、高30，gap8，总206，始终可见。行主体①–④至少888×52；报告link高32最小宽44，undo32高；任何触发/尾键/单据链接>= 28x28px。②③严格显示全量字符串，不折4,280、不以…处理184次。

240px subrow padding16，内宽1136；header24+gap8，上区64（summary 560、outputs552、gap24），再gap12，下区100（stage640、log472、gap24），padding32合计240。summary可两行但不超48px；stage五条20px行，每条标签、线段与耗时共享列，logs最多4×20px。link所在输出区有说明锚点，不能以超长URL撑列。若输入长于本库存，局部report滚动，不修改table grid或遮住按钮。

## 5. Dual-Theme Surface Polarity & Material Craft

PrecisionTable Light：canvas #F1F4F8，table #FFFFFF，ink #182130，secondary #526173，divider #E4E8EF，hover #F6F8FC，expanded #EFF3FC，subrow #F4F6FB，focus #4656AF。Dark：canvas #0E131F，table #182131，ink #F2F6FD，secondary #B2BED0，divider #344053，hover #202D43，expanded #253454，subrow #121C2C，focus #AFBCFF。table radius14，subrow inset edge1px #4656AF14 / #AFBCFF20；无玻璃、无浮卡投影群。

Light状态fg/bg按success #23603B/#E5F2E9、running #244F99/#E8F0FD、warning #775117/#FFF0D7、failed #A12B3E/#FCE7ED、paused #536174/#EAF0F6；Dark则 #A0DBB4/#203F2F、#B1CEFF/#233E65、#F3CF91/#443820、#FFAEBD/#4A2936、#BDCADA/#334258。低对比ghost键的文字仍用ink，失败chip不可只靠红色；hover后局部底色加强而不是新增操作。

Liquid Glass optical contract为blur0、displacement0、opacity1、IOR不适用，参考pro工具的精准并非玻璃镜片。Light/Dark变量跟data-theme；prefers-color-scheme提供缺省。高对比模式提高hairline与focus，不反转状态含义；render fallback无需图片、网络字体或canvas shader。

## 6. Apple Native Spring Physics & Row/Button Micro-Interactions

subrow开合420ms cubic-bezier(0.22, 1.35, 0.36, 1)，只有详情clip高度与inner translateY(-4px)发生弹性，52px行和读数保持静止。hover100ms表面染色；button press .98 scale80ms、release120ms。prefers-reduced-motion:reduce则切换1ms，取消位移/循环running glow；仍保留可感知的静态running标签。

三个动作先event.stopPropagation()，link/undo也隔离。暂停保存lastStatus、设⏸ 已暂停和继续；恢复原状态，不擅自修复失败。Rerun即时● 运行中，单次完成才累计/今日各+1并更新duration；pending期间禁重复rerun。paused仍可执行一次，但排程保持paused，结果写报告；删除invalidate generation，迟来的完成不更新已删除任务，撤销不重放运行。UI只反馈本页状态，无真实job、CloudKit或Linear请求。

pro-summary-trigger role=button/tabindex0/aria-controls/aria-expanded支持自身Enter/Space，group header仅role=group，controls区的keypress不触发行处理。收起report设inert，删除焦点迁往footer恢复，撤销聚焦原行；保留2px offset2的焦点环，不以overflow裁掉。一个aria-live状态节点汇报暂停/重跑/撤销，不把表格整段反复播报。

pro-summary-trigger横跨外grid的1–4列，grid-column:1/5并用subgrid；三个action buttons留在第5列兄弟区，不成为role=button的后代。无subgrid则按244/220/206/170px与16px gap回退；“聚焦行”均聚焦trigger。精密表的run feedback在1000ms一次性结算：六条耗时更新1.6s、2.1s、12.8s、0.6s、0.8s、1.0s，第三条warning与第六条exit 1保持，另外四条success。阶段按更新前后总耗时等比改值，bridge完成后为0.1/0.1/0.2/0.1/0.1s并写提交已确认，review尾两阶段未执行。同步修改既有摘要/日志，失败一次同样增计数；latestResult与排程pause独立，继续返回新结果而非陈旧pre-pause badge。

## 7. Production Data Inventory & Exact DOM Topology

精密表的输入按下面六条写在静态HTML；箭头只表述五列顺序，不在UI追加符号列：

- daily-brief → 每日简报 05:00 → 每天 05:00 · 下次 12h 后 → 累计 142 次 · 今日 1 次 → ● 成功 (1.8s) → 暂停 / Rerun / 删除。
- daily-learning → 每日学习推荐 04:15 → 每天 04:15 · 下次 11h 后 → 累计 98 次 · 今日 1 次 → ● 成功 (2.4s) → 暂停 / Rerun / 删除。
- aidata-pulse → AIData 数仓脉搏 04:00 → 每天 04:00 · 下次 11h 后 → 累计 186 次 · 今日 1 次 → ▲ 耗时偏高 (14.2s) → 暂停 / Rerun / 删除。
- linear-bot-bridge → Linear @bot 桥接 → 每 1m · 刚刚 16:45 → 累计 4,280 次 · 今日 184 次 → ● 运行中 → 暂停 / Rerun / 删除。
- my-pr-patrol → 我的 PR 巡检 → 每 5m · 2m 前 → 累计 860 次 · 今日 36 次 → ● 成功 (0.9s) → 暂停 / Rerun / 删除。
- target-pr-review → 特定人 PR 审查 → 每 5m · 4m 前 → 累计 312 次 · 今日 12 次 → ✕ 失败 (exit 1) → 暂停 / Rerun / 删除。

每subrow有h2「最后一次执行汇报 (Execution Report)」与四data-report-block。daily-brief summary「05:00 的五阶段聚合和投递已完成」；outputs TIA-448、TIA-431；stages ① 个人源采集0.3s、② L2-L3 入仓0.5s、③ Retro-ROI0.4s、④ 学习寻题0.3s、⑤ Brief 投递0.3s；logs `[05:00:01] INFO five stages passed` / `[05:00:01.8] INFO delivery done`。

daily-learning四块为「三题学习推荐已入收件箱」/ TIA-431 / 取候选0.4s、去重0.3s、匹配0.7s、编题单0.5s、投递0.5s / `[04:15:01] INFO questions=3`、`[04:15:02.4] INFO inbox updated`。aidata-pulse四块为「入仓阶段偏高，全轮仍完成」/ TIA-448 / ① 个人源采集1.2s、② L2-L3 入仓9.1s、③ Retro-ROI1.8s、④ 学习寻题1.3s、⑤ Brief 投递0.8s / `[04:00:10.3] WARN ingest latency`、`[04:00:14.2] INFO pulse acknowledged`。linear-bot-bridge四块为「本轮消息路由后等待提交」/ TIA-448注明最近产出 / 消息0.1s、去重0.1s、路由0.2s、提交进行中、确认未开始 / `[16:45:00] INFO bridge routing`、`[16:45:00.4] INFO bridge running`。

默认my-pr-patrol四块填「PR #311 检查巡检成功，结果已记录」/ PR #311 / PR读取0.2s、checks读取0.2s、差异0.1s、保存0.2s、通知0.2s / `[16:43:00] INFO PR311 inspected`、`[16:43:00.9] INFO patrol record saved`。target-pr-review填「PR #308 审查失败，评审提交未执行」/ PR #308 / PR读取0.2s、diff读取0.3s、审查0.6s失败、提交未执行、通知未执行 / `[16:41:00.5] INFO review launched`、`[16:41:01.1] ERROR exit=1 no review submitted`。耗时线以报告内最大已完成秒数为基准，未开始不是成功0s。

TIA/PR标签href只用核实的生产地址；本brief未给地址，所以必须降为当前报告内 #v04-evidence-{job}-{id} 锚点，聚焦已挂载产出说明。它仍是可交互link，不是假href="javascript:void(0)"、不新建屏幕、不猜Github仓库。

```html
<main class="precision-ops-panel topology-compact-pro-table">
  <section class="content">
    <div class="pro-table-header"><h1></h1><p></p></div>
    <div class="pro-table-head-row"><span>任务名称</span><span>运行周期</span><span>累计/今日次数</span><span>最近状态</span><span>操作</span></div>
    <div class="pro-table-rows">
      <article class="pro-row-group" data-job-row data-job="daily-brief">
        <header role="group"><div class="pro-summary-trigger" role="button"><strong data-col="title"></strong><time data-col="schedule"></time><span data-col="counts"></span><span data-col="status"></span></div><div data-col="actions"><button data-action="toggle-pause"></button><button data-action="rerun"></button><button data-action="delete"></button></div></header>
        <div class="subrow-report"><div class="subrow-clip"><h2></h2><div class="detail-upper"><p data-report-block="summary"></p><nav data-report-block="outputs"></nav></div><div class="detail-lower"><ol data-report-block="stages"></ol><pre data-report-block="logs"></pre></div></div></div>
      </article>
      <!-- pro-row-group共六个，全部字段、报告和独立id静态挂载 -->
    </div>
    <div class="pro-table-footer"><span aria-live="polite"></span><div class="pro-undo-bank"><button data-action="restore" data-job="daily-brief"></button><!-- 另五枚 --></div></div>
  </section>
</main>
```

## 8. Explicit Anti-Patterns & Verification Targets

精准表不允许two-page split、5-segment ring gauge或orbital layout；不能塞cron配置、额外工具栏筛选、新增指标或两列任务卡。禁 .caustic-veil、.ruler、Active-Matte、<select>测试选择器、sandbox disclaimers和innerHTML replacement；content直接孩子必须是声明的四个pro节点，不出现hero/fold-panel/secondary。

下游在WebKit1280x800 Light/Dark验证首屏六行第五报告、grid边缘全齐、三个ghost键一直可见；逐行展开四块汇报后收回。按钮不切换报告、pause/continue保留原状态、run只增1、删除和undo复用节点。MutationObserver全根removedElements=0，所有控件/links>=28×28，0px overflow，日志尾与数值无截断。Stage 1只完成文稿与重叠门禁，截图验收和独立Visual Traceback留给后续角色。
