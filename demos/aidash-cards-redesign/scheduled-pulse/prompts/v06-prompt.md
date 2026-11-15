# v06 · 六袋回执架 (topology-paper-pocket-rack)

## 1. Visual Metaphor & Archetype Lock

用 SWWallet 的纸套边缘工艺，而不是它的扇形取卡布局：六个task sleeves依次垂直排列，每个都完整露出五列；点击袋面拉下报告voucher。拓扑是Paper-Pocket Rack，macOS / VS-002 paper remix / CL-002 sage-brass，AppTheme=VoucherRack。X同一列序、Y单袋accordion、Z薄specular rim与纸券层。参考顺序SWWallet纸套、Things抽屉、Apple Wallet文本，绝不引入钱包、金额、额外背卡或隐藏任务。

每袋顶部0.5px亮rim、侧面2px窄退阶，袋与袋隔8px；前景始终是文字，不是巨大袋口。任务14px SF Pro 600、周期/次数13px、日志12px SF Mono、crown20px。SVG使用24×24视框、1.5px圆端描边、16px显示的pause/rerun/trash，tail文字和图标共同出现。stage bars是票据内刻度直条，不做五段圆章。

## 2. Single P0 Focus & Initial Showcase State

P0为一张已送达的晨间回执，daily-brief（第一袋）初始抽开204px券页；另五袋维持60px面，高度不被前袋遮住。rack crown写「定时任务」及「点击袋面查看最后一次汇报」；底部summary lip只作操作说明，不再重复六项状态数据。

初始袋面badge依次为 ● 成功 (1.8s)、● 成功 (2.4s)、▲ 耗时偏高 (14.2s)、● 运行中、● 成功 (0.9s)、✕ 失败 (exit 1)，任务顺序与§7一致。全部未暂停且未删除，三个操作从「暂停」/「Rerun」/「删除」开始；暂停符号必须在切换后支持，不把失败等同停止排程。

## 3. P1 / P2 Progressive Folding & Permanent DOM Contract

六袋面始终作为P1同级对象，P2只有藏在本袋下的四块voucher。initial HTML固定6个sleeve-unit、6个完整voucher夹层，rack-undo-tray预置按job绑定的6个恢复按钮。open state只以data-open与aria-expanded改变，grid-height壳0fr/1fr，内容clip内min-height0，关闭后inert；点击任一未开袋关旧开新，点已开袋则收券，不增页面。

删除一袋用data-deleted把其高度和自身gap占位归零，保留原节点并从键盘路径inert；撤销托盘给出任务名和「撤销删除」。顺次删除多个时只激活最后删袋对应按钮，恢复后可继续撤销前一个，所有键仍原节点。恢复原索引、保留暂停/次数，不自动拉出券页；当前打开袋删除后选择为空。任何状态只变class/属性/已有Text.data，zero innerHTML rebuild、零detach、removedElements = 0；袋口伪元素不参与节点增删。

## 4. Measured Layout & 1280x800 Viewport Geometry

1280x800预算main x32/y20，1216×760、padding24；content1168×712。crown40 + gap12 + sleeve-list604（6×60+5×8+204）+ summary-lip24 + undo-tray32 = 712。袋面只用2px侧边视觉退阶，不真实缩小不同袋的可用列宽；本页未预期overflow为0px，不依靠负margin把第六袋推到窗外。系统chrome交由outer chooser。

净列宽1136（两侧16）：238/220/210/176/228，gap16×4，合计1136。袋面及后续面使用同一grid，即使paper层次不同也不可错列。①–④左齐，⑤右尾；胶囊按钮64/72/58×32、gap8，总210px，所有按钮>=28×28。行点击至少892×60；产出链接min44×30、undo32高。完整中文Title、周期和累计/今日字符串按13px可读，4,280不拆、数值不省略。

204px voucher内padding16，h2高24+gap8，再140px工作区。左456px为结论与产出，右648px为五条阶段和日志，gap32，内宽1136。阶段90px（5×18）+gap6+44px日志；输出link30px、摘要最多36px，中间8px。纸券0.5px top rim置于padding外、不压内容，clip仅用于开合；允许日志长输入局部滚动，初始两行日志无需横滚。

## 5. Dual-Theme Surface Polarity & Material Craft

VoucherRack Light canvas #EDEFE8、sleeve #F9FAF4、ink #27312A、muted #5D6B60、rim #FFFFFF、edge #D6DDCE、hover #F2F6EB、open #EEF4E5、voucher #E9EFDE、focus #396C48。Dark canvas #151B17、sleeve #242D25、ink #F4F7EC、muted #B9C5B5、rim #E6F2D72B、edge #485342、hover #2E3C2E、open #35442F、voucher #1B281C、focus #B7D69C。袋阴影light 0 3px 6px #283F1817、dark 0 3px 7px #060D0766，不能堆六块浓黑投影。

