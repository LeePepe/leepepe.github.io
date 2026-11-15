# v01 · 晨间矿纸卷宗 (topology-stacked-paper-pockets)

## 1. Visual Metaphor, Palette & Anti-Clone Spatial Lock

把定时任务做成可以亲手抽出回执的矿物纸档案袋，而非把圆角表格重新上色。参考 Things 的安静清单与 Wallet 的袋口层次：六个横贯工作面的纸袋垂直排列，前袋唇压住后方报告纸，左侧亮起一条窄而清楚的状态书脊。单个 Coding Writer 只手写 scheduled-pulse/v01.html；不写其他候选、不派下级、不用 Python/Node 模板生成 HTML/CSS。此候选的真正差异是「报告就在原袋下面」，没有侧栏、磁贴或全屏浮层。

锁定 web 呈现的 macOS 工作面；候选坐标为 VS-002 暖色编辑档案、CL-002 Mineral、X=阅读任务及可逆操作、Y=单活跃行内卷宗、Z=袋底/报告纸/前袋唇三层。AppTheme 在这里仅为候选令牌，不能冒充 Owner 已冻结的生产主题。底色 Light #FAF7F2、Dark #161513；纸面 Light #FFFDF8、Dark #25221D；正文 #29251F / #F1EAE0，次要字 #696055 / #BDB2A4，极少量黄铜 #8A6D3B 仅用于卷宗装订细节。所有选择描边服从任务状态色，不拿品牌金替代失败红。

空间反克隆锁：section.content 的直接子节点只有矿纸页眉、pocket-stack-well、恢复栏，袋井只有一列六件 paper-pocket-unit。每件必须有 6px 左脊、顶部内凹拇指缺口、向下打开的双栏内胆。不能挪成 v02 的两列舱体，不能接 v03 的右侧常驻舞台，不能把异常重排成 v04 的置顶英雄。候选专属 CSS 用 mineral-/pocket-/folio- 命名，除规定语义钩子外不得抄其他候选布局；最终跨候选 CSS 类/规则重合率应小于 15%。

## 2. Single P0 Focus, Semantic Status Colors & Initial Showcase State

唯一 P0 是「读懂本次晨间投递是否完成并取走回执」，开场选中每日简报 05:00，完整报告纸已抽出。其余五袋只呈现任务正面，属于同一袋井的同级记录，不另造 KPI 横排、总成功率或执行历史页。P1 永久保留周期、累计/今日次数及三键；P2 是悬停一句话；P3 日志与五段耗时只在对应内胆中展开。三枚绿色结果的完成值遵守 R5 的 1.8s，而不是旧 R4 2.4s/0.9s。

状态不是装饰渐变：#10B981 的 ● 成功 (1.8s) 用于每日简报、每日学习推荐与我的 PR 巡检；#F59E0B 的 ▲ 耗时偏高 (14.2s) 对应 AIData 数仓脉搏；#F43F5E 的 ✕ 失败 (exit 1) 对应特定人 PR 审查；#06B6D4 的 ● 运行中给 Linear @bot 桥接；暂停切换后整条色脊改 #64748B、徽章改 ⏸ 已暂停。色脊用原始色值，文字用同色系可读深墨/浅墨，符号和汉字始终伴随颜色，不能只凭红绿区分。

初始六袋顺序为简报、学习、数仓、桥接、我的巡检、特定人审查；不自动排序。任何一次状态变化都不改变袋顺序。桥接青光仅呼吸于 6px 脊内，失败袋不抖动也不闪烁。截图中的亮绿色成功与下方红色失败必须能同时辨认，选中简报的白纸不能把别的状态变成低对比灰字。

## 3. Hover Brief Preview ([data-hover-brief]) & Click-to-Pull-Out Drawer ([data-report-panel]) Contract

每个 article[data-job-row] 都预先带一条 [data-hover-brief]，置于正面下沿预留的 18px 纸缝；pointerenter 或 :focus-within 把袋面上提 4px，后方短纸再上提 2px，产生合计 6px 的抽纸错层。袋井和相邻行坐标不变。短纸从 opacity 0 到 1、translateY(6px) 到 0；pointerleave 180ms 后回落，移进短纸不能立即关闭。六句短文分别为「晨间五阶段全绿 · 3 题直投 → TIA-448」「题单匹配完成 · 推荐已送达 → TIA-431」「入仓 9.1s 偏高 · 全轮 14.2s → TIA-448」「本轮桥接提交中 · 上次产出 → TIA-448」「巡检结论已归档 → PR #311」「审查退出 1 · 未提交新评审 → PR #308」。仅短纸可显简句，完整摘要留在报告里；一行不塞全部日志。

