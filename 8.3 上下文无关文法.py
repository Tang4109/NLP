'''
!/usr/bin/env python
 _*_coding:utf-8 _*_
@Time    : 2019/11/30 21:09
@Author  :Zhangyunjia
@FileName:  8.3 上下文无关文法.py
@Software: PyCharm
'''

import nltk

# 一个简单的文法
grammar1 = nltk.CFG.fromstring("""
S -> NP VP
VP -> V NP | V NP PP
PP -> P NP
V -> "saw" | "ate" | "walked"
NP -> "John" | "Mary" | "Bob" | Det N | Det N PP
Det -> "a" | "an" | "the" | "my"
N -> "man" | "dog" | "cat" | "telescope" | "park"
P -> "in" | "on" | "by" | "with"
""")

sent = "Mary saw Bob".split()
rd_parser = nltk.RecursiveDescentParser(grammar1)
for tree in rd_parser.parse(sent):
    print(tree)

print('\n当前使用的文法中的产生式：')
for p in grammar1.productions():
    print(p)





