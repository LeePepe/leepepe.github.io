# v05 · 天青折页 (topology-split-accordion-drawer)

## 1. Visual Metaphor & Archetype Lock

借 Things 3 的 Airy Paper Accordion：六条任务在一张清爽的sheet上，打开一条就从其底部露出带小切口的notched paper-lip报告。topology名中的split仅指同一任务的summary/report两部分，绝不是拆成两个页面或两组任务。macOS / VS-005 / CL-006；AppTheme=SkyFold，X五项直接可见、Y一个纸抽屉、Z实心sheet与柔和袋口。这轮探索布局呼吸、组件和动效，Things 3只提供留白参考，不引入checkbox、待办列表或新增功能。

字体SF Pro 14px 500任务名、13px正文、12pxSF Mono日志、22px标题；数列tabular。无多色任务icon，三尾键用24×24 inline SVG暂停、rerun回箭、删除桶，stroke1.5、round joins，实占16px，文字仍常显。Things式低噪声来自64px行内的垂直留白，不能靠隐藏运行次数赢得空间。

## 2. Single P0 Focus & Initial Showcase State

默认展开第二条 daily-learning 的纸口袋，P0是“看清三题推荐是否已投递”。其余五报告收拢，全部六任务依次留在首屏。header只写「定时任务」和「点开任务查看汇报」，不加第二份学习题库或另一个详情入口。

初始完整状态为每日简报05:00 ● 成功 (1.8s)、每日学习推荐04:15 ● 成功 (2.4s)、AIData数仓脉搏04:00 ▲ 耗时偏高 (14.2s)、Linear @bot桥接 ● 运行中、我的PR巡检 ● 成功 (0.9s)、特定人PR审查 ✕ 失败 (exit 1)；屏幕任务Title按§7的空格原样写。六条未暂停，三按钮从暂停起，不把失败行自动写继续；没有删除记录。

## 3. P1 / P2 Progressive Folding & Permanent DOM Contract

P1是每条task-line的五列；P2全部落在本条notched-report-pocket里，不分出下一屏。每个task-sheet-item、六个报告的四模块、deleted-recovery-bar的六个undo入口在initial HTML就存在。折叠壳通过grid-template-rows 0fr/1fr、内部min-height0和inert管理；单展开，重复点击收起、点击新行收旧开新。

删除给原task-sheet-item标data-deleted，使整体高度/行边距归零，节点仍常驻；recovery bar露出任务名称与「撤销删除」。恢复只解除标记回原序位、保留计数和paused，默认收起且不抢另一打开项。最后删除项的undo按钮切换可见，不在每次操作后动态append toast。所有动态值改已存在Text.data，徽章壳、SVG和links都不替换；removedElements = 0、zero innerHTML rebuild及零replaceChildren是不可谈判的动画基础。

## 4. Measured Layout & 1280x800 Viewport Geometry

目标1280x800：main x28/y20、1224×760，padding24，content1176×712。header52 + gap16 + sheet-list596（六条64px与一个212px袋）+ gap16 + recovery32 = 712。行之间不用大gap，靠任务内部18px上下空气；袋增加正常流高度，不absolute覆盖后续行。首屏看见底行和恢复栏，0px unintended overflow，body不能裁切来伪装适配。

task-line两侧16px，净宽1144；grid五列246/226/214/178/216，gap16×4，合计1144。首四列左齐、⑤right；pill按钮宽60/70/56、高32、gap8，总202。①–④整片任务面可点击，至少912×64；links用32高、最小44宽、恢复键32高，全体hit target >= 28x28px。周期和次数按13px完整一行，含4,280及今日184，禁止任何数字ellipsis。

212px纸袋padding16，顶部24px标题+gap8，下方148px内容。左440px区放两行summary和output链接；右672px区含五阶段18px条列90px、8px空与50px日志，gap32，内宽1144。两个结论区块以字重/间距区分，不加四个小灰框。纸口8×4px notch由顶部伪元素绘制，位于留出的边缘空间，不覆盖Title或触发目标。

## 5. Dual-Theme Surface Polarity & Material Craft

SkyFold的Light：canvas #F3F6F9、sheet #FFFFFF、ink #202B35、muted #5A6B78、divider #E3EAF0、hover #F2F7FC、expanded #EEF5FC、pocket #F6FAFE、accent/focus #245D98；Dark：canvas #151D26、sheet #202C38、ink #F0F6FC、muted #B4C4D3、divider #3B4B5A、hover #293D50、expanded #29435B、pocket #1B2D3D、accent #A4D0FF。sheet radius18、pocket下角12、lip inset rim1px #FFFFFF / #D5E7F226；shadow0 3px 7px #35516F10（dark #07101A44），不用整页渐变。

