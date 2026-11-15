# v09 · 安静值守纪事 (topology-editorial-chronicle-list)

## 1. Visual Metaphor & Archetype Lock

采用Calm Editorial Chronicle的排版节奏，但不做画报：一条克制banner、一张有hairline列节奏的list well、每行下的card-stock foldout。锁macOS / VS-002 editorial remix / CL-002 cool-ink，AppTheme=QuietChronicle，X横读五项、Y单行报告、Z实心纸井与暖卡纸。参考Top3为安静editorial列表、Things文字留白、Apple Settings列秩序；不借书签、历史文库或文章详情功能。探索typography、visual-style、component、motion。

banner用22px New York/Georgia，任务14px SF Pro/PingFang600，周期/次数13px，logs12px SF Mono；不能用大标题撑半屏。status是薄药丸，三尾键为低噪声ghost buttons但平时可辨认，hover只提高强度不从无到有。inline SVG24×24、stroke1.4、round joins，以16px图形画pause/rerun/trash并保留文字，不放heading emoji。

## 2. Single P0 Focus & Initial Showcase State

P0=确认每日简报投递，默认第一条daily-brief展开216px暖纸report-card；六条任务同时可扫描，banner仅写「定时任务」和「点击任务，查看最后一次汇报」。不额外摆“今日纪事”长文、重复计数或第二个总结卡。

首屏状态以真实库存六行排序：每日简报 05:00 ● 成功 (1.8s)；每日学习推荐 04:15 ● 成功 (2.4s)；AIData 数仓脉搏 04:00 ▲ 耗时偏高 (14.2s)；Linear @bot 桥接 ● 运行中；我的 PR 巡检 ● 成功 (0.9s)；特定人 PR 审查 ✕ 失败 (exit 1)。初始active未删除，首键都是暂停。paused不预置为失败的替身，使用⏸ 已暂停切换状态支持。

## 3. P1 / P2 Progressive Folding & Permanent DOM Contract

P1六条row-summary-bar固定五列，P2四块报告收在同一行下的row-report-card。initial HTML已经写入6个chronicle-row及6份完整card和trash-pill内6枚restore，点击不再拼HTML。data-open/aria-expanded单选；旧行收回，新行展开，自身再点收起；card的grid高度0fr/1fr由min-height0 clip内壳配合，关闭后inert。

delete把整条article标data-deleted、height归零并从Tab路径排除，保持原DOM；trash pill显示最近删项与「撤销删除」。恢复按job id置回原位、保留次数和排程paused，card关闭且不抢另行展开；删当前行则清空选择。多个删除的恢复按钮原先存在，队列只变可见属性。removedElements = 0、zero innerHTML rebuild，禁止remove、replaceChildren和父级textContent；数值变化只改预留Text.data，所有icon/link节点持续保留。

## 4. Measured Layout & 1280x800 Viewport Geometry

1280x800内main x36/y24、1208×752、padding24，content1160×704。banner52 + gap16 + list-well576（6×60+216报告）+ trash-pill32 + foot28 = 704，trash与foot不另加外margin。第一折页与第六任务都应可见，0px unintended overflow，不通过整页overflow:hidden伪装尺寸；outer chooser而非本页负责macOS框与主题控制。

row-summary-bar左右16px，净1128；五列238/222/210/176/218，gap16×4=64，总1128，前四左齐、⑤right。ghost键宽60/70/56、高32、gap8，总202，即使未hover也保留完整文字与可点面积；①–④行主体至少894×60。报告link最小44×30，trash restore32高，所有row/尾键/link hit target >= 28x28px。不要让secondary退后成为10px灰字，运行时间和4,280次数完整可读，无数字ellipsis。

216px foldout padding16；h2高24、gap8、正文152。左440px区放summary两行、8px间距及30px产出link；右656px区为90px五条阶段、10px间隔、52px日志，gap32，内宽1128。五条阶段18px行，日志最多两行22px加8px内空；暖纸区别于list的冷白，不给四块内容各套边框。纸下角radius10，1px折边只在报告底部，不能造成截字。

## 5. Dual-Theme Surface Polarity & Material Craft

QuietChronicle Light canvas #F0F2F3、well #FFFFFF、ink #253039、muted #5C6A74、hairline #E3E7EA、hover #F5F7F8、expanded #F6F2E9、cardstock #F4EEE1、focus #3B647D；Dark canvas #171D23、well #222C33、ink #F3F6F8、muted #BDC7CF、hairline #3D4B55、hover #2D3B45、expanded #38382E、cardstock #2B2C25、focus #B0D6EA。报告轻影light0 2px 6px #59421E12、dark0 2px 6px #070C0E44，list只用hairline不做六个浮卡。

