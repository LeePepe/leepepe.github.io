# v01 · 青岚内嵌清单 (topology-inset-grouped-list)

## 1. Visual Metaphor & Archetype Lock

以 Apple System Settings 的 Inset Grouped List 为形态参考：一张连续的浅色列表，六条任务只用细分隔线组织；打开的汇报像原本嵌在列表背后的凹槽，而非新开窗口。锁定 macOS 桌面、VS-005 × CL-006 sage remix、X=五列直接操作 / Y=单行汇报折叠 / Z=实心列表与下沉报告，AppTheme 名为 QinglanInset。设计维度为 component、visual-style、motion-interaction、typography-copy。本稿只交付 Stage 1 决策，不写产品代码、不发布，也不替 Owner 选定最终方案。

视觉主次来自 1px leading-indented hairline、16px 分组圆角和墨色退让。Title 用 SF Pro / PingFang SC 14px 600；周期、次数用 13px；报告日志用 SF Mono 12px；面板标题 20px。24×24 inline SVG 用 1.5px currentColor 描边画暂停双竖线、回转箭头、垃圾桶，图形实占 16px，旁有可读按钮文字，绝不引入图标字体。

## 2. Single P0 Focus & Initial Showcase State

P0 是“看清每日简报的最后一次结果”，初次加载只展开 daily-brief 的「最后一次执行汇报 (Execution Report)」。其余五个汇报收起，但每条任务和三个尾按钮均可见；不在标题栏再复制一次任务卡或大数字。标题为「定时任务」，一句次要提示「点击任务查看最后一次汇报」即可。

初始徽章按显示顺序固定：每日简报 05:00 为 ● 成功 (1.8s)，每日学习推荐 04:15 为 ● 成功 (2.4s)，AIData 数仓脉搏 04:00 为 ▲ 耗时偏高 (14.2s)，Linear @bot 桥接为 ● 运行中，我的 PR 巡检为 ● 成功 (0.9s)，特定人 PR 审查为 ✕ 失败 (exit 1)。六条任务都未暂停、未删除，首个操作文字均为「暂停」，不能把失败误当作暂停。

## 3. P1 / P2 Progressive Folding & Permanent DOM Contract

P1 保留每行的五项字段；P2 只有该行之下的四块报告内容。六个 job-row-unit、六个 row-report-drawer、restore-status-bar 和所有静态 SVG、链接、日志文本节点在 initial HTML 中一次挂载。drawer 用 grid-template-rows: 0fr/1fr 配合内部 min-height:0 和裁切壳，不动态造节点；选中行由 aria-expanded 和 data-expanded 表示。单展开策略：打开另一行时关闭前一行，重新点击当前行即收回，不重排任务。

删除设置 data-deleted 并折叠整条 unit 的布局高度、清除其可聚焦状态；节点仍留在原列表顺序。底栏常驻，为每个 job 预置一个恢复按钮，仅激活最近一次删除的按钮；文案为「已删除 每日简报 05:00 · 撤销删除」等。恢复保持次数、暂停标记和既有汇报内容，保持其他当前展开行不变，被恢复行默认收起；若删除了当前展开行则 P0 退回纯列表。全流程 removedElements = 0，零 innerHTML rebuild；状态与数字只改已有 Text.data / 属性，禁止以元素级 textContent 替换 SVG 或子节点。

## 4. Measured Layout & 1280x800 Viewport Geometry

WebKit viewport 精确为 1280x800；外层 chooser 负责 macOS 画框，子页不再画交通灯。main 位于 x32/y24，1216×752，padding24，border-box；边界用 inset shadow 不占尺寸。content 为 1168×704：titlebar56 + 间隙16 + group-card592（6×64 行 + 一个208px报告）+ 间隙12 + restore-bar28 = 704。第一张截图全部六行及完整汇报落在 y48..752 内，0px unintended overflow，不能用 body overflow:hidden 掩盖溢出。

