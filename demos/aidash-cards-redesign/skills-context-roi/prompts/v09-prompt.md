# v09 · 画报凭单分岔桥 (topology-editorial-voucher-bridge)

## 1. Visual Metaphor & Archetype Lock

一张温暖但精确的editorial ledger，上部是六Skill实数表，下部横跨一条低矮三阶段alluvial bridge，桥尾两张小凭单分别读reference与script/Eval。参考Readwise纸感与Wallet凭单，不借杂志风做大标题遮住数字。desktop四维component/chart-dataviz/typography-copy/motion-interaction；VS-008 × CL-002 editorial remix；X=选账行 / Y=底桥加两个detail voucher / Z=实心纸与浅口袋。AppTheme候选EditorialRouteVouchers。

标题New York20px，Skill13px，metric/file12px，凭单副字11px。24×24 inline SVG以1.4px画桥形分岔、纸签，semantic currentColor，中文系统字体。不同于accordion，这里只有共享底桥，不在每行下方开屉。

## 2. Single P0 Focus & Initial Showcase State

初始my-designer选中，桥已打开，三个Prompt与L0及七个终点全可见；默认design_evidence.py作为pin。P0是该Skill可追踪的读取/执行路线；左凭单仍给navigation-evidence-contract.md摘要，右凭单pin为脚本读数并显示两次逃逸归因。凭单不是完整reference名单的第二份副本，只显示当前分支摘要及必要Eval上下文。

## 3. P1 / P2 Progressive Folding & Permanent DOM Contract

P1上表四指标完整；P2桥内六个bridge-sheet及双凭单六组note。换行同时更新桥和两张voucher的所属Skill，重复点所选行折桥、voucher也收但保留节点；再开恢复pin与上次同组预览。hover reference临时高亮左凭单，hover script高亮右凭单；click/键盘确认锁定对应分支，离开回pin，无需弹出新窗口。

用initial HTML永久写好六行、六sheet和notes，removedElements = 0、零innerHTML rebuild；只改变Text.data、dataset与aria。未选sheet和note inert/aria-hidden，点击若导致当前focus变隐藏先回选中row button。Escape统一闭桥和凭单。快速切换状态由selection revision仲裁，过时transitionend不能将新桥关闭。不能通过移动table row改变选择或虚构排序字段。

## 4. Measured Layout & 1280x800 Viewport Geometry

1280x800内main x32/y24、1216×752、padding24后content1168×704；head40+gap8+ledger364+gap8+bridge208+gap8+vouchers68 =704。ledger表头28和六行56，column内宽1136：160/192/220/264/252，四gap12总1136；表头与button一致grid。三行14px指标及7px上下内边距，数字一律tabular且不ellipsis。

bridge图区1136×208，七出口各28px，y6..202；不另加会吃高度的caption，group headings并入出口标签。Prompt x0..176、hub x324..466、终点x708..1136，两段C弧各至少148px；例 d="M 466,90 C 548,90 626,126 708,126 L 708,138 C 626,138 548,104 466,104 Z"，fill闭合M C L C Z、gradient、stroke-width <= 24（实际0.6）。端口文字以12px HTML两行13px，长文件在hyphen断行，必要时值与名称分配同28px的两行，不缩小SVG。双凭单576×68、gap16，padding8，每张标题13px/值11px自然折到3行。行/端口/凭单分支键及路径辅助靶全部 >= 28x28px。

## 5. Dual-Theme Surface Polarity & Alluvial / Paper-Pocket Craft

EditorialRouteVouchers light #F7F1E9底、#FFFCF6账纸、#EEE7DC桥底、#322B29正文、#71625A副字、#8F4B38焦点；dark#211B1C/#342B2A/#292222/#FFF4E9/#D1BFB3/#EEB6A1。两凭单口袋层背纸y3，top rim0.5px#FFFFFFAA，shadow0 3px 8px #3B281812，表无cell边框。左reference用terracotta→brass、右script用terracotta→slateblue，但状态不彩虹。

本案Liquid Glass参数blur0、displacement0、refraction0，bridge和voucher全固体；dark纸不漂白，reduced-transparency继续同样信息。零reference关系灰褐、无pulse，告警小字+浅黄底，不用骷髅emoji。text4.5:1、focus3:1，饱和色只用在选中路径约10%面积。内页不拥有gallery theme/STAR/viewport按钮。

## 6. Apple Native Spring Physics & Flow Animation

桥与凭单一起用480ms cubic-bezier(0.22, 1.35, 0.36, 1)从井里上提4px，height按208与68固定壳收展；文字opacity150ms，不做大幅纸飞入。换Skill只替换可见sheet的class，不将整张表抬升。C中心pulse2100ms由左向右运动，到reference/script终点消隐，冷节点库存连接完全静止。

prefers-reduced-motion时开合1ms、取消上提和pulse，选色与静态箭头仍展示方向。branch focus-visible2px，Enter/Space锁定并聚焦对应凭单说明，Escape再返回row。hover只换凭单内容和同带高亮，不变表里的真实读数，也不把笔触动画当实时遥测。

## 7. Production Data Inventory & Exact DOM Topology

