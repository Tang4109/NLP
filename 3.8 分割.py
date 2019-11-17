'''
!/usr/bin/env python
 _*_coding:utf-8 _*_
@Time    :2019/11/15 12:37
@Author  :Zhangyunjia
@FileName: 3.8 分割.py
@Software: PyCharm
'''
from __future__ import division
import nltk, re, pprint

# 1.计算布朗语料库中每个句子的平均词数
x1 = len(nltk.corpus.brown.words()) / len(nltk.corpus.brown.sents())
print(x1)

# 2.Punkt句子分割器
sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
text = nltk.corpus.gutenberg.raw('chesterton-thursday.txt')
sents = sent_tokenizer.tokenize(text)
pprint.pprint(sents[171:181])

print('//////////////////////////////////////////////////////////')


# 3.重现分词文本

def segment(text, segs):
    words = []
    last = 0
    for i in range(len(segs)):
        if segs[i] == '1':
            words.append(text[last:i + 1])
            last = i + 1
    words.append(text[last:])
    return words


text = "doyouseethekittyseethedoggydoyoulikethekittylikethedoggy"
seg1 = "0000000000000001000000000010000000000000000100000000000"
seg2 = "0100100100100001001001000010100100010010000100010010000"
seg3 = "0000100100000011001000000110000100010000001100010000001"

x2 = segment(text, seg2)
print(x2)

print('//////////////////////////////////////////////////////////')


# 4.计算存储词典和重构源文本的成本
def evaluate(text, segs):
    words = segment(text, segs)
    text_size = len(words)
    # print(words)
    # print(set(words))
    # print(list(set(words)))
    # print(' '.join(list(set(words))))
    # print(len(' '.join(list(set(words)))))
    lexicon_size = len(' '.join(list(set(words))))
    return text_size + lexicon_size


x3 = evaluate(text, seg3)
print(x3)

# 5.使用模拟退火算法的非确定性搜索
from random import randint


def flip(segs, pos):
    # 变异单个位置
    return segs[:pos] + str(1 - int(segs[pos])) + segs[pos + 1:]


def flip_n(segs, n):
    # 变异n个位置
    for i in range(n):
        segs = flip(segs, randint(0, len(segs) - 1))
    return segs


def anneal(text, segs, iterations, cooling_rate):
    temperature = float(len(segs))
    best_segs, best = segs, evaluate(text, segs)
    while temperature > 0.5:
        for i in range(iterations):
            guess = flip_n(best_segs, int(round(temperature)))  # round-四舍五入
            score = evaluate(text, guess)
            if score < best:
                best_segs, best = guess, score
        # score, segs = best, best_segs
        temperature = temperature / cooling_rate
        # print(evaluate(text, segs), segment(text, segs))
        # print(best)

    print()
    print(best_segs,best)
    print(segment(text, best_segs))

print('x4: ///////////////////////////////////')
anneal(text,seg1,5000,1.2)
