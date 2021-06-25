#!/usr/bin/env python27
# -*- coding: utf-8 -*-
# @Time    : 2021/6/23 13:18
# @Author  : handling
# @File    : 4.2_考虑用@property来代替属性重构.py
# @Software: PyCharm
from datetime import timedelta, datetime


class Bucket(object):
	def __init__(self, period):
		self.period_delta = timedelta(seconds=period)
		self.reset_time = datetime.now()
		self.quota = 0

	def __repr__(self):
		return 'Bucket(quota=%d)' % self.quota


def fill(bucket, amount):
	now = datetime.now()
	if now - bucket.reset_time > bucket.period_delta:
		bucket.quota = 0
		bucket.reset_time = now
	bucket.quota += amount


def deduct(bucket, amount):
	now = datetime.now()
	if now - bucket.reset_time > bucket.period_delta:
		return False
	if bucket.quota - amount < 0:
		return False
	bucket.quota -= amount
	return True


bucket = Bucket(60)
fill(bucket, 100)
print(bucket)

if deduct(bucket, 60):
	print('Had 99 quota')
else:
	print('Not enough for 99 quota')
print(bucket)


# 使用属性进行编写，可以判定bucket的状态情况

class Bucket(object):
	def __init__(self, period):
		self.period_delta = timedelta(seconds=period)
		self.reset_time = datetime.now()
		self.max_quota = 0
		self.quota_consumed = 0

	def __repr__(self):
		return 'Bucket(quota=%d)' % self.quota

	@property
	def quota(self):
		return self.max_quota - self.quota_consumed

	@quota.setter
	def quota(self, amount):
		delta = self.max_quota - amount
		if amount == 0:
			self.quota_consumed = 0
			self.max_quota = 0
		elif delta < 0:
			assert  self.quota_consumed == 0
			self.max_quota = amount
		else:
			assert  self.max_quota >= self.quota_consumed
			self.quota_consumed += delta

bucket = Bucket(60)
print('initial', bucket)
fill(bucket, 100)
print('Filled', bucket)
if deduct(bucket, 99):
	print('Had 99 quota')
else:
	print('Not enough for 99 quota')


# 总结
# 1. 利用@property可以为现有的实例属性添加新的功能
# 2. 可以用@property来逐步完善数据模型
# 3. 如果@property用的太过频繁，就应该考虑彻底重构该类，而不应该继续修补这套设计

