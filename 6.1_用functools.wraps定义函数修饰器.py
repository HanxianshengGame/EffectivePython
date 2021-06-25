#!/usr/bin/env python27
# -*- coding: utf-8 -*-
# @Time    : 2021/6/24 17:14
# @Author  : handling
# @File    : 6.1_用functools.wraps定义函数修饰器.py
# @Software: PyCharm

# python 用特殊的语法来表示修饰器，用于修饰函数
# 修饰器能在函数运行之前以及运行完毕之后，分别运行一些附加代码，这使得
# 可以在修饰器里面访问并修改原函数的参数及返回值，以实现约束语意，以及调试程序，注册函数等
from functools import wraps
from pydoc import help


def trace(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(func.__name__, args, kwargs)
        return result

    return wrapper


@trace
def fibonacci(n):
    """:return the n-th Fibonacci number"""
    if n in (0, 1):
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# fibonacci = trace(fibonacci)  # 这就是给fibonacci加上装饰器后的表现

print fibonacci(3)
print(fibonacci)

# 这里我们会发现 fibonacci的表现其实是wrapper， 但对于调试器和对象序列化器
# 需要内省机制（介绍帮助）的那些工具来说，这样的行为会干扰它们的正常运作

# 例如
help(fibonacci)


# 解决办法，使用内置的functools模块中名为 wraps 的辅助函数来解决,
# 它可以帮助开发者编写其他修饰器，将wrap修饰器运用到wrapper函数后，就会将
# 内部函数相关重要元数据全部赋值到外围函数

def trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(func.__name__, args, kwargs)
        return result

    return wrapper


@trace
def fibonacci(n):
    pass

help(fibonacci)


# 总结：
# 1. python 为修饰器提供了专门的语法，使得程序在运行的时候，能够用一个函数来
# 修改另一个函数

# 2. 对于调试器这种依靠内省机制的工具，直接编写修饰器会引发奇怪的行为。
# 3. 内置的functools模块提供了名为wraps的修饰器，开发者在定义自己的修饰器时，
# 应该以 wraps对其做了一些处理，以避免一些问题

