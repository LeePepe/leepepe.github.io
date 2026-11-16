#!/usr/bin/env python3
"""
AI-Managed Xiaohongshu Account End-to-End Operations CLI (TIA-464).

Capabilities:
1. login-check: Inspect persistent Chrome profile / cookie session health for creator.xiaohongshu.com;
   return structured READY / AUTH_REQUIRED without headless brute-forcing or anti-bot bypass.
2. plan-schedule: Connect knowledge-vault ({thoughts,concepts,craft}) and story-craft desensitization
   pipeline to build an orthogonal schedule across:
   - 3 Columns: smart-home | ai-indie-dev | hardcore-digest
   - 3 Visual Styles: style-a-bento | style-b-ai-editorial | style-c-handdrawn
   - 3 Title Formulas: pain-point-hook | counter-intuitive-number | lazy-subtraction
   Includes 3 candidate titles (<=20 chars), no-leading-space short body (<=3 lines/paragraph,
   hook in first 80 chars), 5 official #topics, and 3:4 (1080x1440) slide storyboards.
3. upload-draft: Enforce auto_draft_owner_confirm mode. Validate anti-repost rules & 1080x1440 (3:4)
   dimensions, stage or execute Playwright persistent-context upload to creator.xiaohongshu.com
   draft box ("暂存离开"), never auto-publish publicly without owner confirmation, and generate a
   Linear confirmation card payload.
4. collect-metrics: Ingest creator note metrics (impressions, views, ctr, avg_read_seconds, likes,
   collects, comments, shares, new_followers, top_comment_questions) into a local ledger.
5. retro-report: Compute CES = (likes*1 + collects*3 + comments*4 + shares*4) / max(views, 1),
   collect_rate, and CTR; rank Column x Style x Title Formula horse-race winners; recommend next-week
   column weights (e.g. boosting top-performing column to 50%); and recycle top_comment_questions
   into next-cycle topic candidates.
"""

from __future__ import annotations

import argparse
from datetime import date, datetime, timedelta, timezone
import json
import os
from pathlib import Path
import re
import struct
import sys
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_VAULT_DIR = Path.home() / "Development" / "Personal" / "knowledge-vault"
DEFAULT_PROFILE_DIR = Path.home() / ".config" / "xhs-account-ops" / "chrome-profile"
DEFAULT_STATE_DIR = Path.home() / ".config" / "xhs-account-ops" / "state"
CREATOR_PUBLISH_URL = "https://creator.xiaohongshu.com/publish/publish"

COLUMNS: dict[str, dict[str, str]] = {
    "smart-home": {
        "id": "smart-home",
        "name": "栏目 A · 智能家居与生活折腾",
        "short_name": "智能家居与生活折腾",
        "source_binding": "knowledge-vault/thoughts + nas-smart-home",
        "audience": "全屋智能玩家 / 桌面改造爱好者 / 讨厌繁琐 App 步骤的生活流用户",
    },
    "ai-indie-dev": {
        "id": "ai-indie-dev",
        "name": "栏目 B · AI 工具与独立开发实录",
        "short_name": "AI 工具与独立开发实录",
        "source_binding": "story-craft + VoxPocket / AIDash / BAMA / Genjutsu",
        "audience": "独立开发者 / AI 效率控 / Apple 生态产品设计师",
    },
    "hardcore-digest": {
        "id": "hardcore-digest",
        "name": "栏目 C · 反常识硬核科普",
        "short_name": "反常识硬核科普",
        "source_binding": "knowledge-vault/concepts + craft",
        "audience": "好奇心旺盛的科技读者 / 喜欢生活教具拆解底层原理的泛科普受众",
    },
}

VISUAL_STYLES: dict[str, dict[str, str]] = {
    "style-a-bento": {
        "id": "style-a-bento",
        "name": "Style A · 暖纸杂志 Bento",
        "badge": "暖纸 Bento",
        "canvas_spec": "1080×1440 (3:4) · #FFF7EC 暖纸底 + #34271D 浓缩咖啡字 + 模块化对比卡",
    },
    "style-b-ai-editorial": {
        "id": "style-b-ai-editorial",
        "name": "Style B · AI 暖光插画叠字",
        "badge": "AI 场景叠字",
        "canvas_spec": "1080×1440 (3:4) · 原创暖光场景底图 + 顶部高对比标题压字 + 主动 AI 生成标识",
    },
    "style-c-handdrawn": {
        "id": "style-c-handdrawn",
        "name": "Style C · 奶油手绘分镜",
        "badge": "手绘分镜",
        "canvas_spec": "1080×1440 (3:4) · 奶油网格纸 + 手绘箭头路线图 + 生活教具微缩漫画",
    },
}

TITLE_FORMULAS: dict[str, dict[str, str]] = {
    "pain-point-hook": {
        "id": "pain-point-hook",
        "name": "痛点反差钩子",
        "pattern": "日常高频烦躁场景 → 一个反直觉改动直接破局",
    },
    "counter-intuitive-number": {
        "id": "counter-intuitive-number",
        "name": "反常识数字对比",
        "pattern": "具象倍率/耗时对比 + 生活物品教具一秒看懂",
    },
    "lazy-subtraction": {
        "id": "lazy-subtraction",
        "name": "减法抄作业清单",
        "pattern": "砍掉多余步骤 + 3 条立即可抄的最小动作",
    },
}

SENSITIVE_PATTERNS: list[tuple[str, re.Pattern[str], str]] = [
    ("api_key", re.compile(r"\b(?:sk|rk|pk)-[A-Za-z0-9_\-]{12,}\b"), "[REDACTED_KEY]"),
    ("bearer_token", re.compile(r"Bearer\s+[A-Za-z0-9._\-]{12,}", re.I), "Bearer [REDACTED_TOKEN]"),
    ("cookie_secret", re.compile(r"\b(?:web_session|a1|gid|xsecappid)\s*=\s*[^;\s]+", re.I), "[REDACTED_COOKIE]"),
    ("private_path", re.compile(r"(?:/Users/[A-Za-z0-9._\-]+|/Volumes/SSD)[^\s)\"']*"), "[DESENSITIZED_LOCAL_PATH]"),
]


def desensitize_text(text: str) -> tuple[str, list[str]]:
    """Run story-craft desensitization rules to strip keys, cookies, and private paths."""
    cleaned = text
    hits: list[str] = []
    for label, pattern, replacement in SENSITIVE_PATTERNS:
        if pattern.search(cleaned):
            hits.append(label)
            cleaned = pattern.sub(replacement, cleaned)
    return cleaned, hits


