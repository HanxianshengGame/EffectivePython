#!/usr/bin/env python27
# -*- coding: utf-8 -*-
# @Time    : 2021/6/1 9:34
# @Author  : handling
# @File    : 1.3_了解bytes，str与unicode的区别.py
# @Software: PyCharm

import os


# UTF-8的产生，字母单字节
# 世界上存在着多种编码方式，在ANSi编码下，同一个编码值，在不同的编码体系里代表着不同的字。在简体中文系统下，ANSI 编码代表 GB2312 编码，在日文操作系统下，ANSI 编码代表 JIS
# 编码，可能最终显示的是中文，也可能显示的是日文。在ANSI
# 编码体系下，要想打开一个文本文件，不但要知道它的编码方式，还要安装有对应编码表，否则就可能无法读取或出现乱码。为什么电子邮件和网页都经常会出现乱码，就是因为信息的提供者可能是日文的ANSI
# 编码体系和信息的读取者可能是中文的编码体系，他们对同一个二进制编码值进行显示，采用了不同的编码，导致乱码。这个问题促使了unicode码的诞生。
# 如果有一种编码，将世界上所有的符号都纳入其中，无论是英文、日文、还是中文等，大家都使用这个编码表，就不会出现编码不匹配现象。每个符号对应一个唯一的编码，乱码问题就不存在了。这就是Unicode编码。
# Unicode当然是一个很大的集合，现在的规模可以容纳100多万个符号。每个符号的编码都不一样，比如，U+0639表示阿拉伯字母Ain，U+0041表示英语的大写字母A，“汉”这个字的Unicode编码是U+6C49。
# Unicode固然统一了编码方式，但是它的效率不高，比如UCS-4(Unicode的标准之一)规定用4个字节存储一个符号，那么每个英文字母前都必然有三个字节是0，这对存储和传输来说都很耗资源。
# 为了提高Unicode的编码效率，于是就出现了UTF-8编码。UTF-8可以根据不同的符号自动选择编码的长短。比如英文字母可以只用1个字节就够了。 UTF-8的编码是这样得出来的，以”汉”这个字为例：
# “汉”字的Unicode编码是U+00006C49，然后把U+00006C49通过UTF-8编码器进行编码，最后输出的UTF-8编码是E6B189。


# python2 有两种表示字符序列的类型，分别叫做str和unicode。
# 与python3不同的是，str的实例包含原始的8位值（1个字节8比特）,而unicode的实例，包含Unicode字符。


# Unicode 与 二进制数据的转换：
# Unicode->二进制（str）： encode('UTF-8')
# 二进制(str)->Unicode  ： decode('UTF-8')

# 注意： 编写程序时，一定把编码和解码放在界面外围来做，程序的核心部分使用Unicode字符类型

# python2中，编写接受str或unicode，并总是返回unicode的方法：
def to_unicode(unicode_str):
    if isinstance(unicode_str, str):
        value = unicode_str.decode('utf-8')
    else:
        value = unicode_str
    return value


def to_str(unicode_str):
    if isinstance(unicode_str, unicode):
        value = unicode_str.encode('utf-8')
    else:
        value = unicode_str

    return value


# 在使用str与Unicode字符时，需要注意两个问题：
# 1. 如果str只包含7位ASCII字符，那么Unicode和str实例似乎就成了同一类型

# - 可以使用+拼接str与unicode
# - 可以用等价与不等价进行比较str与unicode
# - 在格式字符串中，可以使用 %s 代表unicode等等

# 2. 在python3中，如果内置的open函数获取了文件描述符，则文件描述符默认采用
# utf-8编码格式来操作文件，而在python2中，文件操作的默认编码为二进制格式。

# 为了进行适配python2与python3， 我们使用 wb 或 rb模式
with open('random.bin', 'wb') as f:
    f.write(to_unicode(str(100)))
with open('random.bin', 'rb') as f:
    print f.read()


# 总结：
# 1. 在python3中，bytes是一种包含8位值的序列，str是一种包含Unicode字符的序列，
# 开发者不能以 > 或者 + 等操作符来混同操作bytes和str实例。
# 2. 在python2中，str是一种包含8位值的序列，unicode是一种包含Unicode字符的序列，
# 如果str只有7位ASCII字符，那么可以通过相关的操作来同时使用str与unicode
# 3. 在对输入的数据进行操作之前，使用辅助函数来保证字符序列的类型与开发者预期
# 相符。
# 4. 从文件中读取二进制数据，或向其中写入二进制数据时，总应该以rb或wb等二进制来开启文件
