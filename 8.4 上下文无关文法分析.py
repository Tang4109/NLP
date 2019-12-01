'''
!/usr/bin/env python
 _*_coding:utf-8 _*_
@Time    : 2019/11/30 21:49
@Author  :Zhangyunjia
@FileName:  8.4 上下文无关文法分析.py
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
# 1.递归下降解析器
print('\n递归下降解析器: ')
rd_parser = nltk.RecursiveDescentParser(grammar1)
for t in rd_parser.parse(sent):
    print(t)

# 2.移位-归约解析器
print('\n移位-归约解析器: ')
sr_parser = nltk.ShiftReduceParser(grammar1, trace=2)  # 跟踪模式
for t in sr_parser.parse(sent):
    print(t)


# 3.使用符合语句规则的子串表接收器
print('\n使用符合语句规则的子串表接收器: ')
def init_wfst(tokens, grammar):
    numtokens = len(tokens)
    # print('numtokens: ',numtokens)
    wfst = [[None for i in range(numtokens + 1)] for j in range(numtokens + 1)]
    # print('wfst: ',wfst)
    for i in range(numtokens):
        productions = grammar.productions(rhs=tokens[i])
        # print('productions: ',productions)
        wfst[i][i + 1] = productions[0].lhs()
    return wfst


def complete_wfst(wfst, tokens, grammar, trace=False):
    index = dict((p.rhs(), p.lhs()) for p in grammar.productions())
    print(index)
    numtokens = len(tokens)
    for span in range(2, numtokens + 1):
        for start in range(numtokens + 1 - span):
            end = start + span
            for mid in range(start + 1, end):
                nt1, nt2 = wfst[start][mid], wfst[mid][end]
                if nt1 and nt2 and (nt1, nt2) in index:
                    wfst[start][end] = index[(nt1, nt2)]
                    if trace:
                        print("[%s] %3s [%s] %3s [%s] ==> [%s] %3s [%s]" %
                              (start, nt1, mid, nt2, end, start, index[(nt1, nt2)], end))
    return wfst


def display(wfst, tokens):
    print('\nWFST ' + ' '.join([('%-4d' % i) for i in range(1, len(wfst))]))
    for i in range(len(wfst) - 1):
        print('%d   ' % i,end=' ')
        for j in range(1, len(wfst)):
            print('%-4s' % (wfst[i][j] or '.'),end=' ')
        print()

groucho_grammar = nltk.CFG.fromstring("""
S -> NP VP
PP -> P NP
NP -> Det N | Det N PP | 'I'
VP -> V NP | VP PP
Det -> 'an' | 'my'
N -> 'elephant' | 'pajamas'
V -> 'shot'261
P -> 'in'
""")
tokens= "I shot an elephant in my pajamas".split()
wfst0=init_wfst(tokens,groucho_grammar)
display(wfst0,tokens)

wfst1=complete_wfst(wfst0,tokens,groucho_grammar)
display(wfst1,tokens)


