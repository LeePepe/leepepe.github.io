# v04 · 异常先行双频指挥架 (topology-exception-cadence-lanes)

## 1. Visual Metaphor, Palette & Anti-Clone Spatial Lock

把定时面板做成航电式指挥架：先看两只已经露出诊断纸的警报抽屉，再看下方快慢两条任务轨。结构的第一原则是「错误比正常更值得先读，但正常任务不消失」，不是把六行列表都涂成红绿渐变。此Prompt只交付一个独立手写候选 scheduled-pulse/v04.html；执行它的Writer专注此文件，不派下级、不重用批量生成HTML/CSS脚本，另外三稿不属于其Owned Path。

坐标身份为web/macOS、VS-007 Avionics command、CL-008 Navy/Alabaster；X为异常就地诊断与三键，Y为exception shelf加双cadence lane，Z为实色舱底、抽出的诊断纸和紧密唇边。候选AppTheme：Light #F7F9FC / Dark #0E131D，台架#E8EEF6 / #152030，抽屉#FFFFFF / #1C2A3C，主字#152238 / #EFF5FF，次字#53667F / #AABAD0，非状态路由色#2C5790。画面比矿纸更冷，比极光更实，比石墨更明确地分两频；禁止全屏霓虹与复古军用绿字。

空间身份证必须是 command-crown-bar、exception-hero-shelf、dual-cadence-lanes、command-restore-dock 四个content直系孩子。上架只有两件，分别特定人失败与数仓慢；下架左fast-minute-lane两件桥接/我的巡检，右daily-batch-lane两件简报/学习。不能在全页面加另一份隐藏六卡列表充门禁，也不能把六份详情送到全局右台或底台。候选CSS使用command-/exception-/cadence-专用语汇，成对class/rule共用目标<15%。

## 2. Single P0 Focus, Semantic Status Colors & Initial Showcase State

唯一P0是「先读退出1的审查，决定是否再跑一次」，失败英雄左侧最先进入视线，Rerun在其右尾可直接点击；数仓右侧慢英雄是P1伴随诊断，不创造第二个强调色主CTA。两只英雄初始半开，露出结论纸而不是预先堆满所有日志；下方四件正常/运行任务保持可扫。P2 hover为一句话产出线索，P3完整五阶段和日志按点击在原卡中抽出。

警告架左件 #F43F5E ✕ 失败 (exit 1)，右件 #F59E0B ▲ 耗时偏高 (14.2s)；快轨桥接 #06B6D4 ● 运行中、巡检 #10B981 ● 成功 (1.8s)；日轨两件同为 #10B981 ● 成功 (1.8s)。暂停用 #64748B ⏸ 已暂停，按钮文字继续。饱和色只在警告唇、状态徽记和窄色带，大片背景不刷纯红/纯橙；状态图符/中文/结果数字一直保留，选中蓝不能掩盖真实异常。

上架直接写「审查进程退出1，未提交新评审」与「入仓9.1s偏高，全轮14.2s完成」，没有证据就不声称权限过期或SQL死锁。左频标题「⚡ 高频分钟级守护 1m–5m」、右频标题「🌅 每日定时批处理 04:00–05:00」是Owner指定文本，不扩充成筛选器或新的产品导航。英雄固定身份不因pause/重跑自动迁到下轨，六任务数量始终唯一。

## 3. Hover Brief Preview ([data-hover-brief]) & Click-to-Pull-Out Drawer ([data-report-panel]) Contract

每件data-job-row内部都有一张[data-hover-brief]短诊断签，放在卡面最后18px预留区域，不和半开的结论纸争同一行。hover或focus-within使前唇及face translateY(-4px)，签从opacity0升至1；文章所在架格不动。六句各有所指：「退出1 · 尚无新评审 → PR #308」「入仓9.1s占主要耗时 → TIA-448」「提交进行中 · 上次产出TIA-448」「检查结论已留档 → PR #311」「晨间三题已投递 → TIA-448」「题单推荐已送达 → TIA-431」。诊断签显示一行，不能在hover时重新造一个报告DOM。

点击body的原生button[data-row-trigger]把对应[data-report-panel]从本卡袋底抽出；动作nav和预览为兄弟节点，不嵌套button。上架初始panel只露74px summary/outputs的半开纸，深处stages/logs已存在但inert；点选后panel展开至216px，能读双栏完整回执。下轨卡初始panel高度0，点击展开216px。同一时间最多一份完整展开；再次点当前卡回初始状态（英雄74px、轨卡0），点新卡把前一件复位再打开新件。

