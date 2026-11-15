# v10 · 同心导流控制台 (topology-concentric-flow-console)

## 1. Visual Metaphor & Archetype Lock

借macOS 26同心容器与Linear inspector的空间逻辑，整台浮起但内容固体：左六Skill选择账、中三阶段Bezier图、右评测/脚本/冷文件诊断dock。所谓同心是嵌套圆角半径递减，不画圆环轨道或新地图。desktop四维component/chart-dataviz/glass-material/layout-navigation；VS-007 × CL-008 navy-blue；X=左表select / Y=右诊断lens / Z=外唇功能玻璃与实心三列。AppTheme候选ConcentricRouteConsole。

20px顶部题、13px行名、12px数值/路径、11px诊断副字；SF Pro/PingFang及SF Mono，24×24 inline SVG1.5px画split与paper-file。顶部只有「Skills 效能与上下文」，没有重复六Skill摘要和旧编号导航。

## 2. Single P0 Focus & Initial Showcase State

首屏my-designer选择账已展开其中央canvas，默认pin design_evidence.py，右dock active lens「脚本」。唯一P0是该Skill的Prompt→L0→两类文件分岔；右dock给46次/P95 310ms/98.5%和行汇总均值140ms。六Skill常驻左账、0调用行明显，中央七终点完整，评测与冷文件lens也能点击到达不需新页面。

## 3. P1 / P2 Progressive Folding & Permanent DOM Contract

左P1四组指标按Skill行五列排列；中央P2六张console-map已挂载，右P2三lens×六Skill的dl也静态存在。选择别行同时更换中图和右lens所属Skill；重复点收中央canvas但仍保留选中行与dock摘要。dock只读检查与选分支，无真实归档、重跑或新建任务能力。「评测 / 脚本 / 冷门文件」是本图明细lens，不是新增产品screen。

规定removedElements = 0、零innerHTML rebuild。button[data-skill-trigger]内纯文本，dock及endpoint独立原生button；未活跃map/lens-panel inert/aria-hidden，选择只改class/dataset、Text.data与aria。hover reference同步dock临时亮对应说明，click固定pin并转对应lens，mouseleave恢复pin/lens。keyboard Enter/Space等效，Escape收图回左行，切行前若focus在旧图要移回新行。latest selection校验阻止过时动画切错dock。

## 4. Measured Layout & 1280x800 Viewport Geometry

1280x800 frame x32/y24、1216×752、padding24，content1168×704：top48 + gap12 + tri604 + gap12 + bottom28。tri三列420/508/216、两gap12，总1168。左表padding8后404px，五列96/72/78/92/50、gap4×4=16，合404；六行98px和上下8px共604。窄脚本与Eval列用11px/12px，92px脚本列最多七行84px加上下5px=94px；50px Eval列最多六行72px加上下5px=82px。名称、调用与Token仍为12px/14px，可在连字符和短单位之间自然换行；不得以仅名称的selector偷藏指标。

中figure内484×580。Prompt88、hub90、出口标签250、两gap28，合484；中心三类入口沿左列y120/184/248，L0中列y240，七出口56px高从y48到440，底branch-strip y468..564。例带 d="M 206,252 C 216,252 224,120 234,120 L 234,132 C 224,132 216,266 206,266 Z"，closed fill用M C L C Z、linearGradient，stroke-width <= 24（实际0.6）。端口56px、250px宽支持长名两行13px和值一行，不把SVG文本scale小。右dock216×604，lens三button各64×32/gap4，content padding12可用192px，脚本/归因可自然多行。全部端口、lens、左行以及图的辅助靶 >= 28x28px。

## 5. Dual-Theme Surface Polarity & Alluvial / Paper-Pocket Craft

ConcentricRouteConsole light#F4F7FC canvas/#FFFFFF left/#EDF3FA center/#F8FAFD dock/#1A2B42 ink/#53677F muted/#265CAD accent；dark#0E131F/#202C3E/#162436/#243248/#F3F7FE/#BACADF/#9DC8FF。外frame radius28，tri panes16，内按钮8，保持28−12=16的同心padding逻辑。选中行只是淡蓝底与侧墨线，dock没有第四层卡框。

