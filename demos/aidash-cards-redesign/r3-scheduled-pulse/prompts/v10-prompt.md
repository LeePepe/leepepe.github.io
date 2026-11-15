# v10 · 工位双页凭证台 (topology-workbench-drawer-matrix)

## 1. Visual Metaphor & Archetype Lock
开发者工位不需要更多仪表盘：顶端一段横向telemetry桥嵌阶段小环，中间双页纸袋只展示一件当前作业，右侧有带短虚切边的回执凭证。VS-007 Swiss Chrono / CL-008的冷纸与靛蓝，CP-002约束纸袋叠层，DV-003约束precision ring，MI-006约束滑出动作。X轴把页轨选择与当前job选择拆成清楚两个操作，Y轴将五段/三题折进右凭证，Z轴为paper deck→凹lip→functional controls而非全屏玻璃。SWWallet、Things3、CleanShot X、Alcove分别借鉴纸层、字距、工具紧凑和凹口；R3-WorkbenchVoucher是macOS26候选AppTheme，不新增命令面板或runner业务。

## 2. Single P0 Focus & Initial Showcase State
默认page-rail选「高频脉搏 3 · Minute Pulse」，pocket deck里我的PR行原位展开，04:10完成、每5分钟，是唯一主焦点。另两快job及两张慢纸头全部能辨认其名称，日批标题「每日批处理 2 · Daily Batch」可点击换深度，不重印job。顶桥ring读数5/5、旁注「晨报阶段 · 04:01」，与当前PR不是同一分母。perforated-voucher初始缩在右侧，只有40px拉柄与「执行回执」字样；11月15日04:15是固定展示时钟。顶桥不加第二份selected job summary。

## 3. P1 / P2 Progressive Folding & Permanent DOM Contract
页轨负责快慢两页的展示顺序，deck负责单任务行内展开，voucher负责structured receipt。P1只留节律、时间与环语义；P2为当前执行操作、五stage与学习三题。两个task-page、五job、五SVG circle、整份voucher在首个HTML parse时常驻；点击绝不innerHTML、outerHTML、replaceChildren、insertAdjacentHTML，也不克隆另一份current row。class/dataset与CSS变量控制页深度、凭证展开与highlight；hidden正文inert，外露paper-head按钮始终能Tab。selectedJobId独占，ring selectedStage只控制voucher既有行，不改PR选择。开票时当前任务正文收束为摘要，保证明细只有一处；Esc回凭证柄，第二次收当前job，状态不被reset。运行文本只写已有live叶节点。

## 4. Measured Layout & 1280x800 Viewport Geometry
工位卡1120x608px位于(80,96)，未占用区域33.50%，>=22% whitespace。外内距24px后content1072x560：telemetry-bridge-top80px，gap20，deck-and-voucher384px，gap20，workbench-status-lip56px。center三列page-rail112px、pocket-deck-stage588px、perforated-voucher324px，中间两24px缝，总1072。deck内16pxpadding、上24px安全位，四个未选纸头40px+选中区域144px=304px，再留24px底部空间，合384px；两页名称都在这些纸头中，不产生第二rail任务表。右票正文宽292px，左五stage136px与右三question144px、gap12；stage30px、题52px，分组标题与padding最多80px，总236px在384px内。票滑出使用右324px自身预留区，不覆盖deck或推大main。唇r12px/depth12px，paper corner16px，卡corner24px，perforation只准7个1px点标边，不能画ruler刻度。字阶13/15/20/32，按钮32px、page button40px，ringhit32x32px，最低28x28px；时间/14s留64px槽。所有-6pxpeek与spring超调保留8px内空，要求0px unintended scroll overflow且不用全页裁切掩盖。

## 5. Dual-Theme Surface Polarity & Liquid Glass / Paper-Pocket Craft
工位AppTheme Light desk #F1F4F8、deck #E6ECF4、paper #FFFFFF、ink #27354D、muted #5A6980、accent #485BB8、success #276A4E、warning #88580D、focus #086CCF。Dark对应#0E1522、#1C2B40、#2D4059、#F1F6FF、#BECDE4、#B4C4FF、#9EE0BF、#F0CB88、#8BC3FF。top bridge的底是实deck，paper和voucher也实面；只有页轨的操作胶囊可用薄glass：IOR1.5、8pxbevel、blur7px、saturation145%、0.5pxspecular，Safari/Reduce Transparency落为deck实色不嵌glass-on-glass。袋唇以独立front Shape内凹切口压纸，0.5px inner highlight为#FFFFFFDC/#FFFFFF2B；环境三停Light0 1px 3px #20324F0A, 0 8px 18px #20324F12, 0 22px 38px #20324F18，Dark#00000018/#0000002A/#00000036，虚切票边没有重影。日期、5/5、3题、运行14s全用tabular numerals，亮Dark CTA配深desk字而非白字，小面积语义状态退居次要。

