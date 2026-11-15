# v07 · 六舱精密导流架 (topology-tactile-rack-conduit)

## 1. Visual Metaphor & Archetype Lock

参考Flighty的精密信息分舱和SWWallet浅托盘层次，把六Skill做成2×3可读工作舱。每舱拉手指向下方共同的conduit inspector；不是太空飞船控制面板，不发明运行服务。desktop四维component/chart-dataviz/layout-navigation/motion-interaction；VS-003 × CL-003 slate-cyan；X=舱button / Y=拉出共用导流托盘 / Z=浅凹舱与实心托盘。主题候选PrecisionConduitRack。

标题20px、舱名13px、指标12px、脚本及小注11px，使用SF Pro/PingFang和SF Mono。24×24 SVG用1.5px刻画三孔拉手与分叉，不把状态变为无字灯珠。舱内四metric形成一块读数面，不额外制造四盒套盒。

## 2. Single P0 Focus & Initial Showcase State

初始my-designer舱拉手伸出6px，conduit-inspector-bay完整打开，默认design_catalog.py路径高亮。P0为「my-designer读取和执行走向」，不是最大调用舱。六舱全露四项证据，archive-deck-helper保留在右下、带30d 零调用徽章；filter-bar只给「全部 / 30d 零调用」真实筛选，不加隐藏测试状态。

## 3. P1 / P2 Progressive Folding & Permanent DOM Contract

P1舱内四读区不折叠；P2托盘的六份route-face和右dl明细。点击舱拉出本人托盘，click已选舱退托盘，选另舱只替换活跃route-face。全部/零调用筛选改变CSS可见高度、inert及aria-hidden，不移走任何舱，切回恢复同一对象；默认全部，首次图仍完整。筛选若隐藏所选舱则收托盘，不自动选新舱、不能显示旧图归到新Skill。

所有bay、route-face、静态读数和输出按钮自初HTML常驻：removedElements = 0，零innerHTML rebuild。改变class、dataset、Text.data与aria即可；不以重排DOM实现筛选。hover branch点亮对应路径和明细，click.pin固定，离开恢复pin；Escape退托盘并回bay。动画回调带最新selection校验。原生button容纳舱文本与拉手，分支按钮在托盘独立，不嵌套交互角色。

## 4. Measured Layout & 1280x800 Viewport Geometry

1280x800下main x32/y24、1216×752、padding24；content1168×704为filter40+gap16+rack304+gap16+inspector296+gap12+foot20。rack列576×2/gap16，行96×3/gap8；bay padding12后552×72，名20px，metric横排四个132px区/gap8，读数最多4行12px。长脚本自然在连字符和下划线断，不能让P95或成功率消失。

inspector是figure880 + gap16 + dl240，padding16后实际内部1136需figure880/gap16/dl240正好。figure图区880×264，Prompt x0..128、hub x260..374、右标签x562..880；七个端口32px高从y16至240，文件名12px加值11px可两行。C带例如 d="M 374,110 C 434,110 494,30 562,30 L 562,42 C 494,42 434,124 374,124 Z"，closed fill遵M C L C Z，stroke-width <= 24，实描边0.75。dl240×264内pad12，分支全名允许三行而不是ellipsis。所有bay拉手、筛选键、端口button与路径辅助命中 >= 28x28px，架外无horizontal overflow。

## 5. Dual-Theme Surface Polarity & Alluvial / Paper-Pocket Craft

PrecisionConduitRack light底#EEF3F6、舱#F9FCFE、井#E4EDF2、字#172D3B、副字#506877、cyan#176B85；dark#111C25/#22323F/#172630/#F0F8FC/#AFC5D3/#9AD9EA。凹舱顶缘inset 0 1px 3px #15364B14，托盘前缘1px#FFFFFF66高光，背垫translateY(4px)。拉手只是小垫片，不能是全排粗边框或网格刻度。

Liquid Glass光学不启用：blur0、refraction0、displacement0，架与数据固体。有效refs带blue→cyan，scripts带blue→sage，冷文件连接灰青且静态。状态文字4.5:1，focus边3:1；reduced-transparency同实心舱，data-theme变化只换变量。警告不是泛红整舱，归档为读数建议，不是真实删除命令。

## 6. Apple Native Spring Physics & Flow Animation

托盘296px展收为470ms cubic-bezier(0.22, 1.35, 0.36, 1)，内部route-face向前translateY(-5px)归位，拉手伸6px；切舱只移动选择底片，不拆下整架。C中心1px柔光粒子用2000ms单向运动，脚本端点arrival轻亮90ms，不改变数值。冷门relation无粒子。hover明细100ms高亮，同高dl不随内容推架。

prefers-reduced-motion取消伸拉、粒子与弹性，CSS只静态切选中outline及route显示；滤镜按钮32px高。Tab次序按舱DOM自然顺序、再branch、再明细可读项。focus2px，Escape不清除已点branch记忆；screen reader能听到selected Skill与具体path名。

## 7. Production Data Inventory & Exact DOM Topology

