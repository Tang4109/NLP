'''
!/usr/bin/env python
 _*_coding:utf-8 _*_
@Time    :2019/11/13 14:09
@Author  :Zhangyunjia
@FileName: 3.3 使用Unicode进行文字处理.py
@Software: PyCharm
'''
from __future__ import division
import nltk, re, pprint
import codecs

# 1.codecs模块
path = nltk.data.find('corpora/unicode_samples/polish-lat2.txt')
f = codecs.open(path, encoding='latin2')
for line in f:
    line = line.strip()
    print(line)
    # python特定的编码
    print(line.encode('unicode_escape'))

# 2.Unicode字符
print('//////////////////////////////////////////////')
print(ord('a'))
print('\u0061')
print(u'\u0061')

# 3.repr()转化字符串
print('//////////////////////////////////////////////')
nacute = u'\u0144'
nacute_utf = nacute.encode('utf8')
print(repr(nacute))

# 4.Unicodedata模块
print('//////////////////////////////////////////////')
import unicodedata

lines = codecs.open(path, encoding='latin2').readlines()
line = lines[2]
for c in line:
    if ord(c) > 127:
        print('%r U+%04x %s' % (c.encode('utf8'), ord(c), unicodedata.name(c)))

print('/////////////////////////////////////////////////')
print(line)
print(line.find(u'zosta\u0142y'))
line = line.lower()
print(line)
print(line.encode('unicode_escape'))
print('//////////////////////////////////////////////////')
# 5.re模块
m=re.search(u'\u015b\w*',line)
print(m.group())

print('//////////////////////////////////////////////////')
print(nltk.word_tokenize(line))

