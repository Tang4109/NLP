'''
!/usr/bin/env python
 _*_coding:utf-8 _*_
@Time    :2019/11/13 10:04
@Author  :Zhangyunjia
@FileName: 3.1.7 NLP的流程.py
@Software: PyCharm
'''
from __future__ import division
import nltk, re, pprint
from urllib.request import urlopen
from bs4 import BeautifulSoup

# 1.下载网页
url = 'http://www.gutenberg.org/files/58700/58700-0.txt'
response = urlopen(url)
html = response.read().decode('utf-8')  # 返回的数据格式为bytes类型，需要decode()解码，转换成str类型
html = html[750:2300]

# 2.去除标记，剥除HTML,获得原始文本
soup = BeautifulSoup(html)
text = soup.get_text()
# print(text)

# 3.对原始文本进行分词，获得熟悉的文本结构
tokens = nltk.word_tokenize(text)
# print(type(tokens))
# 4.选择感兴趣的标识符
token = tokens[10:50]
print(token)

# 5.转换为nltk.Text对象
text_nltk = nltk.Text(token)
print(text_nltk)

# 6.将所有词汇小写并提取词汇表
words = [w.lower() for w in text_nltk]
# print(type(words))
vocab = sorted(set(words))
# print(type(vocab))
# print(vocab)