详情始终附着自己的job article，上架或下轨只做必要的垂直伸展，不变更两列身份；不使用遮住其他任务的absolute全屏层。文章增长由content内部受控纵向滚动承接，header/footer保持sticky、其他卡可通过同一内容井继续到达。scrollIntoView仅在报告真的越过下缘时做最近边界对齐，不每次跳到页面顶部；普通hover绝不滚动。

报告露出执行结论摘要、真实关联的TIA-448/TIA-431/PR #311/PR #308胶囊、五条状态计时、语法高亮尾日志。链接地址未给时用本卡初始已挂载的 #command-<job>-<output>来源说明锚点，点击展开说明并聚焦，远程repo/workspace不猜。报告、Text/span、确认条、恢复控件初载全在DOM，removedElements = 0；动作、链接、撤销stopPropagation，不会意外展开或关闭卡。Esc还原当前卡的半开/闭合状态，并把焦点还到发起face。

## 4. Measured 1280x800 Viewport Geometry & Spatial Bounding Boxes

1280×800 CSS px作为内页测量场。水平64..1216宽1152；command-crown-bar初始(64,40,1152,40)，exception-hero-shelf(64,96,1152,234)，dual-cadence-lanes(64,346,1152,394)，command-restore-dock(64,760,1152,28)。上架与下架都两列568px、缝16，2×568+16=1152；上架下缘330，和双轨346之间留16px分区空气，不再插统计横栏。

英雄bbox分别(64,96,568,234)、(648,96,568,234)。内边12，净544；face112、到半开paper的间隙8、半开report74、上下padding24，总218，另16px为装订及底影余量。face内部：标题/状态24，周期18，累计/今日18，动作32，预览18，加2px内部缝总112。三键置于32px带右尾，64/72/58高32、间距8，组宽210；计数不挤到操作带，因此所有字段完整。

每条cadence lane高394，顶部标题32，后留14，两个卡h164且中间16：32+14+164+16+164=390，底留4。卡外框x64或648，y392与572，高164；padding12后净544×140，face112+底部28px抽屉余量。快捷卡同样标题、周期、累计/今日、状态和三键，不把daily任务改为省略次数的小胶囊。hover短签独占18px，满题名与4,280/184在544px里可读。

完整hero高度376：face112+gap8+report216+padding24+底余量16=376。上架被选中则shelf高376、另一英雄仍234顶对齐，双轨整体下移142到y488；内容总下缘882，允许内容井内scroll，并为760位置的sticky恢复栏保留44px底部安全区。轨卡完整高度380：face112+gap8+report216+padding24+底余量20=380，同行lane标题不移动，只有同lane后续卡顺延。初始bbox与展开bbox是两组明确状态，不要求展开后仍把所有细节塞进800px。

report净宽544，列分248/280、中缝16。左列结论最多48px、outputs32、间隙8、终端72、来源说明32，总192；右列五段每行30=150，计时单位与状态说明留32，共182≤216。计时标签允许两行14px，条轨短但数字清楚；未知阶段用文字pending不塞0s。标题20、任务14、正文12、mono日志11四档；button/capsule高度≥28，CJK自然换行、数字不截断、横向无溢出。content用唯一内部纵滚，不在两条lane各放一个窄滚动条。

## 5. Dual-Theme Surface Polarity & Tactile Drawer Lip Craft

航电的抽屉质感靠硬朗但细致的阶面：英雄角半径16，轨卡半径10，顶唇厚3px、装订高光1px；Light报告纸#FFFFFF比架底#E8EEF6高一阶，Dark报告纸#23344A比架底#152030高一阶。异常色带只宽4px并延伸顶口一角，红英雄底 tint最多10%、橙英雄最多9%，正常卡不铺整面绿色。保持「两只预警 / 两条节奏轨」两组主要容器，避免每个summary/log又套一个醒目的border盒。

内高光 inset 0 1px 0 在Light白alpha.85、Dark白alpha.09；接触阴影2px .09/.28、环境影12px .06/.18。装饰拉手是右上32×3px的低亮度短线，与右尾Rerun按钮位置分离；半开paper两侧内缩8px，像从命令架拉出签条，不用矿纸凹弧缺口，也不加玻璃refraction或极光ambient bloom。唇边可用局部linear渐变，但禁止repeating条纹/扫描线。

冷白界面上的红/金状态字改深色同系墨，深蓝界面用可读浅墨，原始 #F43F5E/#F59E0B等留给带与点；字至少4.5:1，控件边界/焦点至少3:1。task级按钮16px本地inline SVG、24viewBox/1.6stroke配全称，only Owner频率标题保留既定emoji，不能再加装饰emoji导航。此稿全部实色，减透明度模式无需换实现；减运动模式只停spring与青灯脉冲，不损失告警层级。

## 6. Apple Native Spring Physics & 3-Button Permanent DOM Micro-Interactions

