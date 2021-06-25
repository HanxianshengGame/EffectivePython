#!/usr/bin/env python27
# -*- coding: utf-8 -*-
# @Time    : 2021/6/1 10:15
# @Author  : handling
# @File    : 1.4_用辅助函数来取代复杂的表达式.py
# @Software: PyCharm

# 这节课主要是说，把复杂的逻辑拆出来，变成辅助函数，之后单行调用即可， 而不要写
# 十分复杂的单行表达式


my_values = {'red': 1}
red = int(my_values.get('red', [''])[0] or 0)  # 虽一行，但晦涩难懂


def get_first_int(values, key, default=0):  # 拆出来的逻辑
    found = values.get(key, [''])
    if found[0]:
        found = int(found[0])
    else:
        found = default
    return found


red = get_first_int(my_values, 'red', 0)

# 总结:
# 1. 开发者很容易过度运用python的语法特性， 从而写出那种特别复杂难理解的单行表达式
# 2. 请把复杂的表达式移入辅助函数中，且如果反复使用相同的逻辑，更应该这样做
# 3. 使用if/else 表达式， 要比用or和and这样的boolean操作符写出的表达式更清晰