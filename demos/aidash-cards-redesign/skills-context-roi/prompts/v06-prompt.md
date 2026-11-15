# v06 · 双页航路存折 (topology-passbook-route-folio)

## 1. Visual Metaphor & Archetype Lock

借Apple Wallet票夹与Swiss passbook的双页摊开感，左叶登记六Skill、右叶展开一个Skill的读取路线，书脊只是轻阴影而不是拖拽装饰。desktop方向：component、chart-dataviz、layout-navigation、motion-interaction；VS-002 × CL-002 cool-brass remix；X=左叶点行 / Y=右叶路由明细 / Z=实心双页和附着的冷门票。AppTheme候选RoutePassbookFolio，保持不同于矩阵或玻璃工作台的整本纸张拓扑。

New York20px书名，SF Pro13px名称，12px指标与文件，11px页注；数字tabular，中文PingFang。24×24 inline SVG绘一本开页与三向箭，1.5px currentColor。页码装饰不出现抽象指标代码，标题直说「Skills 读取与执行」。

## 2. Single P0 Focus & Initial Showcase State

首翻页固定my-designer，右叶完整铺出三段Prompt→SKILL.md→L1/Scripts，默认pin为interaction-layering.md。唯一P0是选中Skill的阅读去向，不是六Skill总调用大数。左叶六个指标行全部露出；右下票签单独强调remotion-video.md的0命中而不是新告警中心。

## 3. P1 / P2 Progressive Folding & Permanent DOM Contract

左叶四组读数P1常驻；右叶六个folio-route-page在一个网格格位叠放，P2选中才可读和可focus。右下zero-hit-voucher随Skill更新，只有my-designer有给定的冷门reference，其他Skill显示「引用明细未记录」，不能永远拿同一冷文件指责所有Skill。重复选中左行合拢路线，页标题保持，重新点再展开。

所有pages与voucher文本、paths及按钮在initial DOM存在，removedElements = 0、零innerHTML rebuild。左button的五列为纯文本子项，右分支button独立；以class/dataset、Text.data和aria属性驱动，未选页inert/aria-hidden。hover给临时阅读圈，pointerleave回pin；点击/键盘确认留下branch，Escape收右页并回左行。选另行时右页淡退而非真实翻转180°，避免文字镜像及焦点错位；最新请求覆盖未完成动效。

## 4. Measured Layout & 1280x800 Viewport Geometry

1280x800内main x32/y24宽1216高752，padding24后content1168×704。title48 + gap16 + spread640。spread列520/632、gap16；左skills-left-leaf跨640px，右routes-right-leaf572px，zero-hit-voucher在其下56px，gap12。三个是spread的直接孩子，不能把票签挪出成第四张大卡。

左叶padding12后496px：五列112/92/100/106/70，四gap4=16合496；head32、六行94、上下12及余20页脚共640。窄Eval列11px自然换行，case/pass/catch/escape最多六行13px=78，行94足够，不改数字。右页内608×548，Prompt列100、hub108、出口标签284，两段58各一；出口七个48px高，y60..396，detail在y420..528共108px。例带 d="M 266,236 C 286,236 306,82 324,82 L 324,94 C 306,94 286,250 266,250 Z"；M C L C Z全闭合、渐变fill，stroke-width <= 24（实际0.7）。出口使用48px高HTML label，路径配28px辅助靶，所有可操作区域 >= 28x28px，最长文件名不溢右页。

## 5. Dual-Theme Surface Polarity & Alluvial / Paper-Pocket Craft

RoutePassbookFolio light canvas#F1F3F0、左页#FFFCF4、右页#F6F9F1、ink#29352D、secondary#5C6C60、accent#3E684A；dark #151D19/#28322A/#202D25/#F4F7EA/#B9C9B7/#B5D3A6。中缝左右各4px的柔阴影，页边radius16，内票签radius8，与同心圆角数学相协调。票签有1px纸口高光而无夸张斜切。

本双页不透玻璃：optical blur0、displacement0、IOR不使用，backdrop-filter为none。曲带green→teal读references、green→indigo读scripts，冷文件灰库存关系、无pulse；色只是组别，数字仍是证据。正文4.5:1、focus3:1；dark左页不保持奶白，reduce-transparency保持实心折页。外层主题切换仅CSS变量，不重建folio。

## 6. Apple Native Spring Physics & Flow Animation

展开右页使用490ms cubic-bezier(0.22, 1.35, 0.36, 1)，page translateX(6px)归零、内容opacity180ms；收起同高度过渡，右票签跟随selectedSkill无跳动。点击branch只让其渐变fill增亮，不扩大轮廓。沿有效C中心的1px柔珠2300ms单向游走，reference与script各错开120ms；冷文件连接从头至尾静止。

prefers-reduced-motion立即换页、停微光、不横移，方向使用静态arrow；Tab仍按左行到右分支再票签，Escape回选中左行。按钮focus-visible2px，无⌘快捷键覆盖浏览器。48px端口可以鼠标与键盘选择，触发器aria-controls指向本人永久page id。

## 7. Production Data Inventory & Exact DOM Topology

