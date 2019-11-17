'''
!/usr/bin/env python
 _*_coding:utf-8 _*_
@Time    :2019/11/17 17:07
@Author  :Zhangyunjia
@FileName: 4.4 函数-结构化编程的基础.py
@Software: PyCharm
'''
from __future__ import division

from urllib.request import urlopen

import nltk, re, pprint
from bs4 import BeautifulSoup

url = "http://www.archives.gov/national-archives-experience/charters/constitution_transcript.html"

# 计算高频词的函数

# def freq_words(url):
#     freqdist = nltk.FreqDist()
#     soup=BeautifulSoup(url)
#     text = soup.get_text()
#     for word in nltk.word_tokenize(text):
#         freqdist.inc(word.lower())
#     return freqdist
#
#
# fd = freq_words(constitution)
# print(fd.keys()[:20])
html=urlopen(url).read()
soup = BeautifulSoup(html)
text = soup.get_text()
words = nltk.word_tokenize(text)
fd = nltk.FreqDist(word.lower() for word in words)
print(type(fd.keys()))
print(list(fd.keys())[:20])


