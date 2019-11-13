'''
!/usr/bin/env python
 _*_coding:utf-8 _*_
@Time    :2019/11/13 8:58
@Author  :Zhangyunjia
@FileName: 3.1.4 读取本地文件.py
@Software: PyCharm
'''

from __future__ import division
import nltk, re, pprint

f = open('document.txt','r')
for line in f:
    print(line.strip())

# raw = f.read()
# print(raw)

#检查当前目录
import os
path=os.listdir('.')
print(path)
print('////////////////////////////////////////////////////////')
#读取NLTK中的语料库文件
path=nltk.data.find('corpora/gutenberg/melville-moby_dick.txt')
raw=open(path,'r').read()
print(raw)