正文点击入口为独立原生 button[data-row-trigger]，覆盖标题、周期、次数、状态四区；尾部 action nav 是其兄弟，不允许 button 包 button。点击已选袋收起，点击另一袋先收起旧内胆再抽出新内胆，始终最多一个完整报告。所有六个 [data-report-panel] 自首次载入起存在，收起用 grid 行高/opacity/inert，绝不替换 HTML、拆卸节点或重建 span。报告的可见高度为 208px，上下透明裁切层只裁报告纸，不裁卡面按钮或 focus ring。

内胆有两栏：左栏「执行结论摘要」与可点 TIA-448、TIA-431、PR #311、PR #308 胶囊；右栏五段彩色计时与高亮日志尾部。产出标签依任务实际关联显示，不给每袋重复全部链接。未知外部 URL 不能编造：胶囊链接到本袋预先存在的 #folio-<job>-<output> 产出说明，展开并聚焦同一报告里的来源文字；不请求真实 Linear 或 GitHub。点击胶囊、三个按钮、撤销都阻止事件冒泡，不切换袋。

## 4. Measured 1280x800 Viewport Geometry & Spatial Bounding Boxes

以 CSS px、border-box、1280×800 内层 viewport 为准，不把外部画廊 bezel 算进页面。内容横界 x=64..1216，净宽 1152；页眉 x64 y40 w1152 h48，袋井 x64 y104 w1152 h632，恢复栏 x64 y752 w1152 h32。main 高 800，不添加自己的主题或屏幕尺寸开关。井内左右各 12px，袋面 x76 w1128；上下余量至少 12px，保护负向提起与内凹袋口的阴影。

六个正面每张 h56、相邻间隔 8；单活跃报告 h208，面与报告间距 8。总占高算式 6×56 + 5×8 + 208 + 8 + 2×12 = 616 ≤ 632。默认展开第一袋：六张 face 的 y 分别 116、396、460、524、588、652，各自高 56；简报的报告从 y180 到388。最后一面到708，井底保留 28px。换到最末袋后其面为y436..492、报告为y500..708，仍在736 的井底内；不采用所有报告同时撑开的超高滚动平面。

面内水平净宽 1096（左右16），用五区 228 / 212 / 198 / 164 / 230，加四个16px 间隔，和为1096。四区整体触发面 w866；右尾宽230，三个键为64/72/58×30、间隔8，总210，靠右20px 空气。面中上层内容高30、下层短纸18，外围纵向各4px；最宽标题和「累计 4,280 次 · 今日 184 次」不省略。标题14px/600，周期与计数12px，章名20px，日志11px monospace；数字启用 tabular-nums。点击目标至少28×28，胶囊高度30。

内胆 x92 w1096，左右列宽452与628，中缝16。标题与结论区高40；胶囊行32；右侧五条高20的刻度行共100，下面日志48，纵向8px呼吸。右侧每条给 158px 标签、剩余轨道与52px数值，不用颜色条代替数字。若用户字体放大导致内胆内容超208，则只给内胆开启纵向滚动并预留 scrollbar-gutter，不缩到不可读、也不把标题横向截成 …。

## 5. Dual-Theme Surface Polarity & Tactile Drawer Lip Craft

浅色的袋底是 #EEE7DA，抽出的报告是更亮的 #FFFDF8；深色的袋底 #1B1814，前袋面 #25221D，报告 #302B23，用亮度递进说明前后关系。Light 阴影用暖黑 alpha .06/.04 的 1px 接触层与 10px 环境层；Dark 接触影 .26，加白 alpha .07 的 inset 0 1px 0 顶沿。边框只在口沿和脊根各一根半透明发丝，不给四字段分别画盒子。最外井是一个整体容器，六件是里面的档案记录。

拇指缺口位于袋顶中心，宽36、高8，以两枚曲线或局部 mask 做凹弧；缺口只能作用于装饰袋唇，不 cut 掉命中区域或汉字。前唇厚2px，后纸向内缩8px，两侧露1px暖纸边；悬停时露出短纸而不是把整篇报告提前显示。长内容下层可实色裁切，选中纸以层级和左脊亮度表现，不用夸张旋转或拟真牛皮贴图。

矿纸候选不使用内容玻璃或折射滤镜，文字下层为实色。动作图标是24×24 viewBox、1.5px圆端的本地 inline SVG，显示16px并保留暂停、Rerun、删除文字；无图标字体、外部图片请求或装饰 emoji。正文对比至少4.5:1，图标/焦点至少3:1；原始 #10B981 等只用于书脊、色点和轨道，浅色徽章字另用深色同系墨，不把低对比艳绿直接当小字。

