#!/usr/bin/env python27
# -*- coding: utf-8 -*-
# @Time    : 2021/6/1 13:09
# @Author  : handling
# @File    : 1.10_尽量使用enumerate取代range.py
# @Software: PyCharm

# range 在一系列整数迭代是很有效的, 但在迭代列表时,如果有须知索引的需求时
# 就显得十分乏力, 既要len取长度,用range进行遍历,还要再用idx取元素

flavor_list = ['ss', 'ss', 'sss', 'ssss']
for idx in range(len(flavor_list)):
    flavor = flavor_list[idx]


# python 提供了内置的enumerate函数,以解决该问题, enumerate把各种迭代器包装为
# 生成器, 以便稍后产生输出值,生成器每次产生一对输出值, 其中,前者代表
# 循环下标,后者表示从迭代器中取到的下一个序列元素,这样更加简洁

for idx, flavor in enumerate(flavor_list):
    print('{0}: {1}'.format(idx, flavor))

for idx, flavor in enumerate(flavor_list, 1):  # 1为起始计数点
    print('{0}: {1}'.format(idx, flavor))

# 总结:
# 1. enumerate 函数提供了一种精简的写法,可以在便利迭代器时获知每个元素的索引.
# 2. 尽量用enumerate 来改写那种将range与下表访问相结合的序列遍历代码.
# 3. 可以给 enumerate 提供第二种参数,以指定开始计数时所用的值(默认是0)