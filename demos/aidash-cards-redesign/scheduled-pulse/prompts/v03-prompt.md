# v03 · 石墨抽屉轨工作台 (topology-split-drawer-workbench)

## 1. Visual Metaphor, Palette & Anti-Clone Spatial Lock

用 Linear 的精密工作台读任务，不用极光霓虹去烘托状态：左侧是六只浅而紧凑的工具抽屉，右侧是一张始终在原位置的汇报案板。选择只把证据送进案板，绝不把左轨顶开。此稿分配的单文件工作为 scheduled-pulse/v03.html，要求一个 Writer 独立手写它的静态结构、专属CSS和事件状态机；不调用下级、不修改别稿、不从共享生成器吐出四个换色版本。

锁定 web/macOS 的 VS-007 Linear precision、CL-008 的 graphite支系；AppTheme 候选 Light #F4F5F8、Dark #111318，轨井 #E8EBF0 / #151923，卡面 #FFFFFF / #202632，右台 #FCFCFD / #1B202A，正文 #1B2230 / #E9EDF5，次字 #5E697B / #A5B0C3。选择焦点允许低饱和石墨蓝 #647A9C，不能替代任务的红/绿/金/青。X 为轨内高频动作，Y 为42/58 master-detail，Z 为色染正面与独立实色报告台。

不可替换的空间指纹是 split-workbench-frame 下的 left-drawer-rail 与 right-report-stage，六个job只在左，六份常驻报告只在右。卡内不插长卷宗，也不把报告移到下方，不重排异常到英雄区。专属命名采用 workbench-/rail-/stage-，四方案 CSS 类与规则成对重合 <15%；相同data钩子仅代表业务行为，不授权复用另稿布局骨架。

## 2. Single P0 Focus, Semantic Status Colors & Initial Showcase State

P0 是「锁定一项问题，在右台看清哪段耗时偏高」。开场选择第三只 AIData 数仓脉搏 04:00，右侧完整显示14.2s回执和9.1s入仓长条；其他五卡同样留在左轨，标题、周期、累计/今日、状态、尾键均可读。常见操作是P1，悬停速览是P2，深日志是P3；不要再加一份重复状态汇总，工作台只有两个主阅读容器。

左卡状态渐变只是6–10%局部染色，标志本身用规定原色：简报、学习与我的巡检为 #10B981 的 ● 成功 (1.8s)，数仓为 #F59E0B 的 ▲ 耗时偏高 (14.2s)，特定人审查为 #F43F5E 的 ✕ 失败 (exit 1)，Linear @bot 为 #06B6D4 的 ● 运行中。暂停操作时左卡以 #64748B 和 ⏸ 已暂停反馈，右台保留最后结果。状态符号与汉字不能省，只亮一盏灯不合格。

顺序固定 daily-brief、daily-learning、aidata-pulse、linear-bot-bridge、my-pr-patrol、target-pr-review；不因选中或出错跳行。selected 胶边沿用该job状态色，右台顶缘也用同色一点关联，主体仍石墨中性。开场不要故意暂停另一项来凑灰色展示，灰色由可达的暂停操作验收。R5 将三件成功耗时明确锁为1.8s，旧R4学习2.4s、巡检0.9s不是本轮断言。

## 3. Hover Brief Preview ([data-hover-brief]) & Click-to-Pull-Out Drawer ([data-report-panel]) Contract

每个 rail article 的底部预留16px一行 [data-hover-brief]。鼠标进入或键盘focus-within时，卡面 translateY(-4px)，短条由透明滑入；外侧grid槽固定，六卡轨坐标完全不动。局部hover不选择任务、不改右台、不抢焦点，不让卡放大压住上下行。延迟100ms再离开可避免pointer从触发面移到尾键时闪灭。

速览文案为六条独立线索：「五段完成 · 三题投递 TIA-448」「推荐已到达 TIA-431」「9.1s 在入仓段 · 全轮14.2s」「提交仍进行 · 上次单据TIA-448」「PR #311 已完成检查归档」「PR #308：exit 1，评审未提交」。左轨有限宽度，句子用12px，控制在30个CJK等宽单位以内，不能让一行凭空变为三行，也不能用 … 截掉产出号。

button[data-row-trigger] 覆盖左卡正文，不包含同卡 nav 中的三个原生按钮；点击另一任务时右台把旧 [data-report-panel] 退到x=-12px，新报告从x=16px进入，卡轨selection属性更新但box不变。点击当前任务收起右台内容到一个静态案板唇，右侧面积及左轨保持；再次点击还原原报告。所有六份报告从 HTML 初始就常驻 right-report-stage，只切换class、opacity、inert和aria-expanded；不得replaceChildren或移节点到新父级。

