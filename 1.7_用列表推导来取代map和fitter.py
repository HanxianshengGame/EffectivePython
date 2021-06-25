#!/usr/bin/env python27
# -*- coding: utf-8 -*-
# @Time    : 2021/6/1 11:52
# @Author  : handling
# @File    : 1.7_用列表推导来取代map和fitter.py
# @Software: PyCharm

# 列表推导式是生成集合的最佳选择，map和fitter显得十分晦涩难懂


a = [1, 2, 3, 4, 5, 6, 7, 8]
squres = [x**2 for x in a if x % 2 == 0]  # 是map和fitter结合后的的简写版
print(squres)


# 总结：
# 1. 列表推导式比内置map和fitter函数更加清晰，无需额外编写lambda表达式
# 2. 列表推导可以跳过输入列表中的某些原始，如果改用map来做，那就必须辅以fitter方能实现
# 3. 字典和集也支持列表推导式