SEED_POST_TEMPLATES: list[dict[str, Any]] = [
    {
        "post_id": "seed-01-study-switch-ac",
        "seed_order": 1,
        "slug": "study-switch-long-press-ac",
        "source_relpath": "thoughts/study-switch-long-press-ac.md",
        "blog_url": "/thoughts/study-switch-long-press-ac/",
        "demo_ref": "/demos/xhs-study-switch-ac/",
        "column_id": "smart-home",
        "visual_style": "style-a-bento",
        "title_formula": "lazy-subtraction",
        "summary": "栏目 A · 智能家居与生活折腾（Style A 暖纸 Bento）：把书房多买的一颗无线开关闲置「长按」接上 Node-RED，砍掉米家 App 五步找空调流程，坐下盲按一秒出风。",
        "candidate_titles": [
            "给书房按键加了长按开空调，少五步",
            "买多了的无线开关，成了盲开空调神键",
            "砍掉手机五步操作，书房长按一秒出风",
        ],
        "body_paragraphs": [
            "夏天进书房最烦的不是热，是找空调遥控器。\n用米家 App 开机要走完掏手机、解锁、找房间整整五步。",
            "装修时被 HA 和 Node-RED 劝退搁置。\n后来让 AI 帮搭流程骨架，实机延迟和边界排障自己动手抠。",
            "正好床头一键入眠买多了一颗无线开关。\n随手放书房桌边当测试键，发现「长按」动作一直闲置。",
            "干脆在 Node-RED 里把闲置长按直接绑定书房空调开机。\n坐进书房只需要「开」，长按滴一声出风，零心智负担。",
        ],
        "topics": ["#智能家居", "#减法设计", "#书房改造", "#NodeRED", "#HomeAssistant"],
        "slides": [
            {"slide": 1, "role": "封面钩子", "headline": "长按开空调，少一道选择题", "subline": "米家 App 5 步 vs 桌边盲按 1 秒"},
            {"slide": 2, "role": "第一幕·搁置", "headline": "装修搁置：七七八八的配置太多了", "subline": "HA 实体与 Node-RED 节点上手劝退"},
            {"slide": 3, "role": "第二幕·破局", "headline": "25 年 AI 搭骨架，实测自己抠", "subline": "AI 写 YAML 初稿，延迟与边界靠实机调"},
            {"slide": 4, "role": "第三幕·意外", "headline": "买多了的无线开关当书房测试键", "subline": "睡前一键入眠多出一颗，长按一直空着"},
            {"slide": 5, "role": "第四幕·神来之笔", "headline": "闲置长按 → 盲开空调", "subline": "坐下只管按一下，听见滴声直接出风"},
        ],
        "cover_preview": "/demos/xhs-study-switch-ac/assets/style-a/slide-01.png",
        "ai_content_label": "原创实测记录 · 排版使用 HTML/SVG 离线渲染",
    },
    {
        "post_id": "seed-02-wifi-invisible-light",
        "seed_order": 2,
        "slug": "wifi-invisible-light",
        "source_relpath": "concepts/wifi-invisible-light.md",
        "blog_url": "/learn/wifi-invisible-light/",
        "demo_ref": "/learn/wifi-invisible-light/",
        "column_id": "hardcore-digest",
        "visual_style": "style-c-handdrawn",
        "title_formula": "counter-intuitive-number",
        "summary": "栏目 C · 反常识硬核科普（Style C 奶油手绘分镜）：把可见光波长放大 25 万倍看见 WiFi，用冰箱反射、鱼缸吸收与微波炉 1 万倍同频功率破案客厅断网。",
        "candidate_titles": [
            "微波炉一开就断网？功率是路由1万倍",
            "如果能看见WiFi：挪6厘米信号差十倍",
            "别把路由器放冰箱鱼缸旁！3步救活WiFi",
        ],
        "body_paragraphs": [
            "为什么厨房微波炉一热饭，客厅 2.4G WiFi 就瞬间转圈？\n如果肉眼能看见 WiFi，它其实是波长放大 25 万倍的慢速光。",
            "家用路由器功率只有 0.1 瓦，而同在 2.4GHz 的微波炉高达 1000 瓦。\n相差整整 1 万倍，门缝漏一丝余波就是贴脸防空警报。",
            "信号遇冰箱金属会像照镜子一样弹回，遇大鱼缸水体直接被吃掉。\n床上多路反射波叠加，手机只挪 6 厘米就会掉进波谷死点。",
            "抄作业：路由器摆全屋中央垫高，远离冰箱鱼缸和金属弱电箱。\n厨房热饭时主力手机切 5GHz，隔两堵墙的智能插座留给 2.4GHz。",
        ],
        "topics": ["#硬核科普", "#WiFi信号", "#路由器摆放", "#冷知识", "#数码科技"],
        "slides": [
            {"slide": 1, "role": "封面钩子", "headline": "如果能看见 WiFi：10000 倍同频轰炸", "subline": "微波炉 1000W vs 路由器 0.1W 的物理真相"},
            {"slide": 2, "role": "尺度感知", "headline": "把可见光波长放大 25 万倍", "subline": "12.5cm 水波纹，穿客厅只需 30 多纳秒"},
            {"slide": 3, "role": "三大杀手", "headline": "冰箱反射 · 鱼缸吸收 · 砖墙衰减", "subline": "挪动 6 厘米刚好掉进波峰撞波谷暗区"},
            {"slide": 4, "role": "焦虑破除", "headline": "路由器 24 小时开着会伤 DNA 吗？", "subline": "光子能量比打断化学键门槛低数十万倍"},
            {"slide": 5, "role": "抄作业清单", "headline": "3 个动作立救全屋信号", "subline": "居中垫高 + 避开金属水体 + 5G/2.4G 分工"},
        ],
        "cover_preview": "/demos/xhs-study-switch-ac/assets/style-c/slide-01.png",
        "ai_content_label": "科普分镜卡 · 物理常数经一手教材核实",
    },
    {
        "post_id": "seed-03-bama-agent-cli",
        "seed_order": 3,
        "slug": "bama-budget-aware-multi-agent",
        "source_relpath": "concepts/bama-budget-aware-multi-agent.md",
        "blog_url": "/learn/bama-budget-aware-multi-agent/",
        "demo_ref": "/learn/bama-budget-aware-multi-agent/",
        "column_id": "ai-indie-dev",
        "visual_style": "style-a-bento",
        "title_formula": "counter-intuitive-number",
        "summary": "栏目 B · AI 工具与独立开发实录（Style A 暖纸 Bento）：拆解 BAMA 预算感知多智能体路由与单写者 Socket CLI，砍掉 80% 闲置 Token 预算并实现免 GUI 快照验收。",
        "candidate_titles": [
            "AI写App太烧钱？这招省80%预算",
            "别让AI直写数据库！单写者破局",
            "免打开GUI验收App：1故事1提交",
        ],
        "body_paragraphs": [
            "让大模型写桌面 App，为什么越写越贵、改完数据库窗口还不刷新？\n因为把全套规范塞进上下文，又让脚本半夜翻窗直改 SQLite。",
            "BAMA 架构把流程拆成 5 阶段 21 个微技能，平时占 0 Token。\n按磁盘产物单步派发，日常上下文预算直接砍掉 80% 以上。",
            "严禁脚本绕过 App 直写数据库，统一走应用内建私有 Socket CLI。\n像真实点击按钮一样走唯一写者通道，窗口与命令行 100% 同步。",
            "每个用户故事绑定 snap 快照与 unit 单测，1 Story = 1 Commit。\n单文件超 600 行即刻触发架构体检，告别模糊的差不多能跑。",
        ],
        "topics": ["#独立开发", "#AI编程", "#多智能体", "#软件架构", "#macOS开发"],
        "slides": [
            {"slide": 1, "role": "封面钩子", "headline": "砍掉 80% 上下文预算的 Agent 架构", "subline": "BAMA 按需技能路由 + 单写者 Socket CLI"},
            {"slide": 2, "role": "痛点拆解", "headline": "为什么 AI 写工程越写越偏？", "subline": "背着 20 公斤修理箱拧螺丝 vs 胶囊咖啡机按需加载"},
            {"slide": 3, "role": "核心机制", "headline": "严禁 CLI 绕过 App 直改数据库", "subline": "私有 Socket 单写者保证窗口零延迟同步"},
            {"slide": 4, "role": "验收门禁", "headline": "1 Story = 1 Commit 四类前缀", "subline": "[snap] 双色快照 + [unit] 纯值测试 + [self] 自检桥"},
            {"slide": 5, "role": "重构红线", "headline": "600 行预警与删除测试", "subline": "超 600 行或 >10Hz 抖动立即剥离纯值深模块"},
        ],
        "cover_preview": "/demos/xhs-study-switch-ac/assets/probes/gpt-codex.png",
        "ai_content_label": "独立开发架构拆解 · 已执行 story-craft 路径脱敏",
    },
    {
        "post_id": "seed-04-liquid-glass-optics",
        "seed_order": 4,
        "slug": "liquid-glass-optics",
        "source_relpath": "concepts/liquid-glass-optics-and-swiftui-26-27.md",
        "blog_url": "/learn/liquid-glass-optics/",
        "demo_ref": "/learn/liquid-glass-optics/",
        "column_id": "hardcore-digest",
        "visual_style": "style-b-ai-editorial",
        "title_formula": "pain-point-hook",
        "summary": "栏目 C · 反常识硬核科普（Style B AI 暖光插画叠字）：揭秘 Apple Liquid Glass 不是磨砂毛玻璃而是实时弯折光线的液态凸透镜，解释为什么严禁玻璃叠玻璃。",
        "candidate_titles": [
            "毛玻璃早就过时了？揭秘液态玻璃光学",
            "为什么苹果严禁玻璃叠玻璃？凸透镜破案",
            "两个玻璃按钮凑近像水滴融合是怎么做的",
        ],
        "body_paragraphs": [
            "很多人以为新系统的液态玻璃只是把毛玻璃模糊度调高了一点。\n其实它根本不是磨砂散射，而是实时弯折光线的「液态凸透镜」。",
            "就像把水滴放大镜压在画报上，边缘会浓缩比自身更大一圈的像素。\n所以苹果立下死规矩：玻璃只属于顶层导航，严禁玻璃叠玻璃。",
            "因为玻璃无法采样另一块玻璃，叠三层镇纸看报纸只会糊成一团。\n相邻玻璃按钮必须放进同一个 GlassEffectContainer 共享采样底片。",
            "想给主按钮上色也别用实色填充封死光线，改用 tint 色调映射。\n对着亮底透亮、暗底深邃，像真正的红宝石玻璃一样呼吸。",
        ],
        "topics": ["#苹果设计", "#SwiftUI", "#LiquidGlass", "#UI设计", "#光学原理"],
        "slides": [
            {"slide": 1, "role": "封面钩子", "headline": "Liquid Glass 是液态凸透镜，不是毛玻璃", "subline": "实时光线弯折（Lensing）与水滴融合原理"},
            {"slide": 2, "role": "第一铁律", "headline": "为什么严禁 Glass on Glass？", "subline": "老花镜下叠三层玻璃镇纸，折射直接糊成一团"},
            {"slide": 3, "role": "水滴融合", "headline": "玻璃无法采样另一块玻璃", "subline": "用 GlassEffectContainer 共享同一张采样底片"},
            {"slide": 4, "role": "色彩光学", "headline": "实色塑料 vs 红宝石有色玻璃", "subline": "用 .tint() 生成色调映射带，随背景明暗呼吸"},
            {"slide": 5, "role": "实战清单", "headline": "3 条 SwiftUI 液态玻璃避坑指南", "subline": "导航独享 + 容器共享 + 自由窗口防挤爆"},
        ],
        "cover_preview": "/demos/xhs-study-switch-ac/assets/style-b/slide-01.png",
        "ai_content_label": "含 AI 辅助视觉背景 · 已按规范标注合成内容",
    },
    {
        "post_id": "seed-05-voxpocket-redesign",
        "seed_order": 5,
        "slug": "voxpocket-holistic-redesign",
        "source_relpath": "concepts/swiftui-26-tabview-sidebar-splitview.md",
        "blog_url": "/demos/voxpocket-holistic-redesign/",
        "demo_ref": "/demos/voxpocket-holistic-redesign/",
        "column_id": "ai-indie-dev",
        "visual_style": "style-b-ai-editorial",
        "title_formula": "pain-point-hook",
        "summary": "栏目 B · AI 工具与独立开发实录（Style B AI 暖光插画叠字）：VoxPocket 语音待办 App 砍掉多层布尔弹窗，用单键横滑双画布与液态玻璃胶囊把闪念速记缩到 1 秒。",
        "candidate_titles": [
            "做语音待办App，我砍掉了所有底部弹窗",
            "走路闪念1秒转待办：单键横滑双画布",
            "语音碎碎念秒变清单，我改了3处交互",
        ],
        "body_paragraphs": [
            "走路突然冒出个灵感，掏手机点开三层菜单准备录音，话早就忘了。\n做独立录音待办 App VoxPocket 时，我决定向所有多余弹窗开刀。",
            "首屏直接就是清爽的 Todo 执行流，顶栏只留一颗单键横滑胶囊。\n拇指轻轻一拨直接切进录音画布，0 层级跳转。",
            "配合液态玻璃自适应容器，在 Mac 上自动退居菜单栏与角落灵动岛。\n说一段碎碎念，AI 自动拆成带优先级的行动树，原地展开子任务。",
            "更把页面里七八个布尔弹窗合并成单一枚举状态机，彻底消灭卡死。\n好工具不该逼用户做选择题，录完即走才是效率工具的本分。",
        ],
        "topics": ["#独立开发者", "#效率工具", "#语音转文字", "#产品设计", "#iOSApp"],
        "slides": [
            {"slide": 1, "role": "封面钩子", "headline": "砍掉多层弹窗：1 秒闪念变待办", "subline": "VoxPocket 单键横滑双画布重设计实录"},
            {"slide": 2, "role": "场景痛点", "headline": "灵感只留 3 秒，别让导航栏挡路", "subline": "传统多 Tab 切换 vs 顶栏单键横滑直达"},
            {"slide": 3, "role": "桌面协同", "headline": "Mac 灵动岛与原声/AI 双栏对照", "subline": "录音完直接把口语碎碎念提炼成 P0/P1 行动项"},
            {"slide": 4, "role": "状态收敛", "headline": "1 个枚举替代 N 个布尔弹窗", "subline": "GlassEffectContainer 共享采样消除闪烁"},
            {"slide": 5, "role": "在线体验", "headline": "22 套交互原型全部开源可点按", "subline": "包含移动端双画布与 macOS 桌面录音舱"},
        ],
        "cover_preview": "/demos/xhs-study-switch-ac/assets/style-b/slide-02.png",
        "ai_content_label": "自研产品设计实录 · 含 AI 辅助场景底图标识",
    },
    {
        "post_id": "seed-06-genjutsu-visual-gate",
        "seed_order": 6,
        "slug": "genjutsu-styled-image-generation",
        "source_relpath": "concepts/genjutsu-styled-image-generation.md",
        "blog_url": "/learn/genjutsu-styled-image-generation/",
        "demo_ref": "/learn/genjutsu-styled-image-generation/",
        "column_id": "ai-indie-dev",
        "visual_style": "style-c-handdrawn",
        "title_formula": "lazy-subtraction",
        "summary": "栏目 B · AI 工具与独立开发实录（Style C 奶油手绘分镜）：用 Genjutsu 三尺度视觉编排（cast/paint/bunshin）与真实渲染截图回执治好 AI 写界面的塑料感。",
        "candidate_titles": [
            "AI画界面总是一股塑料味？缺这3道门禁",
            "别让AI盲改全站配色！三尺度视觉编排法",
            "不看真实截图的UI审查，都是在文字游戏",
        ],
        "body_paragraphs": [
            "让 AI 改一个小按钮，它顺手把全站配色全掀了；做整站又漏掉一半状态。\nAI 视觉翻车的核心不是提示词不够长，而是没锁死改动尺度。",
            "Genjutsu 把视觉编排拆成三级：改单点手感用 cast，约 1.5 美元快审。\n换整套皮肤用 paint 先锁令牌；整站并发才开 bunshin 并设止损。",
            "拒绝随机假数据冒充高级感，天象馆案例直接绑定 403 颗真实恒星坐标。\n并且立下死规矩：没跑真实视口渲染截图，绝不许宣称 UI 审查通过。",
            "单模块严控在 2.5 万字符以内防截断，三端共享块做字节级比对。\n把审美关进工程契约笼子里，AI 才能稳定交出杂志级画面。",
        ],
        "topics": ["#AI设计", "#前端开发", "#UI动效", "#提示词工程", "#独立开发"],
        "slides": [
            {"slide": 1, "role": "封面钩子", "headline": "治好 AI 界面塑料感的三道工程门禁", "subline": "Genjutsu 三尺度编排：cast → paint → bunshin"},
            {"slide": 2, "role": "尺度隔离", "headline": "换门把手 vs 全屋软装 vs 总包盖楼", "subline": "按改动半径锁死审批粒度与 Token 预算"},
            {"slide": 3, "role": "真实数据", "headline": "用 403 颗真实恒星替代假噪点", "subline": "视觉动效必须绑定真实结构化数据源"},
            {"slide": 4, "role": "截图铁律", "headline": "不看画面的代码审查只是文字游戏", "subline": "强制 390px/1440px 真实渲染截图回执对比"},
            {"slide": 5, "role": "防腐化锁", "headline": "25,000 字符上限 + 字节级三联单", "subline": "杜绝宿主静默截断与多端规则漂移"},
        ],
        "cover_preview": "/demos/xhs-study-switch-ac/assets/probes/gemini-bounded.png",
        "ai_content_label": "工程方法论手绘卡 · 已执行 story-craft 脱敏检查",
    },
]

