'''
!/usr/bin/env python
 _*_coding:utf-8 _*_
@Time    : 2019/11/30 15:07
@Author  :Zhangyunjia
@FileName:  7.6 关系抽取.py
@Software: PyCharm
'''
import nltk, re

# 1.查找关系
IN = re.compile(r'.*\bin\b(?!\b.+ing)')
for doc in nltk.corpus.ieer.parsed_docs('NYT_19980315'):
    for rel in nltk.sem.extract_rels('ORG', 'LOC', doc, corpus='ieer', pattern=IN):
        print(nltk.sem.rtuple(rel))


# 2.设计对标记敏感的模式
print('\n')
from nltk.corpus import conll2002

vnv = """
(
is/V|             # 3rd sing present and
was/V|            # past forms of the verb zijn ('be')
werd/V|           # and also present
wordt/V           # past of worden ('become')
)
.*                # followed by anything
van/Prep          # followed by van ('of')
"""

VAN = re.compile(vnv, re.VERBOSE)
for doc in conll2002.chunked_sents('ned.train'):
    for r in nltk.sem.extract_rels('PER', 'ORG', doc, corpus='conll2002', pattern=VAN):
        # print(nltk.sem.clause(r, relsym='VAN'))
        print(nltk.sem.rtuple(r,lcon=True,rcon=True))
