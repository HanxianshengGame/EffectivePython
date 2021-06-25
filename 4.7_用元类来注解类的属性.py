#!/usr/bin/env python27
# -*- coding: utf-8 -*-
# @Time    : 2021/6/24 11:59
# @Author  : handling
# @File    : 4.7_用元类来注解类的属性.py
# @Software: PyCharm

# 元类的更有用的功能： 可以在某个类刚定义好但是尚未使用的时候，
# 提前修改或注解该类的属性，这种写法回合描述符搭配起来，令这些属性
# 可以更加详细地了解自己在外围类中的使用方式

class Field(object):
	def __init__(self, name):
		self.name = name
		self.internal_name = '_' + self.name

	def __get__(self, instance, instance_type):
		if instance is None:
			return self
		return getattr(instance, self.internal_name, '')

	def __set__(self, instance, value):
		setattr(instance, self.internal_name, value)


class Customer(object):
	first_name = Field('first_name')
	last_name = Field('last_name')
	prefix = Field('prefix')
	suffix = Field('suffix')


foo = Customer()
print foo.__dict__
foo.first_name = 'Euclid'
print foo.__dict__


# 下面我们用元类来注解类的属性

class Meta(type):
	def __new__(mcs, name, bases, class_dict):
		for key, value in class_dict.items():
			if isinstance(value, Field):
				value.name = key
				value.internal_name = '_' + key

		cls = type.__new__(mcs, name, bases, class_dict)
		return cls


class DatabaseRow(object):
	__metaclass__ = Meta


class Field(object):
	def __init__(self):
		self.name = None
		self.internal_name = None

	def __get__(self, instance, instance_type):
		if instance is None:
			return self
		return getattr(instance, self.internal_name, '')

	def __set__(self, instance, value):
		setattr(instance, self.internal_name, value)


class BetterCustomer(DatabaseRow):
	first_name = Field()
	last_name = Field()
	prefix = Field()
	suffix = Field()


foo = BetterCustomer()
print foo.__dict__
foo.first_name = 'Euler'
print foo.__dict__

# 借助元类，我们可以在某个类完全定义好之后， 率先修改该类的属性
# 描述符可以和元类够有效地结合起来，以便对某种行为做出装饰，或在程序运行时探查相关信息
# 如果把元类与描述符相结合，那就可以在不使用weakref模块的情况下避免内存泄露
