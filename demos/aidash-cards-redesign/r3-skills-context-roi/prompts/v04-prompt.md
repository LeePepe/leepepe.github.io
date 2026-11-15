# v04 · 流带钱包阶梯 (topology-sankey-wallet-cascade)

## 1. Visual Metaphor & Archetype Lock

这是 R2 披露分岔门的精工进化，不是重着色：一条五列流向图压在三张错阶钱包纸页上，路径以真实面片替代132px管线。选 VS-007 精密遥测与 CL-008 靛蓝/海军纸面，CP-002 钱包、IP-001 联动；X=同图内分岔定位，Y=多列图到错阶袋，Z=流场0/三纸页1、2、3/前袋沿4。参考 Linear/Flighty 的精密标签、SWWallet 的堆叠与 Owner A-v09袋口，不把VS-007常规无弹跳偏好置于R3明确Spring要求之上。Vault可证CP-002与VS-002/VS-005；Sankey、Alcove、CleanShot X暂无匹配，具体流带由本提示几何规定。desktop单卡范围，不落生产代码。

## 2. Single P0 Focus & Initial Showcase State

初始 L0 55% 是最高亮带：branch=l0、stage=2/S7，walletFront=disclosure/open=true。三卡呈阶梯，披露页上抽64px，摩擦/提案标签各露32px，其余内容潜入同一袋体。五列顶部题签只标次序与短名，舞台不是五个平权大KPI。点缓存命中选Stage1，点第三列选门禁纸内面，点第五列翻到已挂载的提案纸；这不改变观察数据本身。hover支流提前照亮相应题签但退出hover不更改当前前卡。

## 3. P1 / P2 Progressive Folding & Permanent DOM Contract

P1用crown的五个stage按钮与小分母注，P2把全部门禁、返工、提案和诊断收在wallet三张article内。所有SVG <path> ribbons、全5个trace stage nodes、全部S1..S12 metric readouts及每个pocket drawer从initial load起永久挂在DOM。交互仅改CSS类/变量/transform、dataset、aria与已有textContent，不准innerHTML/outerHTML/replaceChildren/insertAdjacentHTML、不准先清空再重绘。三卡沿Z轴交接，inactive正文inert/aria-hidden，但外露卡签可聚焦；任何瞬间只有一张正文接受输入。Esc把前卡归袋并返回其标签，Tab/Enter/Space和click选流同效。固定一个selection owner，不能各列独立抢状态。

## 4. Measured Layout & 1280x800 Viewport Geometry

1280x800预算：main=(88,76)1104x648，padding28，内1048x592；外部留白30.1375%，即308,608px²，>=22%。四行crown48、canvas284、wallet196、pill28，加三个12px沟=592。crown5×200px+4×12px=1048；SVG viewBox="0 0 1048 284"，五列锚点x=32/248/464/680/896，标签保留32px条带。wallet三纸共用1000x196槽，offsetY=0/24/48，抽取只在槽内变换，脚注pill不浮动。数字13px以上且no ellipsis，文本允许两行，所有展开态0px unintended scroll overflow；目标至少28x28px、默认32px，细带以外置32x32px标签代理命中。

钱包全表按纸面分组阅读：32px口径签与140px正文共172px，余24px留凹口与peek。dl内常驻质量S1-S3、实践S4/S6、摩擦S8/S9、披露S7/S5、提案S10以及context五片/cache/P95分面，任何时刻只一面可交互。五片用五行20px，其余每项最多两行20px、每面至多三项；切分组是现有指标导航，非生成表行或额外页面。

S7起点x248，T=100px：上带 d="M 248,74 C 320,74 374,38 464,38 L 464,93 C 374,93 320,129 248,129 Z"；下带 d="M 248,129 C 320,129 374,160 464,160 L 464,205 C 374,205 320,174 248,174 Z"。独立越界在y240以15px旗尺呈现，不作为第三守恒支。S11五片100px尺=12/8/16/40/24px，cache另一100px尺=96.8/3.2px，各自放在左列上下隔开的局部坐标区；必要时用平移而不非等比缩放厚度。全体branch都闭合填充 M x0,y0 C x0+64,y0 x1-64,y1 x1,y1 L x1,y1+h C x1-64,y1+h x0+64,y0+h x0,y0+h Z。Gates→S8→S10仅1.5px中性连接符，禁止以这些不同分母画假流量延续，五列仍连成诊断链。

## 5. Dual-Theme Surface Polarity & Alluvial / Paper-Pocket Craft

Light固定desk #F8FAFC、card #FFFFFF、wallet #EDF0F7、ink #202B40、muted #536078、l0 #4D5AB0、l1 #2B7395、flag #995C30、focus #315CBD；Dark对应#0E131F、#1C2536、#2A3448、#F1F5FC、#BAC7DC、#B8BEFF、#9AD7ED、#EFC094、#B8D0FF。闭合带用linearGradient 0% opacity.22→100%.58，同支色贯穿，不用粗stroke模拟面积；1px rim为白.55/.18。前袋中央凹12px，16px口沿，圆角20px内折14px，0.5px白色内亮边；纸卡投影0 5px 15px #14203C12，靠亮度阶而非厚黑阴影区分Z。字体SF Pro13/16/22，读数tabular numerals；24x24 currentColor图标1.75px。实体内容opacity1/blur0/refraction0，主题和窗口框只在外chooser；若功能tooltip玻璃化，Safari/Reduce Transparency必须提供不透明card回退及>=4.5:1正文对比。

