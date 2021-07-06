#!/usr/bin/env python27
# -*- coding: utf-8 -*-
# @Time    : 2021/6/25 11:01
# @Author  : handling
# @File    : 6.2_考虑以contextlib和with语句来改写可复用的tryfinally代码.py
# @Software: PyCharm

# 开发者可以用python的with语句来表达这些代码的运行时机

# 例如： 把互斥锁放入with语句，表示仅程序持有改锁才能得到运行
from threading import Lock

lock = Lock()
with lock:
    print('lock is held')

# 等同于

lock.acquire()
try:
    print('Lock is held')
finally:
    lock.release()


# 这种with可以通过内置的contextlib模块来处理自己编写的对象和函数实现，该模块提供了contextmanager的修饰器
# 一个简单的函数，只需经过 contextmanager修饰，即可用在with语句之中


def my_function():
    print('some debug data')
    print('error log here')


my_function()

from contextlib import contextmanager


@contextmanager
def debug_logging(level):
    try:
        yield
    finally:
        print('old_level', 1)


with debug_logging(2):
    print 'inside:'
    my_function()
print('after')
my_function()

# yield 表达式所在的地方，也是with语句要展开的地方， with块所抛出的
# 异常都会被yield表达式重新抛出，这使得开发者可以在辅助函数捕获


# 使用带有目标的with语句,具体做法是在yield表达式后返回一个变量

@contextmanager
def open_file(file, mode):
    file_obj = open(file, mode)
    try:
        yield file_obj
    finally:
        file_obj.close()



# 1. 可以用with语句来改写 try/finally 块的逻辑，提升复用程度，并使得
# 代码更加整洁

# 2. 内置的contextlib模块提供了名叫contextmanager的修饰器，
# 开发者只需要用它来修饰自己的函数，即可令改函数支持 with语句

# 3. 情景管理器可以通过yield语句向with语句返回一个值，此值
# 会赋给由as关键字指定的变量，改机制阐明了这个特殊情景的编写动机
# 并令 with 块中的语句可以直接访问这个目标变量