row-five-cols 两端各留16px，内部可用1136px；统一 CSS grid 为 240 / 220 / 210 / 180 / 222px，四处 gap16，合计1136。前四列左对齐、数字 tabular-nums；最后一列 justify-self:end。三枚胶囊宽60/72/58、高32、gap8，总206px。行主体①–④的点击区域连续覆盖至少898×64，按钮与报告链接均 >= 28x28px，恢复按钮高28；报告链接用32px高。周期和次数保持完整一行，不出现数字省略号。

208px 报告井内 padding16，先放24px标题与8px间距；其余144px为左480px（结论36、间距8、链接32）与右624px（五条阶段读数及三行日志）的两列工作区，间隔32。五阶段采用一个92px高的纵向紧凑条列，每行16px、3px间距；日志在独立48px带内。报告文字只在各自容器自然折行，不横跨任务列；内容增多时限定井内可滚动，初始给定内容无需滚动。

## 5. Dual-Theme Surface Polarity & Material Craft

QinglanInset Light：canvas #F4F6F3，group #FFFFFF，ink #17241C，secondary #526157，hairline #E0E6DF，hover #F0F5EF，expanded #F5FAF3，report-well #EAF0E7，focus #236846。Dark 对应 canvas #141A17，group #202924，ink #F0F6EF，secondary #A9B8AD，hairline #39453C，hover #2A372E，expanded #29392D，well #17221B，focus #9AD6AC。浅色井 inset 0 1px 3px #19351F14，深色井 inset 0 1px 4px #07100966；列表没有整排浮起阴影。

状态以低彩度药丸承载，不只靠圆点辨义。Light 的 success fg/bg=#23623B/#E6F2E7，running=#185B86/#E6F0F8，warning=#805316/#FFF2D9，failed=#A12E37/#FBE9EA，paused=#526157/#E9EDE9；Dark 为 #9CD7AC/#243C2B、#A7D6FA/#223B4D、#F2CC88/#45351E、#FFAAB3/#46282D、#BBC6BD/#343F36。paused 仍清晰，不能把整条任务降到不可读透明度。

此案不使用 backdrop-filter，也不做折射；Liquid Glass optical parameters 明确为 blur0、displacement0、透明度0，内容为不透明纸面。外观响应 data-theme=light|dark，未指定时随 prefers-color-scheme；主题变化只替换变量，不重挂列表。按钮 hover 加 #2368460D / #9AD6AC14 的局部底色，expanded 的底色不是第二个玻璃层。

## 6. Apple Native Spring Physics & Row/Button Micro-Interactions

报告开合采用 460ms cubic-bezier(0.22, 1.35, 0.36, 1)，展开时内页 translateY(-6px)->0，外壳高度保持同一时间曲线，关闭不先 hidden。文字 opacity 用180ms ease-out，避免弹性越界导致字形伸缩。尾按钮按下仅 scale(.97) 90ms，松开140ms；行 hover 只染色，不抬升整张列表。prefers-reduced-motion:reduce 时所有位移/弹性为0、开合1ms，running 点不循环呼吸。

[data-action="toggle-pause"]、[data-action="rerun"]、[data-action="delete"] 都先 event.stopPropagation()；恢复及报告链接也阻止冒泡。暂停记录 previousStatus，显示 ⏸ 已暂停 / 继续；继续恢复该任务原先状态而非统一写成功。Rerun 立即显示 ● 运行中，完成后累计和今日各+1、更新耗时；每任务只容许一次在途重跑，重复点击禁用至完成，不新增第六字段。暂停中可重跑一次，但完成仍显示 ⏸ 已暂停，耗时写入报告；删除发生在重跑期间则失效旧回调，恢复不凭空增加次数。

inset-summary-trigger 上用 role=button、tabindex=0、aria-controls 与 aria-expanded，row-five-cols 自身只为 role=group，Enter/Space 仅在 event.target 等于行触发器时响应，按钮键盘事件不得被行劫持。隐藏报告的内部内容 inert 且 aria-hidden=true，展开后解除；删除前焦点转至对应恢复按钮，恢复后回该任务行。报告 link 的可见标签与 aria-label 对应真实单据，焦点环2px、offset2。

