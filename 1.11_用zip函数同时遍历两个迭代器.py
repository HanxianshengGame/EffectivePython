#!/usr/bin/env python27
# -*- coding: utf-8 -*-
# @Time    : 2021/6/1 13:30
# @Author  : handling
# @File    : 1.11_用zip函数同时遍历两个迭代器.py
# @Software: PyCharm

# 如果相同索引处的两个元素之间有关联,需要平行迭代这两份列表, 但又不需要索引
# 这个值的额外空间占用,就使用zip吧
import itertools

names = ['hanzhenjiang', 'lise', 'marie']
letters = [len(n) for n in names]
for name, count in zip(names, letters):
    pass

# 内置的zip有两个问题

# 1. python2 中的zip并不是生成器,而是会把开发者所提供的那些迭代器,都平行地
# 遍历一遍, 在此过程中,会将迭代器产生的值汇聚成为元组,并将那些元组构成的列表完整
# 地返回给调用者,这可能能会占用很大内存导致崩溃.

# 解决办法使用 itertools模块的izip

for name, count in itertools.izip(names, letters):
    pass

# 2. 如果遍历的迭代器长度不同, zip 会在最短处停止生产元组

names.extend(['hzj'])
for name, count in zip(names, letters):
    print name, count

# 如果想继续遍历,或不确定zip封装的列表等长, 建议改用itertools内置模块的
# izip_longest

for name, count in itertools.izip_longest(names, letters):
    print name, count


# 总结:
# 1. 内置的zip函数可以平行的遍历多个迭代器
# 2. python3 中的zip相当于生成器, 会在遍历过程中生产元组, 而python2中的zip
#    则是直接把元组完全生成好,并一次性返回整份列表
# 3. 如果提供的迭代器长度不等, zip 会提前终止
# 4. itertools内置模块的 izip_longest 函数可以平行遍历多个迭代器, 而不在乎他们的长度
# 是否相等