## 6. Apple Native Spring Physics & Flow Animation

钱包交接用500ms cubic-bezier(0.22, 1.35, 0.36, 1)，hover卡签 peek translateY(-6px)，open和peek组合成一个transform。流场活跃branch中心线放2px微光粒子，用animateMotion沿对应cubic centerline 2600ms循环，非活跃列只细亮边；motion不能把比率本体变粗。题签focus与hover使同一closed path亮起，点击后前纸抬升；快速点击应从当前几何续接，不重排节点。prefers-reduced-motion: reduce 停粒子、取消弹性与peek，100ms opacity映射选择，仍可键盘抽卡与Esc回收。

## 7. Production Data Inventory & Exact DOM Topology

crown五站顺序：Stage1 S11上下文构成（50,000 tok / 96.8%缓存）→Stage2 S7渐进披露分流（L0 55% / L1 45% / 越界15%）→Stage3 S1/S2/S3触发与门禁（命中2/8、拦截8/40、误报4/40、审计9/12）→Stage4 S8/S9返工与逃逸摩擦（返工18次/重试6次/逃逸3+5）→Stage5 S10提案转化与健康度（my-designer0.4、code-review1.2、team-lead1.8 proposals/100 runs）。可见总标题“全链路回溯”，语义是operational/data lineage。第三站定义解释命中2/8指S1 Pin Drift落后2/8，不把其包装成触发成功。

披露钱包装S11 50,000 tok=100%五片：System / AGENTS 6,000 tok(12%)、Skills 4,000 tok(8%)、Tool schemas 8,000 tok(16%)、Tool results 20,000 tok(40%)、Conversation 12,000 tok(24%)。Cache命中96.8%（96,800/100,000 eligible requests）、未命中重算3.2%（3,200/100,000），独立于tokens总额；S7 L0索引浅读55%、L1局部深读45%，另有独立重叠越界全量深读15%且不编样本数。摩擦卡保存S8 20会话/18次编辑返工/6次重试与S9 [IMPL_BUG]3/[SPEC_GAP]5。门禁内面S1 2/8 behind、S2 8/40=20%拦截/4/40=10%独立误报、S3 9/12审计/48 eval cases/本周+6、S4 my-designer40次加载及R1证据入口、S6 12脚本执行/触达8/40=20%，脚本次数不代表触达。提案卡含S10三注册skill报告读数和查看建议、收藏、稍后、撤销，仅本地操作。S5 暂无统计与S12 Search P95 18,400 tok·120次/7天在pill入口的已有诊断内面，full S1..S12 readouts常驻；S10不计算货币节省也不解释成因果得分。

```html
<main class="aidash-card topology-sankey-wallet-cascade">
  <section class="content">
    <div class="sankey-crown-bar"><nav class="crown-five-stages"></nav></div>
    <figure class="cubic-sankey-canvas"><svg viewBox="0 0 1048 284"><defs></defs><g class="cascade-context"></g><g class="cascade-cache"></g><g class="cascade-disclosure"></g><g class="cascade-overlap-flag"></g><g class="cascade-lineage-links"></g><g class="cascade-particles"></g></svg><figcaption class="cascade-hit-labels"></figcaption></figure>
    <section class="wallet-pocket-stack"><article class="cascade-context-sheet"></article><article class="cascade-friction-sheet"><div class="cascade-gates-face"></div></article><article class="cascade-proposal-sheet"><dl class="cascade-diagnostics"></dl></article></section>
    <aside class="s5-s12-pill-rail"></aside>
  </section>
</main>
```

outline里的nav展开5按钮、article带常驻标签/正文/动作、g展开closed cubic paths；不能运行时填空。content直接孩子不得使用hero、fold-panel或secondary。

## 8. Explicit Anti-Patterns & Verification Targets

本进化尤其拒绝R2 stroke-width132/74/58及任何>24粗管；55+45+15=100、96.8%cache第六片、因果美元收益都是数据失败。.caustic-veil、.ruler、Active-Matte、<select>测试开关、沙盒免责copy、innerHTML换卡也不接受。不能重用同脚本做十个换皮方案，不能触达真实CloudKit/Linear/遥测。

四个交互证据态×双主题：1首次L0/S7/披露前卡；2键盘选cache-hit到第一站，缓存分母独立且前纸换面；3点第三站门禁再第四站摩擦，8/40与4/40分离、18/6不求和；4第五站建议收藏→稍后→撤销→Esc袋回收。按1280x800检查对象identity、五站同节点、零滚动溢出、三阶标签均可达、数值无省略、Reduce Motion停粒子。所有R3 prompt段落重叠<=20%是写完成标记的前置。