为避免可交互控件嵌在另一个button角色内，inset-summary-trigger跨外grid第1–4列（grid-column:1/5），内部继承这四列的subgrid，三枚原生键位于第5列兄弟节点；不支持subgrid时用§4前四个固定宽度和同gap。焦点返回均指此trigger而非group壳。重跑的本页结算延迟明确为1000ms，六任务的新耗时依次1.6s、2.1s、12.8s、0.6s、0.8s、1.0s；第三项仍耗时偏高、第六项仍exit 1，其余成功。已完成阶段按新总时长/旧总时长同比缩放，桥接五阶段则0.1/0.1/0.2/0.1/0.1s并更新结论为提交确认完成；失败行最后两阶段仍未执行。每次结算刷新既有摘要/日志及latestResult，失败尝试也计一次；暂停只遮盖排程badge，继续必须读最新结果，不恢复过时缓存。

## 7. Production Data Inventory & Exact DOM Topology

必须原样展示以下库存；每条 [data-job-row] 包含以下五列，表内最后一列不是菜单，也不能以悬停才出现的图标代替：

| data-job | Title | 运行时间 / 周期 | 运行次数 | 最后一次状态 | 尾操作 |
|---|---|---|---|---|---|
| daily-brief | 每日简报 05:00 | 每天 05:00 · 下次 12h 后 | 累计 142 次 · 今日 1 次 | ● 成功 (1.8s) | 暂停 / Rerun / 删除 |
| daily-learning | 每日学习推荐 04:15 | 每天 04:15 · 下次 11h 后 | 累计 98 次 · 今日 1 次 | ● 成功 (2.4s) | 暂停 / Rerun / 删除 |
| aidata-pulse | AIData 数仓脉搏 04:00 | 每天 04:00 · 下次 11h 后 | 累计 186 次 · 今日 1 次 | ▲ 耗时偏高 (14.2s) | 暂停 / Rerun / 删除 |
| linear-bot-bridge | Linear @bot 桥接 | 每 1m · 刚刚 16:45 | 累计 4,280 次 · 今日 184 次 | ● 运行中 | 暂停 / Rerun / 删除 |
| my-pr-patrol | 我的 PR 巡检 | 每 5m · 2m 前 | 累计 860 次 · 今日 36 次 | ● 成功 (0.9s) | 暂停 / Rerun / 删除 |
| target-pr-review | 特定人 PR 审查 | 每 5m · 4m 前 | 累计 312 次 · 今日 12 次 | ✕ 失败 (exit 1) | 暂停 / Rerun / 删除 |

每个井具备四个 data-report-block：summary、outputs、stages、logs。daily-brief 的摘要为「05:00 简报已投递，采集与入仓完成，学习候选已进入收件箱。」；产出标签 TIA-448、TIA-431；五条完整名称为 ① 个人源采集 0.3s、② L2-L3 入仓 0.5s、③ Retro-ROI 0.4s、④ 学习寻题 0.3s、⑤ Brief 投递 0.3s，条长按耗时/0.5s映射，旁有文字值；日志三行为 `[05:00:00] INFO collect complete`、`[05:00:01] INFO warehouse committed`、`[05:00:01.8] INFO brief delivered TIA-448`。