五种pill的Light fg/bg为success #275F42/#E6F1E8、running #2A5B88/#E6F0F8、warning #77521C/#F6ECD6、failed #983243/#F7E6EB、paused #5A6874/#E8EDF1；Dark为 #ADD8BC/#2B4333、#B6D8F5/#2B4358、#EED09B/#453C28、#F2B3C1/#4A303B、#C9D3DC/#3B4B58。banner文字不抢红色故障语义，饱和度只在小徽章和focus点上。

本案的Liquid Glass设定是none：blur0、displacement0、IOR不适用、opaque paper；稿纸不是暗色玻璃上叠暗色玻璃。hover与expanded仅调上述solid tokens；data-theme驱动双主题，未指定随系统prefers-color-scheme。不采用在线字体、纹理图、噪点shader或材质调试切换栏。

## 6. Apple Native Spring Physics & Row/Button Micro-Interactions

warm foldout开合490ms cubic-bezier(0.22, 1.35, 0.36, 1)，内卡translateY(-5px)->0、grid高度同步；不让标题字在展开时变号，不rotate整张纸。文字opacity180ms，ghost键hover140ms加强底色与描边、press .98 scale90ms。prefers-reduced-motion:reduce取消位移和running循环，开合1ms即时布局，保留静态徽章。

所有toggle-pause、rerun、delete处理器先event.stopPropagation()，undo和link也阻止行开合。暂停缓存previousStatus、改⏸ 已暂停/继续，继续恢复缓存，不能消除原来的失败。rerun立刻● 运行中，完成单轮才累计/今日各+1并更新duration；pending锁与generation token防多次结算和删后迟到更新。paused中一次run完成仍paused、最新result写报告；删除取消未提交反馈，undo只恢复本页对象而非重启任务。

chronicle-summary-trigger role=button/tabindex0/aria-controls/aria-expanded，自身Space/Enter展开；summary-bar仅role=group，原生三键key事件不连带toggle。关闭report内容inert/aria-hidden，删除前焦点移到trash restore，恢复回原row；focus2px offset2不能被list clip吞掉。点击report的label聚焦本报告产出说明，文本选择和log复制不收纸页，aria-live只反馈短动作句。

chronicle-summary-trigger覆盖grid前四列（grid-column:1/5）并subgrid继承，tail第五列独立兄弟，避免role button内再含controls。fallback238/222/210/176px与16px gap，恢复后的row focus只落trigger。每轮Rerun在1000ms结算，六任务新耗时锁定1.6s、2.1s、12.8s、0.6s、0.8s、1.0s；前二/桥接/巡检成功，脉搏仍偏高，审查仍exit 1。阶段值按新总时长比例更新，bridge改五条0.1/0.1/0.2/0.1/0.1s并写提交确认已完成，review两后项仍未执行。已有摘要及logs刷新，失败尝试也累计一次；latestResult接受新结算、paused仅作排程遮罩，继续不得显示陈旧成功或running缓存。

## 7. Production Data Inventory & Exact DOM Topology

纪事的每行五项按如下清单保持原词面；这不是另一个timeline，每个job只出现一次：

- 任务=每日简报 05:00，data-job=daily-brief；时间=每天 05:00 · 下次 12h 后；次数=累计 142 次 · 今日 1 次；末次=● 成功 (1.8s)；操作=暂停 | Rerun | 删除。
- 任务=每日学习推荐 04:15，data-job=daily-learning；时间=每天 04:15 · 下次 11h 后；次数=累计 98 次 · 今日 1 次；末次=● 成功 (2.4s)；操作=暂停 | Rerun | 删除。
- 任务=AIData 数仓脉搏 04:00，data-job=aidata-pulse；时间=每天 04:00 · 下次 11h 后；次数=累计 186 次 · 今日 1 次；末次=▲ 耗时偏高 (14.2s)；操作=暂停 | Rerun | 删除。
- 任务=Linear @bot 桥接，data-job=linear-bot-bridge；时间=每 1m · 刚刚 16:45；次数=累计 4,280 次 · 今日 184 次；末次=● 运行中；操作=暂停 | Rerun | 删除。
- 任务=我的 PR 巡检，data-job=my-pr-patrol；时间=每 5m · 2m 前；次数=累计 860 次 · 今日 36 次；末次=● 成功 (0.9s)；操作=暂停 | Rerun | 删除。
- 任务=特定人 PR 审查，data-job=target-pr-review；时间=每 5m · 4m 前；次数=累计 312 次 · 今日 12 次；末次=✕ 失败 (exit 1)；操作=暂停 | Rerun | 删除。

