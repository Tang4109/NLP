'''
!/usr/bin/env python
 _*_coding:utf-8 _*_
@Time    :2019/11/13 8:31
@Author  :Zhangyunjia
@FileName: 处理RSS订阅.py
@Software: PyCharm
'''
#第三方python库：通用输入解析器
import feedparser
llog=feedparser.parse('http://languagelog.ldc.upenn.edu/nll/?feed=atom')

print(llog['feed']['title'])
print(len(llog.entries))
print(llog.entries)

post = llog.entries[2]
print(post)
print(post.title)

content=post.content[0].value
print(content[:100])

print('//////////////////////////////////////')

#获取纯文本数据
import nltk
from bs4 import BeautifulSoup
soup=BeautifulSoup(content)
text=soup.get_text()
#分词
tokens = nltk.word_tokenize(text)
print(tokens)