徽章五态Light success #2D633D/#E3EFDF、running #265B88/#E7EFF8、warning #805A1E/#FAEED4、failed #96323C/#F6E4E7、paused #5A685A/#E6EBE3；Dark success #B5DEAF/#2B422B、running #B1D5F6/#294053、warning #EFD09A/#453922、failed #F4B2BA/#462B33、paused #C8D1BF/#3B4937。胶囊text继承ink，rerun hover仅一处sage light色，不给每袋分配彩虹。

没有实际Liquid Glass：optical参数blur0、displacement0、IOR not applicable、paper opacity1。顶部specular rim只是不透明纸材质的0.5px inset线；纸券不采样玻璃、不用网络texture。data-theme选择以上Light/Dark，缺省跟系统prefers-color-scheme；reduce transparency时仍保持同样纸面。expanded状态只加内凹边和柔影，不出现第二个套框。

## 6. Apple Native Spring Physics & Row/Button Micro-Interactions

抽券采用510ms cubic-bezier(0.22, 1.35, 0.36, 1)，券内translateY(-9px)->0、外壳height同步；sleeve-face及列数字永不移动。收券同曲线510ms，opacity160ms，不能预先display:none。hover纸袋上缘亮120ms而非整袋抬升；button press translateY(1px)90ms/释放140ms。prefers-reduced-motion时券位移和弹性全部停用，1ms高度切换、无LED闪烁。

三个尾键pause/continue、Rerun、delete调用event.stopPropagation()，report links与restore也隔离。暂停存previousStatus并改⏸ 已暂停/继续；恢复原结果而非无条件成功。一次Rerun立刻● 运行中，到完成才两计数各+1、duration更新；pending token禁止重复click累加。paused手工run后仍paused、报告写新结果；delete使pending generation失效，restore不重新触发任务。UI是本页状态交互，不启动宿主进程。

sleeve-summary-trigger role=button、tabindex0、aria-controls对应voucher、aria-expanded准确；袋面容器仅role=group；自身Enter/Space可开合，native三键的keyboard不经袋面handler。关闭内容inert与aria-hidden，删除把焦点移到undo button，恢复回同一袋面；单据可Tab访问，焦点环2px并留2px offset，不被纸clip裁切。

sleeve-summary-trigger须覆盖前四列，grid-column:1/5且subgrid继承列尺寸，controls放第5列兄弟；fallback238/220/210/176px与16px gap，袋面壳不承载button角色。focus回袋面意指此trigger。重跑1000ms后的券面新读数依次1.6s成功、2.1s成功、12.8s耗时偏高、0.6s成功、0.8s成功、1.0s审查失败exit 1。完成阶段耗时按总秒数比例调整，bridge以0.1/0.1/0.2/0.1/0.1s全部完成并改摘要确认已到达；审查提交和通知仍未执行。已有log与结论同步覆写对应Text.data，失败计一次尝试。latestResult存本轮，paused仅控制排程标签，继续读取最新券面结果而不是旧缓存。

## 7. Production Data Inventory & Exact DOM Topology

每袋五列的词面按以下票面数据逐项落实；id仅作为data-job，禁止成为第六列：

| sleeve身份 | 名称① | 节奏② | 次数③ | 末次④ | 控制⑤ |
|:--|:--|:--|:--|:--|:--|
| daily-brief | 每日简报 05:00 | 每天 05:00 · 下次 12h 后 | 累计 142 次 · 今日 1 次 | ● 成功 (1.8s) | 暂停、Rerun、删除 |
| daily-learning | 每日学习推荐 04:15 | 每天 04:15 · 下次 11h 后 | 累计 98 次 · 今日 1 次 | ● 成功 (2.4s) | 暂停、Rerun、删除 |
| aidata-pulse | AIData 数仓脉搏 04:00 | 每天 04:00 · 下次 11h 后 | 累计 186 次 · 今日 1 次 | ▲ 耗时偏高 (14.2s) | 暂停、Rerun、删除 |
| linear-bot-bridge | Linear @bot 桥接 | 每 1m · 刚刚 16:45 | 累计 4,280 次 · 今日 184 次 | ● 运行中 | 暂停、Rerun、删除 |
| my-pr-patrol | 我的 PR 巡检 | 每 5m · 2m 前 | 累计 860 次 · 今日 36 次 | ● 成功 (0.9s) | 暂停、Rerun、删除 |
| target-pr-review | 特定人 PR 审查 | 每 5m · 4m 前 | 累计 312 次 · 今日 12 次 | ✕ 失败 (exit 1) | 暂停、Rerun、删除 |

