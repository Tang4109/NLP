'''
!/usr/bin/env python
 _*_coding:utf-8 _*_
@Time    :2019/11/13 11:12
@Author  :Zhangyunjia
@FileName: 3.2.1 字符串的基本操作.py
@Software: PyCharm
'''
from __future__ import division
import nltk, re, pprint

# 1.三重引号字符串实现两行之间的换行
couplet = '''zyj is a handsome boy.
But zrf not!
Yes,I agree.'''
print(couplet)

# 2.小栗子
a = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1]
b = [' ' * 2 * (7 - i) + 'love' * i for i in a]
for line in b:
    print(line)

# 3.小栗子,不要再行尾输出换行符
sent = 'zyj is a handsome boy.'
for char in sent:
    print(char, end=' ')
print('\n//////////////////////////////////////////')
# 4.小栗子，小写
from nltk.corpus import gutenberg

raw = gutenberg.raw('melville-moby_dick.txt')
fdist = nltk.FreqDist(ch.lower() for ch in raw if ch.isalpha())
# fdist.plot()
print(fdist.keys())

# 5.in,find,join操作符
print('\n//////////////////////////////////////////')
phrase = 'it is a good thing,or something that is interesting.'
if 'thing' in phrase:
    print('found thing')
pos = phrase.find('thing')
print(pos)
print(phrase.join(','))