柔和徽章在Light为success #286243/#E7F3EB、running #265F98/#E7F2FE、warning #7D571B/#FFF1D7、failed #A43145/#FCE8EE、paused #536779/#E8EFF5；Dark为 #A6DDBA/#274536、#AFD6FF/#254362、#F4D391/#483921、#FFB6C4/#4C2C39、#BDCFE0/#35495B。不要将Things的天蓝用到所有按钮，只有focus、rerun hover与当前袋口少量着色。

本案Liquid Glass optical参数明确关闭：blur0、IOR不使用、displacement0、完全不透明paper。玻璃风格的高亮只是一条0.5px视觉rim，不用backdrop-filter；无图片纹理、无外部字体依赖。data-theme决定两套色，系统prefers-color-scheme作默认；reduced transparency自然采用相同实心表面，不另加材质开关。

## 6. Apple Native Spring Physics & Row/Button Micro-Interactions

notched pocket开/关统一520ms cubic-bezier(0.22, 1.35, 0.36, 1)，内页translateY(-7px)->0，切口和袋唇留在容器顶边；字和图标不scale、不rotate。task hover染色140ms，键press scale(.97)80ms、release140ms，袋影从浅到深180ms。prefers-reduced-motion:reduce取消所有位移，以1ms切换高度，running只保持静态状态。

pause/continue、Rerun、delete均使用event.stopPropagation()，禁止它们触发task-line开合；链接与undo同样隔离。暂停记住前一badge，文字变⏸ 已暂停/继续；继续恢复原badge。rerun立刻● 运行中，完成后各+1到累计/今日、写最新耗时；paused执行一次后依然paused，错误不冒充成功。每job锁定in-flight generation，重复run不重复计数，删除取消未提交反馈，恢复只恢复已有状态。

things-summary-trigger role=button、tabindex0、aria-expanded与aria-controls绑定口袋，task-line只role=group；Enter/Space要检查自身event.target，native按钮保持键盘独立。收起内容inert、aria-hidden，避免hidden links参与Tab；删除先将焦点送恢复栏，撤销后返回任务行。报告内容可复制，点击日志或产出不导致袋合起，aria-live以简洁状态句反馈动作。

things-summary-trigger占外grid第1–4列并继承subgrid，原生三键只放第5列兄弟节点；不让button语义包住button。回退四列246/226/214/178px、gap16，restore后的“任务行焦点”就是trigger。本页的一次重跑1000ms结算，新的六耗时锁定1.6s、2.1s、12.8s、0.6s、0.8s、1.0s；脉搏仍偏高、审查仍exit 1，其他均成功。已有完成阶段依新/旧总时长同比缩放；桥接0.1+0.1+0.2+0.1+0.1s，结论改提交确认完成，审查两后续阶段仍未执行。刷新原日志与摘要并为失败尝试也加一次计数；排程paused与latestResult分存，暂停后的重跑不重启排程，继续也不恢复旧报告结果。

## 7. Production Data Inventory & Exact DOM Topology

纸页库存以下列契约写入每条 [data-job-row]；括号注明id但不作为额外可见栏：

每日简报 05:00（daily-brief）：周期「每天 05:00 · 下次 12h 后」；次数「累计 142 次 · 今日 1 次」；状态「● 成功 (1.8s)」；右尾「暂停」「Rerun」「删除」。

每日学习推荐 04:15（daily-learning）：周期「每天 04:15 · 下次 11h 后」；次数「累计 98 次 · 今日 1 次」；状态「● 成功 (2.4s)」；右尾「暂停」「Rerun」「删除」。

AIData 数仓脉搏 04:00（aidata-pulse）：周期「每天 04:00 · 下次 11h 后」；次数「累计 186 次 · 今日 1 次」；状态「▲ 耗时偏高 (14.2s)」；右尾「暂停」「Rerun」「删除」。

Linear @bot 桥接（linear-bot-bridge）：周期「每 1m · 刚刚 16:45」；次数「累计 4,280 次 · 今日 184 次」；状态「● 运行中」；右尾「暂停」「Rerun」「删除」。

我的 PR 巡检（my-pr-patrol）：周期「每 5m · 2m 前」；次数「累计 860 次 · 今日 36 次」；状态「● 成功 (0.9s)」；右尾「暂停」「Rerun」「删除」。

特定人 PR 审查（target-pr-review）：周期「每 5m · 4m 前」；次数「累计 312 次 · 今日 12 次」；状态「✕ 失败 (exit 1)」；右尾「暂停」「Rerun」「删除」。

