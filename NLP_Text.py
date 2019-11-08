'''
!/usr/bin/env python
 _*_coding:utf-8 _*_
@Time    :2019/11/8 16:06
@Author  :Zhangyunjia
@FileName: NLP_Text.py
@Software: PyCharm
'''

def generate_model(cfdist,word,num=15):
    for i in range(num):
        print(word)
        word=cfdist[word].max()

def plural(word):
    if word.endswith('y'):
        return word[:-1]+'ies'
    elif word[-1] in 'sx' or word[-2:] in ['sh','ch']:
        return word+'es'
    elif(word.endswith('an')):
        return word[:-2]+'en'
    else:
        return word+'s'