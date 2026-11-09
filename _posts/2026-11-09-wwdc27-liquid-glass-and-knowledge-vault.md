---
layout: post
title: "直击痛点的求知笔记：WWDC 25/26 (OS 26 → OS 27) Liquid Glass、动效管线与硬核科普专栏上线"
date: 2026-11-09
categories: apple swiftui wwdc knowledge-vault
permalink: /learn/wwdc27-and-knowledge-vault-launch/
---

把最近沉淀在 **Personal Knowledge Vault** 里的 **WWDC 25/26 (OS 26 → OS 27) Liquid Glass 与动效全系列（8 节核心课精华）** 以及 **「如果能看见 WiFi」标杆科普拆解** 整理成了全新的独立阅读专栏：

👉 **[立即进入 `/learn/` 专栏阅读器：直击痛点的求知笔记](/learn/)**

---

## 为什么做这个专栏？

看技术视频或硬核科普时，最怕按教材目录记流水账，过两周全忘光。这个专栏里的每一篇卡片都严格遵循同一套**「认知破案闭环」**：

1. **⚡ 一句话本质（TL;DR）**：先抛反常识结论与量级数字，3 秒立住全局坐标系；
2. **🎯 核心痛点直答（Pain-Point Q&A）**：用透镜、三通水管、穿孔图钉、冰箱与鱼缸等日常物理教具替代枯燥公式，直击工程与生活中的真问题；
3. **✅ 立即可用清单（Actionable Checklist）**：收敛为 ≤3 条马上能照着改代码的实操处方；
4. **🎬 叙事与表达技法（Craft）**：拆解苹果工程师与顶级科普作者是怎么把复杂概念“讲人话”的。

---

## 专栏 7 篇完整文章直达

### 🍎 专题一：WWDC 25/26 (OS 26 → OS 27) Liquid Glass 与动效（8 节课精华）

1. **[01 · WWDC25/26 (OS 26 → OS 27) Liquid Glass 与动效 8 节课全景导读地图](/learn/wwdc27-glass-motion/)**
   - 把 UI 彻底拆成「顶层液态光学控制层（Liquid Glass）」与「底层全画幅内容流（Pipeline）」——含 8 节课寻宝表、OS 26→27 进化对照与 10 分钟按需切入指南。
2. **[02 · Liquid Glass 光学第一性原理与 SwiftUI 26→27 实战破案](/learn/liquid-glass-optics/)**
   - 为什么 Liquid Glass 是实时弯折光线的「液态凸透镜（Lensing）」而非磨砂毛玻璃？为什么严禁玻璃叠玻璃？详解 `GlassEffectContainer` 共享采样区、有色玻璃映射、Toolbar 三级防挤爆与 `@State` Macro。
3. **[03 · SwiftUI 27 高级图形与动效管线：Metal Shader 扭曲、时间流与图钉对齐](/learn/swiftui-shader-pipeline/)**
   - 拆解 Apple Music 级流体封面与实时歌词：`colorEffect / distortionEffect / layerEffect` 选型、Domain Warping 二次噪声采样、`TimelineView` 时间流注入，以及 `.alignmentGuide(.bottom) { $0[.top] }` 图钉孔位反转法。
4. **[04 · SwiftUI 27 高性能滚动与多元素拖拽：LazyStack 帧预取与纸牌级重排](/learn/swiftui-scroll-drag/)**
   - 揪出 `LazyVStack` 叶子视图 `if` 过滤导致内存暴涨、`onAppear` 废掉帧间预取（Prefetching）三大掉帧元凶；用 `.reorderContainer` + `.dragContainer` + `.dropConfiguration` 实现纸牌接龙级成叠拖拽与非法弹回。
5. **[05 · macOS 27 AppKit 与 iOS 27 UIKit 现代化：自由缩放窗口、同心圆角与手势革命](/learn/appkit-uikit-27/)**
   - iOS 27 让 iPhone 窗口在 Mac 镜像与 iPad 上全面支持自由拖拽缩放（`UIScreen.main`、`idiom` 与 `orientation` 彻底失效）；macOS 27 AppKit 全面转向手势识别器、`NSControl.Events` 与 `NSView.cornerConfiguration` 同心圆角。

### 🎬 专题二：叙事与表达技法（好内容是怎么讲懂的）

6. **[06 · WWDC 视觉化与架构讲法拆解：水管数据流、图钉几何与贴纸叙事法](/learn/wwdc-storytelling-craft/)**
   - 提炼 6 节高分 WWDC 动效课的 8 步剧本骨架：先拿迷你玩具（贴纸本/折纸/纸牌）当靶子，用物理教具替掉数学公式，故意展示直觉写法翻车，再用 2 行代码完成画面质变。

### 📡 专题三：物理与硬件（看不见的世界可视化）

7. **[07 · 如果能看见 WiFi：看不见的光、室内信号破案与科普脚本技法](/learn/wifi-invisible-light/)**
   - 把可见光波长放大 25 万倍，穿过客厅只需 30 多纳秒——用冰箱反射、鱼缸吸收、微波炉 1 万倍同频干扰破案室内断网，并附「把不可见变成可见」九步科普脚本拆解。

---

## WWDC 25/26 8 节课 × 专栏映射速查表

| 站次 | 官方课程 | 核心教具 / 示范 App | 对应专栏深度页 |
|---|---|---|---|
| **第 1 站** | **[WWDC25 · 219]** Meet Liquid Glass | 光学凸透镜 + 凝胶水滴 | [02 · Liquid Glass 光学与实战](/learn/liquid-glass-optics/) |
| **第 2 站** | **[WWDC25 · 323]** Build a SwiftUI app with the new design | Landmarks 风景探索 | [02 · Liquid Glass 光学与实战](/learn/liquid-glass-optics/) |
| **第 3 站** | **[WWDC26 · 269]** What's new in SwiftUI (OS 27) | Stickers 贴纸相册 | [01 · 全景导读](/learn/wwdc27-glass-motion/) / [02 · 玻璃实战](/learn/liquid-glass-optics/) |
| **第 4 站** | **[WWDC26 · 322]** Compose advanced graphics effects | 水管拼接 + 图钉对齐（播客歌词） | [03 · Metal Shader 与动效管线](/learn/swiftui-shader-pipeline/) |
| **第 5 站** | **[WWDC26 · 321]** Dive into lazy stacks and scrolling | Origami 折纸长列表 | [04 · LazyStack 预取与拖拽](/learn/swiftui-scroll-drag/) |
| **第 6 站** | **[WWDC26 · 271]** Build powerful drag and drop | Solitaire 纸牌接龙 | [04 · LazyStack 预取与拖拽](/learn/swiftui-scroll-drag/) |
| **第 7 站** | **[WWDC26 · 289]** Modernize your AppKit app | Mac 天气卡片 + 状态栏弹窗 | [05 · AppKit 与 UIKit 27 现代化](/learn/appkit-uikit-27/) |
| **第 8 站** | **[WWDC26 · 278]** Modernize your UIKit app | Mac 镜像下自由拉伸的 iPhone 窗口 | [05 · AppKit 与 UIKit 27 现代化](/learn/appkit-uikit-27/) |

👉 **[点此进入 `/learn/` 专栏总览开始阅读 →](/learn/)** ｜ 💭 **[阅读日常随笔专栏：`/thoughts/` 思考与感悟 →](/thoughts/)**
