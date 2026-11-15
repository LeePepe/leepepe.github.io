# v01 · 分流纸袋账 (topology-alluvial-pocket-ledger)

## 1. Visual Metaphor & Archetype Lock

把流向看成铺在桌面的半透明账带，纸袋不是另一张仪表盘，而是沿账带找到证据的收纳口。锁定 desktop / macOS 画框，VS-005 纸感留白、CL-006 晴空与鼠尾草、CP-002 立体钱包和 IP-001 图表联动；X＝分岔选取，Y＝横向五站加底部抽取，Z＝实体纸面 0、袋口 2、抽出纸页 3。参考 Things 3 的安静选中态、SWWallet 的前后纸层及 R2 B-v04/B-v06、A-v09，不复用它们的粗管或重建脚本。Vault 命中 CP-002、VS-005、CL-006；Alcove、CleanShot X、Sankey 检索无条目，不冒称已有组件源码。设计维度仅限组件、数据图、折叠与动效，十套仍属于同一 AIDash 家族，不冻结生产 AppTheme。

## 2. Single P0 Focus & Initial Showcase State

唯一 P0 是 L0 索引浅读 55% 的上支账带；初始 activeBranch=l0，selectedStage=2（S7），pocket=evidence-disclosure，open=true。55% 用 32px 数字贴在带尾，其他读数维持 13px，禁止把 50,000 tok 再做并列大数。五站按钮只有 S7 着色。底袋已抽出披露证据纸页 72px，另两页仅露 36px 标签：摩擦、提案。点 L1 将 P0 转为 45%，点越界旗只选独立 15% 读数，不改正常分流合计；五站点击导航到已有对应证据，不过滤出伪造的分支级 ROI。

## 3. P1 / P2 Progressive Folding & Permanent DOM Contract

P1 是五站轨道及各分母的简短说明，P2 收入三页共享纸袋，诊断全表作为提案页的页内口径抽页。初次 HTML 解析就挂载所有 SVG <path> 流带、全部 5 个 trace stage 节点、S1..S12 的完整 metric readouts 和所有 pocket drawers，包括暂不展示的页内诊断。点击只能修改 class、dataset、CSS 变量、aria 状态和已有叶子 textContent；零 innerHTML / outerHTML / replaceChildren / insertAdjacentHTML，也不能 remove、clone 或重新创建交互节点。折入的区域保持对象身份，通过 transform 与 opacity 退出视野，设置 inert 和 aria-hidden，不能让透明按钮留在 Tab 顺序。单一 state 记录 branch/stage/sheet；hover 只是暂亮，mouseleave 恢复选择，Enter/Space 提交，Esc 收页并将焦点交回打开它的按钮。

## 4. Measured Layout & 1280x800 Viewport Geometry

预算以 1280x800 CSS px 内窗计，外 chooser 提供 macOS 窗口和主题。main 位于 (88,76)，1104x648，padding 28，content 1048x592；外部净留白 308,608px²＝30.1375%，超过 >=22%。content 四行 64 / 300 / 172 / 20px，间隔 12px 共 36px；合计 592px。rail 五格各 200px，四个 12px 间隔；袋中三页宽 1000px、固定共用 172px well，只上移不增加高度。图域 1048x300，SVG viewBox="0 0 1048 300"，绘图与标注分区，文字不能压带。

诊断抽页采用常驻分组而非把十二行塞入172px袋井：顶部32px口径签，正文最多108px；质量、实践、披露、上下文各有独立data-face，实践每面至多两项、上下文分五片面与cache/P95面。五片面采用五行20px内联名称/数量，无第二份可见切片条图；其余面每项最多两行20px。各面永久存在，单面可见且其余inert，以页签切换，不生成新DOM。选择全表入口时先呈质量面，Esc回提案纸签。

