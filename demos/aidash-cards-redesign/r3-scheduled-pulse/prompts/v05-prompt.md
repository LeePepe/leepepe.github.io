# v05 · 双时序档案柜 (topology-chronicle-split-cabinet)

## 1. Visual Metaphor & Archetype Lock
一个60/40不对称的小档案柜，左边双页文件袋承担操作，右边竖向仪表轨承担验印与结果抽屉。不是R2双栏列表放大，而是快慢文件纸从同一袋唇抽出，右轨把圆环和票据上下接成一个工具。锁定VS-007精密计时、CL-008蓝白极性，CP-002纸袋+DV-003五段仪表+MI-006阻尼抽取。X＝左页选任务、右侧选阶段；Y＝左快慢双页切换、右回执按需展开；Z＝实纸在前盖后叠放、仅page-tab是功能玻璃。SWWallet/Things 3负责纸层和内容节制，CleanShot X/Alcove负责工具与凹口的native观感。R3-ChronicleCabinet为候选AppTheme，仍只是单张macOS26定时卡。

## 2. Single P0 Focus & Initial Showcase State
左页tab初选「每日批处理 2」，个人数仓晨报在自己纸行内展开，显示04:01完成和「阶段通过」，右轨5/5是同一次记录的紧凑读数，不额外放一个左侧巨大5/5。另一个每日学习条露04:15已投递3题；背后的快页露三个任务头，保证五个名称各只有一个可见位置。时钟11月15日04:15。右下Linear receipt默认闭合，留40px抽取柄，三题正文未展开。P0集中于左侧当前纸及其立即运行，右环只做陪衬与钻取。

## 3. P1 / P2 Progressive Folding & Permanent DOM Contract
日批/高频按钮使已存在的纸页换深度，绝非移除再插入另一页。P1是另一页的paper-head摘要与右轨caption，P2是当前操作正文及右下结构化回执。初次加载就要拥有两个page、五个job条、五个SVG圆段和完整五stage/三question receipt；非活动正文transform入袋、aria-hidden/inert，外露标题仍可操作。右轨展开回执时只把其顶部ring从144px收为112px，不删除它。共用selectedJobId和selectedStageId，切快页保留原日批记录，选段自动把相应receipt行标亮。零innerHTML/outerHTML/replaceChildren/insertAdjacentHTML；类名、CSS custom properties、dataset和既有textContent是唯一驱动面。所有焦点路径可用Tab/Enter/Space，Esc把票收回触发柄，下一步归纸。

## 4. Measured Layout & 1280x800 Viewport Geometry
把柜体放在(80,80)，1120x640px，外部留白30%，>=22%目标有余量。padding24后content1072x592；cabinet-grid高536、gap16、cabinet-foot-bar高40。grid净宽扣24px间隔后1048，以60/40得到629px左file bay、419px右instrument rail。左bay 20px内距，tabs40px，空16px，纸面440px；非活动三标题每44px，活动日批两行64px+168px，剩余作为袋内空气。右rail 20px内距，header32px、gap12、figure144px、gap16、article292px，共496px。receipt开启在article自身固定292px里展开，五段每26px，三题各36px，分组题头和padding总54px可容纳292px；五阶段紧凑左列160px与三题右列183px分开布局，不把八行全叠一列。凹唇radius16px/depth12px，纸角18px、柜角28px。控件默认32px、page tab40px、ring有效hit32x32px，任何按钮>=28x28px；字体13/15/20/32px，段标签13px但不压缩省略。足栏只是静态时钟/状态，不放独立固定底部CTA。展开和peek的外接矩形均收在24px安全边内，1280x800中需0px unintended scroll overflow。

## 5. Dual-Theme Surface Polarity & Liquid Glass / Paper-Pocket Craft
柜体的Light AppTheme为desk #F2F4F8、cabinet #E9EDF4、paper #FFFFFF、ink #28324B、muted #5D6880、accent #4F5CB9、pass #28664D、warn #86560C、focus #0967CD；Dark依次为#0F1522、#1D293D、#2D3B53、#F1F5FF、#BECAE0、#BBC4FF、#9EDBBB、#EDC986、#8ABBFF。左纸和右票据均不透明，轨道实底稍暗于当前纸，用亮度而非笼状1px线区分。concave纸唇独立叠在page上，中心圆裁切搭配0.5px内高光，Light #FFFFFFD6/Dark #FFFFFF2C；三层ambient depth shadow分别0 2px 4px #21314B0A, 0 10px 22px #21314B12, 0 28px 46px #21314B16，Dark改#00000018/#00000028/#00000036。page-tab可采用IOR1.5、10pxbevel、blur8px/saturation140%、薄specular功能玻璃，Safari/reduced-transparency使用cabinet实色，无玻璃采样玻璃。所有读数含5/5、3题、cadence、日期、14s为tabular-nums；浅色白字CTA靠深accent，深色CTA深desk字靠亮accent。