外top-bar为唯一功能玻璃：IOR1.5、bevel10px、displacement14px、blur2.5px、saturation145%，light白alpha.76/dark蓝黑alpha.8，仅采样solid canvas。WebKit fallback及reduce-transparency用#FFFFFF/#29394F实心唇和0.5px高光，不叠glass。三列内容绝不backdrop-filter。reference蓝→靛、script蓝→青，cold灰色库存关系且无pulse；text4.5:1、focus3:1，dark不残留白dock。outer chooser仍独占theme/viewport/SELECT/STAR控制。

## 6. Apple Native Spring Physics & Flow Animation

中央map换页460ms cubic-bezier(0.22, 1.35, 0.36, 1)，横移5px归零，右dock仅opacity160ms更新；收图保持整个604px tri外壳不变，让canvas内部0fr而非抹掉figure。端点pin色90ms响应，微光粒子沿真实C中心1950ms单向走，冷库存无光，drawer-like dock纸口只动2px不挥舞。

prefers-reduced-motion取消位移、光粒与弹性，map/lens即时切换，静态箭头与selected-outline维持理解；功能玻璃fallback仍是单层。focus-visible2px/offset2，Tab先六行后七branch再三lens；Escape回选择表，不弹新窗口。脉冲只表方向、不能当运行状态或改calls数字。

## 7. Production Data Inventory & Exact DOM Topology

