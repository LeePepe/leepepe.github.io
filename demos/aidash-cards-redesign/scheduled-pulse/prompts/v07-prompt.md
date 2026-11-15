# v07 · 静音值守机架 (topology-tactile-ops-rack)

## 1. Visual Metaphor & Archetype Lock

参考 CleanShot 的克制utility panel与音频机架的recessed LED，做六个横向slot，不做音频仪表或旋钮。macOS / VS-003 Precision Studio / CL-003 desaturated metal，AppTheme=SilentRack；X五列工位、Y单个铰链汇报bay、Z金属面板和凹入舱。路线Top3为CleanShot快捷面板、Audio-Rack触觉键、Raycast可读状态；不继承这些工具的业务按钮。维度限material、component、motion、typography。

金属质感用垂直很浅的双色渐变与细内缘，绝不使用拉丝图片。SF Pro14px任务名、13px内容、SF Mono12px日志、20px面板标题；status LED是6px凹点加完整文字。右侧三键为tactile segmented-style cluster，各键仍是真实button、各有间隙，24×24 inline SVG以1.6px描边画pause/rerun/trash，16px图形旁保留文字。不是一个不可区分的三段toggle。

## 2. Single P0 Focus & Initial Showcase State

初始打开第三slot aidata-pulse，P0解释耗时偏高而非制造警报墙。bezel只写「定时任务」和「点击任务查看执行汇报」，六条任务正常依域顺序排列；不把实时桥接LED做循环心跳抢注意力，也不重复顶部故障卡。

六slot初值完整为每日简报 05:00 ● 成功 (1.8s)、每日学习推荐 04:15 ● 成功 (2.4s)、AIData 数仓脉搏 04:00 ▲ 耗时偏高 (14.2s)、Linear @bot 桥接 ● 运行中、我的 PR 巡检 ● 成功 (0.9s)、特定人 PR 审查 ✕ 失败 (exit 1)。全部active未删除，首键暂停；暂停态⏸ 已暂停由交互到达，不用失败状态替代。

## 3. P1 / P2 Progressive Folding & Permanent DOM Contract

P1六块slot-face不隐藏，P2为本slot的bay加相邻log strip组成的完整报告。initial HTML已含6个rack-slot、6个slot-report-bay、6个slot-log-strip以及restore dock中6枚undo；每报告的四内容块已就位。bay与log作为同一逻辑Execution Report两段，用同一个data-open同步高度及aria-controls的两个id，report bay以aria-owns关联log footer；只允许一个slot开，点同slot关闭。

bay壳grid0fr/1fr，日志footer也有常驻clip，closed时两者inert/aria-hidden；open时共同占238px。删slot只切data-deleted、高度与行gap归零而不remove，dock亮起「已删除… · 撤销删除」。Undo按job id回原位、保留计数与暂停，report默认关闭、不抢现有选中；删除选中slot后选择为空。全根removedElements = 0，zero innerHTML rebuild；更新状态只写预置Text.data/attributes，禁止替换LED、按钮或日志节点。

## 4. Measured Layout & 1280x800 Viewport Geometry

1280x800窗内main x40/y24、1200×752、padding24，content1152×704。bezel40 + gap12 + bays616（6×58+5×6+238）+ gap8 + restore28 = 704。报告插在选中slot正下，后续slot顺延，初始六slot与完整bay/log都可见；restore dock最少28高。0px unintended overflow，不准用整页clip吞掉机架底部，外层chooser画系统chrome。

slot-face左右16px后1120；grid宽234/216/206/172/228，gap16×4，总1120。首四左齐，tail右齐；分段键宽64/74/58、高32、gap4，总204，hit targets全>=28×28。整块①–④触发面至少876×58，不用LED作为唯一入口。report链接30px高最小44宽，restore28高；完整14.2s、exit 1、4,280与184不截断，数值tabular。

238px报告分为bay190与log-strip48。bay含padding16上下、h2=24、gap8、上区52、gap10、下区64，合计190；内宽1120，上区summary560/outputs536/gap24。下区五并排stage槽，各214.4宽gap12，槽中文字可两行和独立数字。footer48含顶部gap8及40px日志内容（两行20px），左右16px；这两段在视觉/ARIA上属于同一报告，关闭时日志不能独自露在summary外。

## 5. Dual-Theme Surface Polarity & Material Craft

SilentRack Light canvas #E8ECEF、metal #F1F4F6、ink #202A33、secondary #55636E、rim #FFFFFF、seam #CDD6DD、hover #E7EFF5、open #E0EAF2、bay #DCE4EA、log #D3DEE5、focus #245F89；Dark canvas #111820、metal #25323D、ink #F2F6FA、secondary #B9C7D2、rim #DCEEFF26、seam #465866、hover #2E4353、open #345063、bay #182833、log #13212C、focus #A6D8FA。金属面仅metal->hover 8%混合的垂直光线，bay用inset 0 2px 5px #15283820 / #050D1466，radius8。

