'''
!/usr/bin/env python
 _*_coding:utf-8 _*_
@Time    :2019/11/13 17:40
@Author  :Zhangyunjia
@FileName: 3.5 正则表达式的有益应用.py
@Software: PyCharm
'''
from __future__ import division
import nltk, re, pprint

# 1.提取字符块
word = 'dsjdgjrueghdjsofishROREIPjdvszkklzsdorvgh'
x1 = re.findall(r'[aeiou]', word)
print(x1)
print(len(x1))

wsj = sorted(set(nltk.corpus.treebank.words()))
fd = nltk.FreqDist(vs for word in wsj for vs in re.findall(r'[aeiou]{2,}', word))
print(fd.items())

# 2.忽略内部元音
print('/////////////////////////////////////////////')
regexp = r'^[AEIOUaeiou]+|[AEIOUaeiou]+$|[^AEIOUaeiou]'


def compress(word):
    pieces = re.findall(regexp, word)
    return ''.join(pieces)


english_udhr = nltk.corpus.udhr.words('English-Latin1')
x2 = nltk.tokenwrap(compress(w) for w in english_udhr[:75])
print(x2)

# 3.提取辅音元音序列
print('///////////////////////////////////////////////')
rotokas_words = nltk.corpus.toolbox.words('rotokas.dic')
cvs = [cv for w in rotokas_words for cv in re.findall(r'[ptksvr][aeiou]', w)]
cfd = nltk.ConditionalFreqDist(cvs)
cfd.tabulate()

# 4.nltk.Index()转为有用索引
print('///////////////////////////////////////////////')
cv_word_pairs = [(cv, w) for w in rotokas_words for cv in re.findall(r'[ptksvr][aeiou]', w)]
cv_index = nltk.Index(cv_word_pairs)
print(cv_index['ka'])