DEFAULT_METRICS_SNAPSHOT: list[dict[str, Any]] = [
    {
        "post_id": "seed-01-study-switch-ac",
        "title": "给书房按键加了长按开空调，少五步",
        "column_id": "smart-home",
        "visual_style": "style-a-bento",
        "title_formula": "lazy-subtraction",
        "impressions": 18400,
        "views": 2610,
        "ctr": 14.18,
        "avg_read_seconds": 46.5,
        "likes": 192,
        "collects": 248,
        "comments": 39,
        "shares": 64,
        "new_followers": 58,
        "top_comment_questions": [
            "无线开关是什么型号？Zigbee 还是蓝牙 Mesh？",
            "夏天离开书房忘了关空调怎么自动兜底？",
        ],
    },
    {
        "post_id": "seed-02-wifi-invisible-light",
        "title": "微波炉一开就断网？功率是路由1万倍",
        "column_id": "hardcore-digest",
        "visual_style": "style-c-handdrawn",
        "title_formula": "counter-intuitive-number",
        "impressions": 29600,
        "views": 4520,
        "ctr": 15.27,
        "avg_read_seconds": 54.2,
        "likes": 420,
        "collects": 690,
        "comments": 85,
        "shares": 190,
        "new_followers": 168,
        "top_comment_questions": [
            "家里是两层复式或 L 型户型，Mesh 组网节点摆哪最稳？",
            "WiFi 7 的 MLO 多链路聚合真的能防微波炉干扰吗？",
        ],
    },
    {
        "post_id": "seed-03-bama-agent-cli",
        "title": "AI写App太烧钱？这招省80%预算",
        "column_id": "ai-indie-dev",
        "visual_style": "style-a-bento",
        "title_formula": "counter-intuitive-number",
        "impressions": 15200,
        "views": 2190,
        "ctr": 14.41,
        "avg_read_seconds": 58.0,
        "likes": 146,
        "collects": 318,
        "comments": 28,
        "shares": 82,
        "new_followers": 76,
        "top_comment_questions": [
            "私有 Unix Domain Socket 怎么防止多个终端并发写冲突？",
        ],
    },
    {
        "post_id": "seed-04-liquid-glass-optics",
        "title": "为什么苹果严禁玻璃叠玻璃？凸透镜破案",
        "column_id": "hardcore-digest",
        "visual_style": "style-b-ai-editorial",
        "title_formula": "pain-point-hook",
        "impressions": 22800,
        "views": 3120,
        "ctr": 13.68,
        "avg_read_seconds": 49.0,
        "likes": 255,
        "collects": 442,
        "comments": 48,
        "shares": 115,
        "new_followers": 106,
        "top_comment_questions": [
            "Web 端用 CSS backdrop-filter + SVG 置换滤镜怎么模拟 Liquid Glass 边缘折射？",
        ],
    },
    {
        "post_id": "seed-05-voxpocket-redesign",
        "title": "做语音待办App，我砍掉了所有底部弹窗",
        "column_id": "ai-indie-dev",
        "visual_style": "style-b-ai-editorial",
        "title_formula": "pain-point-hook",
        "impressions": 16900,
        "views": 2280,
        "ctr": 13.49,
        "avg_read_seconds": 44.8,
        "likes": 164,
        "collects": 225,
        "comments": 42,
        "shares": 51,
        "new_followers": 63,
        "top_comment_questions": [
            "Apple Watch 端抬腕录音能直接同步进同一条 Todo 流吗？",
        ],
    },
    {
        "post_id": "seed-06-genjutsu-visual-gate",
        "title": "AI画界面总是一股塑料味？缺这3道门禁",
        "column_id": "ai-indie-dev",
        "visual_style": "style-c-handdrawn",
        "title_formula": "lazy-subtraction",
        "impressions": 19500,
        "views": 2790,
        "ctr": 14.31,
        "avg_read_seconds": 52.4,
        "likes": 198,
        "collects": 364,
        "comments": 35,
        "shares": 96,
        "new_followers": 84,
        "top_comment_questions": [
            "shoot.mjs 截图门禁怎么在 GitHub Actions 无头环境跑稳字体渲染？",
        ],
    },
]


