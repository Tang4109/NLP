'''
!/usr/bin/env python
 _*_coding:utf-8 _*_
@Time    :2019/11/17 20:26
@Author  :Zhangyunjia
@FileName: 4.5 函数的高级特性.py
@Software: PyCharm
'''
from __future__ import division
import nltk, re, pprint

# 1.作为参数的函数
sent = ['it', 'is', 'a', 'good', 'boy']


def extract_property(prop):
    return [prop(word) for word in sent]


def last_letter(word):
    return word[-1]


print(extract_property(len))
print(extract_property(last_letter))

# 2.lambda表达式
print(extract_property(lambda w: w[-1]))


# 3.高阶函数filter|map
def is_content_word(word):
    return word.lower() not in ['a', 'of', 'the', 'and', 'will', ',', '.']


sent2 = ['take', 'care', 'of', 'the', 'sense', 'and', 'the', 'a', 'will', '.']
x1 = list(filter(is_content_word, sent2))
print(x1)

print('高阶函数map计算结果：//////////////////////')
lengths = list(map(len, nltk.corpus.brown.sents(categories='news')))
x2 = sum(lengths) / len(lengths)
print(x2)
print('链表推导式的计算结果：//////////////////////')
lengths2 = [len(w) for w in nltk.corpus.brown.sents(categories='news')]
x3 = sum(lengths) / len(lengths)
print(x3)

# 4.计算每个词中的元音数量
print('高阶函数map/filter计算每个词中的元音数量：//////////////////////')
x4 = list(map(lambda w: len(list(filter(lambda c: c.lower() in "aeiou", w))), sent2))
print(x4)
print('链表推导式计算每个词中的元音数量：//////////////////////')
x5 = [len([c for c in w if c.lower() in 'aeiou']) for w in sent2]
print(x5)

# 5.参数的命名
print('参数的命名：////////////////////')


def repeat(msg='<empty>', num=1):
    return msg * num


x6 = repeat(num=3, msg='zyj')
print(x6)

# 6.就地的参数链表*args/就地的关键字参数词典**kwargs
print('就地的参数链表*args/就地的关键字参数词典**kwargs:////////////////////')


def generic(*args, **kwargs):
    print(args)
    print(kwargs)


generic(1, 2, 3, 'zyj', 'zrf', age=24, name='xhh')

# 7.小栗子
song = [['four', 'calling', 'birds'],
        ['three', 'French', 'hens'],
        ['two', 'turtle', 'doves']]

print(song[0])
print(list(zip(song[0], song[1], song[2])))
print(*song)
print(list(zip(*song)))
