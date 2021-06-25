#!/usr/bin/env python27
# -*- coding: utf-8 -*-
# @Time    : 2021/6/23 11:11
# @Author  : handling
# @File    : 3.4_用super初始化父类.py
# @Software: PyCharm

# 菱形继承会带来多次基类构造器的调用，导致结果与预期有偏差
# python 2.2 增加了内置的super函数，并且重新定义了方法解析的顺序
# (以标准的流程来安排超类之间的初始化顺序（深度优先，从左至右），也保证了钻石顶部那个公共基类的
# __init__方法只会运行一次)

class MyBaseClass(object):
    def __init__(self, value):
        self.value = value


class TimesFiveCorrect(MyBaseClass):
    def __init__(self, value):
        super(TimesFiveCorrect, self).__init__(value)
        self.value *= 5


class PlusTwoCorrect(MyBaseClass):
    def __init__(self, value):
        super(PlusTwoCorrect, self).__init__(value)
        self.value += 2


class GoodWay(TimesFiveCorrect, PlusTwoCorrect):
    def __init__(self, value):
        super(GoodWay, self).__init__(value)

foo = GoodWay(5)
print foo.value
from  pprint import pprint
pprint(GoodWay.mro())


# 先调用 TimeFiveCorrect 的__init__，又会调用PlusTwoCorrect.__init__, PlusTwoCorrect
# .__init__会调用到 MyBaseClass.__init__(), 到达了钻石体系的顶部后，所有的初始化方法会按照
# 与上述顺序相反的顺序来运作


# python2 中的问题注意点：
# super语句写起来费解麻烦

# python采用标准的方法解析来解决菱形继承问题