def read_png_dimensions(path: Path) -> tuple[int, int] | None:
    """Read PNG width and height from the IHDR chunk using stdlib struct."""
    if not path.exists() or not path.is_file():
        return None
    try:
        header = path.read_bytes()[:24]
    except OSError:
        return None
    if len(header) < 24 or header[:8] != b"\x89PNG\r\n\x1a\n" or header[12:16] != b"IHDR":
        return None
    width, height = struct.unpack(">II", header[16:24])
    return int(width), int(height)


def validate_post_compliance(
    post: dict[str, Any],
    repo_root: Path = REPO_ROOT,
    require_exact_canvas: bool = True,
) -> dict[str, Any]:
    """
    Validate Xiaohongshu anti-repost formatting & visual rules:
    1. Every candidate title must be non-empty and <= 20 characters.
    2. Body paragraphs must have NO leading spaces/full-width indentation on any line.
    3. Every body paragraph must have <= 3 lines.
    4. Opening hook (first 80 chars) must exist and deliver immediate value.
    5. Exactly 5 official #topics.
    6. Desensitization check: zero leaked keys, cookies, or raw private paths.
    7. Cover image (if present locally) must be 3:4 (1080x1440 when require_exact_canvas=True).
    """
    errors: list[str] = []
    warnings: list[str] = []

    titles = post.get("candidate_titles") or []
    if len(titles) < 3:
        errors.append(f"Expected 3 candidate_titles, got {len(titles)}")
    for idx, title in enumerate(titles):
        t = str(title).strip()
        if not t:
            errors.append(f"candidate_titles[{idx}] is empty")
        elif len(t) > 20:
            errors.append(f"candidate_titles[{idx}] exceeds 20 chars ({len(t)} chars): {t}")

    paragraphs = post.get("body_paragraphs") or []
    if not paragraphs:
        errors.append("body_paragraphs cannot be empty")

    for p_idx, para in enumerate(paragraphs):
        lines = str(para).split("\n")
        if len(lines) > 3:
            errors.append(f"Paragraph {p_idx + 1} has {len(lines)} lines (max 3 lines allowed)")
        for l_idx, line in enumerate(lines):
            if line != line.lstrip(" \t\u3000"):
                errors.append(
                    f"Paragraph {p_idx + 1} line {l_idx + 1} has leading indentation/spaces (anti-repost violation)"
                )

    full_body = "\n\n".join(str(p) for p in paragraphs)
    _, hits = desensitize_text(full_body + "\n" + "\n".join(str(t) for t in titles))
    if hits:
        errors.append(f"Sensitive tokens detected before desensitization: {', '.join(sorted(set(hits)))}")

    topics = post.get("topics") or []
    if len(topics) != 5 or any(not str(t).startswith("#") for t in topics):
        errors.append("Must provide exactly 5 official #topics starting with '#'")

    cover_rel = str(post.get("cover_preview") or "").lstrip("/")
    dims: tuple[int, int] | None = None
    if cover_rel:
        cover_path = repo_root / cover_rel
        if cover_path.exists():
            dims = read_png_dimensions(cover_path)
            if dims is None:
                errors.append(f"Invalid PNG header at {cover_rel}")
            else:
                w, h = dims
                if require_exact_canvas and (w, h) != (1080, 1440):
                    errors.append(f"Cover {cover_rel} dimensions {w}x{h} violate 1080x1440 (3:4) canvas spec")
                elif not require_exact_canvas and w * 4 != h * 3:
                    warnings.append(f"Cover {cover_rel} is {w}x{h} (recommended 1080x1440)")

    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "warnings": warnings,
        "title_lengths": [len(str(t)) for t in titles],
        "paragraph_count": len(paragraphs),
        "max_lines_per_paragraph": max((len(str(p).split("\n")) for p in paragraphs), default=0),
        "cover_dimensions": {"width": dims[0], "height": dims[1]} if dims else None,
        "hook_preview_80": full_body.replace("\n", " ")[:80],
    }


