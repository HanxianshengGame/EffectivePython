#!/usr/bin/env python27
# -*- coding: utf-8 -*-
# @Time    : 2021/6/24 15:51
# @Author  : handling
# @File    : 5.1_用subprocess模块来管理子进程.py
# @Software: PyCharm
import os
import subprocess

# 基本的运行子进程

# 开启子进程并执行
# args参数。可以是一个字符串，可以是一个包含程序参数的列表。要执行的程序一般就是这个列表的第一项，或者是字符串本身。
#
# proc = subprocess.Popen(
# 		['echo', 'Hello from the child!'],
# 		stdout=subprocess.PIPE,
# 		stdin=subprocess.PIPE,
# 		shell=True)
# out, err = proc.communicate()  # 进行交流，返回标准输出与标准错误
# print(out.decode('utf-8'))
#
# # 子进程状态  poll检查子进程是否已结束，设置并返回returncode属性。
# proc = subprocess.Popen(['sleep', '0.3'], shell=True)
# while proc.poll() is None:
# 	print('Working....')
#
# print('Exit status', proc.poll())


# 把子进程从父进程剥离管理
from time import time


def run_sleep(period):
    proc = subprocess.Popen(['sleep', str(period)], shell=True)
    return proc


start = time()
procs = []
for _ in range(10):
    proc = run_sleep(0.1)
    procs.append(proc)

for proc in procs:
    proc.communicate()
end = time()
print('Finished in %.3f seconds' % (end - start))


# 与子进程输送数据，并获取子进程的输出数据

def run_openssl(data):
    env = os.environ.copy()
    env['password'] = b''
    proc = subprocess.Popen(
            ['openss'], 'enc', '',
            env=env,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE
    )
    proc.stdin.write(data)
    proc.stdin.flush()
    return proc


# 1. 可以用subprocess模块运行子进程，并管理其输入流与输出流
# 2. Python解释器能够平行运行多条子进程，这使得开发者可以充分利用CPU的处理能力
# 3. 可以给communicate方法传入 timeout 参数，以避免子进程死锁或失去响应（python3）

