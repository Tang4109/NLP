'''
!/usr/bin/env python
 _*_coding:utf-8 _*_
@Time    :2019/11/15 16:52
@Author  :Zhangyunjia
@FileName: 3.9 格式化-从链表到字符串.py
@Software: PyCharm
'''
from __future__ import division
import nltk, re, pprint

# 1.从链表到字符串
silly = ['I', 'am', 'ZYJ', '.']
x1 = ' '.join(silly)
print(x1)

x2 = ';'.join(silly)
print(x2)

x3 = ''.join(silly)
print(x3)

# 2.字符串与格式
print('//////////////////////////////////')
word = 'cat'
sentence = """hello
world
"""
print(word)
print(sentence)

print('//////////////////////////////////')
fdist = nltk.FreqDist(['dog', 'cat', 'dog', 'cat', 'dog', 'snake', 'dog', 'cat'])
for word in fdist:
    print(word, '->', fdist[word], ';')

print('//////////////////////////////////')
for word in fdist:
    print('%s->%d;' % (word, fdist[word]))

print('//////////////////////////////////////')
template = 'Lee wants a %s right now'
menu = ['sandwich', 'spam fritter', 'pancake']
for snack in menu:
    print(template % snack)

# 3.排列
print('////////////////////////////////////////////')
count, total = 3205, 9375
x4 = "accuracy for %d words: %2.4f%%" % (total, 100 * count / total)
print(x4)

print('////////////////////////////////////////////')


def tabulate(cfdist, words, categories):
    print('%-16s' % 'category')
    for word in words:
        print('%6s' % word)
    print()
    for category in categories:
        print('%-16s' % category, )  # row heading
        for word in words:  # for each word
            print('%6d' % cfdist[category][word], )  # print table cell
        print()


from nltk.corpus import brown

cfd = nltk.ConditionalFreqDist((genre, word) for genre in brown.categories() for word in brown.words(categories=genre))
genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
modals = ['can', 'could', 'may', 'might', 'must', 'will']
tabulate(cfd, modals, genres)