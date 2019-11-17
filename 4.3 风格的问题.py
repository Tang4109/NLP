'''
!/usr/bin/env python
 _*_coding:utf-8 _*_
@Time    :2019/11/16 15:39
@Author  :Zhangyunjia
@FileName: 4.3 风格的问题.py
@Software: PyCharm
'''
from __future__ import division
import nltk, re, pprint

# 1.sorted(set(tokens))
tokens = ['racter', 'set', 'encoding', ':', 'UTF-8', '***', 'START', 'OF', 'THIS', 'PROJECT']
word_list = []
# 初始化
word_list.insert(0, tokens[0])

len_word_list = len(word_list)

i = 1
while (i < len(tokens)):
    j = 0
    while j < len_word_list and word_list[j] < tokens[i]:
        j += 1
    print('i:', i)
    if j == 1 or tokens[i] != word_list[j]:
        word_list.insert(j, tokens[i])
        len_word_list += 1
    i += 1

print(word_list)

word_list = sorted(set(tokens))
print(word_list)

# 2.循环计数器
print('/////////////////////////////////////////////////')
fd = nltk.FreqDist(nltk.corpus.brown.words())
cumulative = 0.0
for rank, word in enumerate(fd):
    cumulative += fd[word] * 100 / fd.N()
    print('%3d %6.2f%% %s' % (rank + 1, cumulative, word))
    if cumulative > 25:
        break

# 3.使用循环变量找出文本中最长的一个词
print('找出文本中最长的词: ')
text = nltk.corpus.gutenberg.words('milton-paradise.txt')
longest = ''
for word in text:
    if len(word) > len(longest):
        longest = word
print(longest)

# 4.使用两个链表推导式找出文本中最长的词们
print('使用两个链表推导式找出文本中最长的词们: ')
maxlen = max(len(word) for word in text)
longests = [word for word in text if len(word) == maxlen]
print(longests)

# 5.链表推导式中使用循环变量
print('使用循环变量来提取链表中的连续重叠的n-grams: ')
sent = ['1', '2', '3', '4', '5', '6']
n = 3
sents = [sent[i:i + n] for i in range(len(sent) - n + 1)]
print(sents)
print(nltk.ngrams(sent, 3))

# 6.使用循环变量构建多维结构
print('使用循环变量构建多维结构: ')
m, n = 3, 7
array = [[set() for i in range(n)] for j in range(m)]
array[2][5].add('Alice')
pprint.pprint(array)
