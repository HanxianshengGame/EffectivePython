#!/usr/bin/env python27
# -*- coding: utf-8 -*-
# @Time    : 2021/6/23 14:13
# @Author  : handling
# @File    : 4.3_用描述符来改写需要复用的@property.py
# @Software: PyCharm


# 代码中的属性有时具备相同的@property表现，但是也算要写给定的属性描述，没有
# 达到复用的目的，因此我们使用描述符来
from weakref import WeakKeyDictionary


class Grade(object):
	def __get__(*args, **kwargs):
		pass

	def __set__(*args, **kwargs):
		pass


class Exam(object):
	math_grade = Grade()
	writing_grade = Grade()
	science_grade = Grade()


exam = Exam()
exam.writing_grade = 40
# Exam.__dict__['writing_grade'].__set__(exam, 40)

print(exam.writing_grade)


# Exam.__dict__['writing_grade'].__get__(exam, Exam)

# 转义规则： 如果exam实例没有名字为writing_grade的属性，那么python就会转向Exam类，
# 并在该类中查找同名的类属性， 这个类属性，如果是实现了__get__ 和 __set__方法的对象，
# 那么python就认为该对象遵从描述符协议


# 我们使用弱引用字典来解决内存泄露问题，以及实例共享 Grade的处理方案

class GradeNew(object):
	def __init__(self):
		self._values = WeakKeyDictionary()

	def __get__(self, instance, instance_type):
		if instance is None:
			return self
		return self._values.get(instance, 0)

	def __set__(self, instance, value):
		if not (0 <= value <= 100):
			raise ValueError('Grade must be between 0 and 100')
		self._values[instance] = value


class Exam(object):
	math_grade = GradeNew()
	writing_grade = GradeNew()
	science_grade = GradeNew()


# 如果想要复用@property方法与其验证机制，可以自己定义描述符类
# WeakKeyDictionary 可以保证描述符类不会内存泄露
# 通过描述符协议来实现属性的获取和设置操作时，不要纠结于__getattrbute__的方法与具体运作细节
