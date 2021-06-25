#!/usr/bin/env python27
# -*- coding: utf-8 -*-
# @Time    : 2021/6/4 12:14
# @Author  : handling
# @File    : 3.1_尽量用辅助类来维护程序的状态，而不要用字典和元组.py
# @Software: PyCharm


# 总结：
# 1. 不要使用包含其他字典的字典，也不要使用过长的元组
# 2. 如果容器中包含简单而不可变的数据，那么可以先使用 nametuple 来表示
# 待稍后有需要时，再修改为完整的类
# 3. 保存内部状态的字典如果变得比较复杂，就该把这些代码拆分为多个辅助类。


import collections

Grade = collections.namedtuple('Grade', ('score', 'weight'))
grade = Grade(1, 2)
print grade.score + grade.weight
print grade[0] + grade[1]

# nametuple 的局限
# 尽管 nametuple 在很多场合都非常有用，但也有弊端
# 1. nametuple无法指定各参数的默认值，对于可选属性的数据来说不方便
# 2. nametuple 实例的各项属性，可以通过下标访问，但不利于未来迁移到类，这需要格外注意
