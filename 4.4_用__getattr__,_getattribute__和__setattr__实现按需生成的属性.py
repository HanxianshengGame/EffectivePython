#!/usr/bin/env python27
# -*- coding: utf-8 -*-
# @Time    : 2021/6/23 15:19
# @Author  : handling
# @File    : 4.4_用__getattr__,_getattribute__和__setattr__实现按需生成的属性.py
# @Software: PyCharm

# 1. __getattr__ 会在系统对该类的实例字典中找不到待查询的属性时触发，非常适合实现无数据结构的按需访问

class LazyDB(object):
	def __init__(self):
		self.exists = 5

	def __getattr__(self, name):
		value = 'value for {0}'.format(name)
		setattr(self, name, value)
		return value


class LoggingLazyDB(LazyDB):
	def __getattr__(self, name):
		print('Called __getattr__{0}'.format(name))
		return super(LoggingLazyDB, self).__getattr__(name)


# 2. __getattribute__方法在程序每次访问（存不存在）属性时，检查全局事务状态, 是必触发事件

class ValidatingDB(object):
	def __init__(self):
		self.exists = 5

	def __getattribute__(self, name):
		# 这里也可以做属性过滤
		print('Called __getattribute__(%s)' % name)
		try:
			return super(ValidatingDB, self).__getattribute__(name)
		except AttributeError:
			value = 'Value for %s' % name
			setattr(self, name, value)
			return value


# hasattr 函数： 判断对象是否已经拥有相关的属性，并用内置的getattr来获取属性值

data = LoggingLazyDB()
print data.__dict__
print hasattr(data, 'foo')
print data.__dict__


# 注意点： 如果调用 hasattr 或者 getattr 函数，__getattribute__都会执行
#
# 只要对实例的属性赋值， 无论是直接赋值，还是通过内置的setattr函数赋值， 都会触发
# __setattr__方法

# setattr 与 getattribute注意：每次访问对象的属性们都会触发，这可能导致死循环

class BrokenDictionaryDB(object):
	def __init__(self, data):
		self._data = data

	def __getattribute__(self, name):
		print('Called __getattribute__{0}'.format(name))
		return self._data[name]  # 死循环，不停触发 __getattribute__


# 解决办法是使用 super().getattribute方法，从实例的属性字典里取得_data 属性值,
# setattr同理


class DictionaryDB(object):
	def __init__(self, data):
		self._data = data

	def __getattribute__(self, name):
		data_dict = super(DictionaryDB, self).__getattribute__('_data')
		return data_dict[name]


data = {'a': '111'}
db = DictionaryDB(data)
print db.a


# 要点
# 1. 通过 __getattr__ 和 __setattr__ ，我们可以用惰性的方式来加载并保存对象的属性
# 2. 要理解 __getattr__ 和 __getattribute__ 的区别：前者只会在待访问的属性缺失时触发，后者
# 只会在每次访问属性时触发
# 3. 如果要在 __getattribute__ 和 __setattr__方法中访问实例属性，那么直接通过 super()
# object类的同名方法来做，防止无线递归