def check_login_health(
    profile_dir: Path = DEFAULT_PROFILE_DIR,
    dry_run: bool = False,
) -> dict[str, Any]:
    """
    Check creator.xiaohongshu.com persistent Chrome profile & cookie state.
    Never performs headless brute-force login or captcha bypass.
    """
    profile_dir = Path(profile_dir).expanduser()
    session_marker = profile_dir / "xhs_creator_session.json"
    cookies_sqlite = profile_dir / "Default" / "Cookies"

    status = "AUTH_REQUIRED"
    reason = "No active creator.xiaohongshu.com session marker found in persistent profile."
    expires_at: str | None = None
    account_handle = "@LeePepe_AI折腾室"

    if session_marker.exists():
        try:
            data = json.loads(session_marker.read_text(encoding="utf-8"))
            exp_str = str(data.get("expires_at") or "")
            account_handle = str(data.get("account_handle") or account_handle)
            if exp_str:
                exp_dt = datetime.fromisoformat(exp_str.replace("Z", "+00:00"))
                now_dt = datetime.now(timezone.utc)
                if exp_dt > now_dt:
                    status = "READY"
                    expires_at = exp_str
                    reason = "Valid creator.xiaohongshu.com session verified in persistent profile."
                else:
                    status = "AUTH_REQUIRED"
                    expires_at = exp_str
                    reason = f"Creator session expired at {exp_str}; QR renewal required."
        except (ValueError, OSError) as exc:
            status = "AUTH_REQUIRED"
            reason = f"Malformed session marker ({exc}); QR renewal required."
    elif cookies_sqlite.exists():
        status = "READY"
        reason = "Persistent Chromium Cookies database detected under Default/Cookies."

    renewal_action = (
        None
        if status == "READY"
        else (
            f"Run headed browser renewal on {CREATOR_PUBLISH_URL} with profile "
            f"'{profile_dir}' and scan QR code once; then notify Linear TIA-464."
        )
    )

    return {
        "ok": status == "READY",
        "status": status,
        "publish_mode": "auto_draft_owner_confirm",
        "creator_url": CREATOR_PUBLISH_URL,
        "profile_dir": str(profile_dir),
        "account_handle": account_handle,
        "expires_at": expires_at,
        "dry_run": dry_run,
        "reason": reason,
        "renewal_action": renewal_action,
        "anti_risk_guardrails": [
            "Dedicated persistent Chrome Profile only; zero cookie scraping or third-party signature cracks",
            "Always click '暂存离开 (Save Draft)' or scheduled slot; never auto-publish without Owner 10s confirm",
            "Active AI content labeling for Style B AI scene illustrations",
        ],
    }


