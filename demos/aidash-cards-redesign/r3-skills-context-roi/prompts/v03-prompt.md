# v03 · 纸沿观测舱 (topology-alcove-ribbon-console)

## 1. Visual Metaphor & Archetype Lock

收敛为一个纸沿观测舱：顶唇是状态夹，左侧柔软流带与右侧五步回溯并列，底袋只有两个诊断方向。VS-005 + CL-006 + CP-002 + IP-001/IP-003；X坐标=选流与选站，Y坐标=manifold/stepper分栏再进入双tab口袋，Z坐标=纸唇2、实体台面0、抽纸3。Things 3 的朴素间距和 SWWallet 的凹口是已命中vault依据；Alcove只借用 brief 的纸唇意象，Alcove/CleanShot X/Sankey未获vault条目，不据此宣称实现能力。macOS desktop 单卡，R2分岔和全链路回溯仅提取核心，不保留粗管与动态生成。

## 2. Single P0 Focus & Initial Showcase State

把“越界全量深读 15%”独立旗带设为唯一P0，activeBranch=violation，selectedStage=2（S7）。顶唇展示小号50,000 tok、96.8%缓存、S5 暂无统计，不参与抢焦点。底袋默认tab=friction/open=true，上抽48px，显示18返工、6重试和3/5逃逸；这是全局摩擦摘要，不声称由越界造成。切换L0/L1正常支只换定义，S7旗仍独立；双tab分别“摩擦诊断 S8/S9”和“提案转化 S10”。

## 3. P1 / P2 Progressive Folding & Permanent DOM Contract

P1保留五步列表和顶唇，P2被双tab口袋接纳，统计口径以已有口袋内抽页容纳。首载即永久拥有全部SVG <path> ribbons、所有5 trace stage nodes、S1..S12 metric readouts与每个pocket drawer；标签和完整正文也必须预先存在。通过class、dataset和CSS custom properties管理选中/展开/平移，禁止innerHTML、outerHTML、replaceChildren、insertAdjacentHTML和卸载重建。两tab panel只切transform/opacity，非当前面inert且aria-hidden，不能用display:none打断抽取。hover由临时preview字段控制，click/Enter/Space才提交，stepper以aria-current=step表达，Esc关闭抽页并回到当前tab。隐藏指标并非删除数据。

## 4. Measured Layout & 1280x800 Viewport Geometry

1280x800内 main x88/y76/1104x648，padding28，content1048x592。外空白30.1375%=308,608px²，满足>=22%；上下左右余量76/76/88/88。纵向dock64+gap16+split320+gap16+pocket176=592。split用692px图域、24px沟、332px stepper；5行56px加4×10px=320。图的SVG viewBox="0 0 692 280"，下40px留分母注；口袋全开正文146px加30px tab，不改变176px总高度。任何peek也只能进入预留16px沟，0px unintended scroll overflow。32x32px代理标签保障8px/3.2px窄带可选，控制绝不小于28x28px；正文13px且CJK换行，数值不截断。

dual-tab下的全表是分页口径夹：32px分组签，余144px固定正文。质量面S1-S3、实践面S4/S6、摩擦面S8/S9、披露面S7/S5、提案面S10；context分五slice面与cache/P95面，五片各20px行高。每组面保持mounted，只transform换位与inert互斥；长说明最多两行20px，不能把完整十二项清单叠在176px口袋里。默认全表打开质量面，tab依然承担原摩擦/提案选择。

用T=100px局部单位绘S7：d="M 230,64 C 320,64 382,30 482,30 L 482,85 C 382,85 320,119 230,119 Z"为55px；d="M 230,119 C 320,119 382,148 482,148 L 482,193 C 382,193 320,164 230,164 Z"为45px。独立15px旗 d="M 244,236 C 320,236 408,218 490,218 L 490,233 C 408,233 320,251 244,251 Z"。S11五片厚12/8/16/40/24，总100；cache单独尺100输出96.8与3.2。所有其他带按闭合式 M x0,y0 C x0+36,y0 x1-36,y1 x1,y1 L x1,y1+h C x1-36,y1+h x0+36,y0+h x0,y0+h Z，具体h取各自分母；跨站门禁和返工线只是细导航边，不推导未知数量分配。

## 5. Dual-Theme Surface Polarity & Alluvial / Paper-Pocket Craft

Light指定desk #F3F5F4、paper #FFFFFF、lip #EAF0EC、ink #1D3028、muted #52665B、l0 #356E50、l1 #426B96、flag #95502F、focus #245EB2；Dark逐项为#151E1B、#21302A、#2B3C33、#EEF8F0、#B7CDBD、#A5DDB9、#ADCEEF、#EDB694、#ACD0FF。linearGradient fill沿带从0%/.22到100%/.58，每条有1px #FFFFFF高光（.52/.20），旗用铜色不装红色告警成功漏斗。纸唇中间凹9px，两端收12px圆角，0.5px inner highlight用白.6/.15，投影0 6px 16px #18302512。正文SF Pro13、标签14、P0 32，数字tabular-nums；24×24 currentColor内联icon的线宽1.6px。表面opacity1，内容无glass/blur/位移折射；仅功能popover可有玻璃且Safari及Reduce Transparency用同色不透明替代。正文对比>=4.5:1，大字>=3:1，不靠低透明度文字做层级。

