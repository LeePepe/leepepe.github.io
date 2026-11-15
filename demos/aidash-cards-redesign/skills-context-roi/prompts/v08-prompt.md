# v08 · 伸缩抽屉导流井 (topology-telescopic-skill-drawers)

## 1. Visual Metaphor & Archetype Lock

以Alcove的浅层抽出感和纸档案柜为参考，六条水平Skill抽屉在左，右井采用先竖向汇入再横向分岔的C曲带；最后一窄列是一张script/Eval明细纸。不是六层全屏sheet，也不是普通左右表格换皮。desktop四维component/chart-dataviz/layout-navigation/motion-interaction；VS-005 × CL-006 warm-indigo remix；X=抽屉button / Y=固定高右井 / Z=抽屉伸6px与凹井。候选AppTheme=TelescopicConduitFile。

13px抽屉名、12px主要数据、11px细项、20px井标题。SF Pro/PingFang中文，文件SF Mono。24×24 inline SVG画抽屉拉槽与竖转横分叉，1.5px currentColor；不使用ruler刻度。标题和说明直接落在frame里，不额外做hero盒。

## 2. Single P0 Focus & Initial Showcase State

首抽屉my-designer伸出6px，中央井永久打开，L0之后reference与script两组清楚分开，默认navigation-evidence-contract.md为pinnedBranch。单P0是从Prompt到具体文件的上下文去向；最右纸片展示该分支62%/2.4k tok与本Skill Eval归因，而非另一份六Skill总账。所有六抽屉和僵尸建议同时可见。

## 3. P1 / P2 Progressive Folding & Permanent DOM Contract

左抽屉P1四组账目排2×2，每条button包含标题及所有四组纯文本；P2中央井的六份route-map和右纸片六份detail-note。click不同Skill切两者到本人节点，重复click retract流井，仅保留选中标签；再click恢复pin。抽屉伸缩只transform、不改变列宽，避免右图跳动。

六li、六route-map、六detail-note以及所有paths和branch按钮都在initial HTML；removedElements = 0、零innerHTML rebuild，单用data-open/class、Text.data、aria。隐藏panel inert且aria-hidden，右note也跟随隐藏，不能留上一Skill数据。hover临时聚焦分支，click/Enter/Space锁定，leave退到pin；Escape让focus回已选抽屉。分支变化只改existing text，不创建一份新的detail；快速多点以latest intent覆盖过时timer。

## 4. Measured Layout & 1280x800 Viewport Geometry

1280x800窗内main x32/y24宽1216高752、padding24后content1168×704。唯一直接孩子telescopic-roi-frame为三列460/456/220、gap16两次，合1168。左列上下8px：六抽屉108px/gap8共688，8+688+8=704；每抽屉内部padding8，可用444×92，标题16、gap2、两排metric各37px。每排两格216px/gap12，读数11px/12px且最多三行，脚本两文件占两行、均值/P95/成功率占第三行；全部16+2+74=92px，不挤下条抽屉。脚本长名在连字符断行，右宽220px也允许自然断名不截数据。

中央井padding8后440×688。三个Prompt节点各128×40并排不放得下，因此竖排在x12/y36、88、140，再向y228的L0 hub x12..156汇合，出口位于x180..440。七个出口56px高，y232起至624；终点全名两行13px和值一行13px。输入先竖向C合流，如 d="M 40,76 C 40,146 80,158 80,228 L 92,228 C 92,158 52,146 52,76 Z"；输出如 d="M 156,242 C 164,242 170,244 180,244 L 180,256 C 170,256 164,254 156,254 Z"，closed filled cubic-Bezier、gradient fill，stroke-width <= 24（实际0.5）。中央线路短也要C不是折线。视觉光带不撑宽列，label是HTML1:1覆盖。button、抽屉拉手和路径辅助靶 >= 28x28px。

## 5. Dual-Theme Surface Polarity & Alluvial / Paper-Pocket Craft

