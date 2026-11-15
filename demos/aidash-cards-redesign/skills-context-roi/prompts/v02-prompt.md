# v02 · 双栏分岔总账 (topology-split-ledger-bifurcation)

## 1. Visual Metaphor & Archetype Lock

把Swiss账簿的对齐秩序与Linear inspector并置：左页管六条Skill的证据，右页管被选中Skill的阅读路线。不是两个任务列表，也不是左右各一张总分仪表。desktop；component、chart-dataviz、layout-navigation、motion-interaction四维；VS-007 × CL-008，X=左栏行选择 / Y=固定右栏inspect / Z=实心双页。候选AppTheme=SwissForkLedger，继承AIDash靛蓝种子但不宣布Owner已选。

主标题20px，行名13px，读数12px，SF Mono文件名11px，中文使用系统字体。24×24 SVG分叉标与折页箭头1.25px，只有功能图标使用currentColor；不在四个metric列头写编号暗号。

## 2. Single P0 Focus & Initial Showcase State

my-designer在左账第一行选中，右stage从一开始完整展示三类Prompt、L0、四个reference和三个script。单P0为「这次上下文读到了哪里」，标题的小提示「选择 Skill，右侧查看读取与执行去向」。初始锁定design_evidence.py分支，明细带呈现46次/P95 310ms/98.5%。其他五行可立即选取，僵尸行不被滤掉。

## 3. P1 / P2 Progressive Folding & Permanent DOM Contract

左栏P1是四metric紧凑账目，右栏P2六份route-sheet重叠占同一stage网格单元。它们各自从首HTML存在，未选者opacity0、inert、aria-hidden；切换只动画translateX(8px)→0及opacity，不先卸载旧图。点选同一行令右图折至摘要但左六行留住；再点恢复上次分支。状态以selectedSkill、routeOpen、pinnedBranch三个字段管理。

removedElements = 0与零innerHTML rebuild是硬条件。button[data-skill-trigger]及figure内所有出口按钮预置；明细用已有Text.data更新，任何计数变化不建立新span。右侧入口/标签是可聚焦HTML，SVG视觉路径aria-hidden不导致双份读屏。hover展示previewBranch，mouseleave退回pinnedBranch；click、Enter或Space固定选择，Escape只取消预览再收右图，焦点回选中行。不可见图在过渡完成前持续禁止Tab进入，快速换行以最新状态覆盖旧timeout。

## 4. Measured Layout & 1280x800 Viewport Geometry

1280x800内外壳x24/y24宽1232高752、padding24；content1184×704。summary-strip40 + gap12 + split-stage616 + gap12 + cold-alert24 =704。split用grid-template-columns:640px 528px、gap16。左表padding12后616px，列136/114/118/132/100，gap4×4=16，总616；表头28、六行94、上下12，总616。窄列允许脚本在连字符/下划线处自然换行，多行读数不能只在tooltip里。

右栏内部504×592，route图区高492，详细条84，间距16。图区Prompt列88、L0列86、终点列260、两段间隔35各一，合计504。七个出口56px高，前四上组、后三下组，y48起按56px排列；长文件两行13px，值另行13px，target仍56px。枢纽置y228..286，入口三个分布y164/228/292。例带 d="M 209,238 C 226,238 226,64 244,64 L 244,76 C 226,76 226,252 209,252 Z"；stroke-width <= 24，实际0.5px，fill用horizontal linearGradient。右栏窄但曲率真实，禁止为大弧线挤掉文件全名。支流视觉中心两侧另设28px透明按钮靶，>= 28x28px。

## 5. Dual-Theme Surface Polarity & Alluvial / Paper-Pocket Craft

SwissForkLedger light为#F8FAFC底、#FFFFFF左页、#F1F4FA右井、#182336文字、#526177副字、#4755B6选中；dark用#0E131F/#1C2434/#151D2B/#F2F5FC/#B6C1D5/#ABB3FF。只有中缝投影0 2px 10px #101D3A0A，四列没有边框小格。表选中以左侧3px墨条及淡底表达，不用霓虹填满整行。

本案全实心，Liquid Glass optical设blur0、refraction0、displacement0；右stage曲带是渐变墨，不是backdrop-filter。冷门参考的库存支线灰色且无运动，「0 命中 · 冷门冗余告警」在底lip持续可见。切dark时两页都改变语义色，不把浅纸留成刺眼白。减少透明度时图的选中带加实色边，文字4.5:1、交互边3:1。

## 6. Apple Native Spring Physics & Flow Animation

右图换页480ms cubic-bezier(0.22, 1.35, 0.36, 1)，纸页横移8px、opacity分离180ms；右stage高度不动。点击已选行收图同样480ms，将内部routeOpen的grid从1fr降0fr，标题和选择不跳。每条有效C带中心用SVG animateMotion小珠2100ms游走，错峰90ms，不给0命中轨珠。高亮响应90ms，明细84px壳固定不抖动。

prefers-reduced-motion降低为即时页切、停pulse、取消横移，边缘箭头继续示路。左行按钮撑满94px高度、右出口至少28px；键盘从账到图的Tab顺序按输入、L0、references、scripts、详情，不用方向键偷偷切主题。focus-visible2px靛蓝线。

## 7. Production Data Inventory & Exact DOM Topology

