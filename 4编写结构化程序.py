'''
!/usr/bin/env python
 _*_coding:utf-8 _*_
@Time    :2019/11/16 10:45
@Author  :Zhangyunjia
@FileName: 4编写结构化程序.py
@Software: PyCharm
'''
from __future__ import division
import nltk, re, pprint

# 1.关于python赋值和引用
# 字符串是深复制
foo = 'zyj'
bar = foo
foo = 'zrf'
print(foo, bar)

# 链表是浅复制
print('////////////////////////////////')
foo = ['zyj', 'zrf']
bar = foo
foo[1] = 'xhh'
print(foo, bar)

# 小栗子
print('小栗子：////////////////////////')
empty = []
nested = [empty, empty, empty]
print(nested)
nested[1].append('python')
print(nested)
for n in nested:
    print(id(n))

# 小栗子
print('小栗子：////////////////////////')
nested = [[]] * 3
print(nested)
# id相同
for n in nested:
    print(id(n))

# 小栗子
print('小栗子：////////////////////////')
nested = [[], [], []]
print(nested)
# id不同
for n in nested:
    print(id(n))

# 覆盖对象引用
print('覆盖对象引用：////////////////////////')
nested = [[]] * 3
nested[1].append('python')
print(nested)
nested[1] = ['monty']  # 覆盖对象引用
print(nested)

print('//////////////////////////////////////')
width = max([len(n) for n in nested])
for n in nested:
    print('%*d' % (width, id(n)), end=' ')
# 复制链表中的对象引用
x = nested[:]
print()
for n in x:
    print('%*d' % (width, id(n)), end=' ')

import copy

# 只复制结构而不复制任何对象引用
y = copy.deepcopy(nested)
print()
for n in y:
    print('%*d' % (width, id(n)), end=' ')

# 2.等式
print('等式：///////////////////////////////////')
size = 5
python = ['Python']
snake_nest = [python] * 5
snake_nest[0] = ['Python']
for i in range(size):
    for j in range(i + 1, size):
        if (snake_nest[i] != snake_nest[j]):
            print('不相等')
        else:
            print('相等')

        if (snake_nest[i] is snake_nest[j]):
            print('is')
        else:
            print('not is')

# 3.条件语句
print('//////////////////////////////////////')
mixed = ['cat', '', ['dog'], []]
for element in mixed:
    if element:
        print(element)

print('//////////////////////////////////////')
sent = ['sdf', 'ddsgh', 'dffg', 'fgt', 'sdggh']
print(all(len(w) > 4 for w in sent))
print(any(len(w) > 4 for w in sent))
