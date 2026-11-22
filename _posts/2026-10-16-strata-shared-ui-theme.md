---
layout: post
title: "Strata：用苹果糖果色验证一套共享 UI 主题"
date: 2026-10-16
categories: design ui
permalink: /design/strata-shared-ui-theme/
---

Strata · 岩层是一个共享 UI **主题验证网页原型**。用同一张可操作的组件工作台，观察蓝、绿、粉、黄、紫在明暗之间的不同气质。配色受到经典 iMac / iPhone 5C 启发，全部为自定义颜色，不是 Apple 官方设计系统。

这一轮从哑光向 **Glass** 演进：中性底色上放少量静态糖果色形，外层面板用半透明、模糊和细高光表达厚度，内层阅读表面更实。主按钮保留可读的实色配对，没有霓虹或重阴影，也不模拟原生 Liquid Glass 的折射。

![Strata Glass 蓝色浅色桌面工作台，展示圆润的主题控制、按钮、卡片、列表与 tokens]({{ '/strata/v0-2/blue-light-desktop.png' | relative_url }})

工作台只保留三类组件：**Button** 展示主要、次要、轻量操作，以及禁用和加载状态，点击可体验模拟保存；**Card** 包含基础内容卡与统计卡，数字均标明为示例；**List** 支持选择，用中性表面明度、勾号和「已选」文字共同表达状态。

![Strata Glass 绿色浅色桌面工作台，与蓝色主题保持相同结构和尺寸]({{ '/strata/v0-2/green-light-desktop.png' | relative_url }})

共享 tokens 集中管理表面、文字、品牌、语义状态、图表、焦点、字号、间距、圆角与动效，也管理材质透明度、模糊、高光和阴影。明暗分别校准，换色只换值。形状统一为胶囊按钮、圆形色板，以及 **16px 控件／24px 卡片／32px 容器**；窄屏卡片改为单列，为圆润轮廓留出阅读空间。

![Strata Glass 紫色深色桌面工作台，展示独立校准的深色玻璃表面、弱化的内层边缘与浅紫主按钮]({{ '/strata/v0-2/purple-dark-desktop.png' | relative_url }})

顶部可对照玻璃与实底，URL 保留配色、明暗和材质，当前主题可下载为 JSON。减少透明度偏好或不支持模糊的浏览器自动回退实底；减少动态效果时停止动画。页面采用静态 HTML、CSS 和 JavaScript，无后端或真实账号。

真实 Chromium 检查覆盖 20 种主题与材质组合、JSON 下载、按钮反馈、列表选择和键盘焦点；320–1440px 共 100 个组合无横向溢出，控制台无错误。普通文字在实际合成背景上的已检查样本最低对比度为 **4.67:1**，不包含禁用态，也不等同于完整无障碍审计。三张桌面截图均为 1440×1000；下面是 390×844 视口的手机完整滚动页面。

<a href="{{ '/strata/v0-2/blue-light-mobile.png' | relative_url }}"><img src="{{ '/strata/v0-2/blue-light-mobile.png' | relative_url }}" alt="Strata Glass 蓝色浅色手机完整页面，展示胶囊按钮、单列圆角卡片、可选列表及 tokens 下载" width="390" loading="lazy"></a>

这轮留给视觉判断的问题是：通透程度是否合适，圆角比例是否舒服，以及深色层次与手机阅读节奏是否值得保留。**方向仍待判断，原型尚未成为生产规范。**
