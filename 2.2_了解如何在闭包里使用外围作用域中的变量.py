#!/usr/bin/env python27
# -*- coding: utf-8 -*-
# @Time    : 2021/6/1 15:02
# @Author  : handling
# @File    : 2.2_了解如何在闭包里使用外围作用域中的变量.py
# @Software: PyCharm

def sort_priority(numbers, group):
    found = [False]

    def helper(x):
        if x in group:
            found[0] = True
            return 0, x
        return 1, x

    numbers.sort(key=helper)
    return found[0]

# 总结
# 1. 对于定义在某作用域的闭包来说, 它可以引用这些作用域的变量
# 2. 使用默认方式对闭包内的变量赋值,不会影响外围作用域的同名变量
# 3. 程序可以通过可变值(单个元素的列表)来实现与nonlocal语句相仿的机制
# 4. 除了那种比较简单的函数,尽量不适应 nonlocal