## 6. Apple Native Spring Physics & Micro-Interactions
左纸通过--page-offset抬起36px，右receipt沿--receipt-y拉下104px，统一460ms cubic-bezier(0.22, 1.35, 0.36, 1)；figure收缩只做scale(0.86)和位置过渡，caption字号不缩。hover命中纸头translateY(-6px) peek，点击前不改变active-tab。ring用160x160坐标、cx/cy80、r56/stroke6，五circle pathLength100，每段stroke-dasharray="16 84"、offset0/-20/-40/-60/-80、stroke-linecap="round"，起点-90°。hover与focus给单弧亮度高光，点击把receipt相应stage行揭开；没有环绕五个job的线条。手动运行不占整张右轨，直接在被选行的live status显示已排队→运行中→刚刚完成 · 耗时14s，执行时disabled且回调以job ID归属，当前选择变了也不污染别的记录。计时推进只在浏览器内存，无scheduler/CloudKit/Linear请求。prefers-reduced-motion: reduce移除纸抬升、peek、弹性和环闪动，120ms淡入/固定布局保留所有操作。

## 7. Production Data Inventory & Exact DOM Topology
左袋永久资料按两个page归档：高频页含linear-bot-bridge｜Linear @bot 桥接｜每 1 分钟｜04:14完成；my-pr-supervisor｜我的 PR｜每 5 分钟｜04:10完成；pr-auto-review｜PR 自动审查｜每 5 分钟｜04:10完成。日批页含aidata-digest｜个人数仓晨报｜每日 04:00｜04:01完成、5/5通过；daily-learning｜每日学习推荐｜每日 04:15｜04:15完成、已投递3题。UI名不使用旧的「特定人PR」或「每日简报」替代。

instrument-rail的structured receipt明确两个来源。晨报部分五段依次为① 个人源采集 (collect)、② L2-L3 入仓 (normalize_merge)、③ Retro-ROI (retro_roi)、④ 学习寻题 (learning_topics)、⑤ Brief 投递 (digest_push)，每项通过，不造每段时长。学习部分标题「Linear TIA · 3题送达」，内容为怎样区分 Cache 命中率与上下文占比？、如何用证据区分实现缺陷与规格缺口？、如何让增量入仓保持幂等？。题目是固定代表性数据供离线设计，没给真实TIA issue ID，禁止编链接或宣称线上写入；这份学习记录不是五stage镜像。

保持header→figure→article在instrument rail下的父子序列，图标24x24 inline SVG/currentColor/round stroke1.5，与ring有效命中按钮都有可读label。

```html
<main class="cabinet-card topology-chronicle-split-cabinet">
  <section class="content">
    <div class="cabinet-grid">
      <section class="pocket-file-bay"><nav class="file-tempo-tabs"></nav><div class="file-pocket-mouth"><section class="minute-file-page"><div data-job="linear-bot-bridge"></div><div data-job="my-pr-supervisor"></div><div data-job="pr-auto-review"></div></section><section class="daily-file-page"><div data-job="aidata-digest"></div><div data-job="daily-learning"></div></section></div></section>
      <aside class="instrument-rail"><header class="rail-heading"><h1></h1></header><figure class="rail-stage-ring"><svg></svg><output></output><figcaption></figcaption></figure><article class="linear-receipt-file"><button class="file-pull"></button><div class="structured-file-body"><ol class="digest-proof-lines"></ol><ol class="learning-proof-lines"></ol></div></article></aside>
    </div>
    <footer class="cabinet-foot-bar"><time></time><p class="cabinet-live-status" aria-live="polite"></p></footer>
  </section>
</main>
```

## 8. Explicit Anti-Patterns & Verification Targets
双时序柜不接受.caustic-veil、.ruler、Active/Matte bars、<select>调试选择器、沙盒免责字样、五点orbital图与innerHTML节点替换。特别禁止左右两边复印当前任务名称和巨大5/5、只画灰框假抽屉、或者为了展开把整卡推出iframe。内部没有画廊/theme/viewport切换，foot bar也不是macOS固定底部操作栏。

规定四态：S0日批晨报在左展开，右环5/5，回执缩口；S1切高频并选我的PR，背页日批两个标题可达；S2右票抽出并选①，5阶段和3题不遮挡，Esc恢复；S3立即运行经过排队、运行、完成，完成后可重新触发且状态归属正确。Writer应交8张Light/Dark实际1280x800 WebKit截图及DOM引用持久性记录，涵盖五任务、两页、五圆段与票券。检查keyboard focus、Reduce Motion、文字4.5:1、0px意外滚动、零数值…和raw localization keys；本Prompt只冻结候选交接要求，不等同于已做像素验收。
