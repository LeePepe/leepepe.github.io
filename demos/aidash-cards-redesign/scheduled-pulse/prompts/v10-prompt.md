# v10 · 同心浮行托盘 (topology-floating-row-deck)

## 1. Visual Metaphor & Archetype Lock

用macOS 26 Concentric Floating Row Deck的圆角递进：一个玻璃边缘tray，里面六张同级圆角横卡，各自下方弹开report tray。这里的deck是垂直六行，不是横向翻卡或轨道。锁macOS / VS-004 × VS-007 / CL-008 blue-sage，AppTheme=ConcentricTray；X固定五列、Y单行内联抽屉、Z玻璃仅tray外缘和solid rows。Top3参考macOS26同心轮廓、Settings分组、原生popover action胶囊；不复制新功能或额外导航。

外tray radius22、row14、report10，间距8匹配圆角减量；无前后卡遮挡。SF Pro14px600任务、13px周期/次数、SF Mono12px日志、20px标题，数值tabular。tail icon+label按钮采用inline SVG24×24、1.5px描边/round cap、16px光学尺寸，分别pause、回转箭头、桶；不省文字，也不放外链图标库。

## 2. Single P0 Focus & Initial Showcase State

P0为第二条daily-learning的投递回执，初始仅其204pxreport tray展开；六卡任务同屏完整出现，末卡不藏在deck背后。header「定时任务」，column-strip是固定列题，不添加筛选控件；telemetry-foot只是一句行点击说明，不渲染实时遥测的新指标。

启动的六badge序列对应§7任务：● 成功 (1.8s)、● 成功 (2.4s)、▲ 耗时偏高 (14.2s)、● 运行中、● 成功 (0.9s)、✕ 失败 (exit 1)。所有排程active未删除，首按钮都暂停；必须可到达⏸ 已暂停/继续，不将PR失败隐式解释为paused。

## 3. P1 / P2 Progressive Folding & Permanent DOM Contract

P1六card-face全时展示；P2四块report在各自card内正下方，占正常流高度。initial HTML里6个deck-card-row和6个report tray全挂载，restore bar中按job预置6个button。切换data-open、aria-expanded和grid rows0fr/1fr，内层min-height0/inert；single-active策略点新收旧开新，点当前收回，不重排deck。

delete标原article data-deleted，height、gap占位归零并inert，不物理移除；restore bar显任务名与「撤销删除」。恢复回原顺序、保留计数和排程状态，report闭合而不干预当前选中；当前卡删掉则选择为空。全生命周期removedElements = 0、zero innerHTML rebuild，禁止append新toast、模板克隆或replaceChildren。数值和反馈通过已有Text.data/属性修改，SVG、links和report content保留对象identity。

## 4. Measured Layout & 1280x800 Viewport Geometry

精确1280x800：main x24/y20、1232×760、padding24，content1184×712。header40 + gap8 + column-strip24 + deck-stack584 + restore32 + telemetry24 =712；stack584=上下各8px内边距+6×54px面+5×8px卡距+204px展开报告。玻璃外rim不得另加布局宽高。初始第六卡与完整第二tray都落在视口，0px unintended overflow，不以整页clip掩盖越界；chooser持有系统边框与主题开关。

stack左右8px之后row宽1168，row左右16px后净1136；五列244/220/206/176/226、gap16×4，总1136。column-strip自身左右24px（8+16）保持同样grid。首四左齐、tail右齐，三键60/72/58×32、gap8，总206px。①–④点击面至少894×54，link min44×30、恢复32高，全部hit target >= 28x28px。Title、时间、累计/今日数不重复到第二处，不截断4,280或exit 1。

204px report tray位于card-face下，padding16；24pxh2+gap8+140pxbody，内宽1136。左440px结论及output links、右664px阶段与log、gap32。五条阶段各18px共90，6px间隙与44px日志；summary至多两行36px+8px+30px links。tray与row是相邻实心块，底圆角10；展开高度不能挤瘪54pxface或跨到下一卡，报告增量只由本卡承担。

## 5. Dual-Theme Surface Polarity & Material Craft

ConcentricTray Light canvas #EAF0F7、rim-tint #F7FBFFE6、row #FFFFFF、ink #1B2A3A、muted #566B7D、hairline #DCE6F0、hover #F1F7FD、expanded #EBF4FC、report #E5EFF8、focus #235F97；Dark canvas #111B2A、rim-tint #243B54E6、row #203247、ink #F1F7FF、muted #B8CBE0、hairline #3C5672、hover #2B4460、expanded #2D4D6B、report #192E44、focus #AED7FF。rows用light0 2px 5px #214A7310 / dark0 2px 5px #07132640，不做叠卡重阴影。

