# v03 · 象牙值守账页 (topology-swiss-ledger-strips)

## 1. Visual Metaphor & Archetype Lock

将 scheduled-pulse 解释为一张瑞士排版的工作账页：标题、列题、六条ledger strip和末尾印记构成同一张纸。选择 macOS / VS-002 Warm Editorial & Swiss Ledger / CL-002，AppTheme=IvoryDuty；X是固定五列账项，Y是插入本行下方的纸页汇报，Z只允许实体纸面与薄纸袋阴影。参考优先级 Swiss ledger、Apple Wallet纸面、Readwise安静文字；不借它们的金融功能。设计探索限于版面、字形、状态与报告口袋。

任务文字用 SF Pro 14px 500，New York / Georgia仅用于22px masthead，数字为 SF Mono 12px tabular；其他说明13px。状态前导为6px方形beacon，但旁边仍印完整●/▲/✕文案。三个操作是有细边界的矩形ledger keys，radius5，不是药丸。inline SVG 24×24画直线暂停、回转箭头和桶，stroke1.4，保持16px光学尺寸，不画印章emoji。

## 2. Single P0 Focus & Initial Showcase State

P0 聚焦“PR审查为什么没交付”，初始第六条 target-pr-review 的纸袋滑出，标题仍为「定时任务」。六行全部在页内；不在masthead加另一个失败summary，不将失败任务移到第一位。初始仅一页汇报可读，别把“五阶段”拆成第二页。

逐条badge初值：每日简报 05:00＝● 成功 (1.8s)；每日学习推荐 04:15＝● 成功 (2.4s)；AIData 数仓脉搏 04:00＝▲ 耗时偏高 (14.2s)；Linear @bot 桥接＝● 运行中；我的 PR 巡检＝● 成功 (0.9s)；特定人 PR 审查＝✕ 失败 (exit 1)。所有累计/今日数以库存为准，六个首按钮均印「暂停」，没有任何初始删除项。

## 3. P1 / P2 Progressive Folding & Permanent DOM Contract

整页的P1层是一组列标题与六项账行，P2层为收在该条之下的paper-pocket slip。initial HTML就拥有6个 ledger-entry，每个内含完整四块slip；colophon中的6个恢复键亦常驻。用data-expanded和aria-expanded对应单展开逻辑，grid rows0fr/1fr控制袋高度；每次开另一行同时收上一行，点击当前账行则收其纸页。

不可用innerHTML rebuild、replaceChildren、HTML模板重建、节点remove实现任何过渡；removedElements = 0是整页观察器合同。文字改预留Text节点data，inline SVG与link element保留identity。删除用data-deleted归零该entry的高度与分隔线、不卸载；colophon显示「删除了一项 · 撤销删除」并激活最后删除项的恢复键。撤销回原账位，保留状态与计数且默认袋关闭，不打断别行的展开。删除当前袋时先把焦点交给恢复键，随后解除选中。

## 4. Measured Layout & 1280x800 Viewport Geometry

1280x800窗内账页main为x40/y24、1200×752，四周padding24；content1152×704。垂直精算：masthead48 + 空12 + column-head28 + strip-body564（6×60 + 一个204px纸袋）+ 空20 + colophon32 = 704。纸袋位于第六账行正下方也不能落出底边；chooser拥有系统画框，账页不复制浏览器导航或交通灯。初始0px unintended overflow，不能靠clip整页隐藏多余内容。

ledger-column-head与每条entry-face共享一份grid变量：行内左右12px，内容1128，列宽236/222/210/176/236，四个gap12=48，总1128。账名、周期、次数、状态均靠左，尾键组合向右。键宽64/74/58、高30、gap6，总208，末端不漂移；body trigger覆盖①–④的整块连续区域。报告单据链接高30、最小宽44，恢复键32高，行60高，所有动作/链接点击面积>= 28x28px。数列不折数字、不省4,280；周期中文保持13px正文。

204px slip设padding16，报告标题24+间距8+正文140；四块布局为上方两栏摘要与产出60px、下方两栏阶段与日志72px，间距8。阶段为五个并排小条槽，总宽680、各126.4、gap12，每槽文字容许两行、数值独立一行；余下报告日志在392px栏，gap48，总内宽1120。不要画五段圆环；五个小槽是一组阶段模块，不是五张卡。

## 5. Dual-Theme Surface Polarity & Material Craft

IvoryDuty Light用canvas #EEEAE2、paper #FAF7F2、ink #25251F、muted #625E53、rule #DCD5C8、hover #F3EEE4、expanded #F7F1E5、pocket #EFE7D7、focus #0F5132；Dark用canvas #121316、paper #20211F、ink #F3F0E8、muted #B8B3A8、rule #45443D、hover #2B2D28、expanded #2E3028、pocket #191B17、focus #A3D3B6。纸页外侧无粗框；袋缝是1px dotted #BAAD91 / #6D6B59，只在报告顶部出现。

