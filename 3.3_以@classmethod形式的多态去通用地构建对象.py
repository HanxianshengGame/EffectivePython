#!/usr/bin/env python27
# -*- coding: utf-8 -*-
# @Time    : 2021/6/9 11:55
# @Author  : handling
# @File    : 3.3_以@classmethod形式的多态去通用地构建对象.py
# @Software: PyCharm

# 多态，使得继承体系中的多个类都能以各自所独有的方式来实现某个方法。
# 这些类，都满足相同的接口或继承自相同的抽象类，但却有着各自不同的功能
import os
import threading


class InputData(object):
    def read(self):
        raise NotImplementedError


class PathInputData(InputData):
    def __init__(self, path):
        InputData.__init__(self)
        self.path = path

    def read(self):
        return open(self.path).read()


class Worker(object):
    def __init__(self, input_data):
        self.input_data = input_data
        self.result = None

    def map(self):
        raise NotImplementedError

    def reduce(self, other):
        raise NotImplementedError


class LineCountWorker(Worker):
    def map(self):
        data = self.input_data.read()
        self.result = data.count('\n')

    def reduce(self, other):
        self.result += other.result


def generate_inputs(data_dir):
    for name in os.listdir(data_dir):
        yield PathInputData(os.path.join(data_dir, name))


def create_worker(input_list):
    workers = []
    for input_data in input_list:
        workers.append(LineCountWorker(input_data))
    return workers


def execute(workers):
    threads = [threading.Thread(target=w.map) for w in workers]
    for thread in threads: thread.start()
    for thread in threads: thread.join()
    first, rest = workers[0], workers[1:]
    for worker in rest:
        first.reduce(worker)
    return first.result


def mapreduce(data_dir):
    inputs = generate_inputs(data_dir)
    workers = create_worker(inputs)
    return execute(workers)


from tempfile import TemporaryDirectory


def write_test_files(tmpdir):
    # ...
    pass


with TemporaryDirectory() as tmpdir:
    write_test_files(tmpdir)
    result = mapreduce(tmpdir)

print('There are', result, 'lines')


# 在python程序中，每个类只能有一个构造器，即 __init__
# 通过@classmethod机制，可以用一种与构造器相仿的方式来构造类的对象。
# 通过类方法多态机制， 我们能够以更加通用的方式来构建并拼接具体的子类。