五态LED与文字Light success #245D3B/#DFEFE5、running #1D5B8B/#E0EEF9、warning #7E5418/#F9EBCF、failed #A1313D/#F8E4E9、paused #536475/#E1E9F0；Dark success #A7DDB9/#234231、running #ACD9FF/#24475F、warning #EACD91/#453A23、failed #FFB7C0/#4B2E39、paused #C0CFDA/#3A4F5F。LED仅短程box-shadow 0 0 0 2px内凹，禁止霓虹散射盖住正文。

本案不是Liquid Glass：blur0、displacement0、IOR不适用、金属opacity1；tactile键由双色solid背景与inset shadow形成。Light/Dark用data-theme，缺省prefers-color-scheme，reduced transparency无变化。expanded的铰链感来自顶部1pxrim，不在文字上施加透视，不在bay外再包一层glass。

## 6. Apple Native Spring Physics & Row/Button Micro-Interactions

逻辑report共用440ms cubic-bezier(0.22, 1.35, 0.36, 1)开合bay与footer的grid高度，内容translateY(-4px)->0；“hinged”仅指上缘装饰lip展开，不rotateX正文。文字opacity160ms，分段键press inset加强90ms/释放130ms，hover120ms金属边缘变亮。prefers-reduced-motion:reduce关闭LED呼吸和位移，bay/log用1ms高度切换，running语义仍可读。

三个真实button先event.stopPropagation()再操作，restore和link同样隔离。暂停存prePauseStatus、显示⏸ 已暂停并将键改继续；继续回存储状态。Rerun立即● 运行中，结算一轮才累计/今日+1、更新duration；pending防重复触发。paused手动run后保持paused，仅报告更新；delete invalidate run token，迟到结算不可修改被删slot，restore不重放副作用。不上网、不接宿主scheduler或实际PR评审。

rack-summary-trigger role=button、tabindex0，Enter/Space仅自身target响应；slot-face仅role=group，aria-expanded准确并controls两个报告片段。native分段键键盘事件不冒泡到行；bay与log收起均inert。删slot焦点移恢复dock，恢复回face，focus-ring2px offset2不被clip遮掉；链接激活只聚焦本报告产出说明，不能导致收bay。

rack-summary-trigger横跨grid-column:1/5，用subgrid继承234/216/206/172px和16px gap；不支持时显式复制这些四列。分段三键在兄弟第5列，绝不落在另一button语义内；返回face的焦点均落trigger。Rerun反馈延迟1000ms，六slot新耗时为1.6s、2.1s、12.8s、0.6s、0.8s、1.0s；第三依然warning，第六仍exit 1，其余success。已完成阶段按新总/旧总等比变化，bridge更新0.1/0.1/0.2/0.1/0.1s并注明提交确认完成，review后两项仍未执行。摘要与log strip原节点内容同步刷新，失败尝试也增一次。latestResult持续更新，而paused仅改变排程可见状态，继续不得复活旧running值。

## 7. Production Data Inventory & Exact DOM Topology

机架固定六slot五列；此表的job id只用于data-job，不显示为编号列：

| slot | ①任务 | ②时间/周期 | ③次数 | ④状态读数 | ⑤独立键 |
| -- | -- | -- | -- | -- | -- |
| daily-brief | 每日简报 05:00 | 每天 05:00 · 下次 12h 后 | 累计 142 次 · 今日 1 次 | ● 成功 (1.8s) | 暂停 · Rerun · 删除 |
| daily-learning | 每日学习推荐 04:15 | 每天 04:15 · 下次 11h 后 | 累计 98 次 · 今日 1 次 | ● 成功 (2.4s) | 暂停 · Rerun · 删除 |
| aidata-pulse | AIData 数仓脉搏 04:00 | 每天 04:00 · 下次 11h 后 | 累计 186 次 · 今日 1 次 | ▲ 耗时偏高 (14.2s) | 暂停 · Rerun · 删除 |
| linear-bot-bridge | Linear @bot 桥接 | 每 1m · 刚刚 16:45 | 累计 4,280 次 · 今日 184 次 | ● 运行中 | 暂停 · Rerun · 删除 |
| my-pr-patrol | 我的 PR 巡检 | 每 5m · 2m 前 | 累计 860 次 · 今日 36 次 | ● 成功 (0.9s) | 暂停 · Rerun · 删除 |
| target-pr-review | 特定人 PR 审查 | 每 5m · 4m 前 | 累计 312 次 · 今日 12 次 | ✕ 失败 (exit 1) | 暂停 · Rerun · 删除 |

