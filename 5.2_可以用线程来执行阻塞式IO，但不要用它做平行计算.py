#!/usr/bin/env python27
# -*- coding: utf-8 -*-
# @Time    : 2021/6/24 16:46
# @Author  : handling
# @File    : 5.2_可以用线程来执行阻塞式IO，但不要用它做平行计算.py
# @Software: PyCharm


# 因为受到全局解释器锁的限制，多条python线程并不能在多个CPU核心上平行执行字节码
# python多线程可以轻松模拟在同一时刻执行多任务的效果
# 可以平行执行多个系统调用，这使得程序在执行阻塞式I/O操作时，执行一些运算操作