六舱四读数的真实领域分别是7d/30d与会话/僵尸、L0/L1 Token与KV Cache、具体scripts调用和avg/P95/成功率、eval-cases.json用例/周增/通过/拦逃。L0标题解读为SKILL.md Token，L1为references/*.md平均连带Token，Cache是KV Cache命中率，舱内会话数标为活跃会话数。拉出的Prompt→L0→L1/Scripts是第五项，不新增设备状态字段：

| 工作舱 Skill | 频次与活跃证据 | 上下文载入证据 | 脚本性能证据 | eval-cases.json成效 |
|---|---|---|---|---|
| my-designer | 7d 42 次 · 30d 156 次 · 28 会话 | L0 1.8k tok · L1 +3.4k tok · Cache 96.8% | design_evidence.py 46次 · 均值 140ms · P95 310ms · 成功率 99.1% | 24 用例 (+4 本周) · 100% 通过 · 拦截 19 / 逃逸 2 |
| team-lead | 7d 68 次 · 30d 240 次 · 41 会话 | L0 2.1k tok · L1 +2.8k tok · Cache 97.4% | goal-queue.py 64次 · ci-monitor.py 38次 · 均值 — · P95 420ms · 成功率 99.5% | 32 用例 (+6 本周) · 100% 通过 · 拦截 27 / 逃逸 1 |
| design-studio | 7d 19 次 · 30d 74 次 · 16 会话 | L0 1.5k tok · L1 +2.2k tok · Cache 95.9% | design_catalog.py 39次 · 均值 — · P95 480ms · 成功率 100% | 18 用例 (+2 本周) · 100% 通过 · 拦截 11 / 逃逸 0 |
| m2-dispatcher | 7d 51 次 · 30d 188 次 · 35 会话 | L0 1.6k tok · L1 +1.9k tok · Cache 97.1% | herdr-dispatch.sh 52次 · 均值 — · P95 260ms · 成功率 99.2% | 20 用例 (+3 本周) · 100% 通过 · 拦截 15 / 逃逸 1 |
| linear-board | 7d 33 次 · 30d 112 次 · 22 会话 | L0 1.4k tok · L1 +1.5k tok · Cache 96.5% | linear-bot-bridge.py 44次 · 均值 — · P95 350ms · 成功率 98.8% | 16 用例 (+2 本周) · 100% 通过 · 拦截 9 / 逃逸 0 |
| archive-deck-helper | 7d 0 次 · 30d 0 次 · 0 会话 · 30d 零调用 · 建议归档 | L0 2.6k tok · L1 +4.8k tok · Cache 0.0% | render_legacy.py 0次 · 均值 — · P95 0ms · 成功率 — | 4 用例 (+0 本周) · 75% 通过 · 拦截 0 / 逃逸 3 |

my-designer的托盘先出现三个Prompt意图：UI 探索画廊48%、实现后截图回溯34%、规范审计18%，再是SKILL.md (L0 入口 · 1.8k tok)。reference四端口navigation-evidence-contract.md 62%·2.4k tok、interaction-layering.md 28%·1.6k tok、appearance-ledger.md 19%·1.4k tok、remotion-video.md 0 命中 · 冷门冗余告警·3.1k tok。script三端口design_evidence.py 46次·P95 310ms·98.5%、design_catalog.py 39次·P95 480ms·100%、verify_design_cases.py 18次·P95 190ms·100%。dl中全文「拦截 19 次 · 逃逸 2 次 [1 IMPL_BUG / 1 SPEC_GAP]」，明确行级99.1%与单脚本98.5%两个作用域。

refs hit的分母为Skill调用，多个reference可同读，不能归一化成100%分配；scripts的宽度按组内calls另映，不以P95改变带宽。remotion保留2px灰库存线而不假装非零。其他舱托盘只有已知本人L0/script，未知意图/refs显示「意图分类未记录」「引用明细未记录」；avg —与未给的逃逸分类不臆造。零调用舱P95 0ms说明未运行，无实际读取/执行流，不可删掉。此处采用批准的可视库存，不宣称核实磁盘目录。

```html
<main class="precision-conduit-rack topology-tactile-rack-conduit">
  <section class="content">
    <menu class="rack-filter-bar"><li><button data-rack-filter="all">全部</button></li><li><button data-rack-filter="zero">30d 零调用</button></li></menu>
    <div class="six-bay-rack"><article data-skill-row data-skill="my-designer"><button data-skill-trigger><strong></strong><span class="bay-four-readouts"></span><i class="bay-pull-tab"></i></button></article><article data-skill-row data-skill="team-lead"></article><article data-skill-row data-skill="design-studio"></article><article data-skill-row data-skill="m2-dispatcher"></article><article data-skill-row data-skill="linear-board"></article><article data-skill-row data-skill="archive-deck-helper"></article></div>
    <section class="conduit-inspector-bay"><figure class="conduit-route-view"><div class="rack-route-faces"><section data-bifurcation-panel data-skill="my-designer"><svg></svg><nav class="rack-route-ports"></nav></section></div></figure><dl class="conduit-file-spec"></dl></section>
    <footer class="rack-audit-foot"><p></p></footer>
  </section>
</main>
```

补齐其余五article中的button/四读数，以及五份route-face；pull-tab是无交互装饰，按钮本体才触发。Stage 1只写候选，不执行shell脚本、不发布、不修改监控服务。

## 8. Explicit Anti-Patterns & Verification Targets

导流架禁旧S1–S12和S1/S2/S3/S4/S5/S6/S7/S8/S9/S10/S11/S12 visible code，禁stroke-width > 24、.caustic-veil、.ruler、Active-Matte、<select>test switch、sandbox disclaimers、innerHTML replacement及remove/replaceChildren。content不许hero/fold-panel/secondary直子类，也不许设备健康、开机按钮等虚构功能。

后续WebKit1280x800 light/dark验六舱四读数、完整托盘路径与至少28px按钮。交互包括全部/零调用往返、六舱开合、七分支hover/click与keyboard，MutationObserver严格removedElements = 0；筛掉选中时不得误归到另一Skill，unknown不是空白死图。检查avg缺失、75%通过、冷带无pulse、脚本成功率范围及文件无截断。此设计稿不冒充浏览器结果。
