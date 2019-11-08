'''
!/usr/bin/env python
 _*_coding:utf-8 _*_
@Time    :2019/11/8 15:57
@Author  :Zhangyunjia
@FileName: 生成英语名词的复数形式.py
@Software: PyCharm
'''
def plural(word):
    if word.endswith('y'):
        return word[:-1]+'ies'
    elif word[-1] in 'sx' or word[-2:] in ['sh','ch']:
        return word+'es'
    elif(word.endswith('an')):
        return word[:-2]+'en'
    else:
        return word+'s'

print(plural('fairy'))
print(plural('woman'))