总账右stage是第五项指标，左四项不作排名加权。左表L0为SKILL.md Token，L1为references/*.md平均连带Token，Cache就是KV Cache命中率；28会话等指活跃会话数。下表是每行的固定生产读数；没有给出的avg展示「均值 —」，不是估算：

| 左页名称 | ① 频次/会话证据 | ② L0/L1与Cache | ③ scripts/*.py 执行读数 | ④ eval-cases.json 用例与拦逃 |
|---|---|---|---|---|
| my-designer | 7d 42 次 · 30d 156 次 · 28 会话 | L0 1.8k tok · L1 +3.4k tok · Cache 96.8% | design_evidence.py 46次 · 均值 140ms · P95 310ms · 成功率 99.1% | 24 用例 (+4 本周) · 100% 通过 · 拦截 19 / 逃逸 2 |
| team-lead | 7d 68 次 · 30d 240 次 · 41 会话 | L0 2.1k tok · L1 +2.8k tok · Cache 97.4% | goal-queue.py 64次 · ci-monitor.py 38次 · 均值 — · P95 420ms · 成功率 99.5% | 32 用例 (+6 本周) · 100% 通过 · 拦截 27 / 逃逸 1 |
| design-studio | 7d 19 次 · 30d 74 次 · 16 会话 | L0 1.5k tok · L1 +2.2k tok · Cache 95.9% | design_catalog.py 39次 · 均值 — · P95 480ms · 成功率 100% | 18 用例 (+2 本周) · 100% 通过 · 拦截 11 / 逃逸 0 |
| m2-dispatcher | 7d 51 次 · 30d 188 次 · 35 会话 | L0 1.6k tok · L1 +1.9k tok · Cache 97.1% | herdr-dispatch.sh 52次 · 均值 — · P95 260ms · 成功率 99.2% | 20 用例 (+3 本周) · 100% 通过 · 拦截 15 / 逃逸 1 |
| linear-board | 7d 33 次 · 30d 112 次 · 22 会话 | L0 1.4k tok · L1 +1.5k tok · Cache 96.5% | linear-bot-bridge.py 44次 · 均值 — · P95 350ms · 成功率 98.8% | 16 用例 (+2 本周) · 100% 通过 · 拦截 9 / 逃逸 0 |
| archive-deck-helper | 7d 0 次 · 30d 0 次 · 0 会话 · 30d 零调用 · 建议归档 | L0 2.6k tok · L1 +4.8k tok · Cache 0.0% | render_legacy.py 0次 · 均值 — · P95 0ms · 成功率 — | 4 用例 (+0 本周) · 75% 通过 · 拦截 0 / 逃逸 3 |

右账my-designer的三类意图为UI 探索画廊48%、实现后截图回溯34%、规范审计18%；中心严格为SKILL.md (L0 入口 · 1.8k tok)。四reference出口：navigation-evidence-contract.md：62% · 2.4k tok；interaction-layering.md：28% · 1.6k tok；appearance-ledger.md：19% · 1.4k tok；remotion-video.md：0 命中 · 冷门冗余告警 · 3.1k tok。下三个script出口：design_evidence.py：46次 · P95 310ms · 98.5%；design_catalog.py：39次 · P95 480ms · 100%；verify_design_cases.py：18次 · P95 190ms · 100%。明细中完整列「拦截 19 次 · 逃逸 2 次 [1 IMPL_BUG / 1 SPEC_GAP]」。把行的99.1%标成「Skill脚本汇总成功率」，分支98.5%标为「此脚本成功率」，口径不可偷换。

references百分比按Skill调用命中而非排他分流，可以合计超过100；scripts按calls计，带宽分别在自己的组映射，绝不按token和ms混算。remotion为灰色2px库存关联，不代表非零读取。其余五图只显示本人L0已知token、本人已知脚本及缺失态「意图分类未记录」「引用明细未记录」，路线比例不借用第一行。archive图禁脉冲，P95 0ms旁说明「未运行」。approved inventory不等于实际磁盘文件存在证明，不能在此读取或执行脚本。

```html
<main class="swiss-fork-ledger topology-split-ledger-bifurcation">
  <section class="content">
    <nav class="ledger-summary-strip"><h1></h1><span></span></nav>
    <div class="split-ledger-stage">
      <section class="skill-table-column"><header class="ledger-col-head"></header><ol class="ledger-records"><li data-skill-row data-skill="my-designer"><button data-skill-trigger></button></li><li data-skill-row data-skill="team-lead"></li><li data-skill-row data-skill="design-studio"></li><li data-skill-row data-skill="m2-dispatcher"></li><li data-skill-row data-skill="linear-board"></li><li data-skill-row data-skill="archive-deck-helper"></li></ol></section>
      <figure class="bezier-bifurcation-column"><figcaption></figcaption><div class="ledger-route-sheets"><section class="ledger-route-sheet" data-bifurcation-panel data-skill="my-designer"><svg></svg><nav class="ledger-endpoint-buttons"></nav></section></div><dl class="ledger-file-strip"></dl></figure>
    </div>
    <aside class="cold-ref-alert-lip"><span></span></aside>
  </section>
</main>
```

所有li内部写齐五列button，ledger-route-sheets静态补其余五份panel，不克隆数据或改变以上parent树。Stage 1交接仅此候选，无发布、无连接Linear、无额外页面。

## 8. Explicit Anti-Patterns & Verification Targets

双账不能露S1–S12旧代码（S1、S2、S3、S4、S5、S6、S7、S8、S9、S10、S11、S12）；拒绝stroke-width > 24、.caustic-veil、.ruler、Active-Matte调试条、<select>测试切换、sandbox disclaimers、innerHTML replacement和物理卸载。禁止hero/fold-panel/secondary直子类以及在右栏再复制六行左表。

Writer应验证十次快速左右换行仍只激活一张图，右详情与所选Skill一致，六行四项均可读；WebKit1280x800 light/dark截图展示完整文件名及分组。MutationObserver必须removedElements = 0、隐藏页无焦点；脚本和reference按钮 hover/click/keyboard 都更新明细。0命中没有流量动画，99.1与98.5两个作用域同时保留。这是待执行验收，不声称当前已渲染。