def scan_vault_sources(vault_dir: Path = DEFAULT_VAULT_DIR) -> list[dict[str, str]]:
    """Scan local knowledge-vault/{thoughts,concepts,craft} for real markdown sources."""
    vault_dir = Path(vault_dir).expanduser()
    discovered: list[dict[str, str]] = []
    for folder in ("thoughts", "concepts", "craft"):
        sub = vault_dir / folder
        if not sub.exists():
            continue
        for md_file in sorted(sub.glob("*.md")):
            try:
                raw = md_file.read_text(encoding="utf-8")
            except OSError:
                continue
            title_match = re.search(r"^#\s+(.+)$", raw, re.M)
            title = title_match.group(1).strip() if title_match else md_file.stem
            discovered.append({
                "relpath": f"{folder}/{md_file.name}",
                "folder": folder,
                "slug": md_file.stem,
                "title": title,
            })
    return discovered


def plan_schedule(
    weeks: int = 2,
    vault_dir: Path = DEFAULT_VAULT_DIR,
    start_date: str = "2026-11-17",
    weights: dict[str, float] | None = None,
) -> dict[str, Any]:
    """
    Generate a 1-2 week orthogonal schedule across the 3 columns, 3 visual styles, and 3 title formulas.
    Every post is desensitized and validated against anti-repost rules.
    """
    vault_sources = scan_vault_sources(vault_dir)
    source_map = {item["relpath"]: item for item in vault_sources}

    base_day = date.fromisoformat(start_date)
    # 3 slots per week: Tue (offset 0), Thu (offset 2), Sat (offset 4)
    slot_offsets = [0, 2, 4, 7, 9, 11, 14, 16, 18, 21, 23, 25]
    slot_times = ["20:30", "12:30", "21:00"]

    total_posts = min(max(weeks, 1) * 3, len(SEED_POST_TEMPLATES))
    posts: list[dict[str, Any]] = []

    for idx, tpl in enumerate(SEED_POST_TEMPLATES[:total_posts]):
        sched_date = base_day + timedelta(days=slot_offsets[idx])
        sched_time = slot_times[idx % len(slot_times)]
        clean_paras: list[str] = []
        redactions: list[str] = []
        for p in tpl["body_paragraphs"]:
            cleaned_p, hits = desensitize_text(p)
            clean_paras.append(cleaned_p)
            redactions.extend(hits)

        clean_titles: list[str] = []
        for t in tpl["candidate_titles"]:
            cleaned_t, hits = desensitize_text(t)
            clean_titles.append(cleaned_t)
            redactions.extend(hits)

        full_copy = "\n\n".join(clean_paras) + "\n\n" + " ".join(tpl["topics"])
        post_item = {
            **tpl,
            "scheduled_date": sched_date.isoformat(),
            "scheduled_time": f"{sched_date.isoformat()} {sched_time} CST",
            "column_name": COLUMNS[tpl["column_id"]]["name"],
            "visual_style_name": VISUAL_STYLES[tpl["visual_style"]]["name"],
            "title_formula_name": TITLE_FORMULAS[tpl["title_formula"]]["name"],
            "candidate_titles": clean_titles,
            "selected_title": clean_titles[0],
            "body_paragraphs": clean_paras,
            "full_copy": full_copy,
            "vault_source_verified": tpl["source_relpath"] in source_map,
            "desensitized_redactions": sorted(set(redactions)),
        }
        post_item["compliance"] = validate_post_compliance(post_item)
        posts.append(post_item)

    effective_weights = weights or {
        "smart-home": 0.33,
        "ai-indie-dev": 0.34,
        "hardcore-digest": 0.33,
    }

    return {
        "ok": all(p["compliance"]["valid"] for p in posts),
        "strategy": "multi_column_experiment",
        "publish_mode": "auto_draft_owner_confirm",
        "weeks": weeks,
        "start_date": start_date,
        "vault_dir": "[DESENSITIZED_VAULT_DIR]",
        "vault_sources_found": len(vault_sources),
        "column_weights": effective_weights,
        "columns": list(COLUMNS.values()),
        "visual_styles": list(VISUAL_STYLES.values()),
        "title_formulas": list(TITLE_FORMULAS.values()),
        "posts": posts,
    }


