'''
!/usr/bin/env python
 _*_coding:utf-8 _*_
@Time    : 2019/11/29 9:36
@Author  :Zhangyunjia
@FileName:  7.2 分块.py
@Software: PyCharm
'''

import nltk

# 1.基于正则表达式的NP分块器的例子

sentence = [("the", "DT"), ("little", "JJ"), ("yellow", "JJ"), ("dog", "NN"), ("barked", "VBD"), ("at", "IN"),
            ("the", "DT"), ("cat", "NN")]

grammar = 'NP: {<DT>?<JJ>*<NN>}'

cp = nltk.RegexpParser(grammar)
result = cp.parse(sentence)
print('分块结果： ', result)
# result.draw()

# 2.由2个规则组成的简单的分块语法
sentence2 = [("Rapunzel", "NNP"), ("let", "VBD"), ("down", "RP"),
             ("her", "PP$"), ("long", "JJ"), ("golden", "JJ"), ("hair", "NN")]

grammar2 = r"""
  NP: {<DT|PP\$>?<JJ>*<NN>}   # chunk determiner/possessive, adjectives and noun
      {<NNP>+}                # chunk sequences of proper nouns
"""
cp2 = nltk.RegexpParser(grammar2)
result2 = cp2.parse(sentence2)
print('result2: ', result2)

# 3.分块的小栗子:{<V.*> <TO> <V.*>}
cp3 = nltk.RegexpParser('CHUNK: {<V.*> <TO> <V.*>}')
brown = nltk.corpus.brown
for sent in brown.tagged_sents():
    tree = cp3.parse(sent)
    for subtree in tree.subtrees():
        # print(subtree.label())
        if subtree.label() == 'CHUNK':
            print(subtree)

# 4.简单的加缝器
sentence4 = [("the", "DT"), ("little", "JJ"), ("yellow", "JJ"), ("dog", "NN"), ("barked", "VBD"), ("at", "IN"),
             ("the", "DT"), ("cat", "NN")]

grammar4 = r'''
NP:
{<.*>+}       #Chunk everything
}<VBD|IN>+{   #Chink sequences of VBD and IN
'''

cp4 = nltk.RegexpParser(grammar4)
result4 = cp4.parse(sentence4)
print('result4: ',result4)
