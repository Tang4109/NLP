'''
!/usr/bin/env python
 _*_coding:utf-8 _*_
@Time    :2019/11/7 6:58
@Author  :Zhangyunjia
@FileName: 最有可能跟在给定词后面的词.py
@Software: PyCharm
'''

import nltk
from nltk.book import *

def generate_model(cfdist,word,num=15):
    for i in range(num):
        print(word)
        word=cfdist[word].max()

text=nltk.corpus.genesis.words('english-kjv.txt')
bigrams=nltk.bigrams(text)
cfd=nltk.ConditionalFreqDist(bigrams)
print(cfd['living'])
print(generate_model(cfd,'living'))


