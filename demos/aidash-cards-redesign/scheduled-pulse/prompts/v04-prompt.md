# v04 · 五签阶梯钱包 (topology-stepped-wallet-well)

## 1. Visual Metaphor & Archetype Lock
这一张把SWWallet的五层卡片真正保留成阶梯钱包井：前三签的纸头刻「高频」，后两签属于「日批」，前袋盖下角同时容纳环形小仪表与向上揭开的回执。采用VS-005安静纸感、CL-006 Sky-Sage，但完成色退到细印记，不做彩虹钱包。CP-002是层级依据，DV-003约束环的precision，MI-006与MP-001指导揭纸触感。X＝点击五签中的一签，Y＝三加二节律标签折叠为纸头，Z＝五层z-index、袋盖、当前抽卡之间有可解释遮挡。Things 3的行内展开、CleanShot X的悬浮紧凑度和Alcove凹边只作参考；R3-SteppedWallet候选AppTheme用于macOS26卡片，绝不新增管理页。

## 2. Single P0 Focus & Initial Showcase State
钱包一开始选每日学习推荐，最后一签露出完整面，唯一主数字为3题，记录04:15完成 / 每日3题直投Linear。它自己的标题留在该签，不复制到masthead。其余四签以40px纸头显示各自名字、频率和最近时间；「Fast Trio 3 / Daily Duo 2」是节律分界，不是导航新功能。角部小环仍显示晨报的5/5及04:01，尺寸退到112px，不和3题抢主位。peel-receipt-pocket首屏合上，只有「执行回执」揭角按钮可见；时钟11月15日04:15，不自动开始播放运行过程。

## 3. P1 / P2 Progressive Folding & Permanent DOM Contract
P1藏在签头和钱包角的环caption，P2进前盖下的回执。必须在首个HTML中挂好五个li任务签、fast/daily两页分组内容、五个SVG circle和整份五段/三题回单。这里两页不是再复制一份任务：ol中前三li即快页、后二li即慢页，以data-page配对切换标签；另行生成副列表禁止。未选正文通过类名与CSS变量压入井中并设inert，标题按钮独立可达。selectedJobId只允许一个；选新卡是对已有Element的transform与z-order变更。没有innerHTML、outerHTML、replaceChildren或insertAdjacentHTML，不在任何点击中创建卡、段或回执；aria-expanded与已有text leaf可变。开回单时把当前签操作缩回，留摘要与同一个按钮；Esc收揭角，焦点归还，再按Esc归签。

## 4. Measured Layout & 1280x800 Viewport Geometry
给钱包1080x640px、x100/y80，未覆盖视口32.50%，留白>=22%。24pxpadding后content1032x592；wallet-masthead44px，16px间隙，stepped-card-stack352px，16px间隙，ring-and-receipt-dock164px。五卡宽度从984/976/968/960到952px、横向都居中；四条未选纸头各40px，当前展开面144px，合304px；井内另留顶部40px与底部8px安全空间，总352px，上抽32px的端点与超调仍有余地。选中任何卡重排偏移，但名字都在同一352px井内，不裁掉五层后卡。dock是168px ring pod +24px gap +840px receipt pocket；回执打开时stack缩224px、dock长292px，总592px不变。receipt正文五段置左368px，三题右368px，gap24，行间6px，段行28px、题行40px。唇凹口r16px/depth16px，钱包外角30px，卡角18px，揭角有效块36x36px；其他目标32px，底限28x28px。13px是最小UI字，15px任务名、20px标题、32px主读数；所有timestamp留68px独立槽。hover与超调端点需要外框24px安全留空，验证0px unintended scroll overflow而不是给body加裁切盖住错误。

## 5. Dual-Theme Surface Polarity & Liquid Glass / Paper-Pocket Craft
钱包色极性明确分前后：Light canvas #F3F5F7、well #E5EAF0、card #FFFFFF、ink #263246、muted #5B677B、accent #235FB1、success #27694C、warning #87570C、focus #075EC9；Dark canvas #111923、well #1D2B3B、card #304156、ink #F1F6FF、muted #BFCDDF、accent #A7CAFF、success #9EDDB9、warning #F1C982、focus #8CBFFF。不透明卡面靠亮度和相互遮挡区分，五张卡不涂五种颜色。前袋唇用两段水平线接中央内凹圆口，独立cover层带0.5px inner specular highlight（#FFFFFFDD / #FFFFFF2B）；Light环境影0 1px 2px #182C420A, 0 8px 20px #182C4212, 0 24px 44px #182C4216，Dark为相同几何的#00000018/#0000002A/#00000038。被压在后方的卡影要变浅，不叠五次黑影。functional glass只准masthead节律小控：IOR1.5、bevel10px、blur7px、saturation140%、rim0.5px，Safari或reduced transparency改well实面。主读数/时刻/5/5/14s启用tabular-nums；暗CTA亮蓝背景上用深ink替代白字。