方beacon与状态文字采用Light success #0F5132 on #E4ECE3、running #204D78 on #E5ECF4、warning #785516 on #F4EAD0、failed #922F2F on #F6E4DF、paused #615E55 on #EAE6DD；Dark对应 #AAD4B5/#293A2C、#ACCDF0/#293647、#E9CD8E/#403821、#F2B0A5/#432C28、#C5BFB1/#373830。每组字与背景必须达到正文4.5:1；不让brass装饰占满状态栏。

这里的 Liquid Glass 参数为无折射、无backdrop、IOR不适用、blur0、displacement0、opacity1。实体纸口袋用0 2px 4px #4F3D1912（dark #05060340）与顶部浅rim，不加载纸纹图片或网络字体。hover增加局部纸色，expanded加内凹而非发光框；Light/Dark经data-theme替换全套变量，系统prefers-color-scheme仅为未指定主题的默认。

## 6. Apple Native Spring Physics & Row/Button Micro-Interactions

纸页从袋口向下露出，clip壳开合480ms cubic-bezier(0.22, 1.35, 0.36, 1)，内部translateY(-5px)到0；标题和键位不弹跳，不使用纸片rotate3d造成字形透视。袋缝跟随高度，滑页opaque渐变只160ms。按ledger key时inset shadow加强90ms，hover120ms；prefers-reduced-motion把纸位移和高度过渡归1ms、所有闪光停用。

三个键的事件在首行调用event.stopPropagation()：暂停保存originalStatus并显示⏸ 已暂停/继续，恢复排程后返回原徽章；Rerun立即进入● 运行中，完成总数和今日数各+1，duration按新报告更新，不展开纸页；删除只折掉账项并在colophon提供撤销。每任务pending flag与generation token防重复run与删除后的晚回调；暂停期间手工重跑可完成，但排程标记仍暂停，不能因重跑重启周期。

ledger-summary-trigger role=button、tabindex0，aria-controls=本条slip；entry-face只用role=group，Space/Enter限定到自身；native buttons的键盘及report links的点击都不冒泡。关闭纸袋inert、aria-hidden，避免在不可见单据上落焦点；恢复后焦点回原face。产出点击只聚焦当前slip中的说明锚，不展开兄弟账项，无宿主或真实调度器副作用。

ledger-summary-trigger作为一个连续可点区域跨第1–4列，采用grid-column:1/5与subgrid；action keys仅占兄弟第5列。fallback使用236/222/210/176px和12px gap，任何焦点回账行均指trigger，避免role嵌套吞掉真实button。账页Rerun结算时间为1000ms；六账项新秒数分别1.6、2.1、12.8、0.6、0.8、1.0，成功/成功/耗时偏高/成功/成功/失败exit 1为明确结果。阶段秒数按新旧总数比例更新，桥接改0.1+0.1+0.2+0.1+0.1s且摘要写确认完成，审查提交/通知仍未执行。用已有行文更新摘要与日志，失败执行也计一次；lastResult保存本轮结果，paused是排程遮罩，继续展示最新lastResult而不是暂停前的旧值。

## 7. Production Data Inventory & Exact DOM Topology

账页六项的每行栏目必须按①至⑤写入，禁止用某条缺省值替补：

| 账项身份 | ① 任务名称 | ② 运行周期 | ③ 累计/今日次数 | ④ 最近状态 | ⑤ 操作键 |
| --- | --- | --- | --- | --- | --- |
| daily-brief | 每日简报 05:00 | 每天 05:00 · 下次 12h 后 | 累计 142 次 · 今日 1 次 | ● 成功 (1.8s) | 暂停 · Rerun · 删除 |
| daily-learning | 每日学习推荐 04:15 | 每天 04:15 · 下次 11h 后 | 累计 98 次 · 今日 1 次 | ● 成功 (2.4s) | 暂停 · Rerun · 删除 |
| aidata-pulse | AIData 数仓脉搏 04:00 | 每天 04:00 · 下次 11h 后 | 累计 186 次 · 今日 1 次 | ▲ 耗时偏高 (14.2s) | 暂停 · Rerun · 删除 |
| linear-bot-bridge | Linear @bot 桥接 | 每 1m · 刚刚 16:45 | 累计 4,280 次 · 今日 184 次 | ● 运行中 | 暂停 · Rerun · 删除 |
| my-pr-patrol | 我的 PR 巡检 | 每 5m · 2m 前 | 累计 860 次 · 今日 36 次 | ● 成功 (0.9s) | 暂停 · Rerun · 删除 |
| target-pr-review | 特定人 PR 审查 | 每 5m · 4m 前 | 累计 312 次 · 今日 12 次 | ✕ 失败 (exit 1) | 暂停 · Rerun · 删除 |

