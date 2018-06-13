---
title: "Swift:Properties"
layout: post
tags: [iOS, Swift, Note, Properties]
categories: [iOS, Swift]
published: ture
---

Properties可以被存储在`class`，`struct`和`enum`（只有computed properties）。

## Stored Properties

可以是变量`var`或常量`let`。

所有stroed properties都需要有值：

* 可以直接设置默认值。Optional有默认的默认值`nil`。
* 或者为lazy properties。
* 剩下的stored properties需要在initializer里面初始化，`let`也可以初始化，有默认值的会覆盖默认值。

### Stored Properties of Constant Structure Instances

如果创造了一个`let`的结构体实例，那么其中的所有properties都不可变，即使是`var`的。（因为结构体为value type）。

但类就可以，因为类是reference type。

### Lazy Stored Properties

当一个property会：

* 初始化比较复杂。
* 可能会用到其他properties，需要在构造函数完成后才可以被确定。
* 可能该property不会被用到。

就可以定义为一个`lazy var`。

> Lazy Property并不是线性安全的，最好保证其只在一个线程内被初始化。

## Computed Properties

Computed Properties并不存储值，而是通过计算的方式提供值（或提供可选的setter）

当一个可以被看做是属性的值，但又可以通过其他属性计算得到时，我们就使用Computed Properties。

* 可以在setter中设置新值的变量名`set(变量名)`。或者使用默认值`newValue`。
* 可以设置为read-only，只设置其`get`，这时可以省略`get`直接写在大括号中

## Property Observers

通过`didSet`和`willSet`改观察值的变化。observers可以添加到任何stroed properties（除了lazy），同时可以添加到任何继承的属性中。

* `willSet`会提供一个默认值`newValue`，为新的值，并且会在值被存储前被调用。
* `didSet`提供一个默认值`oldValue`，为被替换的值，并且在值被存储后的第一时间被调用。

## Global and Local Variables

全局变量或常量永远是lazy的，同时不需要写`lazy`。

## Type Properties

类属性不属于任何实例而是属于类型自己。表示永远只有一个属性对所有实例。

> 所有类属性必须有默认值。并且默认为`lazy`

* `static`来声明类属性。
* `class`来声明可重写的计算类属性。