## 6. Apple Native Spring Physics & Flow Animation

舱底纸页用440ms cubic-bezier(0.22, 1.35, 0.36, 1)从+48px进入0，tab hover peek translateY(-6px)可叠加；tab选择不让dock随之跳动。旗带激活时沿中心曲线播放1.5px dashed pulse，dasharray2 18、dashoffset0→-80/2200ms，其他支只留细rim。鼠标和键盘focus同亮支，结束hover回原选取。prefers-reduced-motion: reduce 禁连续dash流动、overshoot和peek位移，保留80ms opacity与实色选中态；快速tab连点续接当前位移，不能销毁或复制纸页。

## 7. Production Data Inventory & Exact DOM Topology

stepper的五步为全链路回溯：Stage1 S11 上下文构成（50,000 tok / 96.8%缓存）→ Stage2 S7 渐进披露分流（L0 55% / L1 45% / 越界15%）→ Stage3 S1/S2/S3 触发与门禁（命中2/8、拦截8/40、误报4/40、审计9/12）→ Stage4 S8/S9 返工与逃逸摩擦（返工18次、重试6次、逃逸3+5）→ Stage5 S10 提案转化与健康度（my-designer0.4、code-review1.2、team-lead1.8 proposals/100 runs）。Stage3旁口径明确S1 Pin Drift 2/8 behind，短标“命中”不等于健康成功。该链接是operational/data lineage，不能以观察相关性讲因果美元收益。

manifold的S11页完整五片：System / AGENTS=6,000 tok (12%)；Skills=4,000 tok (8%)；Tool schemas=8,000 tok (16%)；Tool results=20,000 tok (40%)；Conversation=12,000 tok (24%)，总50,000 tok=100%。Cache读数单独命中96.8%=96,800/100,000 eligible requests，未命中重算3.2%=3,200/100,000。S7分别L0 索引浅读55%、L1 局部深读45%和越界全量深读15%独立重叠旗，不能编绝对次数。双tab常驻内容存S8 20会话内18次编辑/返工、6次重试，各自计数；S9 [IMPL_BUG]3、[SPEC_GAP]5；S10三注册技能报告读数及查看建议/收藏/稍后/撤销本地动作。提案tab内统计抽页提供S1落后2/8、S2拦截8/40=20%及独立误报4/40=10%、S3审计9/12与48 eval cases/本周+6、S4 my-designer40次加载与R1 review证据入口、S6同技能12脚本执行和触达8/40=20%、S5 暂无统计、S12 Search P95 18,400 tok/120次/7天。脚本12不是触达12，S4/S6摘要“40次加载 · 12脚本 · 触达8/40”不得改口径。

```html
<main class="aidash-card topology-alcove-ribbon-console">
  <section class="content">
    <section class="alcove-kpi-lip"></section>
    <div class="manifold-and-stepper">
      <figure class="bezier-manifold"><svg viewBox="0 0 692 280"><defs></defs><g class="alcove-context-bands"></g><g class="alcove-disclosure-bands"></g><g class="alcove-cache-bands"></g><g class="alcove-independent-flag"></g></svg><figcaption class="alcove-branch-keys"></figcaption></figure>
      <ol class="trace-stepper-list"><li data-stage="1"></li><li data-stage="2"></li><li data-stage="3"></li><li data-stage="4"></li><li data-stage="5"></li></ol>
    </div>
    <article class="dual-tab-pocket"><div role="tablist" class="diagnostic-tabs"></div><section class="friction-tab-panel"></section><section class="proposal-tab-panel"><div class="coverage-insert"><dl class="alcove-all-metrics"></dl></div></section></article>
  </section>
</main>
```

初始源码展开每个g的闭合path、每个li的按钮和全量panel读数，以上是父子架构而不是运行时空槽。禁止用hero、fold-panel或secondary替代content直接孩子。

## 8. Explicit Anti-Patterns & Verification Targets

反例一律拦下：stroke-width > 24管（132/74/58），55+45+15归一化，cache96.8%作为第六片，宣称因果美元收益，.caustic-veil/.ruler/Active-Matte、<select>测试开关、沙盒免责词、innerHTML换节点。纸唇不能膨胀成另一个导航页面，动作不能触达真实scheduler、Linear或私有遥测。

验证4状态并各取Light/Dark：①越界旗/S7/摩擦tab抽出首态；②hover L0后Enter选择55%，独立旗和分母未丢；③选择第三站打开统计抽页、再第四站核对逃逸归因；④第五站提案tab收藏、稍后、撤销，再Esc回tab。检查节点身份常驻、鼠标/键盘等价、0px溢出、两tab互斥可聚焦、数字完整、reduced-motion静止。写完成回执前运行全部可用R3 prompts的非标题段落<=20%重叠门禁。
