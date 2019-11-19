'''
!/usr/bin/env python
 _*_coding:utf-8 _*_
@Time    :2019/11/18 16:42
@Author  :Zhangyunjia
@FileName: 4.6 程序开发.py
@Software: PyCharm
'''
from __future__ import division
import nltk, re, pprint


# 函数创建时，创建默认值只创建一次,
# 如果没有给函数提供明确的值，就会一直使用该值

def find_words(text, wordlength, result=[]):
    for word in text:
        if len(word) == wordlength:
            result.append(word)
    return result


x1 = find_words(['it', 'is', 'a', 'good', 'thing'], 4)
print(x1)

x2 = find_words(['it', 'is', 'a', 'good', 'thing'], 4)
print(x2)

x3 = find_words(['it', 'is', 'a', 'good', 'thing'], 4, ['oo'])
print(x3)

