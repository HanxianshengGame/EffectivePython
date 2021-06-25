#!/usr/bin/env python27
# -*- coding: utf-8 -*-
# @Time    : 2021/6/7 17:45
# @Author  : handling
# @File    : 3.2_简单的接口应该接受函数，而不是类的实例.py
# @Software: PyCharm
from collections import defaultdict


# 定制defaultdict类的行为，允许使用者提高函数，在查询字典时，如果没有带查询的值，就用这个函数
# 为该键创建新值， 如果没有待查询的键时，此函数必须必须返回那个键具备的默认值

def log_missing():
    print('Key added')
    return 0


current = {'green': 12, 'blue': 3}
increments = [
    ('red', 5),
    ('blue', 17),
    ('orange', 9),
]

result = defaultdict(log_missing, current)
print('Before:', dict(result))
for key, amount in increments:
    result[key] += amount
print('After:', dict(result))


# 带状态的闭包, 可以很好的和谐两个函数， 但是易读性差

def increment_with_report(current, increments):
    add_count = [0]

    def missing():
        add_count[0] += 1
        return 0

    result = defaultdict(missing, current)
    for key, amount in increments:
        result[key] += amount
    return result, add_count[0]


# 用小型类实现

class CountMissing(object):
    def __init__(self):
        self.added = 0

    def missing(self):
        self.added += 1
        return 0


counter = CountMissing()
result = defaultdict(counter.missing, current)

for key, amount in increments:
    result[key] += amount
assert counter.added == 2


# __call__ 方法强烈地暗示了该类的用途，带状态的闭包

class BetterCountMissing(object):
    def __init__(self):
        self.added = 0

    def __call__(self, *args, **kwargs):
        self.added += 1
        return 0


counter = BetterCountMissing()
counter()
assert callable(counter)
result = defaultdict(counter, current)
for key, amount in increments:
    result[key] += amount
assert counter.added == 2


# 总结：
# 1. 对于连接各种python组件的简单接口来说， 通常应该给其直接传入函数，而不是先定义某个类
# 然后再传入该类的实例
# 2. python中的函数和方法可以像一级类那样引用
# 3. 通过 __call__ 的特殊方法， 可以使得类的实例能够像普通python那样得到调用
# 4. 如果要用函数保存状态，最好定义新的类，并令其实现 __call__ 方法，而不要定义带状态的闭包