#!/usr/bin/env python27
# -*- coding: utf-8 -*-
# @Time    : 2021/6/1 11:23
# @Author  : handling
# @File    : 1.6_在单词切片操作中，不要同时指定start,end和stride.py
# @Software: PyCharm
import itertools

# python提供了somelist[start:end:stride]形式的写法，以实现步进式切割
# 即每n个元素中取一个出来

# 例子：奇偶分组
a = ['red', 'orange', 'yellow', 'green', 'blue']
odds = a[::2]
evens = a[1::2]
print(odds)
print(evens)

# 使用-1做步进值可以反转字符串

x = 'mongoose'
y = x[::-1]
print(y)

# 这种技巧虽对ASCII有用或字节串，但对已经编码为UTF-8的Unicode字符串来说，无法奏效


x = u'谢谢'
print(type(x))
x = x.encode('utf-8')
print(type(x))
y = x[::-1]
z = y.encode('utf-8')   # except

# 步进值为负数，代表从尾部开始向前选，每两个元素中选一个
# 注意：在slice[] 中写3个数字显得过于拥挤，也导致代码难以阅读，
# 如果非要用stride，尽量使用正值，且将切割和步进改为两行。

b = a[::2]
c = b[1:-1]

# 分两行书写会多一份原数据的拷贝，因此应该尽量缩减切割后的列表尺寸，
# 如果对内存用量要求严格，请使用 itertools 的islice方法， 这个
# 方法不允许对 start,end,stride 设置负值

itertools.islice(a, 1, -1, 2)  # except

# 总结
# 1. slice操作3个值是十分费解的
# 2. 尽量使得步进值 stride 为正数， 且与分割操作分离为两步
# 3. 可以考虑内置itertoos模块的islice避免这些费解的功能