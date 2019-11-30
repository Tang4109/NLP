'''
!/usr/bin/env python
 _*_coding:utf-8 _*_
@Time    : 2019/11/30 10:02
@Author  :Zhangyunjia
@FileName:  7.4 语言结构中的递归.py
@Software: PyCharm
'''
import nltk

# 1. 一个分块器，处理 NP， PP， VP 和 S

grammar = r"""
NP: {<DT|JJ|NN.*>+}          # Chunk sequences of DT, JJ, NN
PP: {<IN><NP>}               # Chunk prepositions followed by NP
VP: {<VB.*><NP|PP|CLAUSE>+$} # Chunk verbs and their arguments
CLAUSE: {<NP><VP>}           # Chunk NP, VP
"""

cp1 = nltk.RegexpParser(grammar)
sentence1 = [("Mary", "NN"), ("saw", "VBD"), ("the", "DT"), ("cat", "NN"),
             ("sit", "VB"), ("on", "IN"), ("the", "DT"), ("mat", "NN")]

x1 = cp1.parse(sentence1)
print('x1: ', x1)
# 更深嵌套的句子
sentence1_2 = [("John", "NNP"), ("thinks", "VBZ"), ("Mary", "NN"), ("saw", "VBD"),
               ("the", "DT"), ("cat", "NN"), ("sit", "VB"), ("on", "IN"), ("the", "DT"), ("mat", "NN")]

x1_2 = cp1.parse(sentence1_2)
print('\nx1_2: ', x1_2)

# 用级联分块器构建嵌套结构,让分块器在它的模式中循环
cp1_2 = nltk.RegexpParser(grammar, loop=3)
x1_3 = cp1_2.parse(sentence1_2)
print('\nx1_3: ', x1_3)

# 2.在NLTK中创建树状图

print('\n在NLTK中创建树状图: ')
tree1 = nltk.Tree('NP', ['Alice'])
print('tree1: ', tree1)

tree2 = nltk.Tree('NP', ['the', 'rabbit'])
print('tree2: ', tree2)

tree3 = nltk.Tree('VP', ['chased', tree2])
print('tree3: ', tree3)

tree4 = nltk.Tree('S', [tree1, tree3])
print('tree4: ', tree4)

# 3. 构成树状图对象
print('\ntree4[0]: ', tree4[0])
print('tree4[1]: ', tree4[1])
print('tree4[1].node: ', tree4[1].label())
print('tree4.leaves(): ', tree4.leaves())
print('tree4[1][1][1]: ', tree4[1][1][1])

# tree4.draw()

# 4.使用递归函数来遍历树
print('\n使用递归函数来遍历树:')
def traverse(t):
    try:
        t.label()
        # print('\nt.label_1: ',t.label())
    except AttributeError:
        print(t,end=' ')
    else:
        # print('\nt.label_2: ',t.label())
        print('('+t.label(),end=' ')
        for child in t:
            traverse(child)
        print(')',end=' ')


t = tree4
# print(t)
traverse(t)
