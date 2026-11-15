# v04 · 钱夹流向纸签 (topology-sankey-pocket-stack)

## 1. Visual Metaphor & Archetype Lock

把SWWallet的口袋深度变成六张可读Skill袖页与一张上方流向纸签。口袋仅在袖页底角叠6px，不遮住指标；选中袖页上提后，纸签从袋口展开。参考Apple Wallet纸张与Things 3节制动作，不把钱夹画成横向轮播。desktop，component/chart-dataviz/motion-interaction/layout-navigation；VS-002 × CL-002，X=点袖页 / Y=上方纸签 / Z=三层口袋角。主题候选PocketSankeyWallet。

New York22px标题是唯一serif，其余SF Pro13px、SF Mono12px、辅助11px。24×24 inline SVG1.5px绘纸签与分岔，命名文字伴随图标。每袖页标题和四项指标用紧凑2×2读区，不为每数字另造徽章。

## 2. Single P0 Focus & Initial Showcase State

my-designer袖页第一张抬起6px，纸签320px打开，所有六张袖页仍完整可选。P0为「展开my-designer的读取分岔」，首次选中remotion-video.md，冷门库存关联在图上清晰但不被亮脉冲误认为调用。四reference与三script都在纸签，脚下只读「30d 零调用 · 建议归档」不暗示已有归档功能。

## 3. P1 / P2 Progressive Folding & Permanent DOM Contract

P1是六袖页的四metric；P2为上方sankey-slip-well内六个常驻slip。selectSkill让唯一袖页translateY(-6px)、z-index升一层及对应纸签展开；重复点该袖页放回，纸签卷入井口但保留DOM。右/左按钮焦点顺序按六Skill而非z-index，Escape将纸签闭合后回当前袖页。

纸袋正面与背纸只用pseudo-element，不生成额外数据节点。所有图、标签、详情一次挂载，removedElements = 0、零innerHTML rebuild；明细Text.data和aria-pressed更新，不replaceChildren、不remove。冷门hover先看对应文件，点击锁定；其它branch也如此，离开恢复锁定。新袖页切换时旧纸签inert，只有目标活跃；上提不会把按钮移出原84px可点壳，防快速滑鼠失焦。

## 4. Measured Layout & 1280x800 Viewport Geometry

1280x800窗内main x32/y24、1216×752、padding24，content1168×704为header52+gap12+slip320+gap12+sleeves268+gap12+foot28。sleeves是2列×3行，列576px/gap16、行84px/gap8；纸角在每行预留的6px范围，抬起不与上张文本相交。每袖页padding10后556×64，标题高18，指标4列各约134px、gap6，允许四行11px值。必要时将脚本与Eval二列各自然折行，不可缩到10px以下。

流签内部1136×288，Prompt列184、L0枢纽160、出口标签392，留400px给两段C弧；七出口每32px，y20起到244，详情底部y252..280。例如 d="M 456,130 C 558,130 630,36 744,36 L 744,48 C 630,48 558,144 456,144 Z"，stroke-width <= 24，实描边0.8px，梯度fill和C回程闭合。三个输入不能画成直条相加的条形图。label是1:1 HTML覆盖层，文件名12px可断行。出口button32px高、命中带辅助靶28px，满足 >= 28x28px；签井的clip只裁纸边，不裁标签或focus。

## 5. Dual-Theme Surface Polarity & Alluvial / Paper-Pocket Craft

PocketSankeyWallet light canvas#F5F0E8、sleeve#E9E1D6、paper#FFFCF5、ink#322B24、muted#685E54、forest#245F48；dark用#181B19/#29312C/#343C35/#F8F3E8/#C8C0B2/#A4D2B5。纸袋lip取凹弧clip-path、inset 0 1px 0 #FFFFFF88、背纸y4和y8；shadow0 4px 12px #382C1E12。暗色纸不是棕色黑洞，保留三级可辨亮度。

Liquid Glass不启用，blur0、displacement0、refraction0；sleeves和纸签均固体。reference为forest→sage，script为forest→bluegray，只有被选带加薄金高光。冷门关联灰褐2px、无流光。成功/警告用低彩度底+文本，75%通过不染成成功绿。减少透明度不改变信息，正文字4.5:1，状态边界3:1，主题由外层提供。

## 6. Apple Native Spring Physics & Flow Animation

纸签从translateY(10px)到0，袖页上提translateY(-6px)，均520ms cubic-bezier(0.22, 1.35, 0.36, 1)；背纸仅移动2px，不做旋转翻页遮数据。打开后有效C带中心一道1px光珠2200ms来回循环，进入终点淡出而非弹回逆流；cold库存带不启动。分支选择改变opacity与金边160ms，底明细在固定28px高签尾更新。

prefers-reduced-motion停止纸签位移、袖页抬升和pulse，立即改选中底色与静态方向箭头；依旧具收展语义。纸签已闭时停止所有动画，hidden内容inert。hover只用于preview，不在悬停时自动选Skill。focus-visible2px，原生袖页button整84px可按，内部不再嵌button。

## 7. Production Data Inventory & Exact DOM Topology