## 6. Apple Native Spring Physics & 3-Button Permanent DOM Micro-Interactions

纸袋的运动曲线固定 cubic-bezier(0.22, 1.35, 0.36, 1)：hover 240ms、内胆抽出460ms、旧内胆收起420ms；只给 transform 一点超调，测量高度用单调 ease-out，避免高度弹出井底。按键压下 scale(.97) 100ms，弹回180ms，不让数字 bounce。prefers-reduced-motion 下提纸位移归零、变更在不超过80ms淡入完成，桥接色脊不再循环脉冲；页面失焦也停止呼吸。

[data-action="toggle-pause"] 保存 enabled 排程状态和 lastResult 两个维度。暂停后按钮变继续、脊灰，最近一次报告照常保留；继续恢复最近结算的成功/耗时偏高/失败结果，不能把所有恢复都写成成功。若暂停发生于重跑中，该单次重跑可完成但不重新启用排程，面上最终仍是 ⏸ 已暂停，报告记录真实单次结果。

[data-action="rerun"] 在浏览器候选内立即给青色运行反馈、阻止重复在途点击；同一 job 使用递增 runToken，结算一次才把累计及今日各加1，仅更新既有 Text.data/nodeValue（不得设置父 Element.textContent）。脚本反馈仅驱动当前文档，不启动本机任务，不触达数仓、XPC、Linear 或 GitHub。已失败的审查重跑仍按声明的 exit 1 分支反馈，不能因为点击 Rerun 就凭空修好故障；数仓保持14.2s的慢结果，三个健康任务为1.8s。

[data-action="delete"] 首次激活在本袋已挂载的确认条中询问「删除此任务？」并提供确认/取消，第二次确认后只折叠该 article 的空间并设 inert，不 remove。恢复栏的 [data-action="restore"] 可从预挂载的六个恢复入口分别撤销，不是只支持最近一件；撤销恢复原序与原计数。删除令未结算 token 作废，不让晚到回调改计数。操作之后 focus 留在当前键，删除后移至对应撤销；撤销后回到原触发面。所有按钮对 click 与 keyboard 事件隔离，原生按钮提供 Enter/Space，Esc 收报告回触发面，隐藏内容不参与 Tab 序列。

## 7. Production Data Inventory & Exact DOM Topology

本轮数据边界是 Stage 1 handoff：R5 spec §6、briefs/T5 与 r5/domain 决定结构/状态；累计、今日、周期沿用 r4/domain §2 的声明快照。下面的报告分段是明确的候选内容合同，不宣称查过 live L1–L5，日志是摘要化展示文本而非采集证据。aidash-metrics 的 inspector 当前不支持 scheduled_pulse，不能用它的 Skills ROI 结论证明这些数值。没有新增指标、遥测或生产绑定；将来接入数据前须由上游提供覆盖率、窗口、时间戳和真实报告，缺失用「暂无回执」而非0。当前页面不渲染沙盒免责声明，也不虚构更细故障原因。

| 矿纸袋 id | 正面任务 | 周期文字 | 次数文字 | R5 首次状态 |
|---|---|---|---|---|
| daily-brief | 每日简报 05:00 | 每天 05:00 · 下次 12h 后 | 累计 142 次 · 今日 1 次 | 成功，1.8s，翡翠 |
| daily-learning | 每日学习推荐 04:15 | 每天 04:15 · 下次 11h 后 | 累计 98 次 · 今日 1 次 | 成功，1.8s，翡翠 |
| aidata-pulse | AIData 数仓脉搏 04:00 | 每天 04:00 · 下次 11h 后 | 累计 186 次 · 今日 1 次 | 耗时偏高，14.2s，琥珀 |
| linear-bot-bridge | Linear @bot 桥接 | 每 1m · 刚刚 16:45 | 累计 4,280 次 · 今日 184 次 | 运行中，电光青 |
| my-pr-patrol | 我的 PR 巡检 | 每 5m · 2m 前 | 累计 860 次 · 今日 36 次 | 成功，1.8s，翡翠 |
| target-pr-review | 特定人 PR 审查 | 每 5m · 4m 前 | 累计 312 次 · 今日 12 次 | 失败，exit 1，珊瑚 |

每份报告保留五个可读计时槽位「① 个人源采集」「② L2-L3 入仓」「③ Retro-ROI」「④ 学习寻题」「⑤ Brief 投递」；非晨间任务在同一槽旁明确自己的子阶段名称，不冒充执行了数仓或学习步骤。阶段本色依次青/靛/紫/金/绿；失败覆盖该阶段红，进行中青，未开始/未执行灰且无实心完成条。已完成条按本报告最大已完成秒数归一，数字不可藏；运行中只给已知阶段计时，不给总耗时终值。