TelescopicConduitFile light canvas#F3F1EC、drawer#FFFCF6、well#EAEAF4、note#F9F7F0、ink#303044、secondary#686879、accent#5955AA；dark#181922/#2B2B39/#202131/#32313D/#F5F1FA/#C4C0D1/#C2BCFA。抽屉外圆角12、内纸6、井圆角20；纸口shadow inset 0 1px 2px #15132314、外纸层y3，所有文字前景与阴影脱离。

Liquid Glass显式关闭：blur0、displacement0、refraction0，不能把抽屉半透明叠成六层玻璃。refs紫→蓝、scripts紫→青，冷reference灰色2px库存关联，禁发光。读数90%中性色，选中拉手才用品牌色；正文4.5:1、focus3:1。减少透明度无信息损失，主题随外层data-theme，不加inner theme switch。

## 6. Apple Native Spring Physics & Flow Animation

左抽屉translateX(6px)，中央井内页translateY(-5px)→0，两者450ms cubic-bezier(0.22, 1.35, 0.36, 1)；井收展不裁最右明细字，note固定在220px列。C曲中心流珠2400ms，输入竖弯与输出横弯均按自己path animateMotion，不能用直线从顶扫到底；cold关系无珠。hover改变路径fill-alpha和右纸标题150ms，脉冲不改变实际数值。

prefers-reduced-motion停流珠、取消伸移与spring，静态箭头让竖转横路线仍可理解；收展1ms。focus-visible2px，隐藏图不进Tab，routeOpen=false仍可重新点本抽屉。selection announce只读Skill名一次，不每帧aria-live刷屏。

## 7. Production Data Inventory & Exact DOM Topology