其余五井也必须有完整四块而非占位：daily-learning「04:15 已整理三道学习题并投递。」/ TIA-431 / 候选读取0.4s、去重0.3s、难度匹配0.7s、题单整理0.5s、投递0.5s / `[04:15:01] INFO candidates=3` 与 `[04:15:02.4] INFO learning delivered`。aidata-pulse「入仓完成；L2-L3 阶段耗时偏高，需要关注。」/ TIA-448 / ① 个人源采集1.2s、② L2-L3 入仓9.1s、③ Retro-ROI1.8s、④ 学习寻题1.3s、⑤ Brief 投递0.8s / `[04:00:10.3] WARN warehouse slow` 与 `[04:00:14.2] INFO pulse complete`。linear-bot-bridge「正在处理本轮 @bot 消息，输出待提交。」/ TIA-448（最近已提交单据）/ 消息读取0.1s、去重0.1s、路由0.2s、桥接提交进行中、确认未开始 / `[16:45:00] INFO inbox read` 与 `[16:45:00.4] INFO bridge in progress`。my-pr-patrol「巡检完成，PR #311 的检查结果已更新。」/ PR #311 / PR读取0.2s、检查读取0.2s、对比0.1s、归档0.2s、通知0.2s / `[16:43:00] INFO pull=311` 与 `[16:43:00.9] INFO patrol complete`。target-pr-review「PR #308 审查退出码为1，未提交新评审。」/ PR #308 / PR读取0.2s、diff读取0.3s、审查执行0.6s失败、评审提交未执行、通知未执行 / `[16:41:00] INFO pull=308` 与 `[16:41:01.1] ERROR review exit=1`。非该任务执行的阶段不伪写完成；所有报告保持生产语气。

TIA 与 PR 链接使用 brief 给出的标识作为可点标签。未提供已核实的外部 URL 时，href 指向本井永久挂载的对应产出说明 id（如 #v01-daily-brief-tia-448），点击聚焦说明，不请求真实 Linear/GitHub、不编造仓库 URL、不导航到新页面。Stage 2 只驱动本页状态，不接真实调度器。

```html
<main class="qinglan-panel topology-inset-grouped-list">
  <section class="content">
    <header class="panel-titlebar"><h1></h1><p></p></header>
    <div class="inset-group-card">
      <article class="job-row-unit" data-job="daily-brief" data-job-row>
        <div class="row-five-cols" role="group">
          <div class="inset-summary-trigger" role="button"><span data-col="title"></span><time data-col="schedule"></time><span data-col="counts"></span><span data-col="status"></span></div>
          <div data-col="actions"><button data-action="toggle-pause"></button><button data-action="rerun"></button><button data-action="delete"></button></div>
        </div>
        <section class="row-report-drawer"><div class="recess-clip"><h2></h2><div class="recess-body"><section data-report-block="summary"></section><nav data-report-block="outputs"></nav><ol data-report-block="stages"></ol><pre data-report-block="logs"></pre></div></div></section>
      </article>
      <!-- 依次静态写入 daily-learning / aidata-pulse / linear-bot-bridge / my-pr-patrol / target-pr-review，同样五列与四块井；不得运行时克隆。 -->
    </div>
    <footer class="restore-status-bar" aria-live="polite"><span></span><button data-action="restore" data-job="daily-brief"></button><!-- 另五个按任务绑定的常驻恢复按钮 --></footer>
  </section>
</main>
```

## 8. Explicit Anti-Patterns & Verification Targets

青岚绝不使用两页/双栏任务分组、5-segment ring gauge、orbital layout；阶段读数只能是直线耗时条。禁 .caustic-veil、.ruler、Active-Matte 调试栏、<select> 测试开关、sandbox disclaimers、额外页面和 hero/fold-panel/secondary 直子类。不要将 System Settings 参考误译成七个套盒，五列名单不得被日志挤变形；innerHTML replacement、replaceChildren、remove、卸载再挂载一律禁用。

交付 Coding 后须在 WebKit 1280x800 的 Light/Dark 抓取完整首屏：验6个 [data-job-row]、每行5个 data-col、3个动作；展开/收起六行，逐一检查四报告块。MutationObserver 统计整个交互周期 removedElements = 0；点击暂停、继续、Rerun不改变该行 aria-expanded；删除只收起被删行并清空其选中，不展开任何其他行，撤销恢复原节点 identity。验证运行完成只增一次、暂停中的重跑不改变排程状态、键盘可达、报告链接 >=28px、无文字截断和0px外溢。本文件是候选设计，不声称这些像素测试已执行。
