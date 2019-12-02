'''
!/usr/bin/env python
 _*_coding:utf-8 _*_
@Time    : 2019/12/2 8:18
@Author  :Zhangyunjia
@FileName:  9.1 文法特征.py
@Software: PyCharm
'''

import nltk

# 1.基于特征的文法的例子
nltk.data.show_cfg('grammars/book_grammars/feat0.fcfg')

# 2.跟踪基于特征的图表分析器
print('\n跟踪基于特征的图表分析器:')
tokens = 'Kim likes children'.split()
from nltk import load_parser
cp = load_parser('grammars/book_grammars/feat0.fcfg', trace=2)
trees = cp.parse(tokens)

for tree in trees:
    print(tree)
