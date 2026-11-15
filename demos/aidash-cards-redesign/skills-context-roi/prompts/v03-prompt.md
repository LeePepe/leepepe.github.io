# v03 · 浮光丝带工作台 (topology-glass-ribbon-workbench)

## 1. Visual Metaphor & Archetype Lock

设计一张有清晰操作冠部的macOS工作台：玻璃只是一道浮在顶部的功能唇，六行数据是实心底板，下面宽幅曲带是展开的工作图纸。不是把透明效果抹在每条Skill上。desktop四维component/chart-dataviz/glass-material/motion-interaction；VS-003精密工作台 × CL-003 cyan remix，X=整排选取 / Y=下方宽剧场 / Z=单层玻璃冠与固体图纸。候选主题PrismRibbonBench，参考CleanShot X的轻量工具唇而非复刻其界面。

SF Pro20px标题、13px行名、12px数据与文件、11px图注；PingFang中文，数字tabular。24×24 SVG细描边画分岔、箭头和折叠符，所有图标都有可读名字，不用emoji装饰标题。六行deck严禁变六张同权bento。

## 2. Single P0 Focus & Initial Showcase State

开场的my-designer已选，宽剧场展开；P0是L0后reference/script双出口，而不是顶部Cache大数字。默认appearance-ledger.md高亮，详情为19%/1.4k tok；三类意图、四reference、三script全部已在首屏。冠部写「Skills 上下文工作台」和可操作「收起流向」按钮，脚下Eval strip附完整两次逃逸归因。

## 3. P1 / P2 Progressive Folding & Permanent DOM Contract

P1六行每行四组指标横向齐读；P2在wide-alluvial-theater内六个scene静态叠置，仅当前scene开放。点其他Skill同时换剧场内容、冠部selected标签和Eval条；点同一行或冠部折叠键收图，再开保留该Skill点击的分支。剧场收起只影响图高，六行不作离场动画，绝不能让选择变成数据过滤。

所有li、svg、endpoint按钮、六个Eval归因段在initial HTML出现；removedElements = 0、零innerHTML rebuild。用dataset、CSS自定义属性和原有Text.data更新选择，关闭scene inert且aria-hidden；新scene只解除自身限制。按最新版请求取消过时transitionend工作。hover.preview只点亮一带和明细，点击.pin保存，pointerleave复位到pin，Escape回行。原生button配aria-controls/aria-expanded，scene标签外置HTML避免SVG文字被缩成小字。

## 4. Measured Layout & 1280x800 Viewport Geometry

1280x800桌面frame x32/y24、1216×752、padding24。content1168×704依次crown44/gap12/deck336/gap12/theater260/gap12/escape28。deck六行56，内部宽1136列156/196/216/266/254，gap12×4=48，总1136；所有行与隐藏语义header共享列模板。三个读数文本行各14px，上下7px。较长脚本可断在下划线/连字符，不能截断次数和成功率。

剧场padding8后的1152×244：Prompt x0..172，L0 x340..484，右出口x736..1152；出口七项在y8..204，每个28px，参考四项和脚本三项用浅背景分组而非另占heading高度。branch detail y212..240。C带示例 d="M 484,88 C 572,88 650,148 736,148 L 736,160 C 650,160 572,102 484,102 Z"，stroke-width <= 24（实际1），完整渐变填充闭合；入口分别连接同一SKILL.md hub。label全名用HTML，按钮至少 >= 28x28px，带本体薄于14px却有透明28px靶区，不能用stroke-width32的透明粗管伪充视觉带。

## 5. Dual-Theme Surface Polarity & Alluvial / Paper-Pocket Craft

