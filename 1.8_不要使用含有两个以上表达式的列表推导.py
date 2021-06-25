#!/usr/bin/env python27
# -*- coding: utf-8 -*-
# @Time    : 2021/6/1 11:58
# @Author  : handling
# @File    : 1.8_不要使用含有两个以上表达式的列表推导.py
# @Software: PyCharm

# 列表推导式支持嵌套，但比较晦涩
a = [[1,2,3],[4,5]]
x = [[elem for elem in row] for row in a]
print x

# 总结：
# 1. 列表推导支持多级循环，每一项循环也支持多项条件
# 2. 超过两个表达式的列表推导是很难理解的，应该尽量避免