S7 比例尺 T=100 SVG px：L0 55px，L1 45px。L0 d="M 380,100 C 490,100 550,42 680,42 L 680,97 C 550,97 490,155 380,155 Z"；L1 d="M 380,155 C 490,155 550,164 680,164 L 680,209 C 550,209 490,200 380,200 Z"。越界旗另起带 d="M 400,242 C 480,242 530,226 610,226 L 610,241 C 530,241 480,257 400,257 Z"，15px 仅对独立旗尺 T 映射。左上 S11 五切片厚度 12/8/16/40/24px 共 100；左下 cache 自己的 100px 尺生成 96.8/3.2px。其余闭合支流统一用 M x0,y0 C x0+40,y0 x1-40,y1 x1,y1 L x1,y1+h C x1-40,y1+h x0+40,y0+h x0,y0+h Z；切片边与小缓存未命中不得放大伪造比例。窄带用外置 32x32px 按钮代理命中，所有交互 >=28x28px。袋页动作 32px 高，最大展开和 -6px peek 已纳入 well，任何状态 0px unintended scroll overflow；CJK 可两行、数字与单位不省略，正文 >=13px。

## 5. Dual-Theme Surface Polarity & Alluvial / Paper-Pocket Craft

Light tokens：desk #F5F6F8，surface #FFFFFF，pocket #EDF2EE，ink #182D24，muted #53665B，l0 #2D704C，l1 #426792，flag #956024，focus #245EA8。Dark tokens：desk #141C21，surface #202B31，pocket #2B3935，ink #EFF8F1，muted #B5C8BB，l0 #A2D6B6，l1 #A9C9F2，flag #EAC48F，focus #B7D7FF。每条 <linearGradient> 沿 x 方向使用对应 branch 色，0% stop-opacity=.22、100%=.58；填充闭合 path，rim 为 1px 白色高光（Light .55 / Dark .22），不用线宽画体积。纸袋口中心下凹 10px，嘴沿高度 20px、两端圆角 12px，inset 0 0.5px 0 白色 .6/.16，投影 0 5px 14px #182D2414 / #00000032。全卡 24px 圆角，抽页 16px；SF Pro 13/17/24px 搭配 font-variant-numeric: tabular-nums。图标为 inline 24x24 currentColor 分岔符号、stroke 1.6px，并有文字名称。这里不使用内容玻璃：blur/displacement=0、opacity=1；任何功能 popover 若采用玻璃，必须提供不透明 Safari/Reduce Transparency 回退，文字对比 >=4.5:1，大字 >=3:1。

## 6. Apple Native Spring Physics & Flow Animation

纸页 transform 和 shadow 以 480ms cubic-bezier(0.22, 1.35, 0.36, 1) 抽出或归袋，标签 hover peek translateY(-6px)，在同一变换中叠加 open 偏移而非覆盖。已选带上叠 1.5px 中心虚线脉冲，dasharray 3 21，stroke-dashoffset 0→-96，2400ms linear infinite；它只是光轨，不是带宽编码。hover 提升 fill 强度但不会改变分母、路径厚度或永久选择；focus-visible 同样提供 2px 外圈。快速连点从当前 transform 继续，不能排队动画。prefers-reduced-motion: reduce 下取消流动、overshoot 与 hover 位移，纸页用 100ms opacity 切换，保持全部数据、键盘操作和焦点恢复。

## 7. Production Data Inventory & Exact DOM Topology

轨道按全链路回溯命名且严格依次为 Stage 1: S11 上下文构成 (50,000 tok / 96.8% 缓存) → Stage 2: S7 渐进披露分流 (L0 55% / L1 45% / 越界 15%) → Stage 3: S1/S2/S3 触发与门禁 (命中 2/8 · 拦截 8/40 · 误报 4/40 · 审计 9/12) → Stage 4: S8/S9 返工与逃逸摩擦 (返工 18次 / 重试 6次 / 逃逸 3+5) → Stage 5: S10 提案转化与健康度 (my-designer 0.4 · code-review 1.2 · team-lead 1.8 proposals/100 runs)。Stage 3 的“命中 2/8”保留输入短标，定义抽页说明 S1 Pin Drift 是落后 2/8，不是触发成功率。跨站连线只表示数据与诊断导航，不表示这些不同人群数量守恒。

