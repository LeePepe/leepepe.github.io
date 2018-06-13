---
title: "iOS蓝牙开发"
layout: post
tags: [iOS, Swift, Bluetooth]
categories: [iOS, Swift]
published: ture
---


CoreBluetooth框架提供让Mac或iOS应用通过蓝牙连接其他设备。可以完成发现、探索及交流任务。其他设备包括如心率计算器或其他iOS、Mac设备。

原地址：


标签 : iOS Bluetooth

## Centrals and Peripherals Are the Key Players in Core Bluetooth

在蓝牙连接中，有两个角色：central和peripheral

![Central and peripheral devices]({{site.postimg}}/CB1-1)

peripheral：提供数据和完成任务
central：完成数据的下载和上传，分配任务等。

### advertising packet
AP是一系列打包的数据。
由peripheral提供打包并广播（broadcast）。
central可以通过扫描和收听，获得感兴趣的advertising information。

### Structured of the Data of a Peripheral

![Advertising and discovery]({{site.postimg}}/CB1-2)

Peripheral 包含一个或多个service。
一个service包含实现装置的功能或特征得到的数据。
service由characteristic组成。
characteristic提供service的细节，提供具体数据。

当central成功连接peripheral后，可以发现所有的services和characteristics。同时central可以读取或更改characteristic的数据。

### How Centrals, Peripherals, and Peripheral Data Are Represented

#### Central Side

由于实现的是小飞机蓝牙连接，iOS端为Central Side。所以主要完成该部分。

##### Local Centrals and Remote Periperals

![Core Bluetooth objects on the central side]({{site.url}}/assets/CB1-4.png)

central端：表示为`CBCentralManager`对象，用来管理或连接远程peripheral设备（表示为`CBPeripheral`对象）。包括扫描，发现，连接peripherals。

CBPeripheral结构如下：
![A remote peripheral's tree of services and characteristics]({{site.url}}/assets/CB1-5)

## 实现（Performing Common Central Role Tasks)

### Starting Up a Central Manager

在Controller中声明一个新的变量
`    private var myCentralManager = CBCentralManager()`

此时，设定了该`CBCentralManager`的`delegate`是`self`，所以需要添加`CBCentralManagerDelegate`协议并必须完成函数` centralManagerDidUpdateState:`







