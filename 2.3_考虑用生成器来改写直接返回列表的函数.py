#!/usr/bin/env python27
# -*- coding: utf-8 -*-
# @Time    : 2021/6/2 10:22
# @Author  : handling
# @File    : 2.3_考虑用生成器来改写直接返回列表的函数.py
# @Software: PyCharm

def index_words(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index + 1)
    return result


address = 'Four score and seven years ago...'
result = index_words(address)
print(result[:3])

# 在以上代码中是十分臃肿的，【创建列表，追加，返回】，这些能被生成器给替换显得更加简单
# 同时将所有的结果全放在list再返回，开销是很大的，也要可能造成内存崩溃

# 生成器是使用 yield 表达式的函数，调用生成器函数时，会返回迭代器，每次调用next，就会把生成器
# 推到下一个yield表达式那里

def index_words(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1

# 调用生成器所返回的迭代器，可以传给内置的list函数，将其转换为列表
result = list(index_words(address))
print result


# 总结
# 1. 使用生成器把收集到的结果放在列表返回给调用者更加清晰
# 2. 由生成器函数所返回的那个迭代器，可以把生成器函数体中，传给yield表达式的那些值，逐次产生出来
# 3. 无论输入量有多大，生成器都能产生一系列输出，因为这些输入量和输出量，都不会影响它在执行时所消耗的内存