右台报告包括执行结论摘要、可点产出胶囊、五阶段瀑布与高亮终端尾。没有核实远程地址的 TIA-448/TIA-431/PR #311/PR #308 使用 #stage-<job>-<output> 的合法页内说明锚点，点击在同报告显示已挂载的来源说明并聚焦，不能捏造 repo/workspace。尾键、链接、确认和 restore 一律隔离选择事件；Esc使右台收起并返回选中左卡。未选中的报告不可参与Tab，但不能被删除。

## 4. Measured 1280x800 Viewport Geometry & Spatial Bounding Boxes

main内层基准1280×800，横界64..1216，共1152px。workbench-top-strip是(64,40,1152,48)，split-workbench-frame是(64,104,1152,640)，workbench-foot-rail是(64,760,1152,28)。frame扣18px沟槽后可分配1134px：左42%=476.28，右58%=657.72。左栏x64..540.28，右栏x558.28..1216；这比简报中约530/548的示意坐标稍宽，精确比例优先，不偷偷做成50/50。

左轨六槽每件476.28×100，缝8，6×100+5×8=640；起始y为104/212/320/428/536/644。所有文章的外包围盒在hover、点选和右台切换前后不动；只有内部 rail-face 做-4px抬升，轨井overflow visible保护焦点与阴影。删除不让后面的槽挤上去，原槽保留100px安静空腔，restore回原处。

卡面padding8px，净宽460.28、高84。纵向标题/状态20、周期16、计数/动作28、预览16，三个小间隔合计4，总84。第一行标题最多270px、状态176px，中隙14.28；长标题完整显示。计数与尾键同行，计数字段宽246.28、间隙18、动作宽196：键64/68/52×28，间隙6×2，总196。累计4,280与今日184可用两行12px/13px，不缩成不可读小字；三动作必须肉眼可达且严格靠右。

右台净宽625.72（padding16），可用高608。标题/结论占88，产出带36，分隔12，五阶段瀑布180，分隔16，终端160，来源说明40与间隙8，合计540≤608。瀑布每行36px，标签区域176、图轨397.72、数值52；数仓9.1s最长条不越轨。终端最长2–4行可换行而不横向出界。标题20px、卡名14px、周期/计数/摘要12px、mono日志11px，四档字级足够。

stage内容放大时在608px内容井内auto纵向滚动且scrollbar-gutter稳定，左轨仍静止。报告不可用 min-width:800 把右台撑爆；CJK summary按自然折行，数字/单位只在原子里nowrap。右台至少28px的胶囊、左键28px的命中高度均须测量，不拿图标16px当hit target。深浅主题完全使用同一几何，不另造暗色窄布局。

## 5. Dual-Theme Surface Polarity & Tactile Drawer Lip Craft

石墨候选的层次来自精密台阶而非朦胧玻璃。Light 使用明亮右台与略低亮度轨井，Dark 使用 #111318 背板、#202632 卡正面、#1B202A 台面，各层能辨但不过度厚重。每张抽屉上方有1px浅高光和2px唇边，左侧不是矿纸6px脊，而是贯穿底角的状态染色梯形与2px指示线。正文的实色背景覆盖染色，确保不被渐变吃掉。

顶唇用 inset 0 1px 0 白 alpha .08（Dark）/.75（Light）；下方接触影1px+4px环境影，选中时略多一层8px但不漂浮成卡片墙。右台以一道顶部光切和左侧18px沟槽区分关系，不给摘要、胶囊、瀑布、终端各套一层border cage。轨内六卡是同一容器记录，不把它们算成六个独立报表section。

正文4.5:1与焦点/图符3:1是最低线。灯线保留 #10B981/#F59E0B/#F43F5E/#06B6D4/#64748B，浅主题小字用各自深墨，暗主题小字用浅墨；不要依赖原色小字在白底的对比。卡上的暂停/rerun/trash采用16px inline SVG、24viewBox/1.5stroke配文字，没有emoji图标字体。这里明确无 backdrop-filter、折射玻璃、矿纸缺口、彩色环境光晕，才能和其他三稿真正分离。

## 6. Apple Native Spring Physics & 3-Button Permanent DOM Micro-Interactions

