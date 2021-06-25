#!/usr/bin/env python27
# -*- coding: utf-8 -*-
# @Time    : 2021/6/24 16:56
# @Author  : handling
# @File    : 5.4_考虑用协程来并发地运行多个函数.py
# @Software: PyCharm


# 线程的缺点
# 1. 线程安全需要维护
# 2. 线程占用大量的内存
# 3. 线程启动时的开销比较大

# python 中的携程