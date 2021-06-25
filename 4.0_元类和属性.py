#!/usr/bin/env python27
# -*- coding: utf-8 -*-
# @Time    : 2021/6/23 12:18
# @Author  : handling
# @File    : 4.0_元类和属性.py
# @Software: PyCharm

# metaclass 是一种高于类，又超乎类的概念
# 可以把python的class语句转译为元类， 并令其每次定义
# 具体的类时，提供独特的行为

# python 可以动态地定义对属性的访问操作， 把这些动态属性机制与
# python 的面向对象机制相结合，可以非常顺利将简单的类逐渐变换为复杂的类

# 弊端： 动态属性会覆盖对象的某些行为，从而残生一些意外副作用，要遵循最小
# 惊讶原则。