PrismRibbonBench light底#F2F6FA、板#FFFFFF、图纸#EAF2F8、墨#102D40、次字#486675、焦点#096C94；dark为#0E1821/#1B2A36/#13222D/#EDF8FF/#A9C4D2/#8EDBFA。reference cyan→indigo、scripts cyan→sage，冷门灰蓝无pulse。光学冠只有功能控件：regular玻璃白alpha.72 light、slate alpha.78 dark，IOR1.5、bevel12px、displacement16px、blur2.5px、saturation140%，仅采样实心画布。WebKit无法折射时同色不透明浮唇+0.5px高光，不上斑纹滤镜。

六行deck与theater一律不使用backdrop-filter。减少透明度也将crown变#FFFFFF/#223443，主题切换不重挂载。阴影只冠部0 8px 20px #15324F12，其他纸边靠2%–4%亮度阶；文字至少4.5:1，焦点3:1。此案玻璃层只有一个，禁止glass采样glass。

## 6. Apple Native Spring Physics & Flow Animation

剧场展开500ms cubic-bezier(0.22, 1.35, 0.36, 1)，固体图纸translateY(-6px)归零；scene交接时上层离场opacity120ms，下层入场180ms，壳高最多260。选择波纹仅在相应行下缘点到为止。沿曲带的薄白pulse取中心C路径1900ms匀速移动，ref与script相位不同，hover让该pulse停在终点而非加速假造活跃性。

prefers-reduced-motion禁止位移、pulse、spring，收展1ms并以静态箭头明确方向。鼠标或键盘选出口即时更新详情；focus ring2px。收图前如果焦点在scene内移回选中行，外层chooser保留主题/视口/STAR/SELECT权限，子页不生重复控制栏。

## 7. Production Data Inventory & Exact DOM Topology