六袖页严格保持domain库存，四项分别对应调用与僵尸、上下文、脚本效率、Eval；纸签是第五项Prompt→入口→文件脚本证据。纸面L0对应SKILL.md入口Token，L1读为references/*.md平均连带Token，Cache是KV Cache命中率；会话字段注明活跃会话数。钱夹不能用金额/ROI评分替换这些数：

| 袖页 Skill | 活跃调用账 | 载入与Cache | scripts/*.py 工作账 | eval-cases.json 纸签账 |
|---|---|---|---|---|
| my-designer | 7d 42 次 · 30d 156 次 · 28 会话 | L0 1.8k tok · L1 +3.4k tok · Cache 96.8% | design_evidence.py 46次 · 均值 140ms · P95 310ms · 成功率 99.1% | 24 用例 (+4 本周) · 100% 通过 · 拦截 19 / 逃逸 2 |
| team-lead | 7d 68 次 · 30d 240 次 · 41 会话 | L0 2.1k tok · L1 +2.8k tok · Cache 97.4% | goal-queue.py 64次 · ci-monitor.py 38次 · 均值 — · P95 420ms · 成功率 99.5% | 32 用例 (+6 本周) · 100% 通过 · 拦截 27 / 逃逸 1 |
| design-studio | 7d 19 次 · 30d 74 次 · 16 会话 | L0 1.5k tok · L1 +2.2k tok · Cache 95.9% | design_catalog.py 39次 · 均值 — · P95 480ms · 成功率 100% | 18 用例 (+2 本周) · 100% 通过 · 拦截 11 / 逃逸 0 |
| m2-dispatcher | 7d 51 次 · 30d 188 次 · 35 会话 | L0 1.6k tok · L1 +1.9k tok · Cache 97.1% | herdr-dispatch.sh 52次 · 均值 — · P95 260ms · 成功率 99.2% | 20 用例 (+3 本周) · 100% 通过 · 拦截 15 / 逃逸 1 |
| linear-board | 7d 33 次 · 30d 112 次 · 22 会话 | L0 1.4k tok · L1 +1.5k tok · Cache 96.5% | linear-bot-bridge.py 44次 · 均值 — · P95 350ms · 成功率 98.8% | 16 用例 (+2 本周) · 100% 通过 · 拦截 9 / 逃逸 0 |
| archive-deck-helper | 7d 0 次 · 30d 0 次 · 0 会话 · 30d 零调用 · 建议归档 | L0 2.6k tok · L1 +4.8k tok · Cache 0.0% | render_legacy.py 0次 · 均值 — · P95 0ms · 成功率 — | 4 用例 (+0 本周) · 75% 通过 · 拦截 0 / 逃逸 3 |

展开my-designer的完整纸签：左UI 探索画廊48%、实现后截图回溯34%、规范审计18%；中SKILL.md (L0 入口 · 1.8k tok)；右上references/*.md为navigation-evidence-contract.md 62%/2.4k tok，interaction-layering.md 28%/1.6k tok，appearance-ledger.md 19%/1.4k tok，remotion-video.md 0 命中 · 冷门冗余告警/3.1k tok；右下scripts/*.py为design_evidence.py 46次/P95 310ms/98.5%，design_catalog.py 39次/P95 480ms/100%，verify_design_cases.py 18次/P95 190ms/100%。选到Eval关联处可读「拦截 19 次 · 逃逸 2 次 [1 IMPL_BUG / 1 SPEC_GAP]」。行的99.1%与具体design_evidence.py的98.5%分别注明汇总和单脚本，不能扁平混写。

均值140ms只在已批准的my-designer行呈现，其余未给的mean及逃逸分类不编。命中可能同时发生，62/28/19并非三份排他流，reference组按命中映宽，script组按次数映宽；冷节点2px线只代表库存关系、非读取。其他袖页打开属于本人L0及已知脚本的纸签，未知左意图与右reference写「意图分类未记录」「引用明细未记录」；零调用纸签明确无路径/P95 0ms未运行，不借上一张图。所有建议只读，不实际操作磁盘。

```html
<main class="pocket-sankey-wallet topology-sankey-pocket-stack">
  <section class="content">
    <div class="wallet-roi-header"><h1></h1><p></p></div>
    <section class="sankey-slip-well"><figure class="wallet-route-slip" data-bifurcation-panel data-skill="my-designer"><svg></svg><nav class="slip-file-ends"></nav><figcaption class="slip-detail-seam"></figcaption></figure></section>
    <div class="wallet-skill-sleeves"><article data-skill-row data-skill="my-designer"><button data-skill-trigger><strong></strong><span class="wallet-metric-quartet"></span></button></article><article data-skill-row data-skill="team-lead"></article><article data-skill-row data-skill="design-studio"></article><aside data-skill-row data-skill="m2-dispatcher"></aside><aside data-skill-row data-skill="linear-board"></aside><aside data-skill-row data-skill="archive-deck-helper"></aside></div>
    <footer class="wallet-zombie-foot"><span></span></footer>
  </section>
</main>
```

后三个aside在视觉与键盘上仍是Skill袖页而非次要无用数据，六个均补全button和四metric；井内补齐五份静态本人route-slip。Stage 1只交候选，不写生产代码，也不移除现有门户。

## 8. Explicit Anti-Patterns & Verification Targets

钱夹禁所有旧S1–S12标签（S1、S2、S3、S4、S5、S6、S7、S8、S9、S10、S11、S12），禁stroke-width > 24、innerHTML replacement、.caustic-veil、.ruler、Active-Matte、<select>test switch、sandbox disclaimers及hero/fold-panel/secondary直子类。不可将SWWallet摊平六张普通列表，也不能把袖页堆到只见名称而读不到四metric。

待Writer在WebKit1280x800双主题拍完整纸签与六袖页：上提仍留>=28px命中壳、纸角不压文字。选择六Skill、收展、hover/click七终点的过程中removedElements = 0且焦点可返回；cold带无pulse、全部长文件与数据不截断。再测减少动效后的可达性和窗口无外溢。Stage 1不宣称这些浏览器测试已经发生。
