#!/usr/bin/env python27
# -*- coding: utf-8 -*-
# @Time    : 2021/6/1 12:45
# @Author  : handling
# @File    : 1.9_用生成器表达式来改写数据量比较大的列表推导.py
# @Software: PyCharm

# 列表推导的缺点：1. 在推导过程中，对于输入序列的每个值来说，可能都要创建仅含一项元素的全新列表


# 生成器表达式可以辅助解决这个问题，它是推导和生成器的一种反华，生成器在运行时
# 不会将输出序列都呈现出来，而是会估值为迭代器，这个迭代器每次可以根据生成器表达式
# 产生一项数据。
t = [1, 2, 3, 4, 5, 6]
it = (x for x in t)
for x in it:
    print x

print next(it)  # except
# 注意，生成器表达式生成的迭代器，会逐步递增且不可逆，用完一轮不能继续使用

it = (x for x in t)
roots = ((x, x ** 0.5) for x in it)
for x in roots:
    print x

list1 = [1,2,3,4]
it = (elem for elem in list1)
list1 = None
for elem in it:
    print elem

# 总结：
# 1. 当输入的数据较大时， 列表推导可能因为占用太多内存而出问题
# 2. 由生成器表达式所返回的迭代器，可以逐次产生输出值，从而避免了内存用量
# 3. 把某个生成器表达式所返回的迭代器，放在另一个生成器表达式的 for 子句中，
#    即可将二者组合起来
# 4. 串在一起的生成器表达式执行速度很快
