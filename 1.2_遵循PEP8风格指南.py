#!/usr/bin/env python27
# -*- coding: utf-8 -*-
# @Time    : 2021/5/31 12:03
# @Author  : handling
# @File    : 1.2_遵循PEP8风格指南.py
# @Software: PyCharm

# 《PEP8》: 是针对Python代码格式而修订的风格指南：
# 空白：python中的空白会影响代码的含义，也会影响代码的清晰度。


# 编码风格:
# 1. 使用space来表示缩进，而不要使用tab(制表符)
# 2. 和语法相关的每一层缩进都用4个空格来表示
# 3. 每行的字符数不应该超过79
# 4. 对于占据多行的长表达式来说， 除了首行之外的其余隔行都应该在通常的缩进
# 级别上再加上4个空格。
# 5. 文件中的函数与类之间用两个空行隔开
# 6. 在使用下标来获取列表元素，调用函数或给关键字参数赋值的时候，不要在两旁
# 添加空格
# 7. 为变量赋值的时候，赋值符号的左侧与右侧应该各自写一个空格。

# 命名风格：
# 1. 函数，变量及属性应该用小写字母来拼写，各单词之间以下划线相连，
# lowercase_underscore
# 2. 受保护的实例属性，应该以单个下划线开头，_leading_underscore
# 3. 私有的实例属性，应该以两个下划线开头，例如:__double_leading_underscore
# 4. 类与异常，应该以每个单词首字母均大写的形式来命名，例如：CapitalizedWord
# 5. 模块级别的常量，应该全部采用大写字母来拼写，各单词之间以下划线相连，例如
# ALL_CAPS
# 6. 类中的实例方法（instance method） ，应该把首个参数命名为self，以表示改对象
# 自身。
# 7. 类方法（class method）的首个参数，应该命名为cls，以表示该类自身。

# 表达式和语句: 每件事都应该有直白的做法，而且最好只有一种。
# 1. 采用内联形式的否定词，而不要把否定词放在整个表达式的前面，例如，应该
# if a is not b 而不是 if not a is b

a = False
if a is not True:
    print '111'

if not a is True:
    print '111'

# 2. 不要通过检测长度的办法（如 if len(somelist) == 0） 来判断somelist
# 是否为 [] 或空值，而是应该采用 if not somelist 这种写法来判断，它会假定：
# if 空值将自动评估为False。

# 3. 不要编写单行的if语句，for循环，while循环及except符合语句，而是应该把
# 这些语句分成多行来书写，以示清晰。

# 4. import 语句应该总是放在文件开头
# 5. 引入模块的时候，总是应该使用绝对名称，而不是应该根据当前模块的路径来使用
# 相对名称，例如： 引入bar包中的foo模块时，应该完整的写出from bar import foo，而不是
# 简写为import foo
from bar import foo
# 6. 如果一定要以相对名称来编写import语句，那就采用明确的写法，from.import foo
from. import foo
# 7. 文件中那些import语句应该按顺序划分成三个部分,分别表示标准库模块,第三方模块
# 以及自用模块, 在每个部分之中应该按模块的字母顺序来排列

import math
import sys

# 注意: Pylint 是一款流行的Python源码静态分析工具,它自动检查受测的代码是否符合PEP8风格指南
# ,而且还能找出Python程序中的各种错误

# 要点:
#   1. 当编写Python代码时,总是应该遵循 PEP8风格指南
#   2. 与广大Python开发者采用同一套代码风格,可以使得项目更利于多人协作
#   3. 采用一致的风格来编写代码,可以令后续的行该工作更为容易
