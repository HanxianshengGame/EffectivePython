#!/usr/bin/env python27
# -*- coding: utf-8 -*-
# @Time    : 2021/6/2 18:31
# @Author  : handling
# @File    : 2.6_用关键字参数来表达可选的行为.py
# @Software: PyCharm


def remainder(number, divisor):
    return number % divisor


assert remainder(20, 7) == 6

# python 可以用关键字参数来调用函数，使得读到这行代码的人更容易理解其含义
assert remainder(number=20, divisor=7) == 6


# 总结

# 1. 函数参数可以按位置或关键字来指定
# 2. 只使用位置参数来调用函数，可能会导致这些参数值的含义不够明确，而
# 关键字参数则能阐明每个参数的意图
# 3. 给函数添加新的行为时，可以使用带默认值的关键字参数，以便于原有的函数
# 调用代码兼容
# 4. 可选的关键字参数，总是应该以关键字形式来指定，而不应该以位置参数的形式来指定