'''
!/usr/bin/env python
 _*_coding:utf-8 _*_
@Time    :2019/11/13 16:30
@Author  :Zhangyunjia
@FileName: 3.4 使用正则表达式检测词组搭配.py
@Software: PyCharm
'''
from __future__ import division
import nltk, re, pprint

wordlist = [w for w in nltk.corpus.words.words('en') if w.islower()]

# 1.使用基本的元字符
wordlist1 = [w for w in wordlist if re.search('ed$', w)]
print(wordlist1)
# 2.小栗子
wordlist2 = [w for w in wordlist if re.search('^..j..t..$', w)]
print(wordlist2)

# 3.计数某些拼写出现的次数
num = sum(1 for w in wordlist if re.search('^e-?mail$', w))
print(num)

# 4.范围与闭包（输入法联想提示）
print('//////////////////////////////////////////')
wordlist3 = [w for w in wordlist if re.search('^[ghi][mno][jlk][def]$', w)]
print(wordlist3)

# 5.闭包
print('/////////////////////////////////////////////////////////')
chat_words = sorted(set(w for w in nltk.corpus.nps_chat.words()))
wordlist4 = [w for w in chat_words if re.search('^[^aeiouAEIOU]+$', w)]
print(wordlist4)

# 6.treebank
print('//////////////////////////////////////')
wsj = sorted(set(nltk.corpus.treebank.words()))
print(wsj)
wordlist5 = [w for w in wsj if re.search('^[0-9]+\.[0-9]+$', w)]
print(wordlist5)
wordlist6 = [w for w in wsj if re.search('^[A-Z]+\$$', w)]
print('^[A-Z]+\$$: ', wordlist6)

wordlist7 = [w for w in wsj if re.search('^[0-9]{4}$', w)]
print('^[0-9]{4}$: ', wordlist7)

wordlist8 = [w for w in wsj if re.search('^[0-9]+-[a-z]{3,5}$', w)]
print('^[0-9]+-[a-z]{3,5}$：', wordlist8)

wordlist10 = [w for w in wsj if re.search('^[a-z]{5,}-[a-z]{2,3}-[a-z]{,6}$', w)]
print('^[a-z]{5,}-[a-z]{2,3}-[a-z]{,6}$：', wordlist10)

wordlist11 = [w for w in wsj if re.search('(ed|ing)$', w)]
print('(ed|ing)$：', wordlist11)