工作台只对直接操作做 spring：cubic-bezier(0.22, 1.35, 0.36, 1)，左face hover220ms，右报告横向入场440ms/退场420ms，按下scale(.98)90ms。台框、轨井、数值和计时条不bounce；瀑布新数据以420ms单调长度过渡，未知值保持pending。prefers-reduced-motion 时取消横滑与抬卡、只用≤80ms透明度；运行状态青灯从循环呼吸改静灯，视觉信息一字不少。

[data-action="toggle-pause"] 只改变任务排程enabled与按钮文案，记住lastResult。暂停显示灰色 ⏸ 已暂停/继续，恢复显示最近真实结果而非强改成功；右报告可以继续查看旧失败。处于一次Rerun中暂停不取消已经发起的本页流程，完成更新报告后排程仍paused，灰色面反馈不能被新结果覆盖成已启用。

[data-action="rerun"] 点击后只在当前候选文档进入 ● 运行中，inFlight禁止同job重复结算，runToken过滤旧异步回调；结束一次把累计/今日各+1，仅更新原有 Text.data/nodeValue，禁止设置父 Element.textContent。三健康支路1.8s、数仓支路14.2s警告、审查支路exit1失败，不能暗示点击会修复已知异常。实际scheduler、数据库、Linear/GitHub/API、XPC均不连接；正在运行桥接必须先结算或禁用重复Rerun，不同时开两个不明任务。

[data-action="delete"] 提供轨卡内预挂载的确认/取消态，确认才把卡内容收进原100px槽并inert；六个job article、六个report和原Text节点都持续存在。删除当前选择时右台回空案板唇，左轨不选中另一个job；底部六个已存在的 [data-action="restore"] 分别对被删项可见，逐个恢复原顺序和状态。删除使在途token失效、取消计数提交，撤销不重新运行。操作点击stopPropagation，原生按钮键盘等价；焦点删后去restore、撤销回卡正文，隐藏报告/确认层不可Tab进入。连续动作全过程 removedElements = 0，包括span里的文字节点，不能用外观相同的新节点骗门禁。

## 7. Production Data Inventory & Exact DOM Topology

来源纪律：本稿遵循spec §6 + T5 + r5/domain，周期/次数取r4/domain §2声明库存，其视觉列表与旧耗时被R5取代。下面是Stage1的确定内容，不是live数仓实测，不能从tool_calls推导任务耗时、成功率或故障根因。aidash-metrics inspector没有scheduled_pulse参数，capability probe失败闭合；无L1–L5扩展、私有会话读取或生产reader改动。生产阶段必须先获真实来源、采样窗口、覆盖/新鲜度，未知不得补0；当前手稿只让已声明六任务在可操作页面中可读。

| 左轨键 | 显示标题 | 调度行 | 累计/今日 | 首次徽章文本 |
|---|---|---|---|---|
| daily-brief | 每日简报 05:00 | 每天 05:00 · 下次 12h 后 | 142 / 1 次 | ● 成功 (1.8s) |
| daily-learning | 每日学习推荐 04:15 | 每天 04:15 · 下次 11h 后 | 98 / 1 次 | ● 成功 (1.8s) |
| aidata-pulse | AIData 数仓脉搏 04:00 | 每天 04:00 · 下次 11h 后 | 186 / 1 次 | ▲ 耗时偏高 (14.2s) |
| linear-bot-bridge | Linear @bot 桥接 | 每 1m · 刚刚 16:45 | 4,280 / 184 次 | ● 运行中 |
| my-pr-patrol | 我的 PR 巡检 | 每 5m · 2m 前 | 860 / 36 次 | ● 成功 (1.8s) |
| target-pr-review | 特定人 PR 审查 | 每 5m · 4m 前 | 312 / 12 次 | ✕ 失败 (exit 1) |

计数必须在面上写出「累计 <n> 次 · 今日 <m> 次」，不能只写表中压缩的142/1。六件正面尾键同样都是暂停、Rerun、删除，pause后第一键继续。报告每件有五个可视槽位 ① 个人源采集 / ② L2-L3 入仓 / ③ Retro-ROI / ④ 学习寻题 / ⑤ Brief 投递；对非晨间任务紧接其实际子阶段名，别把统一槽位标题误读为PR真的跑了学习与入仓。普通条分别青/靛/紫/金/绿，失败槽红，pending灰无完成宽度，正在执行青，不造未知秒数。

