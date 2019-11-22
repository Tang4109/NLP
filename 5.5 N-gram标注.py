'''
!/usr/bin/env python
 _*_coding:utf-8 _*_
@Time    :2019/11/22 16:25
@Author  :Zhangyunjia
@FileName: 5.5 N-gram标注.py
@Software: PyCharm
'''
from __future__ import division
import nltk, re, pprint

# 1.一元标注器(Unigram Tagging)
from nltk.corpus import brown
from sklearn.model_selection import train_test_split

print('一元标注器(Unigram Tagging): ')
# 训练
brown_tagged_sents = brown.tagged_sents(categories='news')
# print('brown_tagged_sents: ',brown_tagged_sents)
unigram_tagger = nltk.UnigramTagger(brown_tagged_sents)
# print('unigram_tagger: ',unigram_tagger)
# 测试数据
brown_sents = brown.sents(categories='news')
# 预测
print('brown_sents[2007]: ', brown_sents[2007])
brown_sent_tagged_2007 = unigram_tagger.tag(brown_sents[2007])
print('brown_sent_tagged_2007: ', brown_sent_tagged_2007)
print('brown_tagged_sents[2007]: ', brown_tagged_sents[2007])

print('总体评估： ', unigram_tagger.evaluate(brown_tagged_sents))

# 2.分离训练和测试数据：
print('\n分离训练和测试数据：')
size = int(len(brown_tagged_sents) * 0.9)
train_sents = brown_tagged_sents[:size]
test_cents = brown_tagged_sents[size:]

# train_sents, test_cents = train_test_split(brown_tagged_sents, random_state=0)
print('len of train_sents and test_cents: ', len(train_sents), len(test_cents))

unigram_tagger = nltk.UnigramTagger(train_sents)
score_test = unigram_tagger.evaluate(test_cents)
print('score_test: ', score_test)

# 2.bigram标注器
print('\nbigram标注器：')
bigram_tagger = nltk.BigramTagger(train_sents)
brown_sent_bigram_tagger_2007 = bigram_tagger.tag(brown_sents[2007])
brown_sent_bigram_tagger_4203 = bigram_tagger.tag(brown_sents[4203])
print('brown_sent_bigram_tagger_2007: ', brown_sent_bigram_tagger_2007)
print('brown_sent_bigram_tagger_4203: ', brown_sent_bigram_tagger_4203)
score_test_bigram_tagger = bigram_tagger.evaluate(test_cents)
print('score_test_bigram_tagger: ', score_test_bigram_tagger)

# 3.组合标注器
print('\n组合标注器：')
t0 = nltk.DefaultTagger('NN')
t1 = nltk.UnigramTagger(train_sents, backoff=t0)
# t3=nltk.TrigramTagger(train_sents,backoff=t1)
t2 = nltk.BigramTagger(train_sents, cutoff=3, backoff=t1)
print('score_test_t2: ', t2.evaluate(test_cents))

# 4.存储标注器
print('\n存储标注器:')
# import _pickle as cPickle
from _pickle import dump

# 存储
output = open('t2.pk1', 'wb')
dump(t2, output, -1)
output.close()
# 载入标注器
from _pickle import load

input = open('t2.pk1', 'rb')
tagger = load(input)
input.close()
# 标注
text = "The board's action shows what free enterprise is up against in our complex maze of regulatory laws ."
tokens = text.split()
print(tagger.tag(tokens))

# 5.性能限制
print('\n性能限制:')
x_trigrams = list(nltk.trigrams(brown_tagged_sents[0]))
print('x_trigrams: ', x_trigrams)
cfd = nltk.ConditionalFreqDist(
    ((x[1], y[1], z[0]), z[1]) for sent in brown_tagged_sents for x, y, z in nltk.trigrams(sent))

print('cfd.conditions(): ', cfd.conditions()[:10])
ambiguous_contexts = [c for c in cfd.conditions() if len(cfd[c]) > 1]
ambiguous_ratio = sum(cfd[c].N() for c in ambiguous_contexts) / cfd.N()
print('词性歧义占所有词的比例：', ambiguous_ratio)

# 6.混淆矩阵
test_tags = [tag for sent in brown.sents(categories='editorial') for (word, tag) in t2.tag(sent)]
gold_tags = [tag for (word, tag) in brown.tagged_words(categories='editorial')]
print('test_tags: ', test_tags)
print('gold_tags: ', gold_tags)
confusion_M = nltk.ConfusionMatrix(gold_tags, test_tags)
# print('confusion_M: ',confusion_M)

# 6.跨句子边界标注
print('\n句子层面的N-gram标注：')

