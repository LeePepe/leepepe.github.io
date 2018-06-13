---
title: "Swift: Control Flow"
layout: post
tags: [iOS, Swift, Note]
categories: [iOS, Swift]
published: ture
---

Swift提供了基本的控制流语句，完成条件跳转，循环等。在Swift中，会更倾向于Swift自定义的控制流语句，更多的是为了满足特殊的开发需求。
对所有的条件判断，条件部分都不需要括号，但强制要求`{ }`。

## For-In 循环

For-in循环的目的是为了遍历，包括数字范围的遍历，字符串中字符的遍历，数组遍历等。

For-in的第一个参数由for循环定义，为`let`，生命周期只在循环体内，类型取决于第二参数（可能为`Int`等，或在遍历字典时为tuple）。

## While 循环

while循环分为两种，while和repeat-while，前者为一般的while循环，后者为do-while循环

## if

在if的条件判断中，只支持`Bool`类型的值，其他的值则会产生编译错误。
或在if中提取optional值，如果不为`nil`，则进入if语句。

## switch

switch用来匹配相关的结果，在swift中，switch可以匹配任何类型，并按顺序匹配。
通过`,`分割不同value在同一个case中。

* swift中没有实现fallthrough在switch语句中，同时也不必须添加`break`在每一个case后。
* 通过`break`来跳过某个内容，因为在switch语句中，必须包含至少一个代码句。
* 通过`fallthrough`来延续某些内容。

### case判断

在case判断中，基本的原则就是按**顺序匹配**，当匹配成功，进入该case代码块，同时自动跳过其他case语句块。

但在swift中，匹配的原则很多。

* 直接匹配：相当于执行了`==`操作，这种匹配是最常见最普通的匹配方式，包括`Int`，`Character`，还包括enum中的case。
* 范围匹配：匹配的值符合某个Range内的值，则完成匹配，如对`Int`类型。

```
let approximateCount = 62
let countedThings = "moons orbiting Saturn"
var naturalCount: String
switch approximateCount {
case 0:
	naturalCount = "no"
case 1..<5:
	naturalCount = "a few"
case 5..<12:
	naturalCount = "several"
case 12..<100:
	naturalCount = "dozens of"
case 100..<1000:
	naturalCount = "hundreds of"
default:
	naturalCount = "many"
}
print("There are \(naturalCount) \(countedThings).")
// Prints "There are dozens of moons orbiting Saturn.
```

* tuple匹配：tuple匹配相当于前者对每一个值得匹配，可以对tuple中每一个值进行直接匹配和范围匹配。

在tuple中，使用Value Bindings，当某些值不需要匹配，但需要获得该值的时候，使用`let`得到其值，该值可以在case中使用

```
let anotherPoint = (2, 0)
switch anotherPoint {
case (let x, 0):
	print("on the x-axis with an x value of \(x)")
case (0, let y):
	print("on the y-axis with a y value of \(y)")
case let (x, y):
	print("somewhere else at (\(x), \(y))")
}
// Prints "on the x-axis with an x value of 2"
```

这个例子就可以分别得到x轴，y轴或其他位置上的点。


在tuple中，当使用Value Bindings时，可以通过`where`来判断得到的值是否符合某些条件。

```
let yetAnotherPoint = (1, -1)
switch yetAnotherPoint {
case let (x, y) where x == y:
	print("(\(x), \(y)) is on the line x == y")
case let (x, y) where x == -y:
	print("(\(x), \(y)) is on the line x == -y")
case let (x, y):
	print("(\(x), \(y)) is just some arbitrary point")
}
// Prints "(1, -1) is on the line x == -y"
```

这个例子就得到了对角线的值。


当switch匹配到所有可能的case的时候（通常匹配enum中的case），则不需要default，否则需要default来覆盖所有可能的情况（如覆盖Character和Int等）。

## Control Transfer Statements

通过某些关键字，完成语句的跳转。

* continue
 
	`continue`关键字是告诉循环停止后续部分，并开始下一循环。
对于for循环，条件中的iterator会进入到下一个选择（如果存在）。
* break
	1. 在switch语句中：

		`break`会直接结束switch语句，并跳到switch后的`}`下一句语句执行。
作用是用来忽略某些无需考虑的case，或是跳过default。（因为swift不允许case为空。）
	2. 在循环语句中：
		
		`break`会直接结束循环执行，并跳到循环`}`的下一语句执行
		
* fallthrough
	
	在swift中，switch语句只会执行**符合条件的第一个case**。
	当需要C-style的switch语句执行下一case内容时，需要添加`fallthrough`来跳到下一语句块。

## Labeled Statements

可以对循环体或对条件跳转声明**statement label**，相当于提供给循环或条件一个名称。
当使用`break`和`continue`的时候，可以指定跳转的循环体或条件。

```
label name: while condition {
	statements
}
```

> 默认情况下不添加名称，则跳转当前条件语句或循环体

## Early Exit

`guard`关键字，使用方法相当于if语句，但作用类似于assert和throw。但可操作性更多。

通过`guard`，来保证某些条件必须为真，否则必须执行else内容，相当于用于保证函数的输入合法化。

```
func greet(person: [String: String]) {
guard let name = person["name"] else {
return
}

print("Hello \(name)!")

guard let location = person["location"] else {
print("I hope the weather is nice near you.")
return
}

print("I hope the weather is nice in \(location).")
}

greet(["name": "John"])
// Prints "Hello John!"
// Prints "I hope the weather is nice near you."
greet(["name": "Jane", "location": "Cupertino"])
// Prints "Hello Jane!"
// Prints "I hope the weather is nice in Cupertino."
```

并且通过了guard确认的值，可以在之后的函数体中使用。

> guard确认optional值的目的和if相反，只是为了确保得到该值，并没有相关操作。但当无法取得的时候，则需要提示一些错误信息。guard得到的值生存周期在整个函数体中。
> 
> if条件更多的是在得到某些值后，需要进行相关操作。得到的值的生存周期和有效范围只在if语句中

## 检查API是否有效

可通过`if`或`guard`来判断是否满足系统版本。

```
if #available(iOS 9, OSX 10.10, *) {
// Use iOS 9 APIs on iOS, and use OS X v10.10 APIs on OS X
} else {
// Fall back to earlier iOS and OS X APIs
}
```


