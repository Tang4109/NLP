'''
!/usr/bin/env python
 _*_coding:utf-8 _*_
@Time    :2019/11/13 10:01
@Author  :Zhangyunjia
@FileName: 3.1.6 捕获用户输入.py
@Software: PyCharm
'''
from __future__ import division
import nltk, re, pprint

from click._compat import raw_input

s=raw_input('Enter some text: ')

print('You typed ',len(nltk.word_tokenize(s)),'words')
print(s)