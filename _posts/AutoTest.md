---
layout: post
title:  "WebKit"
categories: 软件工程
author: LeePepe
---


# 测试自动化

测试自动化只是完成了执行测试的动作。

> Wikipedia: the process of writing a computer program to do testing taht would otherwise need to be done manually.

包括
* the setting up of test preconditions.
* the execution of test case.
* the comparison of actual outcomes to predicted outcomes.

提供高效率（efficient）、可重复性（repeatable）、一致性（consistent）的测试。

## Why ?

* Testing needs to cover multiple platforms and releases in a short time.
* Test execution demands a huge amount of time and attention.
* Test result record and reporting is error-prone.

## What ?

Test Automation Process
![TestAutoProcess](/asset/TestAutoProcess)

### Three parts:

* Test driver(测试驱动):
    * 一般使用脚本来做。
    * 替换人操作，利用脚本来完成人为操作。
    * 包括测试引擎和测试脚本。
* Test stub(测试桩):
    * 替换模块，完成测试
* Test harness(测试套):
    * 替换数据库或网络，提供一个假的外部环境下进行测试。

为了模仿真实环境下的运行环境，进行测试。

### Automation Opportunity

* 单元测试：always
* 集成测试：always
* 系统测试：High
* 并发测试：always
* 压力测试：always
* 可靠性测试：always
* 可用性测试：**none**
* 确认测试：Low

## When ?

### “Is” and “Is Not”

* is software development：
    * 测试自动化是一个产品。
    * 需要进行分析、设计、实现和维护。
    * 需要时间、人力、花费和技能。
* is long time investment：
    * 直接代价Upfront costs：需要学习，开发，工具支持。
    * 维护代价：需要升级脚本。
    * 需要考虑回归代价。
* is not silver bullet for testing：
    * 依然需要三个fundamental problems。
    * 测试结果基本一致，多次测试难以找到其它错误。
    * 只会暴露较少的bug。
* is not always recommended：
    * 低执行频率（测试较少)。
    * 脆弱的设计（Fragile design）。
    * 涉及物理设备。
    * 在确认测试的时候没有必要。
* is not complete replacement of manual testing：
    * 不可以代替手工测试

### Factors that Affect Cost (Testability)

* Controllability（可控制性）
* Observability（可观察性）

Approaches to improve controllability and observability:
* Implement configuration options to trigger corner cases.
* 使用测试桩和测试套模拟外部环境。
* 将应用进行分层。
* 使用断言。
* Make program failures obvious.


## How ?

### Techniques:

* Capture/replay（回放）
    *  
* Structural Test Scripts Development
* Data-driven test automation
* Keyword-driven test automation


   A  B  C  D  E  F  G

A  0  0  0 20  0  0 12

B  0  0 10 15  0 16 12

C  0 10  0  0  0 15  0

D 20 15  0  0 12  0 20

E  0  0  0 12  0 10  0

F  0 16 15  0 10  0 14

G 12 12  0 20  0 14  0
