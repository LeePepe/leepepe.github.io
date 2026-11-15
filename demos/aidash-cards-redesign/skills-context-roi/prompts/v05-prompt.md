# v05 · 专业矩阵底屉 (topology-pro-matrix-drawer)

## 1. Visual Metaphor & Archetype Lock

用Linear的紧凑column discipline与Raycast的键盘明确性，做五列Skill矩阵：名称加四组Owner指标。底部抽屉属于矩阵选中项，而非全屏command palette。desktop，component/chart-dataviz/layout-navigation/motion-interaction；VS-007 × CL-008 violet remix；X=矩阵行button / Y=底部纸屉 / Z=矩阵平面与下沉屉。AppTheme候选CommandMatrixDrawer。

20px面板名、13px行标题、12px指标/文件、11px图注；SF Mono仅路径与数字，普通中文系统字体。24×24 SVG使用1.4px描边的分叉、向下chevron；「点击行查看读取路线」是直白入口，不能出现命令代号墙。

## 2. Single P0 Focus & Initial Showcase State

唯一焦点为my-designer的底屉，初始展开244px，先高亮verify_design_cases.py，显示18次/P95 190ms/100%。六行四指标均留在上方，my-designer不是另画大Hero；固定top-rail写当前选择。用户首先看见真实Prompt→L0→references与scripts全分岔，而不是空抽屉等待点击。

## 3. P1 / P2 Progressive Folding & Permanent DOM Contract

P1五列矩阵可一眼对齐，P2只有spring-bifurcation-drawer内的六份静态route-record。每行原生button内部五个span，不包含分支控件；分支控件在独立article内。click另一行更换activeRecord并保持屉高，重复click关闭屉；Escape关闭并把focus归还该行。选中状态和屉开关分别存，关闭并不失去selectedSkill。

规定removedElements = 0、零innerHTML rebuild：预写全部六record，未活跃者inert/aria-hidden、opacity0；已有Text.data改详情，永远不物理移走row。光带hover关联详情，click或Enter固定pin，离开恢复pin；不让mouseover触发行变更。快速连续切换取消旧record的回调；屉内focus离开前若要换Skill，先移至新行，防隐藏focus。外层chooser掌管主题、视口、选择摘要，不在矩阵里加测试下拉。

## 4. Measured Layout & 1280x800 Viewport Geometry

1280x800时main x32/y24、1216×752、padding24，content1168×704；rail44 + gap8 + head32 + gap8 + rows360 + gap8 + drawer244，和704。六行60px。表列可用1136px：168/196/216/260/248 + gap12×4=1136；head和row必须同一CSS grid template、same padding16。指标最多3行14px，高度42余18留padding；僵尸徽章在calls第三行以文字不靠emoji。

底屉有效1136×244，Prompt x0..188、hub x332..472、终点标签x720..1136；七个出口28px高按y20..216，detail占y216..244，图标题并入上方rail不再多占行。样例closed fill d="M 472,118 C 554,118 632,160 720,160 L 720,172 C 632,172 554,132 472,132 Z"；所有支流都遵循M C L C Z，stroke-width <= 24（实际0.6px）。标签作为HTML端口，两个字号最多12/11px，长名允许连字符断开不省略。每端口、行及屉折叠键 >= 28x28px；路径另有28px最小辅助靶，不画粗stroke管。

## 5. Dual-Theme Surface Polarity & Alluvial / Paper-Pocket Craft

CommandMatrixDrawer light #F7F8FC底、#FFFFFF矩阵、#EDF0FA屉、#222744正文、#59617E副字、#514DB4焦点；dark #101421/#202638/#171D2D/#F1F3FF/#B7BED8/#B8B0FF。矩阵无单元格框，只leading hairline，选择底#EEEFFC/#2D2D4B。屉口用两层0.5px亮边与inset 0 2px 6px #13163016，扁平表面与纸屉深度不同。

无Liquid Glass，光学blur0/displacement0/refraction0；所有值在固体背景，流带violet→blue与violet→sage，只有pin亮度提高，不更改带宽。remotion节点灰紫库存关系，0命中无pulse。警告字#805B1B/#F2C981以浅底承载，不给75%通过打绿勾。focus3:1、正文4.5:1；dark不保留白矩阵，减透明度同样纸屉可读。

## 6. Apple Native Spring Physics & Flow Animation

底屉用440ms cubic-bezier(0.22, 1.35, 0.36, 1)从0到244px，内纸translateY(8px)→0，文字只opacity160ms。切Skill不重跑整个屉的弹出，只让新record淡入；选中row左标90ms迁移。沿C带中心微光用stroke-dashoffset周期2000ms，虚线长度6px、gap120px、描边1.2px、低alpha，不能用横扫直线假装流向。

prefers-reduced-motion时C脉冲停止、height与位移1ms结算，方向由静态arrowhead保留。键盘按Tab走六个行再到打开屉七端口，Space不可让body滚动；focus-visible2px/offset2。禁止⌘K劫持宿主或扩展成未声明命令功能。

## 7. Production Data Inventory & Exact DOM Topology