Light五态fg/bg：success #225F41/#E0F0E6、running #205A94/#E2EFFC、warning #7F551A/#FAECD1、failed #A52E46/#FBE4EC、paused #52667A/#E5EEF7；Dark为 #A7E0BB/#244934、#B3DAFF/#274C70、#F5D399/#493D26、#FFB7C9/#4F3040、#C5D7E7/#3B5268。status带符号和文案；小accent不延伸成整卡彩虹，高对比以ink与solid badge保证。

Liquid Glass只在tray周缘8px空隙的伪元素区域：blur16px、saturate125%、概念IOR1.45、bevel8px、displacement0、rim1px #FFFFFFB3 / #D9EEFF33。它不覆盖卡片面积、不作为玻璃父容器；子rows/report完全不透明，外rim采样canvas而非另一glass，不能glass sample glass。WebKit不支持或reduced transparency时rim改为solid #DDE9F3 / #304B65与静态specular edge；结构不变。data-theme覆盖系统缺省prefers-color-scheme，无内页材质控制栏。

## 6. Apple Native Spring Physics & Row/Button Micro-Interactions

卡内tray开合500ms cubic-bezier(0.22, 1.35, 0.36, 1)，inner translateY(-6px)->0和height统一，outer rim固定；文字opacity170ms。hover只row底色120ms，不让整卡hover上提造成行列跳动；icon+label key按下scale(.97)90ms、松开140ms。prefers-reduced-motion:reduce取消弹性位移、运行点动画，以1ms高度切换保留状态。

toggle-pause、rerun、delete均先event.stopPropagation()，report link和restore也隔离。pause保留prePauseStatus、写⏸ 已暂停与继续，resume回原badge；rerun立即● 运行中，完成单轮才累计/今日各+1及更新duration。in-flight flag与generation token保证双击不重复结算、删除后回调失效；paused一次重跑写新报告但排程仍paused，撤销不触发新运行。整个候选只驱动浏览器文档，不连接宿主scheduler、CloudKit或Linear。

deck-summary-trigger role=button/tabindex0/aria-controls/aria-expanded；Enter/Space仅自身target响应，card-face仅role=group，native action键的keydown不可切换tray。closed report inert/aria-hidden，delete把focus送restore bar，undo回原card-face；2px focus环加offset2需在圆角clip内留空间。link点击聚焦同tray的说明锚，复制log不触发行toggle，aria-live短句反馈动作。

deck-summary-trigger以grid-column:1/5和subgrid形成连续四列点击面；无subgrid时固定244/220/206/176px、gap16。三个尾键的第五列是兄弟节点，button角色不嵌controls，所有返回card-face的focus实际落trigger。重跑本页反馈统一1000ms结算，新耗时依次1.6、2.1、12.8、0.6、0.8、1.0秒；第三条仍耗时偏高、第六条仍exit 1、其余成功。完成阶段同比缩放到新总秒数，桥接0.1+0.1+0.2+0.1+0.1s并把摘要改为提交确认结束；审查后两项继续未执行。最新summary/log通过原节点更新，失败运行也加一次；latestResult独立保存，paused排程不被重跑重启，resume显示最新tray结果而非旧徽章。

## 7. Production Data Inventory & Exact DOM Topology

六张card的五列必须原样呈现，数据表字段顺序正是横向UI次序：

| card job id | Title① | 时间与周期② | 累计与今日③ | 末次badge④ | 三个尾键⑤ |
| ---: | :--- | :--- | :--- | :--- | :--- |
| daily-brief | 每日简报 05:00 | 每天 05:00 · 下次 12h 后 | 累计 142 次 · 今日 1 次 | ● 成功 (1.8s) | 暂停 / Rerun / 删除 |
| daily-learning | 每日学习推荐 04:15 | 每天 04:15 · 下次 11h 后 | 累计 98 次 · 今日 1 次 | ● 成功 (2.4s) | 暂停 / Rerun / 删除 |
| aidata-pulse | AIData 数仓脉搏 04:00 | 每天 04:00 · 下次 11h 后 | 累计 186 次 · 今日 1 次 | ▲ 耗时偏高 (14.2s) | 暂停 / Rerun / 删除 |
| linear-bot-bridge | Linear @bot 桥接 | 每 1m · 刚刚 16:45 | 累计 4,280 次 · 今日 184 次 | ● 运行中 | 暂停 / Rerun / 删除 |
| my-pr-patrol | 我的 PR 巡检 | 每 5m · 2m 前 | 累计 860 次 · 今日 36 次 | ● 成功 (0.9s) | 暂停 / Rerun / 删除 |
| target-pr-review | 特定人 PR 审查 | 每 5m · 4m 前 | 累计 312 次 · 今日 12 次 | ✕ 失败 (exit 1) | 暂停 / Rerun / 删除 |