浮光方案的每一行仍保留真实四组账目，流向交互构成第五组；其中L0记录SKILL.md Token，L1标references/*.md平均连带Token，Cache说明为KV Cache命中率，频次旁的会话数是活跃会话数。表内的—是未给的avg，不是计算失败替代：

| 工作台 Skill | 周/月/会话 | Token与缓存开销 | scripts/*.py 数量/效率 | eval-cases.json 评测效果 |
|---|---|---|---|---|
| my-designer | 7d 42 次 · 30d 156 次 · 28 会话 | L0 1.8k tok · L1 +3.4k tok · Cache 96.8% | design_evidence.py 46次 · 均值 140ms · P95 310ms · 成功率 99.1% | 24 用例 (+4 本周) · 100% 通过 · 拦截 19 / 逃逸 2 |
| team-lead | 7d 68 次 · 30d 240 次 · 41 会话 | L0 2.1k tok · L1 +2.8k tok · Cache 97.4% | goal-queue.py 64次 · ci-monitor.py 38次 · 均值 — · P95 420ms · 成功率 99.5% | 32 用例 (+6 本周) · 100% 通过 · 拦截 27 / 逃逸 1 |
| design-studio | 7d 19 次 · 30d 74 次 · 16 会话 | L0 1.5k tok · L1 +2.2k tok · Cache 95.9% | design_catalog.py 39次 · 均值 — · P95 480ms · 成功率 100% | 18 用例 (+2 本周) · 100% 通过 · 拦截 11 / 逃逸 0 |
| m2-dispatcher | 7d 51 次 · 30d 188 次 · 35 会话 | L0 1.6k tok · L1 +1.9k tok · Cache 97.1% | herdr-dispatch.sh 52次 · 均值 — · P95 260ms · 成功率 99.2% | 20 用例 (+3 本周) · 100% 通过 · 拦截 15 / 逃逸 1 |
| linear-board | 7d 33 次 · 30d 112 次 · 22 会话 | L0 1.4k tok · L1 +1.5k tok · Cache 96.5% | linear-bot-bridge.py 44次 · 均值 — · P95 350ms · 成功率 98.8% | 16 用例 (+2 本周) · 100% 通过 · 拦截 9 / 逃逸 0 |
| archive-deck-helper | 7d 0 次 · 30d 0 次 · 0 会话 · 30d 零调用 · 建议归档 | L0 2.6k tok · L1 +4.8k tok · Cache 0.0% | render_legacy.py 0次 · 均值 — · P95 0ms · 成功率 — | 4 用例 (+0 本周) · 75% 通过 · 拦截 0 / 逃逸 3 |

剧场起点是UI 探索画廊48%、实现后截图回溯34%、规范审计18%，汇入SKILL.md (L0 入口 · 1.8k tok)；reference层具体为navigation-evidence-contract.md（62% · 2.4k tok）、interaction-layering.md（28% · 1.6k tok）、appearance-ledger.md（19% · 1.4k tok）、remotion-video.md（0 命中 · 冷门冗余告警 · 3.1k tok）。scripts层为design_evidence.py（46次 · P95 310ms · 98.5%）、design_catalog.py（39次 · P95 480ms · 100%）、verify_design_cases.py（18次 · P95 190ms · 100%）。my-designer脚下需「拦截 19 次 · 逃逸 2 次 [1 IMPL_BUG / 1 SPEC_GAP]」。行99.1%注明汇总，分支98.5%注明单脚本，不合并。

hit百分比是可重叠的调用命中，不能画为和为100的reference饼图；三类意图才是48/34/18的分配。references带宽按组内命中，scripts按组内次数，仅视觉方向有关联，不跨组守恒。remotion节点采用2px灰库存关联闭合带，无流量脉冲。切别的Skill换到本人L0 token及已知脚本；未知意图/refs用「意图分类未记录」「引用明细未记录」，不嫁接my-designer文件。零调用页展示无读取路径，保留P95 0ms并说明未运行，不假造100%成功。

```html
<main class="prism-ribbon-bench topology-glass-ribbon-workbench">
  <section class="content">
    <section class="glass-kpi-crown"><h1></h1><button class="theater-fold-trigger"></button></section>
    <ol class="glass-skill-deck"><li data-skill-row data-skill="my-designer"><button data-skill-trigger><span class="deck-name"></span><span class="deck-frequency"></span><span class="deck-context"></span><span class="deck-scripts"></span><span class="deck-evals"></span></button></li><li data-skill-row data-skill="team-lead"></li><li data-skill-row data-skill="design-studio"></li><li data-skill-row data-skill="m2-dispatcher"></li><li data-skill-row data-skill="linear-board"></li><li data-skill-row data-skill="archive-deck-helper"></li></ol>
    <figure class="wide-alluvial-theater"><div class="theater-scenes"><section class="ribbon-scene" data-bifurcation-panel data-skill="my-designer"><svg></svg><nav class="theater-file-targets"></nav></section></div><figcaption class="theater-branch-strip"></figcaption></figure>
    <footer class="eval-escape-strip"><p></p></footer>
  </section>
</main>
```

Writer把另五个li及五个scene各自静态补齐，上述骨架不授权运行时克隆、不需要第三方脚本资源。只是Stage 1候选，不实现产品、不会发布或执行磁盘脚本。

## 8. Explicit Anti-Patterns & Verification Targets

浮光禁S1–S12及S1/S2/S3/S4/S5/S6/S7/S8/S9/S10/S11/S12旧编号上屏；禁stroke-width > 24、innerHTML replacement、remove与replaceChildren、.caustic-veil、.ruler、Active-Matte、<select>测试switch、sandbox disclaimers。拒绝玻璃数据行、冠部大总分、hero/fold-panel/secondary直子类和另开效果debug栏。

后续测WebKit1280x800两个appearance与reduce-motion：初始宽剧场七个文件全可读，四metric六行齐全；每Skill切换保持removedElements = 0、同一scene node identity。连续hover与点击切换详情正确，非选中scene禁止focus，所有target>=28px，文件名不numeric truncation。玻璃失效fallback不能遮住标题；冷带静态、Eval两个归因都出现。这些是Writer/Reviewer待验要求而不是本稿宣称已过的像素结果。
