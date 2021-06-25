#!/usr/bin/env python27
# -*- coding: utf-8 -*-
# @Time    : 2021/6/24 11:06
# @Author  : handling
# @File    : 4.6_用元类来注册子类.py
# @Software: PyCharm
import json


class BetterSerializable(object):
	def __init__(self, *args):
		self.args = args

	def serialize(self):
		return json.dumps({
			'class': self.__class__.__name__,
			'args': self.args
		})

	def __repr__(self):
		return str(self.args)


registry = {}


def register_class(target_class):
	registry[target_class.__name__] = target_class


def deserialize(data):
	params = json.loads(data)
	name = params['class']
	target_class = registry[name]
	return target_class(*params['args'])


class Meta(type):
	def __new__(mcs, name, bases, class_dict):
		cls = type.__new__(mcs, name, bases, class_dict)
		register_class(cls)
		return cls


# 设定元类，其继承的子类即可自动调用注册
class RegisteredSerializable(BetterSerializable):
	__metaclass__ = Meta


class Vector3D(RegisteredSerializable):
	def __init__(self, x, y, z):
		super(Vector3D, self).__init__(x, y, z)
		self.x, self.y, self.z = x, y, z


v3 = Vector3D(10, -7, 3)
print('Before:   ', v3)
data = v3.serialize()
print('Serialized:', data)
print('After:   ', deserialize(data))



# 1. 在构建模块化的 Python程序时，类的注册是一种非常有用的模式
# 2. 开发者每次从基类中继承子类时，基类的元类都可以自动运行注册代码
# 3. 通过元类来实现类的注册，可以确保所有子类都不会遗漏， 从而避免后续的错误