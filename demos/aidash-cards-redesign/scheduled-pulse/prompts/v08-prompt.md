# v08 · 单色航务工作台 (topology-monospace-ops-console)

## 1. Visual Metaphor & Archetype Lock

从 Developer Workbench 的可读日志与 Flighty Chrono 的时序读数取材，做六条console job lines，而不是shell模拟器。macOS / VS-003 × VS-007 / CL-008 cyan remix；AppTheme=ChronoConsole，X五列工作读数、Y终端级report drawer、Z实心slate控制台。Top3选择Workbench、Flighty列表、Raycast操作胶囊，只提取信息工艺，不引入命令输入框、状态页或跑批功能。

行Title仍是14px SF Pro/PingFang，不将整屏中文强行等宽。周期、次数及duration用13px SF Mono / Menlo，标题20px，log12px；保证tabular-nums。semantic avionics pills带文字，三尾键为清晰bordered pills，24×24 inline SVG stroke1.5/currentColor，pause/rerun/trash实占16px，旁显示文字；禁止ASCII艺术、全绿终端或假命令提示符。

## 2. Single P0 Focus & Initial Showcase State

P0锁“看清桥接本轮进度”，initial load展开第四行linear-bot-bridge，报告明确仍在提交，不虚构完成耗时。其他报告都折叠；六行保持原始顺序，console band只显示「定时任务」与「点击任务查看最近汇报」。footer不是输入命令框，仅承载恢复删除。

初始readouts依次是 daily-brief ● 成功 (1.8s)、daily-learning ● 成功 (2.4s)、aidata-pulse ▲ 耗时偏高 (14.2s)、linear-bot-bridge ● 运行中、my-pr-patrol ● 成功 (0.9s)、target-pr-review ✕ 失败 (exit 1)。六个排程active未删除，首尾键文本「暂停」；暂停后的⏸ 已暂停是真实交互态而非另一个测试select。

## 3. P1 / P2 Progressive Folding & Permanent DOM Contract

P1是可比较的五列line-grid，P2的四块Execution Report在该行下，不新建终端窗。6个console-job-item、6个完整console-report-pane、console-command-bar的6枚恢复键必须在initial HTML存在；数据、SVG、logs节点全常驻。开合用data-expanded/aria-expanded、grid rows0fr/1fr与min-height0内壳，单展开；点击别行收旧开新，再点同一行全部关闭。

删除将原li的height与gap归零并inert，footer显示名称与「撤销删除」，不卸载。restore按稳定job id回原位置，保留暂停/计数，报告默认闭合，其他选中不变；被删是当前展开时清空选择。全根MutationObserver契约removedElements = 0，zero innerHTML rebuild；用Text.data更新读数，不用元素级textContent毁掉LED、link或log子结构。footer原有六个undo仅按队列切可见，不创建新的toast或button。

## 4. Measured Layout & 1280x800 Viewport Geometry

viewport1280x800，main x24/y24、1232×752、padding24；content1184×704。status-band40 + gap12 + col-legend28 + job-lines580（6×56 + 244px报告）+ gap12 + command-bar32 =704。initial第四抽屉全露且第五第六行不落窗外，0px unintended overflow；outer chooser绘macOS边框，本页不重画。溢出检查以scrollWidth/clientWidth真测，禁整体overflow:hidden作弊。

legend与line-grid共享左右16px、gap12：内宽1152，列246/226/214/184/234，sum1104+4×12=1152。首四列left，数字等宽不跳，最后right；动作宽64/74/58、高32、gap6，总208。①–④行主体面至少906×56可点；report link min44×30，undo32px高，所有hit target >= 28x28px。字体fallback SF Mono不存在则Menlo再ui-monospace，Title不做等宽；完整累计4,280/今日184必须容纳。

report244px含padding16、24pxh2、gap8、上区60px（summary560、outputs568、gap24）、gap12、下区108px（stage664、logs464、gap24），总244。stage五行20px+余8px缓冲，logs最多4行22px；上下两区按字重分层，不分裂出四张卡。运行中stage使用短label与文字状态，未开始显示空槽，不显示乱跳计时数字。

## 5. Dual-Theme Surface Polarity & Material Craft

ChronoConsole Light用canvas #EDF2F7、console #F9FBFE、ink #182737、muted #52687B、line #DCE5EF、hover #EEF5FC、expanded #E7F1FD、pane #EAF1F8、focus #145C89；Dark用canvas #0E1117、console #172331、ink #ECF5FF、muted #B1C5D8、line #354A5D、hover #20374B、expanded #25435A、pane #102332、focus #9EDAF8。console radius12、pane10，选中只一条细left rule，不绕整行发光。