画报账六行忠实保留四领域指标，桥提供第五项路线证据；账头L0是SKILL.md Token、L1为references/*.md平均连带Token、Cache为KV Cache命中率，周月旁的会话指活跃会话数。评测确切来自eval-cases.json，不能改成宣传性的健康百分比：

| 画报账 Skill | 7d/30d与活跃 | Token与Cache账 | scripts次数和效率 | eval-cases.json账证 |
|---|---|---|---|---|
| my-designer | 7d 42 次 · 30d 156 次 · 28 会话 | L0 1.8k tok · L1 +3.4k tok · Cache 96.8% | design_evidence.py 46次 · 均值 140ms · P95 310ms · 成功率 99.1% | 24 用例 (+4 本周) · 100% 通过 · 拦截 19 / 逃逸 2 |
| team-lead | 7d 68 次 · 30d 240 次 · 41 会话 | L0 2.1k tok · L1 +2.8k tok · Cache 97.4% | goal-queue.py 64次 · ci-monitor.py 38次 · 均值 — · P95 420ms · 成功率 99.5% | 32 用例 (+6 本周) · 100% 通过 · 拦截 27 / 逃逸 1 |
| design-studio | 7d 19 次 · 30d 74 次 · 16 会话 | L0 1.5k tok · L1 +2.2k tok · Cache 95.9% | design_catalog.py 39次 · 均值 — · P95 480ms · 成功率 100% | 18 用例 (+2 本周) · 100% 通过 · 拦截 11 / 逃逸 0 |
| m2-dispatcher | 7d 51 次 · 30d 188 次 · 35 会话 | L0 1.6k tok · L1 +1.9k tok · Cache 97.1% | herdr-dispatch.sh 52次 · 均值 — · P95 260ms · 成功率 99.2% | 20 用例 (+3 本周) · 100% 通过 · 拦截 15 / 逃逸 1 |
| linear-board | 7d 33 次 · 30d 112 次 · 22 会话 | L0 1.4k tok · L1 +1.5k tok · Cache 96.5% | linear-bot-bridge.py 44次 · 均值 — · P95 350ms · 成功率 98.8% | 16 用例 (+2 本周) · 100% 通过 · 拦截 9 / 逃逸 0 |
| archive-deck-helper | 7d 0 次 · 30d 0 次 · 0 会话 · 30d 零调用 · 建议归档 | L0 2.6k tok · L1 +4.8k tok · Cache 0.0% | render_legacy.py 0次 · 均值 — · P95 0ms · 成功率 — | 4 用例 (+0 本周) · 75% 通过 · 拦截 0 / 逃逸 3 |

my-designer桥左为UI 探索画廊48%、实现后截图回溯34%、规范审计18%；中为SKILL.md (L0 入口 · 1.8k tok)；右reference为navigation-evidence-contract.md（62% · 2.4k tok）、interaction-layering.md（28% · 1.6k tok）、appearance-ledger.md（19% · 1.4k tok）、remotion-video.md（0 命中 · 冷门冗余告警 · 3.1k tok）。script三带为design_evidence.py（46次 · P95 310ms · 98.5%）、design_catalog.py（39次 · P95 480ms · 100%）、verify_design_cases.py（18次 · P95 190ms · 100%）。右凭单写全「拦截 19 次 · 逃逸 2 次 [1 IMPL_BUG / 1 SPEC_GAP]」，99.1%注明Skill汇总，98.5%注明具体脚本，不用一个值覆盖另一个。

hit可多reference并读，62/28/19非互斥，不归一化；script按调用次数另作带宽组，avg/P95是明细不用来做Token守恒。cold reference2px灰关系仅代表库存，不表示非零调用。别的Skill没有已给意图/refs，用本人L0/script和「意图分类未记录」「引用明细未记录」代替猜想；mean —保持缺口，逃逸类型未给也不臆分。archive保持P95 0ms库存并注明未运行、无读取流。没有真实外部链接或归档实施动作。

```html
<main class="editorial-route-vouchers topology-editorial-voucher-bridge">
  <section class="content">
    <header class="editorial-roi-head"><h1></h1><p></p></header>
    <section class="six-skill-ledger"><header class="voucher-ledger-columns"></header><ol class="voucher-ledger-lines"><li data-skill-row data-skill="my-designer"><button data-skill-trigger></button></li><li data-skill-row data-skill="team-lead"></li><li data-skill-row data-skill="design-studio"></li><li data-skill-row data-skill="m2-dispatcher"></li><li data-skill-row data-skill="linear-board"></li><li data-skill-row data-skill="archive-deck-helper"></li></ol></section>
    <figure class="alluvial-bridge-stage"><div class="editorial-bridge-sheets"><section data-bifurcation-panel data-skill="my-designer"><svg></svg><nav class="bridge-file-ends"></nav></section></div></figure>
    <div class="dual-voucher-pockets"><article class="reference-detail-voucher"><h2></h2><dl></dl></article><article class="script-eval-detail-voucher"><h2></h2><dl></dl></article></div>
  </section>
</main>
```

Writer补齐每li五列button、另五bridge-sheet与两voucher本人note；双凭单不延伸第三个卡片。本文件是Stage 1候选handoff，不执行浏览器实现、不发布、不修改产品或shared styles。

## 8. Explicit Anti-Patterns & Verification Targets

画报禁止visible S1–S12及S1、S2、S3、S4、S5、S6、S7、S8、S9、S10、S11、S12；禁stroke-width > 24、innerHTML replacement、remove/replaceChildren、.caustic-veil、.ruler、Active-Matte、<select>测试switch、sandbox disclaimers与hero/fold-panel/secondary直子类。不能用64px数字海报挤掉六行真实metrics，也不能把voucher重复名单造成四组套盒。

Writer须用WebKit1280x800 light/dark验六行表、208px桥全部七端口与两个68px凭单；文字零numeric truncation、自然CJK换行，控件至少28px。六Skill开合、七支流hover/click/keyboard保持removedElements = 0、同一sheet identity、正确凭单scope；冷文件不发pulse、两个逃逸归因完整、unknown不嫁接他Skill。此处只定义待验目标，不给伪像素PASS。
