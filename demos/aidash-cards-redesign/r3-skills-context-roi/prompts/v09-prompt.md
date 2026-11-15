# v09 · 瑞士流向凭证册 (topology-swiss-flow-voucher)

## 1. Visual Metaphor & Archetype Lock

让一条横跨版心的流带桥上承来源、下承三只证据纸袋，采用瑞士编辑式留白而非数据瓷砖。VS-002 + CL-002，IP-001图表联动、IP-003原位凭条、CP-002纸袋钱包；X为桥带选取，Y为三类voucher的单面抽取，Z为桥0/袋背1/抽页2/凹口3。参考SWWallet的纸页层次、Things 3的有序标注、R2 B-v04/v06和A-v09 Owner锚点。Vault的SWWallet/Things可证；Alcove、CleanShot X、Sankey暂无条目，不伪造原生组件来源。desktop单卡设计，家族一致但版式不克隆。

## 2. Single P0 Focus & Initial Showcase State

P0只给L0索引浅读55%的桥尾读数32px；branch=l0、selectedStage=2/S7、activeVoucher=context-disclosure/open=true。左voucher已抽出56px，另两只仅显示36px标签“门禁与返工”“ROI提案与S1-S12全表”。五stage题签在bridge上以小号导航保持顺序，右袋不是永久展开的大表。选支改变定义并聚焦相应站，选voucher切已存在正文；第五站激活右袋提案读数，不把55%当作下游转化率。

## 3. P1 / P2 Progressive Folding & Permanent DOM Contract

三voucher属于同一P2 evidence family，P1是桥上的stage rail与分母注。所有SVG <path> ribbons、5 trace stage nodes、全S1..S12 metric readouts和所有pocket drawers从初始load永久存在。袋面打开用CSS class/variable/transform/opacity、dataset和aria，不允许innerHTML/outerHTML/replaceChildren/insertAdjacentHTML或卸载重建；叶子textContent可单点改变。折页正文inert/aria-hidden，标签可聚焦且aria-expanded准确，stage aria-current。hover仅preview并可mouseleave恢复；Enter/Space/click提交选择，Esc收当前voucher回原标签，禁止透明正文捕获点击。

## 4. Measured Layout & 1280x800 Viewport Geometry

固定1280x800内窗，main x88/y76/1104x648、padding28，content1048x592；main外空白308,608px²即30.1375%，>=22%。四行title48、bridge240、vouchers240、footer28，3gap12，总592。voucher三列各336px、两沟20px=1048；正文每袋内padding20、可用296px宽，最长skill名/标签可两行13px，不truncate数量。SVG viewBox="0 0 1048 240"，上40px stage rail、绘图区160px、底40px branch keys，纸袋已预留peek和56px抽取，不遮footer。所有状态0px unintended scroll overflow，默认32px按钮、最低28x28px，3.2%窄支有32x32px代理。

右voucher全表采用六类口径纸面而非十二项一屏：32px分组签、184px正文、24px安全沿。质量S1-S3，实践S4/S6，摩擦S8/S9，披露S7/S5，提案S10，context五片与cache/P95再拆两面；各面已有readouts，五片行高24px，其余每项最多两行20px且一面最多三项。分组切换不复制同一数据或重建节点，inactive面inert，全表入口落质量组，Esc回右袋标签。

bridge的S7 T=80，上带44px d="M 368,90 C 480,90 574,60 706,60 L 706,104 C 574,104 480,134 368,134 Z"，下带36px d="M 368,134 C 480,134 574,140 706,140 L 706,176 C 574,176 480,170 368,170 Z"。独立12px旗=15%×80，放x780附近单独尺度，非第三partition。S11五片T80：9.6/6.4/12.8/32/19.2；cache另80基准77.44/2.56。闭合面公式 M x0,y0 C x0+48,y0 x1-48,y1 x1,y1 L x1,y1+h C x1-48,y1+h x0+48,y0+h x0,y0+h Z 适用于所有分岔；后续Gates/S8/S10仅细1px导航边，不按异分母画虚构守恒宽度，也不猜五slice与55/45的交叉计数。

## 5. Dual-Theme Surface Polarity & Alluvial / Paper-Pocket Craft

Light exact tokens：desk #FAF7F2、paper #FFFFFF、pocket #EFEADF、ink #28312B、muted #616A5D、l0 #365E47、l1 #5E678B、flag #96603B、focus #315BA2。Dark exact tokens：#181C20、#272D31、#343D3B、#F3F6ED、#C0CCBD、#B7D9B8、#C1C7EE、#ECC29D、#BDD3FF。ribbon linearGradient两stop为0% opacity.22、100% .58，closed fill边用1px白specular .5/.18。凹口10px，纸袋角18px，袋沿0.5px inner-white亮边，影0 5px 14px #29332B12；版面只一根短细对齐线，不整屏格子。SF Pro13/16/22，P0 32，tabular-nums贯穿数量；inline24x24 currentColor icon 1.5px，有可读名称。实体surface不透明blur0/refraction0，glass只能给功能popover并提供Safari/Reduce Transparency opaque回退；双主题正文4.5:1/大字3:1。

