'''
!/usr/bin/env python
 _*_coding:utf-8 _*_
@Time    :2019/11/19 9:46
@Author  :Zhangyunjia
@FileName: 4.7 算法设计.py
@Software: PyCharm
'''
from __future__ import division
import nltk, re, pprint


# 1.迭代与递归求阶乘
def factorial1(n):
    result = 1
    for i in range(n):
        result *= (i + 1)
    return result


def factorial2(n):
    if n == 1:
        return 1
    else:
        return n * factorial2(n - 1)


x1 = factorial1(5)
x2 = factorial2(5)
print(x1, x2)


# 2.字母查找树
def insert(trie, key, value):
    if key:
        first, rest = key[0], key[1:]
        if first not in trie:
            trie[first] = {}
        insert(trie[first], rest, value)
    else:
        trie['value'] = value


trie = nltk.defaultdict(dict)
insert(trie, 'chat', 'cat')
insert(trie, 'chien', 'dog')
trie = dict(trie)
pprint.pprint(trie)
print(trie['c']['h']['a']['t']['value'])


# 3.一个简单的全文检索系统
# def raw(file):
#     contents = open(file).read()
#     contents = re.sub(r'<.*?>', ' ', contents)
#     contents = re.sub(r'\s+', ' ', contents)
#     return contents
#
#
# def snippet(doc, term):
#     text = ' ' * 30 + raw(doc) + ' ' * 30
#     pos = text.index(term)
#     return text[pos - 30:pos + 30]
#
#
# print('Building Index...')
# files = nltk.corpus.movie_reviews.abspaths()
# idx = nltk.Index((w, f) for f in files for w in raw(f).split())
# query = ''
# while query != 'quit':
#     query = raw('query> ')
#     if query in idx:
#         for doc in idx[query]:
#             print(snippet(doc, query))
#     else:
#         print('Not found')

# 4.timeit模块检测

# from timeit import Timer
#
# vocab_size = 100000
# setup_list = 'import random; vocab = range(%d)' % vocab_size
# setup_set = 'import random; vocab = set(range(%d))' % vocab_size
# statement = 'random.randint(0,%d) in vocab' % vocab_size * 2
# x3 = Timer(statement, setup_list).timeit(1000)
# x4 = Timer(statement, setup_set).timeit(1000)
#
# print(x3)
# print(x4)

# 5.动态规划
# 迭代方法
def virahanka1(n):
    if n == 0:
        return ['']
    if n == 1:
        return ['S']
    else:
        s = ['S' + prosody for prosody in virahanka1(n - 1)]
        l = ['L' + prosody for prosody in virahanka1(n - 2)]
        return s + l


# 6.自底向上的动态规划
def virahanka2(n):
    lookup = [[''], ['S']]
    for i in range(n - 1):
        s = ['S' + prosody for prosody in lookup[i + 1]]
        l = ['L' + prosody for prosody in lookup[i]]
        lookup.append(s + l)
    return lookup[n]


# 7.自上而下的动态规划
def virahanka3(n, lookup={0: [''], 1: ['S']}):
    if n not in lookup:
        s = ['S' + prosody for prosody in virahanka3(n - 1)]
        l = ['L' + prosody for prosody in virahanka3(n - 2)]
        lookup[n] = s + l
    return lookup[n]




# 8.默记法
from nltk import memoize
@memoize
def virahanka4(n):
    if n == 0:
        return ['']
    if n == 1:
        return ['S']
    else:
        s = ['S' + prosody for prosody in virahanka4(n - 1)]
        l = ['L' + prosody for prosody in virahanka4(n - 2)]
        return s + l

for i in range(5):
    print(i, virahanka4(i))