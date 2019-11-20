'''
!/usr/bin/env python
 _*_coding:utf-8 _*_
@Time    :2019/11/19 22:04
@Author  :Zhangyunjia
@FileName: 5.2 标注语料库.py
@Software: PyCharm
'''
from __future__ import division
import nltk, re, pprint

# 1.表示已标注的标识符
tagged_token = nltk.tag.str2tuple('fly/NN')
print(tagged_token)
print(tagged_token[0])
print(tagged_token[1])

# 直接从一个字符串构造一个已标注的标识符的链表
sent = '''
... The/AT grand/JJ jury/NN commented/VBD on/IN a/AT number/NN of/IN
... other/AP topics/NNS ,/, AMONG/IN them/PPO the/AT Atlanta/NP and/CC
... Fulton/NP-tl County/NN-tl purchasing/VBG departments/NNS which/WDT it/PPS
... said/VBD ``/`` ARE/BER well/QL operated/VBN and/CC follow/VB generally/RB
... accepted/VBN practices/NNS which/WDT inure/VB to/IN the/AT best/JJT
... interest/NN of/IN both/ABX governments/NNS ''/'' ./.
... '''
x1 = [nltk.tag.str2tuple(t) for t in sent.split()]
print(x1)

# 2.读取已标注的语料库
x2 = nltk.corpus.brown.tagged_words(tagset='universal')  # 不可用
print(x2)

# 3.简化的词性标记集
print('简化的词性标记集: ')
from nltk.corpus import brown

brown_news_tagged = brown.tagged_words(categories='news', tagset='universal')
tag_fd = nltk.FreqDist(tag for (word, tag) in brown_news_tagged)
print('tag_fd: ', tag_fd)
x3 = tag_fd.keys()
print('tag_fd.keys(): ', x3)

x4 = sorted(tag_fd, key=tag_fd.__getitem__, reverse=True)
print('sorted: ', x4)

x5 = tag_fd.most_common()
print('tag_fd.most_common(): ', x5)

x6 = [i[0] for i in tag_fd.most_common()]
print(x6)

# 4.出现在名词之前的词类频率
print('名词: ///////////////////////////////')
print('brown_news_tagged:   ', brown_news_tagged)
print('/////////////////////////////////////////////////////////')
word_tag_pairs = list(nltk.bigrams(brown_news_tagged))
print('x7: //////////////////////////////////////////////////////////')
x7 = nltk.FreqDist(a[0][1] for a in word_tag_pairs if a[1][1] == 'NOUN').most_common()
print(x7)

# 5.新闻文本中最常见的动词

print('\n\n\n新闻文本中最常见的动词:')
wsj = nltk.corpus.treebank.tagged_words(tagset='universal')
print('wsj:\n', wsj)
word_tag_fd = list(nltk.FreqDist(wsj))
print('word_tag_fd:\n', word_tag_fd)
x8 = [word + '/' + tag for (word, tag) in word_tag_fd if tag.startswith('V')]
print('x8:\n', x8)

# 给定词的标记的频率顺序表
print('\n\n\n给定词的标记的频率顺序表:')
cfd1 = nltk.ConditionalFreqDist(wsj)
print(cfd1['cut'].keys())

# 颠倒配对的顺序
print('\n\n\n颠倒配对的顺序:')
cfd2 = nltk.ConditionalFreqDist((tag, word) for (word, tag) in wsj)
print(cfd2['VERB'].keys())
# 同是VD和VN的词汇
print('\n\n\n同是VERB和NOUN的词汇:')
# print(cfd1.conditions())
VERB_NOUN = [w for w in cfd1.conditions() if 'VERB' in cfd1[w] and 'NOUN' in cfd1[w]]
print(VERB_NOUN)
print('\n\n\n周围的文字情况:')
idx1 = wsj.index(('kicked', 'VERB'))
print(wsj[idx1 - 1:idx1 + 1])

# 6.找出最频繁的名词标记的程序
print('\n\n\n找出最频繁的名词标记的程序:')


def findtags(tag_prefix, tagged_text):
    cfd = nltk.ConditionalFreqDist((tag, word) for (word, tag) in tagged_text if tag.startswith(tag_prefix))
    return dict((tag, list(cfd[tag].keys())[:5]) for tag in cfd.conditions())


tagdict = findtags('N', nltk.corpus.brown.tagged_words(categories='news'))
for tag in sorted(tagdict):
    print(tag, tagdict[tag])

# 7.探索已标注的语料库
print('\n\n\n跟在often后面的词汇:')
brown_learned_text = brown.words(categories='learned')
# set是不重复的集合
sorted_brown_learned_text = sorted(set(b for (a, b) in nltk.bigrams(brown_learned_text) if a == 'often'))
print('sorted_brown_learned_text:\n', sorted_brown_learned_text)

print('\n\n\n跟在often后面的词的词性:')
brown_lrnd_tagged = brown.tagged_words(categories='learned', tagset='universal')
print(brown_lrnd_tagged)
tags = [b[1] for (a, b) in nltk.bigrams(brown_lrnd_tagged) if a[0] == 'often']
print(tags)
fd = nltk.FreqDist(tags)
fd.tabulate()


# 7.使用POS标记寻找三词短语
print('\n\n\n使用POS标记寻找三词短语:')
def process(sentence):
    for (w1, t1), (w2, t2), (w3, t3) in nltk.trigrams(sentence):
        if (t1.startswith('V') and t2 == 'TO' and t3.startswith('V')):
            print(w1, w2, w3)

for tagged_sent in brown.tagged_sents():
    # print(tagged_sent)
    process(tagged_sent)