## 6. Apple Native Spring Physics & Flow Animation

凭页抽取用480ms cubic-bezier(0.22, 1.35, 0.36, 1)，签hover peek translateY(-6px)叠在当前56px抽取偏移上，袋体240px不变。active bridge中心线2px微光粒子animateMotion 2800ms循环，rim本身不加粗，hover/focus用同一高亮状态。快速切袋从目前transform续接并保留原node。prefers-reduced-motion: reduce取消粒子、overshoot、hover偏移，90ms opacity选中凭证，不损失标注/分母/键盘恢复。视觉运动不能暗示观察链是同一请求逐站成功。

## 7. Production Data Inventory & Exact DOM Topology

bridge上全链路回溯五题签次序严格：Stage1 S11上下文构成(50,000 tok / 96.8%缓存)→Stage2 S7渐进披露分流(L0 55% / L1 45% / 越界15%)→Stage3 S1/S2/S3触发与门禁(命中2/8、拦截8/40、误报4/40、审计9/12)→Stage4 S8/S9返工与逃逸摩擦(返工18次/重试6次/逃逸3+5)→Stage5 S10提案转化与健康度(my-designer0.4、code-review1.2、team-lead1.8 proposals/100 runs)。命中2/8的S1定义是Pin Drift 2/8 behind；这条是operational/data lineage导航，不证明因果或美元收益。

左凭证完整S11五片：System / AGENTS 6,000 tok(12%)、Skills 4,000 tok(8%)、Tool schemas 8,000 tok(16%)、Tool results 20,000 tok(40%)、Conversation 12,000 tok(24%)，总50,000 tok=100%。另列cache命中96.8%（96,800/100,000 eligible requests）、未命中重算3.2%（3,200/100,000），不能取tokens总额分母；S7 L0索引浅读55%/L1局部深读45%，独立重叠越界全量深读15%且绝对样本量未知。中凭证含S1落后2/8、S2拦截8/40=20%与误报4/40=10%、S3审计9/12/48 eval cases/本周+6、S8 20会话中18次编辑返工与6次重试、S9 [IMPL_BUG]3/[SPEC_GAP]5。右凭证S10报告读数按上述三skill，查看建议/收藏/稍后/撤销只改变本地状态；右全表S4 my-designer40次加载与R1审查证据入口，S6 12次脚本/触达8/40=20%而非12/40，S5 暂无统计，S12 Search P95 18,400 tok/120次/7天，全S1..S12 readouts必须常驻。footer仅口径入口，不再重复大图与相同统计列表，不编货币算法或缺失审查正文。

```html
<main class="aidash-card topology-swiss-flow-voucher">
  <section class="content">
    <header class="editorial-title-row"></header>
    <figure class="bridge-ribbon-svg"><nav class="voucher-five-stage-keys"></nav><svg viewBox="0 0 1048 240"><defs></defs><g class="voucher-context-ribbons"></g><g class="voucher-cache-ribbons"></g><g class="voucher-disclosure-ribbons"></g><g class="voucher-independent-flag"></g><g class="voucher-flow-particles"></g></svg><figcaption class="voucher-branch-labels"></figcaption></figure>
    <div class="three-voucher-pockets"><article class="context-disclosure-voucher"><button class="voucher-tab"></button><div class="voucher-paper-face"></div></article><article class="gates-churn-voucher"><button class="voucher-tab"></button><div class="voucher-paper-face"></div></article><article class="roi-audit-voucher"><button class="voucher-tab"></button><div class="roi-paper-face"></div><dl class="voucher-full-audit-face"></dl></article></div>
    <dl class="s12-s5-footer-grid"></dl>
  </section>
</main>
```

HTML大纲的nav要初始展开5stage按钮、g展开全部closed paths、article含实际读数/动作、dl含完整表，不许运行时渲染空槽。content direct child不得改为hero/fold-panel/secondary。

## 8. Explicit Anti-Patterns & Verification Targets

禁止stroke-width >24粗流管（132/74/58尤其）、55+45+15归一化为100、cache96.8%第六slice以及因果美元收益。.caustic-veil/.ruler/Active-Matte/<select>测试开关/沙盒免责文案/innerHTML换节点都是失败。三voucher不能新增管理工作流，不调用真实Linear、CloudKit、scheduler或私有遥测。

4态×Light/Dark：①L0/S7/左凭证首态；②hover后键盘选L1，45%带与独立15%旗的分母可读；③第三站中凭证门禁、第四站摩擦，误报与18/6、3/5各自不混合；④第五站右提案收藏、稍后、撤销，抽全表再Esc回标签。验证0px溢出、对象identity、全部节点可达、窄支32px命中、无数字截断与Reduce Motion停流；交接前所有可用R3提示<=20%非标题段落重叠。
