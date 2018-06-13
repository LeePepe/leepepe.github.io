---
title: "Swift: Collection Types"
layout: post
tags: [iOS, Swift, Note, Collection Types]
categories: [iOS, Swift]
published: ture
---

在Swift中，包含三种结构，分别是Array，Set，Dictionary。

三种的实现都是`struct`。即值拷贝。

声明时需要注明存储值得类型。只可以按类型存储。

当声明为`var`时，三者都可更改。当声明为`let`时，三者都不可修改。

> 当我们需要声明一个固定数组或字典时，最好声明成`let`。这样可以在编译时保证该常量不会改变。

## Array

数组在一定顺序下存储值。并可以有重复的值。

```
var a = Array<String>()
// ... is the same as ...
var a = [String]()
```

通过`for-in`方法可以进行遍历。

### Methods

`init(count: , repeatedValue:)`：构造重复值的数组

`append(_:)`：添加一个成员到尾部。

`insert(_: atIndex:)`：插入到特定位置

`filter(includeElement: (T) -> Bool) -> [T]`：产生新的数组，元素满足条件的。
```let bigNumbers = [2, 47, 118, 5, 9].filter({ $0 > 20 }) // bigNumbers = [47, 118]```

`map(transform: (T) -> U) -> [U]`：将数组转换成另一种类型数组
```let stringified: [String] = [1, 2, 3].map { String($0) }```

`reduce(initial: U, combine: (U, T) -> U) -> U`：将数组转换成为一个值
```let sum: Int = [1, 2, 3].reduce(0) { $0 + $1 }```

`enumerate()`：返回一个tuple，第二个为值，第一个为序号。

`+`可以合并相同类型的数组，同样可以通过`+=`添加新的成员(右值应为相同类型的数组)。

`[]`下标可以用来访问元素或更改元素。但不可以添加新元素到数组尾部。

`shoppingList[4...6] = ["Bananas", "Apples"] `这样的方式可以将4-6的元素替换成后两者，此时成员数量减少了一个。

### 数据结构

可以用数组构造简单的数据结构。

如：

堆栈：
`removeLast()`和`append(_:)`方法

队列：
`removeFirst()`和`append(_:)`

## Sets

Set存储同类型的变量，但只出现一次。

### Hash Values for Set Types

所有的Set存储的类型，必须是完成`Hashable`协议的。

`Hashable`遵从`Equatable`协议，该协议需要实现`==`操作

> `==`操作满足自反性，对称性和传递性。

Set没有短初始化的方式
`var letters = Set<Character>()`

但是根据**type inference**，可以省略类型声明
`var favoriteGenres: Set = ["Rock", "Classical", "Hip hop"]`

### Methods

`insert(_:)`：在Set中，没有所谓的顺序，insert会插入值到第一个位置

`remove(_:)`：从Set中删除某个元素并返回，如果不存在，则返回nil。

`contains(_:)`：判断是否包含某个元素

`sort()`：对Set进行排序，默认为`<`

`sort(isOrderedBefore: (T, T) -> Bool)`：可以自己写一个closure，来排序。

### Set Operations

`intersect(_:)`：交集

`exclusiveOr(_:)`：异或集

`union(_:)`：并集

`subtract(_:)`：补集

![FundamentalSetOperations](img/FundamentalSetOperations.png)


`==`：判断两个集合是否包含同样的元素

`isSubsetOf(_:)`：判断子集

`isSupersetOf(_:)`：判断超集

`isStrictSubsetOf(_:)`：判断为真子集

`isStrictSupersetOf(_:)`：判断真超集

`isDisjointWith(_:)`：判断是否有交集

## Dictionary

字典的key值同样需要满足`Hashable`协议。

```swift
var pac10teamRankings = Dictionary<String, Int>()
// ... is the same as ...
var pac10teamRankings = [String: Int]()
```

可以通过`airports["LHR"] = "London"`添加一个新的项
或通过`if let oldValue = airports.updateValue("Dublin Airport", forKey: "DUB")`可以获得`oldValue`

因为可能某些key并不存在在字典中，所以字典根据下标返回的都是optional

当删除的时候，可以设置某个key的value为`nil`
或通过`removeValueForKey(_:)`删除某个值

通过for-in循环可以遍历整个字典，但返回的是个tuple。

```swift
for (airportCode, airportName) in airports {
    print("\(airportCode): \(airportName)")
}
```