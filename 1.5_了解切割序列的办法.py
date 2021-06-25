#!/usr/bin/env python27
# -*- coding: utf-8 -*-
# @Time    : 2021/6/1 10:41
# @Author  : handling
# @File    : 1.5_了解切割序列的办法.py
# @Software: PyCharm

# python 提供了序列切片操作, 很容易访问由序列中某些原始构成的子集，
#  并且其操作也延申到了 __getitem__ 和 __setitem__ 上


# 基本写法 somelist[start:end],  [start, end) 符合左闭右开原则

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print('First four:', a[:4])
print('Last four:', a[-4:])
print('Middle two:', a[3:-3])

# 注意：
# 1. 如果从开头切片，在start留空，如果取到末尾，将end留空
# 2. 指定切片起止索引时，若从列表尾部向前算，可使用负值表示

# 切割列表时， 即便start与end越界也无所谓, 利用这特性，可以限定输入序列的最大长度

first_twenty_items = a[:20]
last_twenty_items = a[-20:]

# 切割产生的效果

# 1. 在对原列表进行切割后，会产生另外一份全新的列表，系统仍然维护着指向原列表中
# 各个对象的引用。在切割后的列表进行修改，不会影响原列表

b = a[4:]
b[1] = 99
print b
print a

# 2. 赋值时对左侧列表进行切割操作,会把该列表中处在指定范围内的对象替换为新值
# 位于前篇之前和之后的那些值都保持不变
print('before ', a)
a[2:7] = [99, 27, 55]
print('after ', a)

# 3. 如果对赋值操作右侧的列表使用切片，而把起止索引留空，就会产生原列表拷贝
b = a[:]
assert b == a and b is not a

# 4. 如果对赋值左侧的列表使用切片，而不指定起止索引，系统会把右侧的新值复制一份
# ，并用这份拷贝来替换左侧列表的全部内容，而不会重新分配新的列表

b = a
print('before', a)
a[:] = [101, 102, 103]
assert a is b
print('after', a)


# 总结：
# 1. 不要写多余的代码：大概start索引为0，当end索引为序列长度时，应该将其忽略
# 2. 切片操作不会计较start与end索引是否越界， 这使得我们很容易就能从序列的前端或后端
# 开始，对其进行范围固定的切片操作
# 3. 对list赋值的时候，如果使用切片操作，就会把原列表中处在改范围的值换成新值，即便长度不同
# 也可以替换