Light chips success=#225E43/#E1F0E8、running=#205989/#E1EFFA、warning=#795418/#FAECD0、failed=#A22C45/#FBE5EC、paused=#52687C/#E4EDF5；Dark chips=#A4DBBA/#244632、#ABDAFF/#234A66、#F4CE89/#453B23、#FFB4C7/#4B2D3A、#BECFE0/#374F63。用圆点/警告/失败符号+文字，不为不同job编造颜色分类；cyan只用于focus、选中边线和running状态。

Liquid Glass在本案完全不启用：blur0、IOR不适用、displacement0、不透明控制台；pane是solid color不是黑洞渐变。data-theme优先，未指定随prefers-color-scheme；无网络字体、无backdrop嵌套、无canvas特效。键hover提高边缘对比，expanded背景增加一点蓝，不用粗1px围住每cell。

## 6. Apple Native Spring Physics & Row/Button Micro-Interactions

报告抽屉460ms cubic-bezier(0.22, 1.35, 0.36, 1)，外grid高度与inner translateY(-3px)同步，line读数位置静止；closed不先display:none。按钮press inset110ms、hover边缘120ms，无command palette飞入。prefers-reduced-motion时height1ms、零位移、running静态点，不能因为停动画而隐藏进行中标签。

toggle-pause、rerun、delete首句event.stopPropagation()，links/restore也不冒泡。暂停存原status、改⏸ 已暂停/继续，继续还原原status；rerun立刻● 运行中，在单次结算后累计与今日各+1并写duration。每job独立pending flag/generation防双击和删后回调；paused一次run只更新报告结果、最后仍paused，delete取消未提交run feedback，undo不启动真实运行。只操作当前文档，不访问真实调度器或私有telemetry。

console-summary-trigger role=button/tabindex0/aria-controls/aria-expanded，自身Enter/Space可开合；line-grid仅role=group；键区原生button键盘不经行逻辑。closed pane inert/aria-hidden，删除焦点去command-bar undo，恢复回该line。报告产出link点击聚焦同pane常驻说明，不改行选择；log可复制不充当toggle。aria-live播报短结果，而非每轮日志全文。

console-summary-trigger自身grid-column:1/5，前四列由subgrid继承；fallback为246/226/214/184px、gap12。第5列三个原生buttons是兄弟区，console group不再承担button语义；焦点回line就是回trigger。本页run在1000ms后结算，简报1.6s成功、学习2.1s成功、脉搏12.8s偏高、桥接0.6s成功、巡检0.8s成功、审查1.0s失败exit 1。stages按新旧总秒数比缩放，桥接完整五条0.1+0.1+0.2+0.1+0.1s且结论写提交确认完成，审查提交/通知仍未执行。既有结论和日志读数同步更换，失败也只计一次；latestResult独立于paused排程，resume应显示最新结算而非旧readout。

## 7. Production Data Inventory & Exact DOM Topology

console库存逐行标明五域，行内不要渲染以下job id或序号为新字段：

01 daily-brief ｜ 每日简报 05:00 ｜ 每天 05:00 · 下次 12h 后 ｜ 累计 142 次 · 今日 1 次 ｜ ● 成功 (1.8s) ｜ 暂停、Rerun、删除。

02 daily-learning ｜ 每日学习推荐 04:15 ｜ 每天 04:15 · 下次 11h 后 ｜ 累计 98 次 · 今日 1 次 ｜ ● 成功 (2.4s) ｜ 暂停、Rerun、删除。

03 aidata-pulse ｜ AIData 数仓脉搏 04:00 ｜ 每天 04:00 · 下次 11h 后 ｜ 累计 186 次 · 今日 1 次 ｜ ▲ 耗时偏高 (14.2s) ｜ 暂停、Rerun、删除。

04 linear-bot-bridge ｜ Linear @bot 桥接 ｜ 每 1m · 刚刚 16:45 ｜ 累计 4,280 次 · 今日 184 次 ｜ ● 运行中 ｜ 暂停、Rerun、删除。

05 my-pr-patrol ｜ 我的 PR 巡检 ｜ 每 5m · 2m 前 ｜ 累计 860 次 · 今日 36 次 ｜ ● 成功 (0.9s) ｜ 暂停、Rerun、删除。

06 target-pr-review ｜ 特定人 PR 审查 ｜ 每 5m · 4m 前 ｜ 累计 312 次 · 今日 12 次 ｜ ✕ 失败 (exit 1) ｜ 暂停、Rerun、删除。