## 6. Apple Native Spring Physics & Micro-Interactions
抽签的physics为500ms cubic-bezier(0.22, 1.35, 0.36, 1)，当前卡translateY(-32px)，背卡收束4px级位差；悬停只有目标签translateY(-6px) peek，不洗牌。回单向上升128px，右下揭角最多rotate(-4deg)，旋转只施于无文字的corner-patch。环用160方viewBox、center80/r54/stroke6，五circle pathLength100、stroke-dasharray="16 84"，offset0/-20/-40/-60/-80；stroke-linecap="round"给每一弧精确气隙，初始中心5/5以tabular-nums对齐。hover亮段而不跑动环，点击段开盖并highlight同stage行，Space/Enter等价。立即运行就在当前卡按钮边给已排队→运行中→刚刚完成 · 耗时14s反馈，按钮禁用防重复，完成后恢复；回调保存目标job避免选择变化串写。整个过程仅内存state，不触真实scheduler与Linear。prefers-reduced-motion: reduce取消peek、揭角和弹性，改120ms淡入及确定位置，仍显示完整回执。

## 7. Production Data Inventory & Exact DOM Topology
五签要保留这些原始标识、名称和cadence，最新记录采用同一04:15展示时钟：

| 签号 | id | 纸头文字 | 周期与已完成时刻 |
|---|---|---|---|
| 1 快 | linear-bot-bridge | Linear @bot 桥接 | 每 1 分钟 · 04:14 |
| 2 快 | my-pr-supervisor | 我的 PR | 每 5 分钟 · 04:10 |
| 3 快 | pr-auto-review | PR 自动审查 | 每 5 分钟 · 04:10 |
| 4 慢 | aidata-digest | 个人数仓晨报 | 每日 04:00 · 04:01 / 5/5通过 |
| 5 慢 | daily-learning | 每日学习推荐 | 每日 04:15 · 04:15 / 3题已送达 |

揭开的纸单以stage属性对应五圆段：collect=① 个人源采集、normalize_merge=② L2-L3 入仓、retro_roi=③ Retro-ROI、learning_topics=④ 学习寻题、digest_push=⑤ Brief 投递；行状态通过，不补造未给出的每段duration。独立学习栏落在「Linear · TIA · 3/3」下，三题是如何让增量入仓保持幂等？、如何用证据区分实现缺陷与规格缺口？、怎样区分 Cache 命中率与上下文占比？。这里只指定代表性题目用于离线卡面选型，不能宣称读取真实Linear记录，也不能杜撰TIA链接；daily-learning不是第二份五阶段晨报。

指定li结构不可替换为五篇article统一网格。页面图标为24x24 inline SVG/currentColor/1.6px圆端，环每个弧旁有>=28px有名称按钮层；装饰钱包盖不进accessibility tree。

```html
<main class="wallet-card topology-stepped-wallet-well">
  <section class="content">
    <div class="wallet-masthead"><h1></h1><nav class="tempo-tabs"></nav><time></time></div>
    <ol class="stepped-card-stack">
      <li class="wallet-slip fast-slip" data-job="linear-bot-bridge" data-page="fast"></li>
      <li class="wallet-slip fast-slip" data-job="my-pr-supervisor" data-page="fast"></li>
      <li class="wallet-slip fast-slip" data-job="pr-auto-review" data-page="fast"></li>
      <li class="wallet-slip daily-slip" data-job="aidata-digest" data-page="daily"></li>
      <li class="wallet-slip daily-slip" data-job="daily-learning" data-page="daily"></li>
    </ol>
    <div class="ring-and-receipt-dock">
      <figure class="segmented-ring-pod"><svg></svg><output></output><figcaption></figcaption></figure>
      <section class="peel-receipt-pocket"><button class="peel-corner"></button><div class="receipt-underleaf"><ol class="five-stage-receipt"></ol><ol class="three-question-receipt"></ol></div></section>
    </div>
  </section>
</main>
```

## 8. Explicit Anti-Patterns & Verification Targets
签头不是五张KPI平铺，不能把SWWallet压成灰底VStack。禁止.caustic-veil和.ruler、Active/Matte bars、<select>内部测试器、沙盒免责copy、五点orbital舞台、innerHTML替换节点，以及文字跟随揭角弯折。卡内dock是回单收纳，不是桌面浮动底栏；不要增加主题/variant控制抢走外层chooser职责。

测试四个完成态：初载选学习/3题、角环5/5且盖合；选Fast Trio中的桥接并看到4个兄弟签头均未重复；揭盖点⑤，五段和三题完整可读，Esc合盖后焦点准确；当前卡立即运行，排队、运行与完成有逐步反馈且可再次执行。四态×两appearance真实WebKit1280x800截图需证明0px意外scroll、无clipping、>=4.5:1文字对比及零数字ellipsis。通过Element引用比较确认快慢两页数据、五li、五circle与回单未被销毁；同路验证键盘、Reduce Motion、无raw localization key。此处是Writer验收目标，不是Stage1渲染通过声明。
