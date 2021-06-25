#!/usr/bin/env python27
# -*- coding: utf-8 -*-
# @Time    : 2021/6/2 16:08
# @Author  : handling
# @File    : 2.5_用数量可变的位置参数减少视觉杂讯】.py
# @Software: PyCharm

# python 令函数接收可选的位置参数*args,能够使得代码更加清晰，减少视觉杂讯

def log(message, values):
    if not values:
        print(message)
    else:
        values_str = ','.join(str(x) for x in values)
        print('{0}: {1}'.format(message, values_str))


log('My numbers are', [1, 2])
log('Hi there', [])  # 即使没有打印的值，也需要手工传一份空列表


def log(message, *values):
    if not values:
        print(message)
    else:
        values_str = ','.join(str(x) for x in values)
        print('{0}: {1}'.format(message, values_str))


log('My numbers are', 1, 2)
log('Hi there')  # 没有打印的值, 就不填入

# 把已有的列表，传入可变参数的函数，调用时需要在列表前加入*操作符，python
# 就会把这个列表里的元素视为位置参数

favorites = [7, 33, 99]
log('Favorite colors', *favorites)


# 可变参数的两个问题

# 1. 变长参数在传给函数时，总是要先转换为元组， 所以如果使用*操作符的生成器为参数，来调用
# 函数，就必须先把生成器完整地迭代一轮， 并把生成器所生成的每个值，都放入元组中。

def my_generator():
    for i in range(10):
        yield i


def my_func(*args):
    print(args)


it = my_generator()
my_func(*it)

# 建议： 只有当我们很确定输入的参数个数比较少，才能让函数接收可变参数


# 2. 如果以后给函数添加新的位置参数，那就必须修改原来调用该函数的那些旧代码

def log(sequence, message, *values):  # 增加新的参数
    if not values:
        pass
    else:
        pass
log('Favorite colors', *favorites) # 这个就会有变化
log(1,2,3,4)  # sequence 为1


# 可以使用关键字参数来表示可选的行为, 来扩展这种接受*args 的函数 参考2.6

