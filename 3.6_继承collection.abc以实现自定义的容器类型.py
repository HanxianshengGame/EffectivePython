#!/usr/bin/env python27
# -*- coding: utf-8 -*-
# @Time    : 2021/6/23 12:13
# @Author  : handling
# @File    : 3.6_继承collection.abc以实现自定义的容器类型.py
# @Software: PyCharm

# python 提供了内置的 collection.abc 模块，该模块定义了一系列的抽象基类，
# 提供了每一类容器类型所应该具备的常用用法, 如果有忘记实现的方法， 也会及时报错

from collections import Sequence

class BadType(Sequence):
    pass

foo = BadType()


# 如果要定制的子类较为简单，可以直接从python容器类继承
# 想正确实现自定义容器，可能编写大量的特殊方法， 可以从collections获得有效帮助