存折的账目来自r4/domain.md，不把call、token、milliseconds混成一个ROI评分。存折中的L0是SKILL.md Token、L1是references/*.md平均连带Token、Cache指KV Cache命中率，会话是活跃会话数。四项加右页路线第五项必须都可达到；Eval列具体标识eval-cases.json：

| 存折 Skill | 周月调用/会话 | Token/Cache账 | scripts效率账 | eval-cases.json结果 |
|---|---|---|---|---|
| my-designer | 7d 42 次 · 30d 156 次 · 28 会话 | L0 1.8k tok · L1 +3.4k tok · Cache 96.8% | design_evidence.py 46次 · 均值 140ms · P95 310ms · 成功率 99.1% | 24 用例 (+4 本周) · 100% 通过 · 拦截 19 / 逃逸 2 |
| team-lead | 7d 68 次 · 30d 240 次 · 41 会话 | L0 2.1k tok · L1 +2.8k tok · Cache 97.4% | goal-queue.py 64次 · ci-monitor.py 38次 · 均值 — · P95 420ms · 成功率 99.5% | 32 用例 (+6 本周) · 100% 通过 · 拦截 27 / 逃逸 1 |
| design-studio | 7d 19 次 · 30d 74 次 · 16 会话 | L0 1.5k tok · L1 +2.2k tok · Cache 95.9% | design_catalog.py 39次 · 均值 — · P95 480ms · 成功率 100% | 18 用例 (+2 本周) · 100% 通过 · 拦截 11 / 逃逸 0 |
| m2-dispatcher | 7d 51 次 · 30d 188 次 · 35 会话 | L0 1.6k tok · L1 +1.9k tok · Cache 97.1% | herdr-dispatch.sh 52次 · 均值 — · P95 260ms · 成功率 99.2% | 20 用例 (+3 本周) · 100% 通过 · 拦截 15 / 逃逸 1 |
| linear-board | 7d 33 次 · 30d 112 次 · 22 会话 | L0 1.4k tok · L1 +1.5k tok · Cache 96.5% | linear-bot-bridge.py 44次 · 均值 — · P95 350ms · 成功率 98.8% | 16 用例 (+2 本周) · 100% 通过 · 拦截 9 / 逃逸 0 |
| archive-deck-helper | 7d 0 次 · 30d 0 次 · 0 会话 · 30d 零调用 · 建议归档 | L0 2.6k tok · L1 +4.8k tok · Cache 0.0% | render_legacy.py 0次 · 均值 — · P95 0ms · 成功率 — | 4 用例 (+0 本周) · 75% 通过 · 拦截 0 / 逃逸 3 |

右页my-designer必须写出UI 探索画廊48%、实现后截图回溯34%、规范审计18%到SKILL.md (L0 入口 · 1.8k tok)，再分reference上组navigation-evidence-contract.md（62% · 2.4k tok）、interaction-layering.md（28% · 1.6k tok）、appearance-ledger.md（19% · 1.4k tok）、remotion-video.md（0 命中 · 冷门冗余告警 · 3.1k tok）；script下组design_evidence.py（46次 · P95 310ms · 98.5%）、design_catalog.py（39次 · P95 480ms · 100%）、verify_design_cases.py（18次 · P95 190ms · 100%）。页尾详情保留「拦截 19 次 · 逃逸 2 次 [1 IMPL_BUG / 1 SPEC_GAP]」。行99.1%是汇总，分支98.5%是该脚本，旁边文字说明范围。

reference命中相互重叠，62+28+19不能强制归一；scripts按次数，不按同样的hit比例分配。零reference用2px灰库存关联，不计为读取量。其余Skill页只有真实已给L0与脚本，Prompt/refs分别显示「意图分类未记录」「引用明细未记录」，缺失avg不补假数；archive页P95 0ms注明未运行，0会话无路线光。冷reference的批准库存不是filesystem ownership核实，本页不触发外部文件操作或真实归档。

```html
<main class="route-passbook-folio topology-passbook-route-folio">
  <section class="content">
    <header class="folio-title-band"><h1></h1><p></p></header>
    <div class="passbook-spread-grid">
      <div class="skills-left-leaf"><header class="folio-ledger-head"></header><ol class="folio-skill-lines"><li data-skill-row data-skill="my-designer"><button data-skill-trigger></button></li><li data-skill-row data-skill="team-lead"></li><li data-skill-row data-skill="design-studio"></li><li data-skill-row data-skill="m2-dispatcher"></li><li data-skill-row data-skill="linear-board"></li><li data-skill-row data-skill="archive-deck-helper"></li></ol></div>
      <figure class="routes-right-leaf"><figcaption></figcaption><div class="folio-page-stack"><section class="folio-route-page" data-bifurcation-panel data-skill="my-designer"><svg></svg><nav class="folio-ports"></nav></section></div><dl class="folio-detail-register"></dl></figure>
      <aside class="zero-hit-voucher"><p></p></aside>
    </div>
  </section>
</main>
```

每个li补齐本人五列button，folio-page-stack一次补五个独立id的page；HTML只是parent树约定，不能把空骨架作为完成实现。Designer止于候选handoff，无生产或部署行为。

## 8. Explicit Anti-Patterns & Verification Targets

存折不得显示S1–S12或S1、S2、S3、S4、S5、S6、S7、S8、S9、S10、S11、S12旧指标代码。禁stroke-width > 24、.caustic-veil、.ruler、Active-Matte、<select>测试选项、sandbox disclaimers、innerHTML replacement、remove/replaceChildren及hero/fold-panel/secondary直子类。左叶不可因窄而只展示top3 Skill或藏住零调用行。

交给Writer后验WebKit1280x800两主题及reduced-motion；六行数完整、右叶七个文件全名无省略、票签只针对有证据的Skill。逐行开合、七分支hover/click与keyboard检同一DOM identity及removedElements = 0，所有28px靶区与focus不被书脊裁切。归因、成功率范围、0命中脉冲禁令逐项通过后再交Reviewer；此稿没有浏览器像素PASS声明。