同心控制台保留五真实指标：左账四项调用/上下文/scripts/Eval，中央交互路线为第五项；控制台明确L0为SKILL.md Token、L1为references/*.md平均连带Token，Cache为KV Cache命中率；会话列写活跃会话数。eval-cases.json与KV Cache要写清来源名字，不生成收益评分：

| 控制台 Skill | 周月调用与会话 | L0/L1与缓存开销 | 执行脚本效率 | eval-cases.json效果 |
|---|---|---|---|---|
| my-designer | 7d 42 次 · 30d 156 次 · 28 会话 | L0 1.8k tok · L1 +3.4k tok · Cache 96.8% | design_evidence.py 46次 · 均值 140ms · P95 310ms · 成功率 99.1% | 24 用例 (+4 本周) · 100% 通过 · 拦截 19 / 逃逸 2 |
| team-lead | 7d 68 次 · 30d 240 次 · 41 会话 | L0 2.1k tok · L1 +2.8k tok · Cache 97.4% | goal-queue.py 64次 · ci-monitor.py 38次 · 均值 — · P95 420ms · 成功率 99.5% | 32 用例 (+6 本周) · 100% 通过 · 拦截 27 / 逃逸 1 |
| design-studio | 7d 19 次 · 30d 74 次 · 16 会话 | L0 1.5k tok · L1 +2.2k tok · Cache 95.9% | design_catalog.py 39次 · 均值 — · P95 480ms · 成功率 100% | 18 用例 (+2 本周) · 100% 通过 · 拦截 11 / 逃逸 0 |
| m2-dispatcher | 7d 51 次 · 30d 188 次 · 35 会话 | L0 1.6k tok · L1 +1.9k tok · Cache 97.1% | herdr-dispatch.sh 52次 · 均值 — · P95 260ms · 成功率 99.2% | 20 用例 (+3 本周) · 100% 通过 · 拦截 15 / 逃逸 1 |
| linear-board | 7d 33 次 · 30d 112 次 · 22 会话 | L0 1.4k tok · L1 +1.5k tok · Cache 96.5% | linear-bot-bridge.py 44次 · 均值 — · P95 350ms · 成功率 98.8% | 16 用例 (+2 本周) · 100% 通过 · 拦截 9 / 逃逸 0 |
| archive-deck-helper | 7d 0 次 · 30d 0 次 · 0 会话 · 30d 零调用 · 建议归档 | L0 2.6k tok · L1 +4.8k tok · Cache 0.0% | render_legacy.py 0次 · 均值 — · P95 0ms · 成功率 — | 4 用例 (+0 本周) · 75% 通过 · 拦截 0 / 逃逸 3 |

中央my-designer完整路由标签：UI 探索画廊48%、实现后截图回溯34%、规范审计18%归入SKILL.md (L0 入口 · 1.8k tok)。references/*.md出口navigation-evidence-contract.md（62% · 2.4k tok）、interaction-layering.md（28% · 1.6k tok）、appearance-ledger.md（19% · 1.4k tok）、remotion-video.md（0 命中 · 冷门冗余告警 · 3.1k tok）；scripts/*.py出口design_evidence.py（46次 · P95 310ms · 98.5%）、design_catalog.py（39次 · P95 480ms · 100%）、verify_design_cases.py（18次 · P95 190ms · 100%）。dock评测lens全文「拦截 19 次 · 逃逸 2 次 [1 IMPL_BUG / 1 SPEC_GAP]」。脚本lens同时标「Skill汇总成功率 99.1%」及「此脚本成功率 98.5%」，两种口径不偷偷统一。

refs hit按调用命中可以同时读取，62+28+19非100%守恒；scripts按次数独立编码，token/ms不拿来画同单位流量。cold节点2px灰库存关联不能发pulse。其余Skill的map用本人L0和已给脚本，缺失左Prompt/右reference为「意图分类未记录」「引用明细未记录」，没有source就不猜均值或逃逸分类。archive保持P95 0ms但说明未运行、0会话没有读取/执行路线。dock建议归档仅说明无真实操作，所有数据来自approved domain而非live遥测请求。

```html
<main class="concentric-route-console topology-concentric-flow-console">
  <section class="content">
    <header class="console-top-bar"><h1></h1><span></span></header>
    <div class="tri-column-console">
      <aside class="skill-list-pane"><ol class="console-skill-records"><li data-skill-row data-skill="my-designer"><button data-skill-trigger></button></li><li data-skill-row data-skill="team-lead"></li><li data-skill-row data-skill="design-studio"></li><li data-skill-row data-skill="m2-dispatcher"></li><li data-skill-row data-skill="linear-board"></li><li data-skill-row data-skill="archive-deck-helper"></li></ol></aside>
      <figure class="center-bezier-canvas"><div class="console-map-stack"><section class="console-map" data-bifurcation-panel data-skill="my-designer"><svg></svg><nav class="console-endpoints"></nav></section></div><figcaption class="console-path-strip"></figcaption></figure>
      <aside class="right-diagnostics-dock"><nav class="diagnostic-lenses"><button data-lens="eval">评测</button><button data-lens="script">脚本</button><button data-lens="cold">冷门文件</button></nav><div class="console-diagnostic-records"><dl data-skill-note="my-designer"></dl></div></aside>
    </div>
    <footer class="console-bottom-lip"><p></p></footer>
  </section>
</main>
```

补五li完整五列button、五console-map、每Skill三lens明细；不得将generic空壳实现当完成。Designer只交候选，不造新功能、不生产实现、不发布或替Owner冻结主题。

## 8. Explicit Anti-Patterns & Verification Targets

控制台严禁S1–S12以及S1/S2/S3/S4/S5/S6/S7/S8/S9/S10/S11/S12上屏；禁stroke-width > 24、.caustic-veil、.ruler、Active-Matte、<select>test switches、sandbox disclaimers、innerHTML replacement及remove/replaceChildren。content不许hero/fold-panel/secondary直子类，不能画同心轨道仪表、虚构archive action或六行只保留名字。

后续WebKit1280x800双主题检查420/508/216三列真实读数与长文件全名、≥28px靶区、无numeric truncation/外溢。六Skill点选收展，七branch hover/click/keyboard，三lens切换皆需正确scope、MutationObserver removedElements = 0、隐藏内容无focus；cold不发光，行级/脚本成功率同时可读，Escape回行。再验glass fallback与reduced-motion可读性，此稿不声明真实渲染通过。