前唇220ms抬起，完整paper480ms抽出，复位440ms，transform采用 cubic-bezier(0.22, 1.35, 0.36, 1)；包围盒高度用不超调的ease-out，防止警告架过冲推撞sticky恢复栏。半开内容不反复自动弹出。青灯2.5s轻呼吸、红灯静止，window不活跃则停循环；prefers-reduced-motion 下位移和自动滚动动画为0、状态淡入≤70ms。Rerun按压scale(.97)100ms，其余常用键不做夸张bounce。

暂停/继续 [data-action="toggle-pause"] 分离enabled与lastResult：暂停灰徽记但英雄仍固定在exception shelf，最近失败/慢结论留在报告；继续恢复最近结果与「暂停」文案，不按颜色自动重新分类。暂停中单次Rerun允许临时青色反馈，完成后仍paused、报告更新，不能把一次运行偷偷恢复成持续排程。

Rerun [data-action="rerun"] 立即进入 ● 运行中，使用inFlight与generation token，一轮终结才累计及今日各+1。三健康任务分支仍1.8s成功，慢任务仍14.2s警告，失败分支仍exit1；不存在「一键修复根因」的未授权能力。桥接初始正在运行则在途键禁用但保留位置，不能开第二轮。回声仅发生本页状态，不调用本机cron、真实任务、数据库、XPC或Linear/GitHub。终端span固定，更新仅用原有Text.data/nodeValue，禁止设置父Element.textContent，不重建HTML。

删除 [data-action="delete"] 先显示卡内预写的「确定删除此任务？」确认/取消；确认后内容高度平滑归零、article标inert，首屏对象不remove；上架用保留栏位的空位，双lane按原order保留归位信息。预置六个 [data-action="restore"] 在command-restore-dock针对已删job分别可见，可撤销多项；删除期间旧token失效、晚到回调不改计数，撤销按原任务身份返回英雄/快轨/日轨、恢复状态且不发起执行。删后focus移到对应restore，恢复后focus回本卡trigger；确认取消回delete。隐藏report深处与确认键不可Tab，原生按钮Enter/Space可用，动作/link/restore隔离冒泡。全main包括Text node的 removedElements = 0 为硬门禁。

## 7. Production Data Inventory & Exact DOM Topology

本稿依据R5主spec §6、T5、r5/domain；r4/domain §2的周期/累计/今日仅作为声明库存，不承袭其旧列表拓扑或成功秒数。此Stage1无实时数仓读写、私有日志读取、采集或生产Snapshot绑定。aidash-metrics capability probe不接受scheduled_pulse，本稿不把该检查包装成L1–L5 ready；生产绑定前需上游真实来源、窗口/覆盖/新鲜度，缺失显示暂无回执而非捏造0。下述分段/日志是明确交付的候选内容，不是对宿主现况的诊断，UI不渲染测试免责声明或沙盒开关。

上架两只对象的正面固定：target-pr-review「特定人 PR 审查」「每 5m · 4m 前」「累计 312 次 · 今日 12 次」「✕ 失败 (exit 1)」；aidata-pulse「AIData 数仓脉搏 04:00」「每天 04:00 · 下次 11h 后」「累计 186 次 · 今日 1 次」「▲ 耗时偏高 (14.2s)」。两只尾键都是暂停、Rerun、删除，左侧仅一个Rerun被强调，不再复制第二个按钮到diagnosis里。

快频轨的两件为linear-bot-bridge：「Linear @bot 桥接」「每 1m · 刚刚 16:45」「累计 4,280 次 · 今日 184 次」「● 运行中」；my-pr-patrol：「我的 PR 巡检」「每 5m · 2m 前」「累计 860 次 · 今日 36 次」「● 成功 (1.8s)」。日频轨的两件为daily-brief：「每日简报 05:00」「每天 05:00 · 下次 12h 后」「累计 142 次 · 今日 1 次」「● 成功 (1.8s)」；daily-learning：「每日学习推荐 04:15」「每天 04:15 · 下次 11h 后」「累计 98 次 · 今日 1 次」「● 成功 (1.8s)」。每件同样三键，标题时间仍保留，不借分栏删字段。

所有报告均保留五个彩色槽位名 ① 个人源采集、② L2-L3 入仓、③ Retro-ROI、④ 学习寻题、⑤ Brief 投递；非晨间任务附实际步骤名称，明确这是各任务五段映射，不能宣称PR执行了数仓入仓。五段正常色为青/靛/紫/金/绿；失败覆盖红，running青、未执行灰且条宽为空。完成条按本报告最大已完成时长定宽，值用s可读；running/pending不能伪填总耗时或写「0s成功」。

