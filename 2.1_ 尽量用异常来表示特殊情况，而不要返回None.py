#!/usr/bin/env python27
# -*- coding: utf-8 -*-
# @Time    : 2021/6/1 14:28
# @Author  : handling
# @File    : 2.1_ 尽量用异常来表示特殊情况，而不要返回None.py
# @Software: PyCharm


# None 有着特殊的含义, 若是作为在异常内的返回值是不合理的
# 异常不应该被隐藏,而是应该抛出

def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError as e:
        raise ValueError(e)


x, y = 5,2
try:
    result = divide(x,y)
except ValueError:
    print('invalid inputs')
else:
    print('result is {0}'.format(result))

# 总结:
# 1. 用None这个返回值来表示特殊意义的函数,很容易使得调用者犯错, 因为None和0以及
# 空字符串之类的值, 在条件表达式中都会评估为 False

# 2. 函数在遇到特殊情况时,应该抛出异常,而不要返回None,调用者看到函数文档所描述的异常hou
# 就会编写相应的代码来处理它们了