每个bay标「最后一次执行汇报 (Execution Report)」，包含summary、outputs、stages及footer logs四元素。简报数据为「晨间五阶段执行已通过，简报送达」/ TIA-448、TIA-431 / ① 个人源采集0.3s、② L2-L3 入仓0.5s、③ Retro-ROI0.4s、④ 学习寻题0.3s、⑤ Brief 投递0.3s / `[05:00:01] INFO stages completed`与`[05:00:01.8] INFO briefing acknowledged`。学习为「三道学习题已匹配投递」/ TIA-431 / 收集0.4s、去重0.3s、匹配0.7s、整理0.5s、发送0.5s / `[04:15:01] INFO selected questions=3`与`[04:15:02.4] INFO recommendation delivered`。

默认脉搏bay为「本轮耗时14.2s，其中入仓9.1s偏高」/ TIA-448 / ① 个人源采集1.2s、② L2-L3 入仓9.1s、③ Retro-ROI1.8s、④ 学习寻题1.3s、⑤ Brief 投递0.8s / `[04:00:10.3] WARN warehouse latency high`与`[04:00:14.2] INFO pulse completed`。桥接为「正在执行消息提交，当前轮尚未结束」/ TIA-448说明为最近产出 / inbox0.1s、去重0.1s、路由0.2s、提交进行中、确认未开始 / `[16:45:00] INFO bridge inbox`与`[16:45:00.4] INFO commit active`。

巡检为「PR #311 checks已读并记录」/ PR #311 / PR0.2s、checks0.2s、比对0.1s、保存0.2s、通知0.2s / `[16:43:00] INFO checks inspected`与`[16:43:00.9] INFO patrol completed`。审查为「PR #308 执行exit 1，评审未提交」/ PR #308 / PR0.2s、diff0.3s、执行审查0.6s失败、提交未执行、通知未执行 / `[16:41:00.5] INFO review task`与`[16:41:01.1] ERROR review exit=1`。每阶段bar按本报告最大完成秒数映射，未完成不伪填百分百，log四元素不能因footer分离而遗漏。

产出label链接本页永久说明 #v07-bay-{job}-{id}，本brief不提供真实外部URL所以不能猜PR repo或伪写已核实地址；点击定位/聚焦说明，不加屏、不请求Linear。DOM必须为六个静态slot，彼此报告与logs id独立：

```html
<main class="silent-rack-panel topology-tactile-ops-rack">
  <section class="content">
    <section class="rack-top-bezel"><h1></h1><p></p></section>
    <div class="rack-bay-collection">
      <article class="rack-slot" data-job-row data-job="daily-brief">
        <div class="slot-face" role="group"><div class="rack-summary-trigger" role="button"><span data-col="title"></span><time data-col="schedule"></time><span data-col="counts"></span><span data-col="status"></span></div><div data-col="actions"><button data-action="toggle-pause"></button><button data-action="rerun"></button><button data-action="delete"></button></div></div>
        <div class="slot-report-bay" id="v07-report-daily-brief" aria-owns="v07-log-daily-brief"><div class="bay-clip"><h2></h2><div class="bay-upper"><p data-report-block="summary"></p><nav data-report-block="outputs"></nav></div><ol data-report-block="stages"></ol></div></div>
        <footer class="slot-log-strip" id="v07-log-daily-brief"><div class="log-height-clip"><pre data-report-block="logs"></pre></div></footer>
      </article>
      <!-- 六slot静态展开书写，全部bay与log-footer同时开合 -->
    </div>
    <aside class="rack-restore-dock"><span aria-live="polite"></span><div class="rack-undo-keys"><button data-action="restore" data-job="daily-brief"></button><!-- 另五常驻键 --></div></aside>
  </section>
</main>
```

## 8. Explicit Anti-Patterns & Verification Targets

静音机架不用two-page split、5-segment ring gauge、orbital layout；严禁装饰音量旋钮、虚构runner页面、LED频闪。不得.caustic-veil、.ruler、Active-Matte、<select>测试开关、sandbox disclaimers和innerHTML replacement；content直子不得hero/fold-panel/secondary。bay-log是一份报告，不能让日志在关闭时泄漏可见。

交给Coding的验证：WebKit1280x800两外观全六slot、第三bay/log初始展开、每行五列及三个分段button；六报告四内容块完整，键盘/鼠标切换只单开；三键不触发开合，暂停/续、rerun恰+1、delete/undo复用Element。全根removedElements=0、点击目标>=28×28、0px意外溢出、无遮挡焦点和无数字截断。此Stage 1完成不包含截图PASS或实机执行声明。
