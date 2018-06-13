---
title: "Swift: Methods"
layout: post
tags: [iOS, Swift, Note]
categories: [iOS, Swift]
published: ture
---

在swift中，函数的作用表示的是一个具有特定名称并执行特定任务的代码块。

同时可以在**函数内定义函数**。

### 函数类型

函数类型为**Tuple1 -> Tuple2**，参数作为Tuple1，返回值作为Tuple2。

如：

`() -> ()`为函数没有参数并返回类型为Void的参数。

`(Int, Int) -> Int`为函数有两个参数，都是`Int`类型，并返回一个`Int`类型的值。

> 当函数没有返回值得时候，其返回一个特殊的类型Void，为空的Tuple，即**()**，定义类型的时候返回值部分依旧是`-> Void`

函数类型和其他类型功能一样（可以作为其他函数的参数或返回值），
并可以赋值给相同类型的变量（或通过Type inference推断而不需要明确声明类型）。

### 返回值

`-> 返回值`来表示函数的返回值

* 没有返回值：可以省略`-> 返回值`这个部分，但函数依然有个返回值类型，为`-> Void`，即空tuple。
* 多个返回值：可以利用tuple来返回多个返回值。
* Optional：返回值可以是optional的，对于tuple也可以使用optional

> (Int, Int)? 和(Int?, Int?)是完全不同的，一个是tuple可能为optional，但其中的值一定存在，第二个为tuple一定存在，但每个值可能为optional。

### 参数

* 所有变量都有internal name和external name。
* internal name：作为方法内部名称。
* external name：作为调用者使用时使用的名称（不建议）。
* `_`来忽略一个特定参数的external name。
* 对于第一个参数，自动忽略external name。
* 对于其他参数，internal自动作为external使用。

* default parameter value，每个参数都可以有默认值，通过`=`来提供默认值，带有默认值的参数都会放到所有参数后面。
* `...`表示该参数可以接收多个值（一个函数最多有一个这样的variadic parameter参数）。该参数永远放在所有参数的最后
* `inout`关键字前缀可以让参数在外部被更改，作用方法是将值传入，由函数进行更改后，传出改变原来的值。



**除第一个参数外，Swift不倾向忽略external name。因为第一个参数的意义会出现在函数名上**

### Override

* 添加`override`来重新`func`或`var`
* 或添加`final`来防止别人重新该方法，变量，或该类。
* `static`前缀来添加type methods/properties。

# Methods

### Modifying Value Types from Within Instance Methods

结构体`struct`和枚举`enum`为value type。当其中的方法需要改变其中的properties时，需要添加关键字`mutating`

> 即便如此，`let`定义的依旧不可以改变，会产生error

## Type Methods

在Swift中，可以在`class`、`sturct`、`enum`中定义类方法。

通过`class`关键字定义可被重写的类方法。