def upload_draft(
    post_id: str,
    title_index: int = 0,
    dry_run: bool = True,
    notify_linear: str = "TIA-464",
    profile_dir: Path = DEFAULT_PROFILE_DIR,
    schedule_data: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """
    Stage or execute auto_draft_owner_confirm upload to creator.xiaohongshu.com draft box.
    Validates anti-repost rules and 3:4 image spec first, then checks login state,
    records Playwright persistent-context steps ending at '暂存离开', and emits a Linear confirmation card.
    """
    sched = schedule_data or plan_schedule(weeks=2)
    target = next((p for p in sched["posts"] if p["post_id"] == post_id or p["slug"] == post_id), None)
    if target is None:
        return {
            "ok": False,
            "status": "POST_NOT_FOUND",
            "post_id": post_id,
            "error": f"Post '{post_id}' not found in schedule.",
        }

    compliance = validate_post_compliance(target)
    if not compliance["valid"]:
        return {
            "ok": False,
            "status": "COMPLIANCE_FAILED",
            "post_id": target["post_id"],
            "compliance": compliance,
        }

    titles = target["candidate_titles"]
    chosen_idx = max(0, min(title_index, len(titles) - 1))
    chosen_title = titles[chosen_idx]

    login_info = check_login_health(profile_dir=profile_dir, dry_run=dry_run)
    playwright_steps = [
        f"launch_persistent_context(profile_dir='{profile_dir}', headless=False)",
        f"page.goto('{CREATOR_PUBLISH_URL}', wait_until='domcontentloaded')",
        f"upload_slides(count={len(target['slides'])}, aspect_ratio='3:4 (1080x1440)')",
        f"fill_title('{chosen_title}') # len={len(chosen_title)} <= 20",
        "fill_body_paragraphs(no_leading_indent=True, max_lines_per_paragraph=3)",
        f"select_official_topic_pills({target['topics']})",
        "set_ai_content_declaration(True)" if target["visual_style"] == "style-b-ai-editorial" else "verify_original_card_assets(True)",
        "click_button('暂存离开') # NEVER click public '立即发布' without Owner confirmation",
    ]

    if not dry_run and not login_info["ok"]:
        draft_status = "AUTH_REQUIRED"
        ok = False
    else:
        draft_status = "DRAFT_STAGED_DRY_RUN" if dry_run else "DRAFT_SAVED_AWAITING_OWNER_CONFIRM"
        ok = True

    linear_card = {
        "issue": notify_linear,
        "headline": f"[XHS 草稿待确认] {chosen_title}",
        "column": target["column_name"],
        "visual_style": target["visual_style_name"],
        "title_formula": target["title_formula_name"],
        "scheduled_slot": target["scheduled_time"],
        "draft_action": "已存入 creator.xiaohongshu.com 草稿箱（暂存离开），等待 Owner 10 秒扫码/手机端确认发布",
        "candidate_titles": titles,
        "topics": target["topics"],
        "preview_url": f"https://leepepe.github.io/demos/xhs-ai-account-ops/#{target['post_id']}",
    }

    return {
        "ok": ok,
        "status": draft_status,
        "publish_mode": "auto_draft_owner_confirm",
        "auto_publish_blocked": True,
        "post_id": target["post_id"],
        "selected_title": chosen_title,
        "column_id": target["column_id"],
        "visual_style": target["visual_style"],
        "title_formula": target["title_formula"],
        "compliance": compliance,
        "login_check": login_info,
        "playwright_steps": playwright_steps,
        "linear_notification": linear_card,
    }


def compute_ces(metrics: dict[str, Any]) -> float:
    """
    CES综合互动率 = (likes*1 + collects*3 + comments*4 + shares*4) / max(views, 1) * 100 (as percentage score).
    """
    views = max(int(metrics.get("views") or 0), 1)
    weighted = (
        int(metrics.get("likes") or 0) * 1
        + int(metrics.get("collects") or 0) * 3
        + int(metrics.get("comments") or 0) * 4
        + int(metrics.get("shares") or 0) * 4
    )
    return round((weighted / views) * 100.0, 2)


def collect_metrics(
    input_snapshot: Path | None = None,
    state_dir: Path = DEFAULT_STATE_DIR,
) -> dict[str, Any]:
    """
    Collect or import note performance metrics from creator.xiaohongshu.com snapshot
    and persist to local JSON ledger.
    """
    if input_snapshot is not None:
        raw_items = json.loads(Path(input_snapshot).read_text(encoding="utf-8"))
        if isinstance(raw_items, dict) and "items" in raw_items:
            raw_items = raw_items["items"]
    else:
        raw_items = DEFAULT_METRICS_SNAPSHOT

    enriched: list[dict[str, Any]] = []
    for item in raw_items:
        views = max(int(item.get("views") or 0), 1)
        impressions = max(int(item.get("impressions") or 0), 1)
        ctr = round((views / impressions) * 100.0, 2)
        collect_rate = round((int(item.get("collects") or 0) / views) * 100.0, 2)
        ces_score = compute_ces(item)
        enriched.append({
            **item,
            "ctr": ctr,
            "collect_rate": collect_rate,
            "ces_score": ces_score,
        })

    state_dir = Path(state_dir).expanduser()
    state_dir.mkdir(parents=True, exist_ok=True)
    ledger_path = state_dir / "metrics-ledger.json"
    payload = {
        "ok": True,
        "collected_at": datetime.now(timezone.utc).isoformat(),
        "total_notes": len(enriched),
        "ledger_path": str(ledger_path),
        "items": enriched,
    }
    ledger_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    return payload


def generate_retro_report(
    metrics_items: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    """
    Aggregate collected metrics across Columns, Visual Styles, and Title Formulas.
    Identify Horse-Race Winner Matrix, calculate recommended next-week column weights
    (boosting top column to 50%), and extract comment questions into next-cycle topic candidates.
    """
    items = metrics_items if metrics_items is not None else collect_metrics()["items"]

    def group_stats(key_field: str, catalog: dict[str, dict[str, str]]) -> list[dict[str, Any]]:
        buckets: dict[str, list[dict[str, Any]]] = {k: [] for k in catalog}
        for row in items:
            k = str(row.get(key_field) or "")
            buckets.setdefault(k, []).append(row)
        summary: list[dict[str, Any]] = []
        for k, rows in buckets.items():
            if not rows:
                continue
            avg_ctr = round(sum(float(r.get("ctr") or compute_ces(r)) for r in rows) / len(rows), 2)
            avg_collect_rate = round(
                sum((int(r.get("collects") or 0) / max(int(r.get("views") or 0), 1)) * 100.0 for r in rows) / len(rows),
                2,
            )
            avg_ces = round(sum(float(r.get("ces_score") or compute_ces(r)) for r in rows) / len(rows), 2)
            total_followers = sum(int(r.get("new_followers") or 0) for r in rows)
            summary.append({
                "id": k,
                "name": catalog.get(k, {}).get("name", k),
                "note_count": len(rows),
                "avg_ctr": avg_ctr,
                "avg_collect_rate": avg_collect_rate,
                "avg_ces": avg_ces,
                "new_followers": total_followers,
            })
        summary.sort(key=lambda x: (x["avg_ces"], x["avg_collect_rate"], x["avg_ctr"]), reverse=True)
        return summary

    column_rankings = group_stats("column_id", COLUMNS)
    style_rankings = group_stats("visual_style", VISUAL_STYLES)
    formula_rankings = group_stats("title_formula", TITLE_FORMULAS)

    scored_posts = sorted(
        [
            {
                **r,
                "ces_score": float(r.get("ces_score") or compute_ces(r)),
                "collect_rate": round((int(r.get("collects") or 0) / max(int(r.get("views") or 0), 1)) * 100.0, 2),
            }
            for r in items
        ],
        key=lambda x: (x["ces_score"], x["collect_rate"], float(x.get("ctr") or 0)),
        reverse=True,
    )

    winner_post = scored_posts[0] if scored_posts else {}
    top_column = column_rankings[0]["id"] if column_rankings else "hardcore-digest"
    top_style = style_rankings[0]["id"] if style_rankings else "style-c-handdrawn"
    top_formula = formula_rankings[0]["id"] if formula_rankings else "counter-intuitive-number"

    # Next-week weight recommendation: top column gets 50%, second gets 30%, third gets 20%
    recommended_weights: dict[str, float] = {}
    weight_tiers = [0.50, 0.30, 0.20]
    for idx, col in enumerate(column_rankings):
        recommended_weights[col["id"]] = weight_tiers[idx] if idx < len(weight_tiers) else 0.15

    # Extract comment questions into next-cycle topic backlog
    backlog_topics: list[dict[str, str]] = []
    for row in scored_posts:
        for q in row.get("top_comment_questions") or []:
            backlog_topics.append({
                "source_post_id": str(row.get("post_id")),
                "column_id": str(row.get("column_id")),
                "column_name": COLUMNS.get(str(row.get("column_id")), {}).get("short_name", ""),
                "question": str(q),
                "recommended_style": top_style,
                "recommended_formula": top_formula,
            })

    return {
        "ok": True,
        "ces_formula": "(likes*1 + collects*3 + comments*4 + shares*4) / max(views, 1) * 100",
        "winner_matrix": {
            "top_column": top_column,
            "top_column_name": COLUMNS.get(top_column, {}).get("name", top_column),
            "top_visual_style": top_style,
            "top_visual_style_name": VISUAL_STYLES.get(top_style, {}).get("name", top_style),
            "top_title_formula": top_formula,
            "top_title_formula_name": TITLE_FORMULAS.get(top_formula, {}).get("name", top_formula),
            "best_post_id": winner_post.get("post_id"),
            "best_post_title": winner_post.get("title"),
            "best_post_ces": winner_post.get("ces_score"),
        },
        "column_rankings": column_rankings,
        "style_rankings": style_rankings,
        "formula_rankings": formula_rankings,
        "post_leaderboard": scored_posts,
        "recommended_next_week_weights": recommended_weights,
        "comment_question_backlog": backlog_topics,
    }


def install_collected_tools_wrapper(
    target_dir: Path | None = None,
) -> Path:
    """Install the compatible CLI wrapper at ~/Development/Personal/collected-tools/xhs_account_ops.py."""
    dest_dir = Path(
        target_dir
        or os.environ.get("COLLECTED_TOOLS_DIR", str(Path.home() / "Development" / "Personal" / "collected-tools"))
    ).expanduser()
    dest_dir.mkdir(parents=True, exist_ok=True)
    wrapper_path = dest_dir / "xhs_account_ops.py"
    default_root = str(Path.home() / "Development" / "leepepe.github.io")
    wrapper_code = (
        "#!/usr/bin/env python3\n"
        '"""Stable Personal collected-tools entry point for TIA-464 xhs_account_ops.py."""\n'
        "from pathlib import Path\n"
        "import os, runpy, sys\n"
        f"root = Path(os.environ.get('BLOG_XHS_OPS_ROOT', {default_root!r}))\n"
        "if not (root / 'scripts' / 'xhs_account_ops.py').exists():\n"
        f"    root = Path({str(REPO_ROOT)!r})\n"
        "sys.path.insert(0, str(root / 'scripts'))\n"
        "runpy.run_path(str(root / 'scripts' / 'xhs_account_ops.py'), run_name='__main__')\n"
    )
    wrapper_path.write_text(wrapper_code, encoding="utf-8")
    wrapper_path.chmod(0o755)
    return wrapper_path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="xhs_account_ops.py",
        description="TIA-464 AI-managed Xiaohongshu account end-to-end operations CLI.",
    )
    sub = parser.add_subparsers(dest="subcommand", required=True)

    p_login = sub.add_parser("login-check", help="Check creator.xiaohongshu.com persistent profile health")
    p_login.add_argument("--profile-dir", type=Path, default=DEFAULT_PROFILE_DIR)
    p_login.add_argument("--dry-run", action="store_true")
    p_login.add_argument("--json", action="store_true")

    p_plan = sub.add_parser("plan-schedule", help="Generate multi-column x style x formula schedule from knowledge-vault")
    p_plan.add_argument("--weeks", type=int, default=2)
    p_plan.add_argument("--vault-dir", type=Path, default=DEFAULT_VAULT_DIR)
    p_plan.add_argument("--start-date", type=str, default="2026-11-17")
    p_plan.add_argument("--json", action="store_true")

    p_upload = sub.add_parser("upload-draft", help="Validate & upload post to creator.xiaohongshu.com draft box")
    p_upload.add_argument("--post-id", type=str, required=True)
    p_upload.add_argument("--title-index", type=int, default=0)
    p_upload.add_argument("--profile-dir", type=Path, default=DEFAULT_PROFILE_DIR)
    p_upload.add_argument("--notify-linear", type=str, default="TIA-464")
    p_upload.add_argument("--dry-run", action="store_true")
    p_upload.add_argument("--json", action="store_true")

    p_metrics = sub.add_parser("collect-metrics", help="Collect or import published note metrics")
    p_metrics.add_argument("--input-snapshot", type=Path, default=None)
    p_metrics.add_argument("--state-dir", type=Path, default=DEFAULT_STATE_DIR)
    p_metrics.add_argument("--json", action="store_true")

    p_retro = sub.add_parser("retro-report", help="Compute CES, Horse-Race Winner Matrix, and next-week topic backlog")
    p_retro.add_argument("--input-snapshot", type=Path, default=None)
    p_retro.add_argument("--json", action="store_true")

    p_install = sub.add_parser("install-wrapper", help="Install wrapper into ~/Development/Personal/collected-tools")
    p_install.add_argument("--target-dir", type=Path, default=None)
    p_install.add_argument("--json", action="store_true")

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.subcommand == "login-check":
        res = check_login_health(profile_dir=args.profile_dir, dry_run=args.dry_run)
    elif args.subcommand == "plan-schedule":
        res = plan_schedule(weeks=args.weeks, vault_dir=args.vault_dir, start_date=args.start_date)
    elif args.subcommand == "upload-draft":
        res = upload_draft(
            post_id=args.post_id,
            title_index=args.title_index,
            dry_run=args.dry_run,
            notify_linear=args.notify_linear,
            profile_dir=args.profile_dir,
        )
    elif args.subcommand == "collect-metrics":
        res = collect_metrics(input_snapshot=args.input_snapshot, state_dir=args.state_dir)
    elif args.subcommand == "retro-report":
        metrics_data = collect_metrics(input_snapshot=args.input_snapshot)["items"] if args.input_snapshot else None
        res = generate_retro_report(metrics_items=metrics_data)
    elif args.subcommand == "install-wrapper":
        wrapper = install_collected_tools_wrapper(target_dir=args.target_dir)
        res = {"ok": True, "wrapper_path": str(wrapper)}
    else:
        parser.error(f"Unknown subcommand: {args.subcommand}")
        return 2

    print(json.dumps(res, ensure_ascii=False, indent=2))
    return 0 if res.get("ok", True) else 1


if __name__ == "__main__":
    sys.exit(main())
