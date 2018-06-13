---
title: "Swift: Closure"
layout: post
tags: [iOS, Swift, Note]
categories: [iOS, Swift]
published: ture
---

闭包(Closure)表示为一块功能性代码块，并可以调用和其同一命名空间的变量。

在很多情况下我们会使用到Closure，如：异步返回，特殊处理的时候，闭包可以让整个代码更加简洁，简单。在闭包内只是很简单的操作的时候，闭包可以变到小到一看就懂。当闭包需要执行很多操作的时候，又给人一种独立的感觉。

函数也可以看成为闭包的一种：

1. 全局函数：有名字，但不可以从函数中获取值。
2. 内嵌函数：有名字，可以从其定义的函数中获取值。
3. 闭包：没有名字，可以获取值。

## 闭包表达式

用`sort`函数来表示闭包的各种写法。

`sort`是Swift标准库提供的方法，每个array变量都有这个方法。

对于`sort`函数，其参数为`((T, T)->Bool)`，类型为一个函数，所以我们可以定义一个函数，再将函数传入（传入函数名）。

```
let names = ["Chris", "Alex", "Ewa", "Barry", "Daniella"]

func backwards(s1: String, _ s2: String) -> Bool {
    return s1 > s2
}
var reversed = names.sort(backwards)
// reversed is equal to ["Ewa", "Daniella", "Chris", "Barry", "Alex"]
```

但这样的写法过于冗余，如果这个函数只用一次，同时我们整个文件又比较大，在寻找`backwards`时，比较麻烦。

```
{ (parameters) -> return type in
    statements
}
```

这是一个标准的闭包表达式，用`{}`来表达一块代码， `(parameters) -> return type in`表示其参数和返回值，`in`后面的为整个闭包内容。

所以我们就可以将上述的写法进行转换：

```
reversed = names.sort({ (s1: String, s2: String) -> Bool in return s1 > s2 })
```

这样写最大的好处就是减少代码阅读的难度，这里我们看到可以将闭包写成一行，如果闭包只有一行，这样的写法同样可以做到减少空间的目的。

又因为type inference，所以参数类型和返回值都可以被我们省略的：

```
reversed = names.sort( { s1, s2 in return s1 > s2})
```

这里我省略了()，在闭包是允许的，同样你也可以加上（）。推断是根据这个**函数在定义**的时候所给出的函数参数的参数和返回值，而不是根据闭包

对于一行表达式的闭包，我们明确地知道它有一个返回值，所以`return`也被我们省略掉了

```
reversed = names.sort( { s1, s2 in s1 > s2} )
```

swift还提供快速参数名：$0, $1, $2一直下去，所以我们可以用快速参数名而不用自己定义参数名：

```
reversed = names.sort( { $0 > $1} )
```

在Swift中，所有的操作符，其实都是函数，如`*`，`>`等。所以我们可以提供一种更简单的方式：

```
reversed = names.sort(>)
```

当函数的最后一个参数为闭包(有可能不在最后一个，如多个闭包，包含变长参数)，我们可以将整个闭包放到整个函数的最后

```
reversed = names.sort() { $0 > $1 } 
reversed = names.sort { $0 > $1 } 
```

如果将闭包移到外部，参数中不包含其他参数的时候，`()`可以被省略。

## Closures Are Reference Types

闭包是作为引用类型，和类，函数属于同一类型，当进行赋值操作时，其实是新建指针指向原实例。

引用类型就会容易导致引用环，尤其是在类中定义一个Closure时，当Closure使用self，并且Closure长期保存在类中的时候，两者之间互相引用，两者就永远存在于heap中。

一：在Closure中，对`self`变量进行`weak`或`unown`声明，保证Closure不是对`self`为强类型引用。

二：通过改变闭包的特性，让闭包不被heap保存。

## Nonescaping Closure

当closure作为函数的参数是，可以在参数前添加关键字`@noescape`，这样闭包会长时间被函数保存，而不会在函数结束后**逃出**。同时，该closure不会被**其他地方引用**，因为该closure是被该函数所持有（类似于class中的func），这样closure可以在调用`self`中的变量或函数时不需要添加`self`关键字，而是closure已经处于`self`中。

## Auto Closures

关键字`@autoclosure`是自动转换成closure的一个方式，当声明该关键字后，在函数内调用时没有任何区别，但是在外部传输变量的时候，可以传一个变量而不是一个closure，这样可以自动转换为closure（要求closure的参数为空）。

	Note：不应当过多使用auto closure，这样会让代码更难读。
	
`@noescape`是直接在`@autoclosure`中声明的，如果需要其escape，则需要`@autoclosure(escaping)`

当closure需要被保存时（数组中等），使用weak或unown来避免引用环。
当closure只是短暂使用，或确认只在该函数中使用时，使用noescape。





