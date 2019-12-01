'''
!/usr/bin/env python
 _*_coding:utf-8 _*_
@Time    : 2019/12/1 10:48
@Author  :Zhangyunjia
@FileName:  8.5 依存关系和依存文法.py
@Software: PyCharm
'''

import nltk

# 1.捕捉依存关系信息
groucho_dep_grammar = nltk.DependencyGrammar.fromstring("""
'shot' -> 'I' | 'elephant' | 'in'
'elephant' -> 'an' | 'in'
'in' -> 'pajamas'
'pajamas' -> 'my'
""")

print(groucho_dep_grammar)

# 2.捕捉附着歧义
pdp = nltk.ProjectiveDependencyParser(groucho_dep_grammar)
sent = 'I shot an elephant in my pajamas'.split()
# print(sent)
trees = pdp.parse(sent)
for tree in trees:
    print(tree)