六pane的共同内容类型是执行结论摘要、产出单据/PR links、各子阶段耗时条和关键日志尾部，h2逐条写「最后一次执行汇报 (Execution Report)」。简报pane：「简报五阶段完成，今日投递成功」；TIA-448、TIA-431；① 个人源采集0.3s、② L2-L3 入仓0.5s、③ Retro-ROI0.4s、④ 学习寻题0.3s、⑤ Brief 投递0.3s；`[05:00:01] INFO pipeline passed`、`[05:00:01.8] INFO briefing pushed`。学习pane：「三题已匹配并投递到收件箱」；TIA-431；取候选0.4s、去重0.3s、难度0.7s、编排0.5s、发送0.5s；`[04:15:01] INFO matched questions=3`、`[04:15:02.4] INFO learning push done`。

数仓pane：「14.2s完成，L2-L3入仓耗时偏高」；TIA-448；① 个人源采集1.2s、② L2-L3 入仓9.1s、③ Retro-ROI1.8s、④ 学习寻题1.3s、⑤ Brief 投递0.8s；`[04:00:10.3] WARN L2-L3 took 9.1s`、`[04:00:14.2] INFO pulse success`。默认桥接pane：「@bot消息已路由，提交阶段正在执行」；TIA-448明确为最近产出；取消息0.1s、去重0.1s、路由0.2s、提交进行中、确认未开始；`[16:45:00] INFO route accepted`、`[16:45:00.4] INFO bridge submitting`。

巡检pane：「PR #311 检查状态已巡检归档」；PR #311；PR0.2s、checks0.2s、差异0.1s、归档0.2s、通知0.2s；`[16:43:00] INFO PR311 read`、`[16:43:00.9] INFO checks archived`。审查pane：「PR #308 审查退出1，后续提交未执行」；PR #308；PR0.2s、diff0.3s、审查0.6s失败、提交未执行、通知未执行；`[16:41:00.5] INFO diff ready`、`[16:41:01.1] ERROR reviewer exit=1`。bar长度依本pane最大完成耗时，进行中/未开始用文字，不捏造新时长或输出。

本brief的TIA/PR只是给定标识，没有已核实外链：href绑定本pane内 #v08-output-{job}-{id}，实际聚焦输出说明，保持drawer。禁止javascript空链接、伪URL、新页面、真实Linear或GitHub调用。outline的ol里静态书写六个li，每个独立id及完整数据：

```html
<main class="chrono-workbench topology-monospace-ops-console">
  <section class="content">
    <header class="console-status-band"><h1></h1><span></span></header>
    <dl class="console-col-legend"><div><dt>任务名称</dt><dd></dd></div><div><dt>运行周期</dt><dd></dd></div><div><dt>累计/今日次数</dt><dd></dd></div><div><dt>最近状态</dt><dd></dd></div><div><dt>操作</dt><dd></dd></div></dl>
    <ol class="console-job-lines">
      <li class="console-job-item" data-job-row data-job="daily-brief">
        <div class="line-grid" role="group"><div class="console-summary-trigger" role="button"><span data-col="title"></span><time data-col="schedule"></time><span data-col="counts"></span><span data-col="status"></span></div><div data-col="actions"><button data-action="toggle-pause"></button><button data-action="rerun"></button><button data-action="delete"></button></div></div>
        <section class="console-report-pane"><div class="console-height-clip"><h2></h2><div class="console-result-register"><p data-report-block="summary"></p><nav data-report-block="outputs"></nav></div><div class="console-trace-register"><ol data-report-block="stages"></ol><pre data-report-block="logs"></pre></div></div></section>
      </li>
      <!-- 另外五条console-job-item完整静态挂载，不用运行时render函数 -->
    </ol>
    <footer class="console-command-bar"><span aria-live="polite"></span><div class="console-recovery-bank"><button data-action="restore" data-job="daily-brief"></button><!-- 五个同级恢复键 --></div></footer>
  </section>
</main>
```

## 8. Explicit Anti-Patterns & Verification Targets

航务控制台排除two-page split、5-segment ring gauge、orbital layout；没有假shell命令、测试状态下拉或新runner屏。禁.caustic-veil、.ruler、Active-Matte、<select>测试、sandbox disclaimers、innerHTML replacement；content父子如outline，不准hero、fold-panel、secondary。不能把“终端级”误解为全部10px小字或黑绿低对比。

Coding需在WebKit1280x800 Light/Dark截图看见全六行与第四pane；列legend与每行边缘一致、三键独立、六报告四块存在。开合及动作全根removedElements=0，rerun恰加一、pause/continue回原状态、delete/undo复用节点、点击links不收pane；键盘可达、targets>=28×28、无数字截断和0px overflow。Stage 1只承诺文稿可供实现，不把这些渲染验证当作已做。
