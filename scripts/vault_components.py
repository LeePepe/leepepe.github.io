"""Instance-safe markup for the vault's declared interactive pattern inventory."""
import html

ALIASES = {"MI-007": "MP-007", "TC-001": "IP-006", "LN-001": "IP-007"}
TITLES = {
    "IP-006": "零术语人话表达 (Plain-Language Microcopy)",
    "IP-007": "就地渐进式入口 (In-Place Progressive Entry)",
    "MP-007": "即时确定性结果回执 (Deterministic Action Receipt)",
}


def normalize_title(item):
    ident = ALIASES.get(item.get("id"), item.get("id"))
    return {**item, "name": TITLES.get(ident, item.get("name", ""))}


def build_live_stage(item):
    ident = ALIASES.get(item.get("id"), item.get("id"))
    tools = [("⌂", "主页"), ("✦", "收藏"), ("◒", "统计"), ("▣", "文件"), ("⌁", "连接"), ("⚙", "设置")]
    stages = {
        "MP-001": ("揭角卡片", '<div class="peel-card"><div class="peel-meta">更新于周一 · 版本 3</div><button class="stage-peel" aria-pressed="false">揭开右上角<span class="peel-corner" aria-hidden="true"></span></button></div>'),
        "MP-002": ("滑动确认", '<div class="stage-track"><button class="stage-thumb" role="slider" aria-label="滑动确认" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100">↠</button></div><div class="stage-controls"><input class="stage-range" type="range" min="0" max="100" value="0" aria-label="确认进度"><button data-reset-confirm>重置</button></div>'),
        "MP-003": ("拉绳灯光", '<div class="cord-visual"><svg viewBox="0 0 260 65" aria-hidden="true"><path class="cord-path" d="M130 0 Q130 20 130 46"></path><ellipse cx="130" cy="4" rx="55" ry="9"></ellipse></svg><button class="stage-cord" aria-pressed="false">● 拉动绳球</button></div>'),
        "MP-004": ("放大工具栏", '<nav class="stage-tools" aria-label="工具栏">' + ''.join(f'<button aria-label="{name}" data-tool="{name}"><span>{icon}</span></button>' for icon, name in tools) + '</nav>'),
        "MP-005": ("消息反馈", '<div class="stage-reactions" hidden>' + ''.join(f'<button aria-label="回应 {emoji}" style="--order:{i}">{emoji}</button>' for i, emoji in enumerate(["👍", "❤️", "🔥", "🎉", "👀"])) + '</div><button class="stage-bubble" aria-expanded="false">长按 / 点击消息 <b>0</b></button>'),
        "MP-006": ("文件入夹", '<div class="stage-drop-zone"><button class="stage-file" draggable="true">报告</button><button class="stage-folder" aria-label="文件夹"><span class="folder-lid" aria-hidden="true"></span>文件夹 <b>0</b></button></div><button data-reset-folder>重置文件夹</button>'),
        "MP-007": ("确定性回执", '<button class="stage-save">保存规则</button>'),
        "MP-008": ("流体背景", '<div class="stage-fluid" aria-label="有机流体"><i></i><i></i><i></i></div><div class="stage-controls"><label>湍流<input type="range" min="0" max="100" value="50" data-fluid-control aria-label="湍流强度"></label><button class="stage-play" aria-pressed="false">暂停流体</button></div>'),
        "MP-009": ("成摞纸牌", '<div class="stage-stack" aria-label="训练动作纸牌"><span data-card="A">训练 A</span><span data-card="B">训练 B</span><span data-card="C">训练 C</span></div><div class="stack-controls"><button data-stack="pickup">成摞抽拉</button><button data-stack="invalid">非法落点回弹</button><button data-stack="legal">合法重排</button></div>'),
        "IP-001": ("图表联动", '<div class="stage-chart">' + ''.join(f'<button data-segment="{x}" aria-pressed="false">{x}</button>' for x in ["有氧", "力量", "核心"]) + '</div><ol class="stage-chart-rows"><li data-segment-row="有氧" data-minutes="32">有氧 · 32 分钟</li><li data-segment-row="力量" data-minutes="24">力量 · 24 分钟</li><li data-segment-row="核心" data-minutes="18">核心 · 18 分钟</li></ol>'),
        "IP-002": ("组合筛选排序", '<div class="stage-filters"><button data-filter="all" aria-pressed="true">全部</button><button data-filter="doing" aria-pressed="false">进行中</button><button data-filter="done" aria-pressed="false">已完成</button><button data-sort aria-label="按耗时排序">耗时 ↑</button></div><ol><li data-status="doing" data-minutes="12">写作 · 12m</li><li data-status="done" data-minutes="8">复盘 · 8m</li><li data-status="doing" data-minutes="20">测试 · 20m</li></ol>'),
        "IP-003": ("列表详情", '<div class="stage-detail"><ol>' + ''.join(f'<li><button data-detail="{name}" data-duration="{duration}" data-parameters="{params}" aria-pressed="false">{name}</button></li>' for name, duration, params in [("训练计划",45,"强度 4"),("提醒规则",18,"每周一"),("周报摘要",12,"最近 7 天")]) + '</ol><div class="stage-inspector" aria-live="polite"><strong>选择一项</strong><span>耗时与参数在此呈现</span></div></div>'),
        "IP-004": ("局部恢复", '<label class="context-label">类别<select data-context><option value="strength">力量训练</option><option value="cardio">有氧训练</option></select></label><ul><li data-context-row="strength">深蹲 · 强度 4</li><li data-context-row="strength">推举 · 强度 3</li><li data-context-row="cardio">慢跑 · 强度 2</li></ul><div class="stage-controls"><button data-empty>严苛筛选</button><button data-relax>放宽当前条件</button></div>'),
        "IP-005": ("状态汇总", '<div class="stage-progress"><svg class="stage-ring" viewBox="0 0 42 42" role="img" aria-label="完成 0%"><circle class="ring-bg" cx="21" cy="21" r="16" pathLength="100"></circle><circle class="ring-value" cx="21" cy="21" r="16" pathLength="100"></circle></svg><div class="stage-tasks">' + ''.join(f'<label><input type="checkbox">{x}</label>' for x in ["热身","力量","拉伸"]) + '</div></div>'),
        "IP-006": ("人话表达", '<button data-plain aria-pressed="false">切换表达模式</button><p class="stage-copy">❌ 术语态：CRON 0 9 * * 1 · RRule FREQ=WEEKLY</p>'),
        "IP-007": ("渐进式入口", '<div class="reminder-row"><label class="stage-switch"><input type="checkbox" role="switch">开启智能提醒</label><button data-advanced aria-expanded="false">高级选项 ▾</button></div><div class="stage-advanced" hidden><label>静音时段<input type="time" value="22:00"></label><label>重复频率<select><option>每周</option><option>工作日</option></select></label></div>'),
        "IP-008": ("角标锚定", '<button data-flip aria-pressed="false">Trailing + Top 正贴</button><div class="badge-space"><div class="stage-badge">训练计划<b>周一 09:00</b></div></div><label class="stage-controls">角标字号<input type="range" min="80" max="120" value="100" data-scale aria-label="角标字号"></label>'),
    }
    if ident not in stages:
        return ""
    title, body = stages[ident]
    return f'<div class="vault-live-stage stage-{ident.lower()}" data-stage-id="{ident}" aria-label="{html.escape(title)} Live Micro-Demo"><div class="stage-caption">{title}</div>{body}<output aria-live="polite"></output></div>'