每row-report-card标题「最后一次执行汇报 (Execution Report)」，四块内容为summary、outputs、stages、logs。简报写「今日简报五阶段完成，已投递」；TIA-448与TIA-431；① 个人源采集0.3s、② L2-L3 入仓0.5s、③ Retro-ROI0.4s、④ 学习寻题0.3s、⑤ Brief 投递0.3s；`[05:00:01] INFO morning aggregation ready` / `[05:00:01.8] INFO brief delivered`。学习写「三道推荐题已去重并送达」；TIA-431；读取0.4s、去重0.3s、匹配0.7s、题单0.5s、投递0.5s；`[04:15:01] INFO three questions matched` / `[04:15:02.4] INFO learning delivered`。

数仓写「本轮脉搏完成，入仓延迟需关注」；TIA-448；① 个人源采集1.2s、② L2-L3 入仓9.1s、③ Retro-ROI1.8s、④ 学习寻题1.3s、⑤ Brief 投递0.8s；`[04:00:10.3] WARN warehouse latency=9.1s` / `[04:00:14.2] INFO pulse result stored`。桥接写「消息路由完成，本轮提交仍在进行」；TIA-448说明为上一轮产出；消息0.1s、去重0.1s、路由0.2s、提交进行中、确认未开始；`[16:45:00] INFO route resolved` / `[16:45:00.4] INFO bridge waiting acknowledgement`。

巡检写「PR #311 最近checks已记录」；PR #311；PR0.2s、checks0.2s、比较0.1s、保存0.2s、通知0.2s；`[16:43:00] INFO checks retrieved` / `[16:43:00.9] INFO patrol result written`。审查写「PR #308 审查退出1，评审没有提交」；PR #308；PR0.2s、diff0.3s、执行0.6s失败、提交未执行、通知未执行；`[16:41:00.5] INFO review execution started` / `[16:41:01.1] ERROR exit=1 submission skipped`。阶段条相对本卡最大完成耗时，不把未开始涂为成功。

链接使用 #v09-output-{job}-{id} 指向本report永久产出说明，点击聚焦并保留选中；brief未给经验证外部URL，不虚构PR仓库或真实生产证据，不加历史屏幕，不访问调度器。六article的每一份报告都完整静态存在，下面是指定亲子树：

```html
<main class="quiet-chronicle-panel topology-editorial-chronicle-list">
  <section class="content">
    <div class="chronicle-banner"><h1></h1><p></p></div>
    <section class="chronicle-list-well">
      <article class="chronicle-row" data-job-row data-job="daily-brief">
        <header class="row-summary-bar" role="group"><div class="chronicle-summary-trigger" role="button"><span data-col="title"></span><time data-col="schedule"></time><span data-col="counts"></span><span data-col="status"></span></div><div data-col="actions"><button data-action="toggle-pause"></button><button data-action="rerun"></button><button data-action="delete"></button></div></header>
        <div class="row-report-card"><div class="chronicle-fold-clip"><h2></h2><div class="chronicle-copy-column"><p data-report-block="summary"></p><nav data-report-block="outputs"></nav></div><div class="chronicle-record-column"><ol data-report-block="stages"></ol><pre data-report-block="logs"></pre></div></div></div>
      </article>
      <!-- 六个chronicle-row按既定序静态填写；每卡完整四块与独立id -->
    </section>
    <aside class="chronicle-trash-pill"><span aria-live="polite"></span><div class="chronicle-restore-keys"><button data-action="restore" data-job="daily-brief"></button><!-- 另五恢复键 --></div></aside>
    <footer class="chronicle-foot"><small>点击行查看汇报</small></footer>
  </section>
</main>
```

## 8. Explicit Anti-Patterns & Verification Targets

纪事不能使用two-page split、5-segment ring gauge、orbital layout；别把editorial变成巨幅数字、长篇文章或history库。禁.caustic-veil、.ruler、Active-Matte、<select>测试控制、sandbox disclaimers、innerHTML replacement和DOM卸载；content直子树不能有hero/fold-panel/secondary。Ghost键不得仅hover可见，纸折边不得裁掉链接。

后续WebKit1280x800双主题验证首屏6行+第一报告、五列与三键；依次展开六报告各四块，动作不连带开合，pause/continue回原status、rerun次数只+1、delete/undo同Element。整个根removedElements=0，links/三键/恢复>=28×28、焦点可达、数值完整且0px溢出。Designer此刻只检查文稿，不填写虚构截图或浏览器PASS。