卷宗正文逐袋写实：简报结论「晨间五阶段已结束，三题已进入投递回执」，产出 TIA-448、TIA-431，五耗时0.3/0.5/0.4/0.3/0.3s；学习结论「三题完成筛选与推荐投递」，TIA-431，子阶段候选/去重/匹配/整理/投递对应0.3/0.2/0.5/0.4/0.4s；数仓「入仓耗时9.1s偏高，本轮仍已完成」，TIA-448，1.2/9.1/1.8/1.3/0.8s。健康结果合计1.8s，数仓合计14.2s，严禁出现面上1.8而报告2.4的冲突。

余下报告也不能留占位：桥接「消息已路由，提交仍在进行」，TIA-448标注上次产出，读取0.1s/去重0.1s/路由0.2s/提交进行中/确认未开始；巡检「PR #311 检查结果已归档」，PR #311，读取/检查/对比/归档/通知为0.4/0.3/0.4/0.3/0.4s；审查「PR #308 审查进程退出1，未提交新评审」，PR #308，读取0.2s/diff0.3s/执行0.6s失败/提交未执行/通知未执行。失败原因仅到退出码，不编造权限、网络或仓库故障。

终端尾部每袋2–3行固定 text spans：简报 `[05:00:01.8] INFO brief delivered TIA-448`；学习 `[04:15:01.8] INFO recommendations=3 delivered`；数仓 `[04:00:10.3] WARN warehouse=9.1s` 与 `[04:00:14.2] INFO pulse finished`；桥接 `[16:45:00.4] INFO awaiting commit`；巡检 `[16:43:01.8] INFO checks saved PR311`；审查 `[16:41:01.1] ERROR review exit=1`。timestamp灰、INFO青绿、WARN琥珀、ERROR珊瑚，命令/标识中性亮墨；不靠 innerHTML 语法着色。

```text
main.topology-stacked-paper-pockets
└─ section.content
   ├─ header.mineral-folio-header
   ├─ div.pocket-stack-well
   │  ├─ article.paper-pocket-unit[data-job-row][data-job="daily-brief"]
   │  │  ├─ div.pocket-face-layer
   │  │  │  ├─ button.pocket-reading-face[data-row-trigger][aria-controls="folio-daily-brief-report"]
   │  │  │  ├─ nav.pocket-tail-tools (toggle-pause / rerun / delete)
   │  │  │  └─ p.pocket-preview-slip[data-hover-brief]
   │  │  ├─ div.pocket-confirm-line (永久确认/取消按钮)
   │  │  └─ section.folio-dossier[data-report-panel]#folio-daily-brief-report
   │  │     ├─ div.folio-conclusion-column (summary / outputs / 对应产出说明)
   │  │     └─ div.folio-timing-column (stages / logs)
   │  └─ article.paper-pocket-unit[data-job-row] ×5，分别手写其他任务与独立报告
   └─ footer.mineral-restore-bar (六个持久 restore 入口及 aria-live 文本)
```

## 8. Explicit Anti-Patterns & Verification Targets

不要把矿纸工艺偷换成旧 R4 的六行表格和一张套用报告；必须能从缺口、前唇、亮脊和抽出内胆认出袋。不要复制 aurora、workbench 或 command 的结构/CSS；不能增 v05..v10、选项测试 select、内层主题切换器、Active/Matte 条、标尺框、条纹 caustic 或无数据依据的统计面板。本文的旧 R4 数据只是库存来源，旧强制五列外观与旧成功耗时不再作为 R5 视觉断言。

Stage 2 以 WebKit 1280×800 检验两主题的初始展开、每袋 hover 与点击；短纸 opacity>0且18px可见，hover不改其他行的 bounding box，六袋报告依次可达且四块齐备，缺口不盖字。用全 main MutationObserver 累积 removedElements = 0，包含文本节点；记录初始节点引用，在暂停/继续、连续Rerun、确认删除、多个撤销和快速换袋后仍相同。检查按键不触发抽屉、计数只结算一次、删除旧回调无效、paused 单次运行后仍paused。

提供真实 PNG 与几何记录，而非把这份 Prompt 的算式当截图：全页无意外横溢出、所有目标≥28px、数值无 …/裁切、状态文字和主题对比通过，键盘能读报告并回原袋。日志不泄露 token、绝对私有路径或原始个人消息。Stage 1 只能验收文件和规格独立性；Owner 选择、实现、视觉回溯、发布由上游后续阶段完成，此叶子不声称已执行。