初始数仓报告：结论「L2-L3 入仓9.1s，占据本轮主要等待；全轮14.2s已完成」，胶囊TIA-448，计时1.2、9.1、1.8、1.3、0.8s，轨长以9.1为100%。终端 `[04:00:10.3] WARN warehouse duration=9.1s` 与 `[04:00:14.2] INFO pulse complete`。这是上游声明的延迟线索，不添加SQL锁、磁盘故障或权限失效等未经给出的原因。

晨间简报报告结论「五段均已结束，三题已进入投递回执」，TIA-448/TIA-431，0.3/.5/.4/.3/.3s；日志 `[05:00:01.8] INFO brief delivered`。学习报告结论「三道题完成去重、匹配和送达」，TIA-431，实际候选/去重/匹配/整理/投递.3/.2/.5/.4/.4s；日志 `[04:15:01.8] INFO learning sent count=3`。两个报告总计1.8，数字与左面一致。

桥接报告结论「本轮路由完成，提交尚在执行」，最近产出TIA-448不能标本轮已产出，消息读取.1/去重.1/路由.2s/提交进行中/回执未开始；日志 `[16:45:00.4] INFO bridge awaiting commit`。我的巡检报告「PR #311 检查结论已更新并归档」，PR #311，读取.4/检查.3/对比.4/归档.3/通知.4s；日志 `[16:43:01.8] INFO PR311 archived`。特定人报告「PR #308 审查退出码1，评审未提交」，PR #308，读取.2/diff.3/执行.6s红色失败，提交与通知标未执行；日志 `[16:41:01.1] ERROR review exit=1`，失败总1.1s只能在报告记，不把左卡exit1改为成功。

日志原文由固定span按timestamp/level/message分色，时间灰、INFO青绿、WARN琥珀、ERROR珊瑚、标识高对比；2–4行不挤满右台，不抄私有原日志，不动态解析innerHTML。每个输出说明id在对应报告中唯一，点击来源胶囊仅打开此说明，不新增虚构详情screen。

```text
main.topology-split-drawer-workbench
└─ section.content
   ├─ header.workbench-top-strip
   ├─ div.split-workbench-frame
   │  ├─ aside.left-drawer-rail
   │  │  └─ article.rail-job-slot[data-job-row] ×6 (固定原序)
   │  │     └─ div.rail-tactile-face
   │  │        ├─ button.rail-reading-trigger[data-row-trigger]
   │  │        ├─ nav.rail-three-controls (toggle-pause / rerun / delete)
   │  │        ├─ p.rail-last-brief[data-hover-brief]
   │  │        └─ div.rail-delete-question (永久confirm/cancel)
   │  └─ section.right-report-stage
   │     └─ article.stage-job-report[data-report-panel] ×6 (与data-job一一对应)
   │        ├─ header.stage-conclusion-header (summary)
   │        ├─ nav.stage-output-capsules (outputs / 对应来源锚点)
   │        ├─ ol.stage-five-step-waterfall (stages)
   │        └─ pre.stage-terminal-tail (logs，固定语法span)
   └─ footer.workbench-foot-rail (逐job restore按钮与反馈文字)
```

## 8. Explicit Anti-Patterns & Verification Targets

任何右台选择导致左卡坐标变化都是FAIL；不能靠全文卸载、隐藏整个rail、重排或者滚动到首行来实现切换。禁止把640px台面改成对话框、折叠长卷宗、底部抽屉或2×3舱。无原始localization key、调试select、内层主题/viewport/SELECT控制、Active/Matte条、ruler、caustic纹、免责声明或v05..v10入口；此稿的价值是固定轨与大面积真实证据，不是多一个总数看板。

阶段2测量 frame42/58、18px沟槽与六槽的固定100px高度；每卡hover有16px、opacity>0的摘要且face抬-4；连续选择六件时rail外框位置100%不变，右报告summary/outputs/五阶段/logs全齐。WebKit1280×800给Light/Dark初始数仓、失败、运行中以及hover/click真实PNG，数仓9.1s条可视；数值与Title无 …、所有命中≥28px、全页无横溢出。

全main MutationObserver和初始Element/Text引用必须证实 removedElements = 0；测试按键不选卡、重复重跑只结算一次、暂停中重跑后仍paused、在途删除不回写、六件多次恢复原槽、胶囊与Esc焦点往返。reduced-motion仍可使用所有功能。静态规格/算式不是浏览器通过证明，独立Visual Traceback与Owner冻结/发布在后续完成，本叶子仅负责这份实现可依的设计稿。
