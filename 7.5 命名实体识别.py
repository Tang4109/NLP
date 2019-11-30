'''
!/usr/bin/env python
 _*_coding:utf-8 _*_
@Time    : 2019/11/30 14:48
@Author  :Zhangyunjia
@FileName:  7.5 命名实体识别.py
@Software: PyCharm
'''

import nltk

sent = nltk.corpus.treebank.tagged_sents()[22]
print(sent)
x1 = nltk.ne_chunk(sent, binary=True)
print('x1: ',x1)

print()
x1_2 = nltk.ne_chunk(sent)
print('x1_2: ',x1_2)
