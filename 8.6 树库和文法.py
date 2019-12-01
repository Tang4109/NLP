'''
!/usr/bin/env python
 _*_coding:utf-8 _*_
@Time    : 2019/12/1 16:10
@Author  :Zhangyunjia
@FileName:  8.6 树库和文法.py
@Software: PyCharm
'''

import nltk

# 1.解析器根据短语结构文法在句子上建立树
from nltk.corpus import treebank

t = treebank.parsed_sents('wsj_0001.mrg')[0]
print('t: ', t)


# 2.搜索树库找出句子的补语
def filter(tree):
    child_nodes = [child.label() for child in tree if isinstance(child, nltk.Tree)]
    return (tree.label() == 'VP') and ('S' in child_nodes)


x2 = [subtree for tree in treebank.parsed_sents() for subtree in tree.subtrees(filter)]
print('x2: ', x2)

# 3.pp附着语料库
print('\npp附着语料库: ')
entries = nltk.corpus.ppattach.attachments('training')
# print('entries: ',entries)
table = nltk.defaultdict(lambda: nltk.defaultdict(set))
# print('table: ',table)
for entry in entries:
    key = entry.noun1 + '-' + entry.prep + '-' + entry.noun2
    # print('key: ',key)
    # print('entry.attachment: ',entry.attachment)
    table[key][entry.attachment].add(entry.verb)

# print('table: ',table.items())

for key in sorted(table):
    # print('key: ',key)
    if len(table[key]) > 1:
        print(key, 'N:', sorted(table[key]['N']), 'V:', sorted(table[key]['V']))

# 4.中央研究院树库语料
print('\n\n中央研究院树库语料: ')
nltk.corpus.sinica_treebank.parsed_sents()[3450].draw()

# 5.加权文法--宾州树库样本中give和gave的用法
print('\n\n宾州树库样本中give和gave的用法: ')


def give(t):
    return t.label() == 'VP' and len(t) > 2 and t[1].label() == 'NP' and (
            t[2].label() == 'PP-DTV' or t[2].label() == 'NP') \
           and ('give' in t[0].leaves() or 'gave' in t[0].leaves())


def sent(t):
    return ' '.join(token for token in t.leaves() if token[0] not in '*-0')


def print_node(t, width):
    output = '%s %s: %s / %s: %s ' % (sent(t[0]), t[1].label(), sent(t[1]), t[2].label(), sent(t[2]))
    if len(output) > width:
        output = output[:width] + '...'
    print(output)


for tree in nltk.corpus.treebank.parsed_sents():
    for t in tree.subtrees(give):
        print_node(t, 72)

# 6.定义一个概率上下文无关文法（PCFG）
print('\n定义一个概率上下文无关文法（PCFG）:')
grammar = nltk.PCFG.fromstring("""
S -> NP VP [1.0]
VP -> TV NP [0.4]
VP -> IV [0.3]
VP -> DatV NP NP [0.3]
TV -> 'saw' [1.0]
IV -> 'ate' [1.0]
DatV -> 'gave' [1.0]
NP -> 'telescopes' [0.8]
NP -> 'Jack' [0.2]
""")

print('grammar: ',grammar)
print()
viterbi_parser=nltk.ViterbiParser(grammar)
trees6 = viterbi_parser.parse(['Jack','saw','telescopes'])
for tree in trees6:
    print(tree)





