#!/usr/bin/env python27
# -*- coding: utf-8 -*-
# @Time    : 2021/6/23 13:07
# @Author  : handling
# @File    : 4.1_用纯属性取代get和set方法.py
# @Software: PyCharm

class Resistor(object):
    def __init__(self, ohms):
        self.ohms = ohms
        self.voltage = 0
        self.current = 0


class VoltageResistance(Resistor):
    def __init__(self, ohms):
        super(VoltageResistance, self).__init__(ohms)
        self._voltage = 0

    @property
    def voltage(self):
        return self._voltage

    @voltage.setter
    def voltage(self, voltage):
        self._voltage = voltage
        self.current = self._voltage / self.ohms


# @property的最大缺点： 和属性相关的方法，只能在子类里共享，与之无关的其他类，无法复用同一份
# 实现代码, 描述符机制可以来复用与属性有关的逻辑


# 总结：
# 1. 编写新类时，应该用简单的public属性来定义其接口，而不要手工实现
# set和get方法
# 2. 如果访问对象的某个属性时，需要表现出特殊的行为，就用@property来定义
# 3. @property方法应该遵循最小惊讶原则，不应该残生奇怪的副作用
# 4. property方法需要执行得迅速一点，缓慢或复杂的工作，放在普通的方法里面


