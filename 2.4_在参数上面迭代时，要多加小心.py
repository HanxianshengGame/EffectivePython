#!/usr/bin/env python27
# -*- coding: utf-8 -*-
# @Time    : 2021/6/2 13:23
# @Author  : handling
# @File    : 2.4_在参数上面迭代时，要多加小心.py
# @Software: PyCharm


def normalize(numbers):
    total = sum(numbers)  # 这里已经迭代完抛出 StopIteration异常
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)


it = read_visits('numbers.txt')
percentages = normalize(it)
print(percentages)


# 上面的结果应该是[],因为迭代器已经失效，在 sum（）函数后


# 自定义容器类型: 把__iter__方法实现为生成器

# 在执行类似 for x in foo这样的语句时， python实际上会调用 iter(foo), 内置的
# iter函数又会调用 foo.__iter__这个特殊方法，该方法必须返回迭代器对象，
# 只需要令 __iter__ 方法实现为生成器，就能在 for x in foo这样的多次遍历中生成新的迭代器，避免失效

class ReadVisits(object):
    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)


visits = ReadVisits(data_path='numbers.txt')
percentages = normalize(visits)
print(percentages)


# 迭代器协议有这样的约定： 如果把迭代器对象传给内置的iter函数，那么该函数会把
# 迭代器返回，反之，如果传给iter函数的是个容器类型的对象，那么iter函数则每次都会
# 返回新的迭代器对象, 于是，根据iter的这种行为来判断输入值是不是迭代器对象本身，来
# 避免迭代器失效的问题


def normalize_defensive(numbers):
    if iter(numbers) is iter(numbers):
        raise TypeError('Must supply a container')
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


# 总结
# 1. 函数在输入的参数上面多次迭代应该小心：如果是迭代器，有可能导致
# 奇怪的行为而丢失值
# 2. python 的迭代器协议，描述了容器和迭代器应该如何与iter和next内置函数，for循环
# 及相关表达式相互配合
# 3. 把 __iter__方法实现为生成器，即可定义自己的容器类型
# 4. 想判断某个值是迭代器还是容器，可以拿该值为参数，两次调用iter函数，若结果相同
# ，则是迭代器，调用内置的next函数，即可令该迭代器前进一步