抽屉四组数据及井中路线第五组全部属于批准范围，脚本均值缺失时用—，L0是SKILL.md入口Token而L1是references/*.md平均连带Token；Cache解读为KV Cache命中率，抽屉会话数是活跃会话数。eval-cases.json清楚列出周增、通过与拦逃：

| 抽屉所属 Skill | 调用与会话读区 | L0/L1/cache读区 | scripts读区 | eval-cases.json读区 |
|---|---|---|---|---|
| my-designer | 7d 42 次 · 30d 156 次 · 28 会话 | L0 1.8k tok · L1 +3.4k tok · Cache 96.8% | design_evidence.py 46次 · 均值 140ms · P95 310ms · 成功率 99.1% | 24 用例 (+4 本周) · 100% 通过 · 拦截 19 / 逃逸 2 |
| team-lead | 7d 68 次 · 30d 240 次 · 41 会话 | L0 2.1k tok · L1 +2.8k tok · Cache 97.4% | goal-queue.py 64次 · ci-monitor.py 38次 · 均值 — · P95 420ms · 成功率 99.5% | 32 用例 (+6 本周) · 100% 通过 · 拦截 27 / 逃逸 1 |
| design-studio | 7d 19 次 · 30d 74 次 · 16 会话 | L0 1.5k tok · L1 +2.2k tok · Cache 95.9% | design_catalog.py 39次 · 均值 — · P95 480ms · 成功率 100% | 18 用例 (+2 本周) · 100% 通过 · 拦截 11 / 逃逸 0 |
| m2-dispatcher | 7d 51 次 · 30d 188 次 · 35 会话 | L0 1.6k tok · L1 +1.9k tok · Cache 97.1% | herdr-dispatch.sh 52次 · 均值 — · P95 260ms · 成功率 99.2% | 20 用例 (+3 本周) · 100% 通过 · 拦截 15 / 逃逸 1 |
| linear-board | 7d 33 次 · 30d 112 次 · 22 会话 | L0 1.4k tok · L1 +1.5k tok · Cache 96.5% | linear-bot-bridge.py 44次 · 均值 — · P95 350ms · 成功率 98.8% | 16 用例 (+2 本周) · 100% 通过 · 拦截 9 / 逃逸 0 |
| archive-deck-helper | 7d 0 次 · 30d 0 次 · 0 会话 · 30d 零调用 · 建议归档 | L0 2.6k tok · L1 +4.8k tok · Cache 0.0% | render_legacy.py 0次 · 均值 — · P95 0ms · 成功率 — | 4 用例 (+0 本周) · 75% 通过 · 拦截 0 / 逃逸 3 |

my-designer井的实际标签为UI 探索画廊48%、实现后截图回溯34%、规范审计18%→SKILL.md (L0 入口 · 1.8k tok)。右A references/*.md：navigation-evidence-contract.md（62% · 2.4k tok）、interaction-layering.md（28% · 1.6k tok）、appearance-ledger.md（19% · 1.4k tok）、remotion-video.md（0 命中 · 冷门冗余告警 · 3.1k tok）；右B scripts/*.py：design_evidence.py（46次 · P95 310ms · 98.5%）、design_catalog.py（39次 · P95 480ms · 100%）、verify_design_cases.py（18次 · P95 190ms · 100%）。note内全文「拦截 19 次 · 逃逸 2 次 [1 IMPL_BUG / 1 SPEC_GAP]」。抽屉汇总99.1%与script分支98.5%分别标scope，不强行校正批准库存。

reference命中率以Skill调用为分母、可多读，所以不可归一化62/28/19；script次数独立，不跨token/ms做守恒宽带。remotion虽常驻但0命中关系是库存线而不是实际读取。非my-designer井使用本人L0与已知script，左未知Prompt写「意图分类未记录」，右未知reference写「引用明细未记录」；没有给avg/文件不猜测。archive井说明P95 0ms未运行、无读取路径，不补假pulse。建议归档只读，禁止连接宿主或外部数据服务。

```html
<main class="telescopic-conduit-file topology-telescopic-skill-drawers">
  <section class="content">
    <div class="telescopic-roi-frame">
      <ol class="skill-drawer-column"><li data-skill-row data-skill="my-designer"><button data-skill-trigger><strong></strong><span class="drawer-metric-pairs"></span><i class="drawer-finger-lip"></i></button></li><li data-skill-row data-skill="team-lead"></li><li data-skill-row data-skill="design-studio"></li><li data-skill-row data-skill="m2-dispatcher"></li><li data-skill-row data-skill="linear-board"></li><li data-skill-row data-skill="archive-deck-helper"></li></ol>
      <figure class="bezier-conduit-well"><figcaption></figcaption><div class="vertical-route-maps"><section data-bifurcation-panel data-skill="my-designer"><svg></svg><nav class="conduit-well-ends"></nav></section></div></figure>
      <aside class="script-eval-ledger"><div class="telescopic-detail-notes"><dl data-skill-note="my-designer"></dl></div></aside>
    </div>
  </section>
</main>
```

其余五li补齐metric-pairs与button，中央、右侧静态补本人map/note，保持三列同一frame树。禁止用共享模板把别案变抽屉壳。Stage 1无HTML实现、无部署或winner冻结。

## 8. Explicit Anti-Patterns & Verification Targets

伸缩柜禁S1–S12及S1/S2/S3/S4/S5/S6/S7/S8/S9/S10/S11/S12旧词，禁stroke-width > 24、innerHTML replacement、remove/replaceChildren、.caustic-veil、.ruler、Active-Matte、<select>测试state、sandbox disclaimers，禁hero/fold-panel/secondary直子类。不能用箭头折线代替C、不能把竖向Prompt层捏成新Skill类别。

Writer待验WebKit1280x800两主题六抽屉全露，440px图区所有端口全名和值可读；伸6px不挤右列，至少28px靶与focus边不裁。逐行收展、hover/click/keyboard branch、Escape回抽屉，MutationObserver严格removedElements = 0。unknown与零调用是数据缺口不是成功路径；0命中无运动、双scope成功率不被混写，页无横向外溢。本稿不声称已过rendered gates。
