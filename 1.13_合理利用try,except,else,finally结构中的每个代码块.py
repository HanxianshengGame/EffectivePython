#!/usr/bin/env python27
# -*- coding: utf-8 -*-
# @Time    : 2021/6/1 13:59
# @Author  : handling
# @File    : 1.13_合理利用try,except,else,finally结构中的每个代码块.py
# @Software: PyCharm

# python 程序的异常处理可能要考虑四种不同的时机, 这些时机可以用
# try, except, else和finally来表述

# finally 块: 可靠地执行代码(一般用于关闭文件描述符)
import json

handle = open('random.bin')
try:
    data = handle.read()
finally:
    handle.close()


# else 块

# try/except/else 如果try没发生异常,就会执行else块,可以利用此性质,尽量缩减try代码块
# 的代码量, 使其结构更容易读

def load_json_key(data, key):
    try:
        result_dict = json.loads(data)
    except ValueError as e:
        raise KeyError(e)
    else:
        return result_dict[key]


# 混合使用

UNDEFINED = object()


def divide_json(path):
    handle = open(path, 'r+')
    try:
        data = handle.read()
        op = json.loads(data)
        value = (op['numerator'],
                 op['denominator'])
    except ZeroDivisionError as e:
        return UNDEFINED
    else:
        op['result'] = value
        result = json.dumps(op)
        handle.seek(0)
        handle.write(result)
        return value
    finally:
        handle.close()


def func():
    try:
        print 1
    except ZeroDivisionError:
        pass
    else:
        print 111
        return True
    finally:
        return False  #??? 返回前也要执行

print func()

# 总结:
# 1. try是否发生异常,都可以利用try/finally 复合语句中的finally做清理工作
# 2. else块可以用来缩减 try块中的代码量,并把没有发生异常时所要执行的语句
# 与 try/except 代码块隔开
# 3. 顺利运行try后,若想使得某些操作在finally的清理代码之前执行,则可以将这些操作
# 写到else块中
