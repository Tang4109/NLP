'''
!/usr/bin/env python
 _*_coding:utf-8 _*_
@Time    :2019/11/16 13:24
@Author  :Zhangyunjia
@FileName: 4.2 序列.py
@Software: PyCharm
'''
from __future__ import division
import nltk, re, pprint

# 1.元组+字符串、链表
t = 'walk',
print(t)

# 2.合并不同类型的序列
words = 'I turned off the djdhffhfh'.split()
print(words)
wordlens = [(len(word), word) for word in words]
print(wordlens)
print(wordlens.sort())
print(' '.join(w for (_, w) in wordlens))

# 3.产生器表达式
print('////////////////////////////////////////')
text = '''
this is a good thing 
it is so interesting.
'''
x1 = [w.lower() for w in nltk.word_tokenize(text)]
print(x1)
x2 = max(x1)
print(x2)
# 产生器表达式效率更高
x3 = max(w.lower() for w in nltk.word_tokenize(text))
print(x3)