披露纸页承载 S7 L0 索引浅读 55%、L1 局部深读 45%、越界全量深读 15%（独立重叠标志，无绝对计数）；S11 50,000 tok =100%，System / AGENTS 6,000 tok (12%)、Skills 4,000 tok (8%)、Tool schemas 8,000 tok (16%)、Tool results 20,000 tok (40%)、Conversation 12,000 tok (24%)；缓存命中 96.8%=96,800/100,000 eligible requests，未命中重算 3.2%=3,200/100,000，单独分母。摩擦纸页列 S8 20 个会话、18 次返工/编辑、6 次重试（两计数不相加）；S9 [IMPL_BUG] 3、[SPEC_GAP] 5。提案纸页列 S10 上述三技能报告读数，不定义货币算法，my-designer 建议可查看/收藏/稍后/撤销，动作只改变本地视图状态。页内常驻诊断读数为 S1 2/8 behind；S2 拦截 8/40=20%、独立误报 4/40=10%；S3 审计 9/12、48 eval cases、本周 +6；S4 my-designer 40 次加载并留 R1 审查证据入口、不编造证据正文；S6 同技能 12 次脚本执行、触达 8/40=20%，12 不是触达次数；S5 暂无统计；S12 Search P95 18,400 tok、120 次 / 7 天。S4/S6 的摘要合写为“40次加载 · 12脚本 · 触达 8/40”，每项仍有独立标签。

```html
<main class="aidash-card topology-alluvial-pocket-ledger" data-p0="l0" data-stage="2">
  <section class="content">
    <nav class="lineage-stage-rail" aria-label="全链路回溯"><button data-stage="1"></button><button data-stage="2"></button><button data-stage="3"></button><button data-stage="4"></button><button data-stage="5"></button></nav>
    <figure class="alluvial-ribbon-stage"><svg viewBox="0 0 1048 300"><defs></defs><g class="context-ribbons"></g><g class="cache-ribbons"></g><g class="disclosure-ribbons"></g><g class="violation-flag"></g><g class="flow-pulses"></g></svg><figcaption class="branch-hit-labels"></figcaption></figure>
    <div class="pocket-evidence-well">
      <article class="trace-pocket-sheet" data-sheet="disclosure"><button class="sheet-tab"></button><div class="sheet-readouts"></div></article>
      <article class="trace-pocket-sheet" data-sheet="friction"><button class="sheet-tab"></button><div class="sheet-readouts"></div></article>
      <article class="trace-pocket-sheet" data-sheet="proposals"><button class="sheet-tab"></button><div class="sheet-readouts"></div><div class="diagnostics-slip"><dl class="s1-s12-readouts"></dl></div></article>
    </div>
    <footer class="metric-footnote-bar"></footer>
  </section>
</main>
```

大纲中的 g、readouts、button 不是运行时模板槽：交付 HTML 必须在初始源码展开真实闭合 paths、标签、所有指标及 actions。不得引入 content 直下的 hero、fold-panel、secondary 通用类。

## 8. Explicit Anti-Patterns & Verification Targets

明确拒绝 stroke-width > 24 的粗管（包括 R2 132/74/58）、把 55+45+15 当作 100%、把 96.8% cache 当第六切片、把全链路回溯说成因果美元节省，以及 .caustic-veil、.ruler、Active-Matte、<select> 测试开关和沙盒免责文案。innerHTML 节点替换同样是失败。不能连接真实调度器、私有遥测、CloudKit 或 Linear；不得伪造补救执行、对话或管理新页面。

Stage 2 核验四个真实交互状态 × Light/Dark：① 首载 L0/S7/披露袋开启；② hover 并键盘提交 L1，纸页解释改为 45% 且五站依旧存在；③ 点击第三站并抽出门禁全表，再选第四站看 18/6 和 3/5，记录对象 identity 不变；④ 第五站收藏后稍后再撤销，Esc 归袋并恢复焦点。每态 1280x800 截图检查 0px 溢出、无数值省略、32px 代理窄带命中区、reduce-motion 停流及相同节点集合；设计提示还须接受所有现有 R3 文件的 <=20% 非标题段落重叠检查。