MATERIAL_PALETTES = {
    "GM-001": ("#E9D6B8", "#1D343A", "#A6DCDC", "#7194B9", "#FFFDF7"),
    "GM-002": ("#182132", "#F5F7FA", "#91DADD", "#9385CC", "#FFF6D8"),
    "GM-003": ("#DEB89B", "#162C37", "#A9CFC8", "#7194B9", "#FFFDF7"),
    "VS-001": ("#0B0D10", "#C8FF00", "#C8FF00", "#F59E0B", "#14181F"),
    "VS-002": ("#FAF7F2", "#163A2A", "#0F5132", "#D97706", "#FFFFFF"),
    "VS-003": ("#0E1117", "#B9D9EC", "#38BDF8", "#F43F5E", "#293B4E"),
    "VS-004": ("#FFF2CE", "#382A30", "#FCCC58", "#FF7689", "#FFFFFF"),
    "VS-005": ("#F8FAFC", "#263443", "#4F97FF", "#57C98B", "#FFFFFF"),
    "VS-006": ("#FFF7E7", "#3F284D", "#FFB89E", "#CBE7FA", "#FFFFFF"),
    "VS-007": ("#141927", "#D2D9FC", "#79DB9B", "#5E6AD2", "#182032"),
    "VS-008": ("#FA2D48", "#FFFFFF", "#FA2D48", "#FFC26B", "#FA2D48"),
}


def build_material_preview(item):
    ident = item.get("id", "")
    bodies = {
        "GM-001": '<div class="glass-content">本周训练 · 3 项</div><div class="glass-chrome">计划　◉　统计</div>',
        "GM-002": '<div class="foil-orb"></div><strong>Metal · Liquid Chrome</strong><div class="foil-band"></div>',
        "GM-003": '<div class="lens-scene"><span>光学透镜</span><div class="lens">聚焦</div><div class="lens lens-secondary">共享容器</div></div>',
        "VS-001": '<strong class="athletic-kpi">84<span>%</span></strong><span>本周达成</span><div class="telemetry-bars"><i></i><i></i><i></i><i></i></div>',
        "VS-002": '<small>WEEKLY LEDGER / 01</small><strong>本周训练账本</strong><div class="ledger-row"><span>力量</span><b>45 min</b></div><div class="ledger-row"><span>有氧</span><b>32 min</b></div>',
        "VS-003": '<small>SESSION / ACTIVE</small><div class="cockpit-dial"></div><strong>128 bpm</strong>',
        "VS-004": '<span class="sticker">完成啦！</span><strong>今日训练 ✓</strong><div class="sticker-small">+18%</div>',
        "VS-005": '<strong>今天，慢慢来</strong><div class="paper-task">✓　热身</div><div class="paper-task">○　力量训练</div>',
        "VS-006": '<div class="breathing-orb"></div><strong>呼吸 · 休息</strong><small>给下一组留一点空白</small>',
        "VS-007": '<small>CHRONO / SESSION</small><strong class="chrono">00:45:32</strong><div class="chrono-row">● 力量　　达成 84%</div>',
        "VS-008": '<small>MOVE / WEEK 01</small><strong class="magazine-title">KEEP<br>MOVING.</strong><span>本周训练记录 →</span>',
    }
    if ident not in bodies:
        return ""
    roles = ("canvas", "ink", "accent", "accent-2", "paper")
    style = ';'.join(f'--preview-{role}:{color}' for role, color in zip(roles, MATERIAL_PALETTES[ident]))
    return f'<div class="vault-material-preview" data-preview-id="{ident}" style="{style}" aria-label="{html.escape(item.get("name", ""))}">{bodies[ident]}</div>'