每袋h2必须为「最后一次执行汇报 (Execution Report)」，包含摘要、outputs链接、stages条、logs四块。简报：「05:00 聚合结束，简报投递完成」/ TIA-448、TIA-431 / ① 个人源采集0.3s、② L2-L3 入仓0.5s、③ Retro-ROI0.4s、④ 学习寻题0.3s、⑤ Brief 投递0.3s / `[05:00:01] INFO sources committed`、`[05:00:01.8] INFO brief sent`。默认学习袋：「三道学习题已完成匹配并送达」/ TIA-431 / 读候选0.4s、去重复0.3s、匹配难度0.7s、编推荐0.5s、送达0.5s / `[04:15:01] INFO matched=3`、`[04:15:02.4] INFO learning sent`。

数仓袋：「入仓9.1s偏高，脉搏全轮已完成」/ TIA-448 / ① 个人源采集1.2s、② L2-L3 入仓9.1s、③ Retro-ROI1.8s、④ 学习寻题1.3s、⑤ Brief 投递0.8s / `[04:00:10.3] WARN L2-L3 slow=9.1s`、`[04:00:14.2] INFO pulse finished`。桥接袋：「消息已路由，桥接提交正在进行」/ TIA-448标为上次产出 / 读消息0.1s、去重复0.1s、选路0.2s、提交进行中、回执未开始 / `[16:45:00] INFO messages routed`、`[16:45:00.4] INFO awaiting commit`。

巡检袋：「PR #311 的checks已巡检并归档」/ PR #311 / PR0.2s、checks0.2s、对比0.1s、归档0.2s、通知0.2s / `[16:43:00] INFO patrol checks ready`、`[16:43:00.9] INFO record committed`。审查袋：「PR #308 审查退出码1，提交阶段未执行」/ PR #308 / PR0.2s、diff0.3s、审查0.6s失败、提交未执行、通知未执行 / `[16:41:00.5] INFO diff loaded`、`[16:41:01.1] ERROR review terminated exit=1`。阶段都是直条+文字值，按本报告最大已完成秒数定长，未执行保持空线和说明。

产出链接可用本袋内 #v05-note-{job}-{id} 定位已存在说明（本brief无经核实外部URL）；不得编造PR repo或启动真实Linear、调度器。点击label聚焦产出锚，保留本页和当前展开状态。结构落实为六个静态item，示意注释不是运行时循环许可：

```html
<main class="sky-fold-panel topology-split-accordion-drawer">
  <section class="content">
    <header class="things-header"><h1></h1><p></p></header>
    <section class="accordion-sheet-list">
      <div class="task-sheet-item" data-job="daily-brief" data-job-row>
        <div class="task-line" role="group"><div class="things-summary-trigger" role="button"><span data-col="title"></span><time data-col="schedule"></time><span data-col="counts"></span><span data-col="status"></span></div><div data-col="actions"><button data-action="toggle-pause"></button><button data-action="rerun"></button><button data-action="delete"></button></div></div>
        <aside class="notched-report-pocket"><div class="paper-clip"><h2></h2><div class="paper-left-copy"><p data-report-block="summary"></p><nav data-report-block="outputs"></nav></div><div class="paper-right-detail"><ol data-report-block="stages"></ol><pre data-report-block="logs"></pre></div></div></aside>
      </div>
      <!-- 六个固定task-sheet-item；02..06带独立报告、链接和controls id -->
    </section>
    <nav class="deleted-recovery-bar"><span aria-live="polite"></span><div class="sheet-recovery-keys"><button data-action="restore" data-job="daily-brief"></button><!-- 五枚对应恢复键 --></div></nav>
  </section>
</main>
```

## 8. Explicit Anti-Patterns & Verification Targets

天青不采用two-page split、5-segment ring gauge、orbital layout；不要借“split”偷换成高频/每日左右两页。禁 .caustic-veil、.ruler、Active-Matte、<select>测试状态、sandbox disclaimers、innerHTML replacement，content直子结构不用hero/fold-panel/secondary。袋口切角只做装饰，不能裁掉控件或遮到运行数。

Coding的证据应覆盖WebKit1280x800 Light/Dark，6条五列/3键、默认第二袋的四块可见、全部六袋可开可收。行外操作不改变展开、pause与resume就地更新、rerun仅一轮计数、delete/undo复用节点，全页removedElements=0；键盘与焦点恢复可靠，全部links/buttons>=28×28、零数字省略号、0px意外overflow。Stage 1不宣称已渲染截图，Independent Reviewer仍需Visual Traceback。
