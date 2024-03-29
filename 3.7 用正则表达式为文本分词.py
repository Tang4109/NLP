'''
!/usr/bin/env python
 _*_coding:utf-8 _*_
@Time    :2019/11/14 14:55
@Author  :Zhangyunjia
@FileName: 3.7 用正则表达式为文本分词.py
@Software: PyCharm
'''
from __future__ import division
import nltk, re, pprint

# 1.定义数据
raw = '''It so chanced, that after the Parsee's disappearance, I was he whom
the Fates ordained to take the place of Ahab's bowsman, when that
bowsman assumed the vacant post; the same, who, when on the last day
the three men were tossed from out of the rocking boat, was dropped
picked me up at last.  It was the devious-cruising Rachel, that in
her retracing search after her missing children, only found another
orphan.
'''
# 2.分词的简单方法
x1 = re.split(r'\s+', raw)
print(x1)
x2 = re.findall(r'\w+|\S\w*', raw)
print(x2)

# 3.NLTK的正则表达式分词器
print('/////////////////////////////////////////////')
text = 'That U.S.A. poster-print costs $12.40... 8% ? _'
pattern = r"""(?x)#set flag to allow verbose regexps
(?:[A-Z]\.)+      #123
|\$?\d+(?:\.\d+)?%? #789
|\w+(?:-\w+)*     #456
|\.\.\.           #1111
|[][.,;"'?():-_`] #2222
"""
x3 = nltk.regexp_tokenize(text, pattern)
print(x3)

x4 = re.findall(r'^.*(ing|ly|ed|ious|ies|ive|es|s|ment)$', 'languageious')
print(x4)
