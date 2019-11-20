'''
!/usr/bin/env python
 _*_coding:utf-8 _*_
@Time    :2019/11/19 21:43
@Author  :Zhangyunjia
@FileName: 5.1 词性标注器.py
@Software: PyCharm
'''
from __future__ import division
import nltk, re, pprint

# 1.词性标注器
text = nltk.word_tokenize("And now for something completely different")
x1 = nltk.pos_tag(text)
print(x1)
print('同形同音异义词：')
text = nltk.word_tokenize("They refuse to permit us to obtain the refuse permit")
x2 = nltk.pos_tag(text)
print(x2)
