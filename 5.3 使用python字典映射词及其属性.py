'''
!/usr/bin/env python
 _*_coding:utf-8 _*_
@Time    :2019/11/20 21:20
@Author  :Zhangyunjia
@FileName: 5.3 使用python字典映射词及其属性.py
@Software: PyCharm
'''
from __future__ import division
import nltk, re, pprint

# 1.python字典

pos = {}
pos['colorless'] = 'ADJ'
pos['ideas'] = 'N'
pos['really'] = 'ADV'
pos['like'] = 'V'

print(pos)
print(list(pos))
print(sorted(pos))

s = [w for w in pos if w.endswith('s')]
print(s)

for word in sorted(pos):
    print(word + ':', pos[word])

print(pos.keys())
print(pos.values())
print(pos.items())

for key, val in sorted(pos.items()):
    print(key + ':', val)

# 2.默认字典
print('\n默认字典:')
frequency = nltk.defaultdict(int)
x1 = frequency['zyj']
print(frequency)
print(x1)

print('\n自定义默认值:')
pos = nltk.defaultdict(lambda: 'N')
x2 = pos['blog']
print(pos)
print(x2)
print(pos.items())

# 3.映射最频繁的n个词，其他映射为UNK
print('\n映射最频繁的n个词，其他映射为UNK:')
alice = nltk.corpus.gutenberg.words('carroll-alice.txt')
print('alice: ', alice)
vocab = nltk.FreqDist(alice).most_common()
print('vocab: ', vocab)
v1000 = vocab[:1000]
print('v1000: ', v1000)

mapping = nltk.defaultdict(lambda: 'UNK')
for v in v1000:
    mapping[v[0]] = v[0]

print('mapping: ', mapping)
alice2 = [mapping[v] for v in alice]
print('alice2: ', alice2[:100])

# 4.计数词性标记出现的次数
print('\n计数词性标记出现的次数:')
counts = nltk.defaultdict(int)
from nltk.corpus import brown

for (word, tag) in brown.tagged_words(categories='news', tagset='universal'):
    counts[tag] += 1
print(counts)
print(counts['NOUN'])
print(list(counts))

print('\nitemgetter: ')
from operator import itemgetter

print('counts.items(): ', counts.items())
print('itemgetter(1): ', itemgetter(1))
x_sort = sorted(counts.items(), key=itemgetter(1), reverse=True)
print('对字典按照itemgetter(1)进行排序：\n', x_sort)

value_sort = [t for t, c in sorted(counts.items(), key=itemgetter(1), reverse=True)]
print('value_sort: ', value_sort)

# 5.通过最后两个字母索引词汇
print('\n通过最后两个字母索引词汇:')
last_letters = nltk.defaultdict(list)
words = nltk.corpus.words.words('en')
print('words[:10]: ', words[:10])
for word in words:
    key = word[-2:]
    last_letters[key].append(word)

print(last_letters['ed'])

# 6.创建颠倒顺序的词字典
print('\n创建颠倒顺序的词字典:')
anagrams = nltk.defaultdict(list)
for word in words:
    key = ''.join(sorted(word))
    # print('key: ',key)
    anagrams[key].append(word)

print(anagrams['aeilnrt'])

# 7.nltk.Index()
print('\nnltk.Index():')
anagrams2 = nltk.Index((''.join(sorted(w)), w) for w in words)
print(anagrams2['aeilnrt'])

# 8.复杂的键和值
print('\n复杂的键和值:')
pos = nltk.defaultdict(lambda: nltk.defaultdict(int))
print('pos: ', pos)
brown_news_tagged = brown.tagged_words(categories='news', tagset='universal')
print('brown_news_tagged: ', brown_news_tagged)
# brown_news_tagged_bigrams = list(nltk.bigrams(brown_news_tagged))
# print('brown_news_tagged_bigrams: ',brown_news_tagged_bigrams)
for ((w1, t1), (w2, t2)) in nltk.bigrams(brown_news_tagged):
    pos[(t1, w2)][t2] += 1

print(pos[('DET', 'right')])

# 9.颠倒字典（通过值来找键）
counts = nltk.defaultdict(int)
for word in nltk.corpus.gutenberg.words('milton-paradise.txt'):
    counts[word] += 1


def value2key(n):
    print(sorted([key for (key, value) in counts.items() if value == n]))


print('\n颠倒字典（通过值来找键）:')
value2key(32)

# 任意两个键都不具有相同值
print('\n任意两个键都不具有相同值: ')
pos = {'colorless': 'ADJ', 'ideas': 'N', 'sleep': 'V', 'furiously': 'ADV'}
pos2 = dict((value, key) for (key, value) in pos.items())
print(pos2['N'])

# 对于多个键具有相同值的情况,使用append为每个词性积累词
print('\n多个键具有相同值的情况: ')
pos.update({'cats': 'N', 'scratch': 'V', 'peacefully': 'ADV', 'old': 'ADJ'})
pos2 = nltk.defaultdict(list)
for key, value in pos.items():
    pos2[value].append(key)

print(pos2)

# 使用NLTK中的索引支持进行相同的操作
pos3=nltk.Index((value,key) for (key,value) in pos.items())
print('pos3: ',pos3)