六voucher均带「最后一次执行汇报 (Execution Report)」及结论、产出、耗时条、log四区域。晨间券为「晨间聚合和投递完成，五个子阶段通过」/ TIA-448与TIA-431 / ① 个人源采集0.3s、② L2-L3 入仓0.5s、③ Retro-ROI0.4s、④ 学习寻题0.3s、⑤ Brief 投递0.3s / `[05:00:01] INFO stage receipt ready`、`[05:00:01.8] INFO brief receipt TIA-448`。学习券为「三题候选已筛选并投递」/ TIA-431 / 候选0.4s、去重0.3s、适配0.7s、成题单0.5s、投递0.5s / `[04:15:01] INFO recommendations=3`、`[04:15:02.4] INFO dispatch done`。

脉搏券为「脉搏完成，入仓阶段耗时9.1s偏高」/ TIA-448 / ① 个人源采集1.2s、② L2-L3 入仓9.1s、③ Retro-ROI1.8s、④ 学习寻题1.3s、⑤ Brief 投递0.8s / `[04:00:10.3] WARN load slow`、`[04:00:14.2] INFO pulse voucher saved`。桥接券为「消息路由就绪，当前提交未完成」/ TIA-448注明上一轮产出 / 读取0.1s、去重0.1s、路由0.2s、提交进行中、确认未开始 / `[16:45:00] INFO inbox accepted`、`[16:45:00.4] INFO bridge commit running`。

巡检券为「PR #311 checks已记录，巡检完成」/ PR #311 / PR0.2s、checks0.2s、比较0.1s、保存0.2s、通知0.2s / `[16:43:00] INFO PR311 checks`、`[16:43:00.9] INFO patrol voucher ready`。审查券为「审查进程退出1，PR #308 无新提交评审」/ PR #308 / PR0.2s、diff0.3s、审查0.6s失败、提交未执行、通知未执行 / `[16:41:00.5] INFO reviewer start`、`[16:41:01.1] ERROR no review submitted exit=1`。五条bar以该券最大完成耗时归一，失败/未执行各有文字，不伪造成功计数。

未核实真实外链时，产出anchor指向该券永久说明 #v06-voucher-{job}-{id}；点击定位/聚焦说明，不展开新券、不新增页面，也不虚构PR地址。静态outline为下述独立sleeve结构，六次展开书写，不用JS克隆一个样板：

```html
<main class="voucher-rack-panel topology-paper-pocket-rack">
  <section class="content">
    <header class="pocket-rack-crown"><h1></h1><p></p></header>
    <ul class="pocket-sleeve-list">
      <li class="sleeve-unit" data-job-row data-job="daily-brief">
        <div class="sleeve-face" role="group"><div class="sleeve-summary-trigger" role="button"><span data-col="title"></span><time data-col="schedule"></time><span data-col="counts"></span><span data-col="status"></span></div><div data-col="actions"><button data-action="toggle-pause"></button><button data-action="rerun"></button><button data-action="delete"></button></div></div>
        <div class="voucher-height-shell"><section class="sleeve-voucher"><h2></h2><div class="voucher-copy"><p data-report-block="summary"></p><nav data-report-block="outputs"></nav></div><div class="voucher-measures"><ol data-report-block="stages"></ol><pre data-report-block="logs"></pre></div></section></div>
      </li>
      <!-- 固定六个sleeve-unit，另外五券四块数据全挂载 -->
    </ul>
    <section class="rack-summary-lip"><small>点击任务查看汇报</small></section>
    <footer class="rack-undo-tray"><span aria-live="polite"></span><div class="voucher-undo-keys"><button data-action="restore" data-job="daily-brief"></button><!-- 五个其他恢复按钮 --></div></footer>
  </section>
</main>
```

## 8. Explicit Anti-Patterns & Verification Targets

回执架拒绝two-page split、5-segment ring gauge、orbital layout；SWWallet参考不能成为半遮六行的扇形卡堆。禁止.caustic-veil、.ruler、Active-Matte、<select>测试开关、sandbox disclaimers、innerHTML replacement；main/content直孩子不采用hero、fold-panel、secondary。不得实体卸载袋子、给卡片旋转透视或在数值上套纸纹。

后续WebKit1280x800 Light/Dark截图须完整六袋+首张券，检查五列一致、每袋3按钮、全部报告四块和真实标签；轮流开合、暂停/继续、rerun、删除/恢复，所有原节点identity不变且全根removedElements=0。tail与报告links>=28×28，恢复焦点可靠，数字无…且0px overflow。此稿未运行浏览器，不将Stage 2的视觉验收目标当作Designer已有证据。
