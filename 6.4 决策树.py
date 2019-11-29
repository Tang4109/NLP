'''
!/usr/bin/env python
 _*_coding:utf-8 _*_
@Time    : 2019/11/26 10:38
@Author  :Zhangyunjia
@FileName:  6.4 决策树.py
@Software: PyCharm
'''
import nltk
# 1.计算标签链表的熵
import math


# 1.计算标签链表的熵
def entropy(labels):
    freqdist = nltk.FreqDist(labels)

    # print('freqdist.items(): ', freqdist.items())
    # print("freqdist['male']: ", freqdist['male'])

    probs = [freqdist.freq(l) for l in nltk.FreqDist(labels)]
    # print('probs: ', probs)
    result = -sum([p * math.log(p, 2) for p in probs])
    # print('result: ',result)
    return result


entropy_ = entropy(['fmale', 'female', 'male', 'xmale'])
print('entropy_: ', entropy_)
