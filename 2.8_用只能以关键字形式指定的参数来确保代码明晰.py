#!/usr/bin/env python27
# -*- coding: utf-8 -*-
# @Time    : 2021/6/2 18:54
# @Author  : handling
# @File    : 2.8_用只能以关键字形式指定的参数来确保代码明晰.py
# @Software: PyCharm


def print_args(*args, **kwargs):
    print 'Positional:', args
    print 'Keyword:   ', kwargs


print_args(1, 2, foo='bar', stuff='meep')


# 在python2中实现只能以关键字来指定的参数
# 在参数中使用 ** 操作符，并且令函数在遇到无效的调用时抛出TypeErrors异常
# 用pop方法可以把期望的关键字参数从kwargs字典中取走，也可以设置pop的第二个参数为默认值

def safe_division_d(number, divisor, **kwargs):
    ignore_overflow = kwargs.pop('ignore_overflow', False)
    ignore_zero_div = kwargs.pop('ignore_zero_division', False)
    if kwargs:
        raise TypeError('Unexpected **kwargs: {0}'.format(kwargs))


safe_division_d(1, 10)
safe_division_d(1, 0)


# 总结
# 1. 关键字参数能够使函数调用的意图更加明确
# 2. 对于各参数之间很容易混淆的函数，可以声明只能以关键字形式指定的参数，以确保调用者
# 必须通过关键字来指定它们。对于接受多个boolean的值更应该这样做
# 3. python2的函数可以接受 **kwargs参数，并手工抛出 TypeError来模拟只能以关键字形式来指定的参数