每个tray h2「最后一次执行汇报 (Execution Report)」，含四块summary、outputs、stages、logs。简报卡数据为「晨间全量聚合五阶段通过，投递已完成」/ TIA-448、TIA-431 / ① 个人源采集0.3s、② L2-L3 入仓0.5s、③ Retro-ROI0.4s、④ 学习寻题0.3s、⑤ Brief 投递0.3s / `[05:00:01] INFO all stages passed`、`[05:00:01.8] INFO briefing receipt saved`。默认学习卡数据为「三题推荐完成去重、匹配与投递」/ TIA-431 / 读取0.4s、去重0.3s、匹配0.7s、题单0.5s、投递0.5s / `[04:15:01] INFO learning candidates=3`、`[04:15:02.4] INFO learning receipt complete`。

脉搏卡为「全轮完成，L2-L3入仓9.1s偏高」/ TIA-448 / ① 个人源采集1.2s、② L2-L3 入仓9.1s、③ Retro-ROI1.8s、④ 学习寻题1.3s、⑤ Brief 投递0.8s / `[04:00:10.3] WARN L2-L3 duration high`、`[04:00:14.2] INFO pulse receipt complete`。桥接卡为「当前消息已路由，桥接提交仍在运行」/ TIA-448注为上次产出 / 消息读取0.1s、去重0.1s、路由0.2s、提交进行中、确认未开始 / `[16:45:00] INFO bridge routing ready`、`[16:45:00.4] INFO submission in progress`。

巡检卡为「PR #311 checks巡检后已归档」/ PR #311 / 读取0.2s、checks0.2s、对比0.1s、保存0.2s、通知0.2s / `[16:43:00] INFO PR311 checks loaded`、`[16:43:00.9] INFO patrol receipt complete`。审查卡为「PR #308 审查exit 1，评审没有提交」/ PR #308 / PR0.2s、diff0.3s、审查0.6s失败、提交未执行、通知未执行 / `[16:41:00.5] INFO review process ready`、`[16:41:01.1] ERROR review receipt exit=1`。stages按报告最大已完成秒数定直条，未执行/进行中不能伪填成功，全部五条都有文字读数。

TIA/PR labels用 #v10-evidence-{job}-{id} 锚至本tray常驻说明；因brief未提供核实URL，不猜仓库、不请求真实服务、不新建产出页面。点击是实际聚焦已有说明且保持tray，并非无响应装饰。outline中六article与六完整tray须静态写全：

```html
<main class="concentric-row-panel topology-floating-row-deck">
  <section class="content">
    <header class="deck-header-bar"><h1></h1><p></p></header>
    <nav class="deck-column-strip"><span>任务名称</span><span>运行周期</span><span>累计/今日次数</span><span>最近状态</span><span>操作</span></nav>
    <section class="floating-deck-stack">
      <article class="deck-card-row" data-job-row data-job="daily-brief">
        <div class="deck-card-face" role="group"><div class="deck-summary-trigger" role="button"><span data-col="title"></span><time data-col="schedule"></time><span data-col="counts"></span><span data-col="status"></span></div><div data-col="actions"><button data-action="toggle-pause"></button><button data-action="rerun"></button><button data-action="delete"></button></div></div>
        <div class="deck-tray-height-shell"><section class="deck-execution-tray"><h2></h2><div class="deck-copy-zone"><p data-report-block="summary"></p><nav data-report-block="outputs"></nav></div><div class="deck-trace-zone"><ol data-report-block="stages"></ol><pre data-report-block="logs"></pre></div></section></div>
      </article>
      <!-- 六同级deck-card-row全静态数据，独立report/controls/output id -->
    </section>
    <aside class="deck-restore-bar"><span aria-live="polite"></span><div class="deck-undo-bank"><button data-action="restore" data-job="daily-brief"></button><!-- 另五枚 --></div></aside>
    <footer class="deck-telemetry-foot"><small>点击任务展开汇报</small></footer>
  </section>
</main>
```

## 8. Explicit Anti-Patterns & Verification Targets

同心deck禁止two-page split、5-segment ring gauge、orbital layout；不允许六卡前后遮挡或左右横滑。禁.caustic-veil、.ruler、Active-Matte、<select>测试开关、sandbox disclaimers、innerHTML replacement与节点remove；content直孩子严格五节点，不出现hero/fold-panel/secondary。玻璃rim只采样实心背景，不能把report托盘二次玻璃化。

Coding与Reviewer应提供1280x800 Light/Dark真截图：六卡五列、第二tray初始完整、3尾键可达、六报告各四块。所有行开合和暂停/继续、rerun、删除/undo验证全根removedElements=0、node identity恒定，三按钮及link不意外展开；累计/今日只结算一次。所有targets>=28×28、keyboard focus可恢复、数值无省略、0px unintended overflow。Stage 1 receipt只能证明文件/结构/独立性，不代替后续渲染测试。
