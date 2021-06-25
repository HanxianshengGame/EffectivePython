#!/usr/bin/env python27
# -*- coding: utf-8 -*-
# @Time    : 2021/6/23 11:59
# @Author  : handling
# @File    : 3.5_多用public属性，少用private属性.py
# @Software: PyCharm

class ApiClass(object):
    def __init__(self):
        self.__value = 5

    def get(self):
        return self.__value


class Child(ApiClass):
    def __init__(self):
        super(Child, self).__init__()
        self._value = 'hello'  # 'ok'


# 1. python 编辑器无法严格保证private字段的私密性
# 2. 不要盲目将属性设置为private， 而是应该从一开始就做好规划，并允许
# 子类更多地访问超类的内部API
# 3. 应该多用protected属性，并在文档中把这些字段的合理用法告诉子类的开发者
# 而不要试图用private属性来限制子类访问这些字段
# 4. 只有当子类不受自己控制时，才可以考虑用private属性来避免名称冲突。
