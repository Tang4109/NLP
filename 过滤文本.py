'''
!/usr/bin/env python
 _*_coding:utf-8 _*_
@Time    :2019/11/8 16:32
@Author  :Zhangyunjia
@FileName: 过滤文本.py
@Software: PyCharm
'''
def unusual_words(text):
    text_vocab=set(w.lower() for w in text if w.isalpha())