专业矩阵的五列是Skill身份和四组实指标，第五个业务指标是行选后的路线图，矩阵上L0的定义是SKILL.md Token，L1的定义是references/*.md平均连带Token，Cache为KV Cache命中率；会话指活跃会话数。不另加评分、排名或成本金额：

| 矩阵键 Skill | 调用/僵尸 | Token负担/缓存 | scripts/*.py 执行绩效 | eval-cases.json 证据列 |
|---|---|---|---|---|
| my-designer | 7d 42 次 · 30d 156 次 · 28 会话 | L0 1.8k tok · L1 +3.4k tok · Cache 96.8% | design_evidence.py 46次 · 均值 140ms · P95 310ms · 成功率 99.1% | 24 用例 (+4 本周) · 100% 通过 · 拦截 19 / 逃逸 2 |
| team-lead | 7d 68 次 · 30d 240 次 · 41 会话 | L0 2.1k tok · L1 +2.8k tok · Cache 97.4% | goal-queue.py 64次 · ci-monitor.py 38次 · 均值 — · P95 420ms · 成功率 99.5% | 32 用例 (+6 本周) · 100% 通过 · 拦截 27 / 逃逸 1 |
| design-studio | 7d 19 次 · 30d 74 次 · 16 会话 | L0 1.5k tok · L1 +2.2k tok · Cache 95.9% | design_catalog.py 39次 · 均值 — · P95 480ms · 成功率 100% | 18 用例 (+2 本周) · 100% 通过 · 拦截 11 / 逃逸 0 |
| m2-dispatcher | 7d 51 次 · 30d 188 次 · 35 会话 | L0 1.6k tok · L1 +1.9k tok · Cache 97.1% | herdr-dispatch.sh 52次 · 均值 — · P95 260ms · 成功率 99.2% | 20 用例 (+3 本周) · 100% 通过 · 拦截 15 / 逃逸 1 |
| linear-board | 7d 33 次 · 30d 112 次 · 22 会话 | L0 1.4k tok · L1 +1.5k tok · Cache 96.5% | linear-bot-bridge.py 44次 · 均值 — · P95 350ms · 成功率 98.8% | 16 用例 (+2 本周) · 100% 通过 · 拦截 9 / 逃逸 0 |
| archive-deck-helper | 7d 0 次 · 30d 0 次 · 0 会话 · 30d 零调用 · 建议归档 | L0 2.6k tok · L1 +4.8k tok · Cache 0.0% | render_legacy.py 0次 · 均值 — · P95 0ms · 成功率 — | 4 用例 (+0 本周) · 75% 通过 · 拦截 0 / 逃逸 3 |

my-designer record路径库存独立写全：UI 探索画廊48%、实现后截图回溯34%、规范审计18%归入SKILL.md (L0 入口 · 1.8k tok)。references/*.md四条为navigation-evidence-contract.md（62% · 2.4k tok）、interaction-layering.md（28% · 1.6k tok）、appearance-ledger.md（19% · 1.4k tok）、remotion-video.md（0 命中 · 冷门冗余告警 · 3.1k tok）；scripts/*.py三条为design_evidence.py（46次 · P95 310ms · 98.5%）、design_catalog.py（39次 · P95 480ms · 100%）、verify_design_cases.py（18次 · P95 190ms · 100%）。details追加「拦截 19 次 · 逃逸 2 次 [1 IMPL_BUG / 1 SPEC_GAP]」。99.1%带「行级汇总」标签，98.5%带「脚本分支」标签，以免相同名字误示矛盾。

references hit是非排他命中，不把62%/28%/19%压成一条100%堆积条；scripts次数和reference tok分开编码。0命中仍画细灰库存连接而非活跃带，位置不能消失。除my-designer外无给定的意图/refs细节：各record显示本人L0和已有脚本C带，左「意图分类未记录」、右「引用明细未记录」，不捏造文件、比例、avg或逃逸分类。archive record显示「30d 零调用 · 无读取路径」，P95 0ms的语义是未运行。归档建议不产生真实数据变更。

```html
<main class="command-matrix-drawer topology-pro-matrix-drawer">
  <section class="content">
    <header class="matrix-top-rail"><h1></h1><span class="matrix-selection-label"></span></header>
    <div class="matrix-head-grid"><span></span><span></span><span></span><span></span><span></span></div>
    <div class="matrix-skill-rows"><section data-skill-row data-skill="my-designer"><button data-skill-trigger><span class="matrix-skill-key"></span><span class="matrix-calls"></span><span class="matrix-tokens"></span><span class="matrix-script-stats"></span><span class="matrix-eval-stats"></span></button></section><section data-skill-row data-skill="team-lead"></section><section data-skill-row data-skill="design-studio"></section><section data-skill-row data-skill="m2-dispatcher"></section><section data-skill-row data-skill="linear-board"></section><section data-skill-row data-skill="archive-deck-helper"></section></div>
    <article class="spring-bifurcation-drawer"><div class="matrix-route-records"><figure class="matrix-route-record" data-bifurcation-panel data-skill="my-designer"><svg></svg><nav class="matrix-branch-buttons"></nav></figure></div><dl class="matrix-detail-line"></dl></article>
  </section>
</main>
```

补五个section和五个figure的常驻内容，不以JS模板复用同一DOM树到所有vXX。Writer实现该候选的具体HTML，Stage 1不跑宿主脚本、不部署、不冻结winner。

## 8. Explicit Anti-Patterns & Verification Targets

矩阵禁止S1–S12与逐项S1/S2/S3/S4/S5/S6/S7/S8/S9/S10/S11/S12上屏；禁止stroke-width > 24、innerHTML replacement、replaceChildren/remove、.caustic-veil、.ruler、Active-Matte、<select>test switches、sandbox disclaimers。禁hero/fold-panel/secondary直子类、未声明command palette和为了紧凑省略数字单位。

Writer用WebKit1280x800检两主题、六行四metrics、正确header列边界与完整底屉；再测全部端口hover/click、Enter/Space行收展、Escape focus、快速六行切换。MutationObserver计removedElements = 0，0命中无pulse，隐藏record无tab stop，所有按钮至少28px。数字不能ellipsis，全部文件名可见，页级scrollWidth不大于clientWidth。这里交付约束而非运行结果。