## 6. Apple Native Spring Physics & Micro-Interactions
deck换页是已有前纸上提24px、背纸退8px，420ms cubic-bezier(0.22, 1.35, 0.36, 1)；右凭证沿x从+240px进到0，500ms同曲线，固定vault容纳其所有终态。纸头hover peek translateY(-6px)，click才选，票把手hover只有亮度/阴影反馈。telemetry ring采用120方SVG、center60/r40/stroke5，5circle各pathLength100、stroke-dasharray="16 84"、offset0/-20/-40/-60/-80、stroke-linecap="round"、-90°起点；centre5/5是精确stage pass读数。hover/focus只亮一弧，click/Enter点亮凭证的对应data-stage行，不让五job围环。立即运行在status-lip已有aria-live走已排队→运行中→刚刚完成 · 耗时14s，running禁double fire；作业状态以原job ID保存在浏览器内存，跨页仍在正确纸上恢复，无真实scheduler/Linear/CloudKit通讯。prefers-reduced-motion: reduce停用位移、peek与超调，100ms淡入或直接终态替代，反馈和凭证可达性不变。

## 7. Production Data Inventory & Exact DOM Topology
Minute Pulse页绑定linear-bot-bridge（Linear @bot 桥接 / 每 1 分钟 / 04:14成功）、my-pr-supervisor（我的 PR / 每 5 分钟 / 04:10成功 / 初始选中）、pr-auto-review（PR 自动审查 / 每 5 分钟 / 04:10成功）。Daily Batch页绑定aidata-digest（个人数仓晨报 / 每日 04:00 / 04:01阶段5/5）与daily-learning（每日学习推荐 / 每日 04:15 / 04:15已投3题）。不要把两个daily job写进Minute Pulse cadence。

右凭证五段的对照是collect→① 个人源采集；normalize_merge→② L2-L3 入仓；retro_roi→③ Retro-ROI；learning_topics→④ 学习寻题；digest_push→⑤ Brief 投递，均通过。学习凭证部分显示Linear TIA / 3/3送达，其三题为如何用证据区分实现缺陷与规格缺口？、怎样区分 Cache 命中率与上下文占比？、如何让增量入仓保持幂等？。作为本轮固定代表性问题，不声称读取或写入实际TIA issue，不造外链或issue编号，也不编造各段duration。三题投递独立于digest五阶段，receipt必须分组标明。

HTML的bridge、三列deck/voucher与status lip保持以下父子组合；24x24工具SVG/currentColor/1.6px round stroke，环必须有5圆段和32方可访问按钮层，图形不能是位图。

```html
<main class="workbench-card topology-workbench-drawer-matrix">
  <section class="content">
    <section class="telemetry-bridge-top"><h1></h1><svg class="bridge-stage-dial"></svg><output></output><p class="telemetry-caption"></p><time></time></section>
    <div class="deck-and-voucher">
      <nav class="page-rail"><button class="minute-page-choice"></button><button class="daily-page-choice"></button></nav>
      <section class="pocket-deck-stage"><article class="minute-deck-page"><div data-job="linear-bot-bridge"></div><div data-job="my-pr-supervisor"></div><div data-job="pr-auto-review"></div></article><article class="daily-deck-page"><div data-job="aidata-digest"></div><div data-job="daily-learning"></div></article></section>
      <aside class="perforated-voucher"><button class="voucher-pull"></button><div class="voucher-paper"><ol class="voucher-stage-lines"></ol><ol class="voucher-question-lines"></ol></div></aside>
    </div>
    <footer class="workbench-status-lip"><button class="run-deck-selection"></button><p class="deck-run-feedback" aria-live="polite"></p></footer>
  </section>
</main>
```

## 8. Explicit Anti-Patterns & Verification Targets
禁.caustic-veil、.ruler、Active/Matte bars、<select>测试开关、沙盒免责文字、五点orbital canvas以及innerHTML暴力替换。工位不能变假命令行或runner status新页，右票不能扩出iframe；status-lip属于卡内反馈，不是macOS固定浮动bottom bar。外层chooser继续独占窗口frame、theme、variant和viewport控制。

指定四态：α快页/我的PR/独立晨报5/5/票收；β切慢页选学习，快页纸头仍可识别；γ右票滑出、点环①，五段与三题完整无遮盖并可Esc归位；δ当前job立即运行经过排队→运行→完成，跨页后反馈不串。Writer须给四态Light/Dark共8张WebKit1280x800实截、元素identity保留记录与keyboard/Reduce Motion结果。验证所有5job/2page/5circle/receipt在初始parse后未被替换、文字4.5:1、0px横纵意外scroll、零数值ellipsis与raw localization keys；Stage1只提供Prompt，不假定渲染完成。
