'''
!/usr/bin/env python
 _*_coding:utf-8 _*_
@Time    :2019/11/12 16:17
@Author  :Zhangyunjia
@FileName: 从网络和硬盘访问文本.py
@Software: PyCharm
'''

from __future__ import division
import nltk,re,pprint
import urllib
from urllib import request
from urllib.request import urlopen
url='http://www.gutenberg.org/files/58700/58700-0.txt'
# proxy={'http':'http://www.someproxy.com:3128'}
#如果不加上下面的这行出现会出现urllib2.HTTPError: HTTP Error 403: Forbidden错误
#主要是由于该网站禁止爬虫导致的，可以在请求加上头信息，伪装成浏览器访问User-Agent,具体的信息可以通过火狐的FireBug插件查询
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
# req = urllib.request.Request(url=url, headers=headers)
# raw = urllib.request.urlopen(req).read()
response=urlopen(url)
raw = response.read().decode('utf-8')  # 返回的数据格式为bytes类型，需要decode()解码，转换成str类型
print(type(raw))
print(len(raw))
print(raw[:75])

tokens=nltk.word_tokenize(raw)
print(type(tokens))
print(len(tokens))
print(tokens[:10])

text=nltk.Text(tokens)
print(type(text))
print(text[1020:1060])



