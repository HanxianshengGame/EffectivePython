#!/usr/bin/env python27
# -*- coding: utf-8 -*-
# @Time    : 2021/6/2 18:41
# @Author  : handling
# @File    : 2.7_用None和文档字符串来描述具有动态默认值的参数.py
# @Software: PyCharm

# 在函数内定义非静态的默认值会引发一定的问题
import json


def decode(data, default={}):
    try:
        return json.loads(data)
    except ValueError:
        return default


# 所有以默认形式来调用decode函数的代码都会共享同一份字典

foo = decode('bad data')
foo['stuff'] = 5
bar = decode('also bad')
bar['meep'] = 1
print('Foo: ', foo)
print('Bar: ', bar)  # 两次打印相同


# 这种不符合预期的做法尽量规避掉，应该使用默认值为None，且在函数的文档字符串中描述它的行为
def decode(data, default=None):
    """
    load json data from a string
    :param data: json data to decode
    :param default: value to return if decoding fails
    """
    if default is None:
        default = {}
    try:
        return json.loads(data)
    except ValueError:
        return default


# 总结：
# 1. 参数的默认值，只会在程序加载模块并读到本函数的定义时评估一次，对于{}或[]
# 等动态的值，这可能导致奇怪的行为。
# 2. 对于以动态值作为实际默认值的关键字参数来说，应该把形式上的默认值写为 None，
# 并在函数的文档字符串里面描述该默认值所对应的实际行为