失败英雄完整内容：执行结论「PR #308 审查进程退出1，未提交新评审」，输出胶囊PR #308指向本卡来源，读取.2s、diff.3s、执行.6s失败、提交未执行、通知未执行；日志 `[16:41:00.5] INFO review started` / `[16:41:01.1] ERROR review exit=1`。慢英雄结论「入仓9.1s偏高，全轮仍完成」，TIA-448，五段1.2/9.1/1.8/1.3/.8s；日志 `[04:00:10.3] WARN warehouse=9.1s` / `[04:00:14.2] INFO pulse finished`。警报解释到证据给出的程度，不编造外部故障细节。

快轨深报告：桥接「消息已经路由，当前提交尚在进行」，TIA-448标上次产出，读取.1/去重.1/路由.2s/提交运行中/确认未开始，日志 `[16:45:00.4] INFO submission pending`；我的巡检「PR #311 的检查结果已归档」，PR #311，读取.4/检查.3/对比.4/归档.3/通知.4s，日志 `[16:43:01.8] INFO PR311 checks archived`。桥接不能借既往胶囊表现为当前已成功。

日轨深报告：简报「五阶段完成，三题已送往投递回执」，TIA-448及TIA-431，.3/.5/.4/.3/.3s，日志 `[05:00:01.8] INFO briefing sent TIA-448`；学习「三题去重匹配完成，推荐已投递」，TIA-431，候选.3/去重.2/匹配.5/整理.4/投递.4s，日志 `[04:15:01.8] INFO recommendations sent count=3`。两个总计1.8s与face一致。终端2–4行timestamp灰、INFO青、WARN金、ERROR红，标识亮墨；用固定span，不能把私有消息/凭据塞进真实语气文本。

```text
main.topology-exception-cadence-lanes
└─ section.content (单一内部纵滚，sticky crown/restore)
   ├─ header.command-crown-bar
   ├─ section.exception-hero-shelf
   │  ├─ article.exception-alert-drawer[data-job-row][data-job="target-pr-review"]
   │  └─ article.exception-alert-drawer[data-job-row][data-job="aidata-pulse"]
   ├─ div.dual-cadence-lanes
   │  ├─ section.fast-minute-lane
   │  │  ├─ header.cadence-minute-heading
   │  │  ├─ article.cadence-guardian-drawer[data-job-row][data-job="linear-bot-bridge"]
   │  │  └─ article.cadence-guardian-drawer[data-job-row][data-job="my-pr-patrol"]
   │  └─ section.daily-batch-lane
   │     ├─ header.cadence-dawn-heading
   │     ├─ article.cadence-daily-drawer[data-job-row][data-job="daily-brief"]
   │     └─ article.cadence-daily-drawer[data-job-row][data-job="daily-learning"]
   └─ footer.command-restore-dock (六个预挂载restore入口)

每一件上架/轨卡各自静态包含：
article[data-job-row]
├─ div.command-drawer-face
│  ├─ button.command-body-trigger[data-row-trigger]
│  ├─ nav.command-tail-actions (toggle-pause / rerun / delete，独立原生button)
│  └─ p.command-preview-sign[data-hover-brief]
├─ div.command-delete-question (confirm/cancel，首屏常驻)
└─ section.command-inner-report[data-report-panel]
   ├─ div.command-evidence-column (summary / outputs / logs / 来源说明)
   └─ div.command-duration-column (stages / 计时状态说明)
```

## 8. Explicit Anti-Patterns & Verification Targets

禁止复制普通列表并另加一张红色标题条；异常必须真是两只234px半开的诊断抽屉，下方必须两条不同频率的并列轨。禁止重复六任务的影子列表、弹出全屏Modal、伪造根因或自动重排英雄；Rerun不等于修复。v05..v10、脚本批量套壳、调试select、内页主题/viewport/选择控件、Active/Matte栏、ruler、caustic斑马纹、raw localization keys和沙盒说明一律不出现。

WebKit1280×800两主题初始状态应测出上234/下394区域、四个下轨face可读、红/金结论先露；hover18px短签opacity>0且抬-4px无需点击。点每一件后完整report有summary/正确输出/五段/logs，增长与唯一内部滚动符合上述142px差值，所有其他任务仍可达，sticky恢复条不盖最后一项；半开英雄深处不可键盘闯入，展开后可读。

静态Prompt验收不代表像素完成。后续提供真实Light/Dark、hover、click PNG及bbox记录，确认≥28px目标、Title/4,280/exit1无 …/裁切、CJK不横溢出、对比通过。全main MutationObserver与初始节点引用检查 removedElements = 0；试暂停恢复、paused单跑、重复Rerun、删除在途任务、多项撤销、链接与Esc焦点，计数仅终结一次且按钮不抽卡。最终Visual Traceback、Owner冻结、部署与Safari打开是上游后续责任，本叶子不越权宣称完成它们。