六张slip标题都叫「最后一次执行汇报 (Execution Report)」，内部四模块严格是结论摘要、产出单据/PR链接、子阶段耗时条、关键日志尾部。简报slip印「晨间聚合完成，简报与学习题单已送达」；链接TIA-448、TIA-431；阶段① 个人源采集0.3s、② L2-L3 入仓0.5s、③ Retro-ROI0.4s、④ 学习寻题0.3s、⑤ Brief 投递0.3s；日志 `[05:00:01] INFO aggregation done` / `[05:00:01.8] INFO delivery acknowledged`。

学习slip印「三题推荐去重后投递完成」/ TIA-431 / 读取候选0.4s、去重0.3s、匹配0.7s、题单0.5s、投递0.5s / `[04:15:01] INFO unique=3` / `[04:15:02.4] INFO learning receipt saved`。数仓slip印「本輪脉搏已完成，入仓9.1s偏高」/ TIA-448 / ① 个人源采集1.2s、② L2-L3 入仓9.1s、③ Retro-ROI1.8s、④ 学习寻题1.3s、⑤ Brief 投递0.8s / `[04:00:10.3] WARN warehouse took=9.1s` / `[04:00:14.2] INFO pulse stored`。

桥接slip印「消息已读取，@bot提交正在执行」/ TIA-448（上次已交付）/ inbox0.1s、去重0.1s、路由0.2s、提交进行中、确认未开始 / `[16:45:00] INFO bridge inbox ready` / `[16:45:00.4] INFO commit pending`。巡检slip印「PR #311 检查结果已记录」/ PR #311 / 读取0.2s、checks0.2s、比较0.1s、记录0.2s、通知0.2s / `[16:43:00] INFO checks fetched` / `[16:43:00.9] INFO patrol receipt written`。初始展开的审查slip印「PR #308 的审查进程退出码1，未提交评审」/ PR #308 / 读取PR0.2s、读取diff0.3s、审查0.6s失败、提交未执行、通知未执行 / `[16:41:00.5] INFO reviewer invoked` / `[16:41:01.1] ERROR reviewer exit=1`。各条宽度相对该报告最大已完成耗时；失败条为砖红，未执行为空槽而非0s成功。

提供给Coding的单据标识不是外部地址证明。没有核实URL则link href=#v03-{job}-output-{identifier}，指向同slip的永久说明标签；可点可聚焦，无新屏、不访问Linear/GitHub。不要为PR #308猜owner/repo。每条outline需静态按库存展开六份：

```html
<main class="ivory-duty-page topology-swiss-ledger-strips">
  <section class="content">
    <header class="ledger-masthead"><h1></h1><p></p></header>
    <section class="ledger-column-head"><span>任务名称</span><span>运行周期</span><span>累计/今日次数</span><span>最近状态</span><span>操作</span></section>
    <div class="ledger-strip-body">
      <section class="ledger-entry" data-job-row data-job="daily-brief">
        <div class="ledger-entry-face" role="group"><div class="ledger-summary-trigger" role="button"><strong data-col="title"></strong><time data-col="schedule"></time><span data-col="counts"></span><span data-col="status"></span></div><div data-col="actions"><button data-action="toggle-pause"></button><button data-action="rerun"></button><button data-action="delete"></button></div></div>
        <aside class="stitched-paper-slip"><div class="slip-height-clip"><h2></h2><div class="slip-upper-register"><p data-report-block="summary"></p><nav data-report-block="outputs"></nav></div><div class="slip-lower-register"><ol data-report-block="stages"></ol><pre data-report-block="logs"></pre></div></div></aside>
      </section>
      <!-- 同纸面六个静态ledger-entry，按02..06填入其完整报告 -->
    </div>
    <footer class="ledger-colophon"><small aria-live="polite"></small><div class="reversal-keys"><button data-action="restore" data-job="daily-brief"></button><!-- 五个其他任务的键常驻 --></div></footer>
  </section>
</main>
```

## 8. Explicit Anti-Patterns & Verification Targets

账页不能退回R1–R3 two-page split、5-segment ring gauge或orbital layout；不要虚构历史账库、配置页或附加字段。禁用 .caustic-veil、.ruler、Active-Matte、<select>状态测试、sandbox disclaimers以及innerHTML replacement；content直子树不得叫hero、fold-panel、secondary。边线仅为纸条分隔与action keys，不能给每数字建灰盒。

验收须记录Light/Dark在1280x800所有六账项和初始失败报告均完整：5列共用grid、每行3键独立响应、六袋各含四块、阶段名称与耗时不截断。全根MutationObserver removedElements=0，轮流展开后按下三键不意外翻袋；删除后撤销节点仍为同对象。键盘可展开与恢复、链接/动作>=28×28、零未预期overflow。这里写的是测试目标，Designer只执行prompt结构与独立性校验，不伪报浏览器测试PASS。
