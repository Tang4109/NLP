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

print('/////////////////////////////////////////////')
regexp=r'^[AEIOUaeiou]+|[AEIOUaeiou]+$|[^AEIOUaeiou]'
def compress(word):
    pieces=re.findall(regexp,word)
    return ''.join(pieces)

english_udhr=nltk.corpus.udhr.words('English-Latin1')
x2=nltk.tokenwrap( compress(w) for w in english_udhr[:75] )
print(x2)






