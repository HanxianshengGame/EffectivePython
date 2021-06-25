#!/usr/bin/env python27
# -*- coding: utf-8 -*-
# @Time    : 2021/6/24 9:53
# @Author  : handling
# @File    : 4.5_用元类来验证子类.py
# @Software: PyCharm

# 元类最简单的一种用途就是验证某个类定义得是否正确。
# 其提供了一种可靠的验证方式，当开发者定义新的类时，它们都会运行验证代码，
# 确保这个新类符合预定规范, 元类的验证时机在 __init__ 之前。


# 为一般的对象定义元类： 从type中继承， 而对于使用元类的其他类来说，
# python默认会将那些类的class语句所含的相关内容，发送给元类的__new__方法,
# 于是，便可以在系统构建出那种类型之前，修改那个类的信息：

class Meta(type):
	def __new__(meta, name, bases, class_dict):
		print(meta, name, bases, class_dict)
		return type.__new__(meta, name, bases, class_dict)


def MyClass(object, metaclass=Meta):
	stuff = 123

	def foo(self):
		pass


# python2的写法有不同，是通过名为 __metaclass__的类属性来指定元类的，
# 而Meta.__new__接口则一致

class Meta(type):
	def __new__(meta, name, bases, class_dict):
		print(meta, name, bases, class_dict)
		return type.__new__(meta, name, bases, class_dict)


class MyClassInPython2(object):
	__metaclass__ = Meta


# 接下来我们来使用元类做验证，元类里所编写的验证逻辑，针对的都是该
# 基类的子类，而不是基类本身

class ValidatePolygon(type):
	def __new__(mcs, name, bases, class_dict):
		if bases != (object,):
			if class_dict['sides'] < 3:
				raise ValueError('Polygons need 3+ sides')
		return type.__new__(mcs, name, bases, class_dict)


class Polygon(object):
	__metaclass__ = ValidatePolygon
	sides = None

	@classmethod
	def interior_angles(cls):
		return (cls.sides - 2) * 180


class Triangle(Polygon):
	sides = 3



# 1. 通过元类，我们可以在生成子类对象之前，先验证子类的定义是否合乎规则
# 2. Python2 和 Python3 指定元类的语法略有不同
# 3. Python 系统把子类的整个class语句体处理完毕之后，就会调用其元类的__new__方法
