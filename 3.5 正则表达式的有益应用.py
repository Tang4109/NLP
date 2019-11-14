'''
!/usr/bin/env python
 _*_coding:utf-8 _*_
@Time    :2019/11/13 17:40
@Author  :Zhangyunjia
@FileName: 3.5 正则表达式的有益应用.py
@Software: PyCharm
'''
from __future__ import division
import nltk, re, pprint

# 1.提取字符块
word = 'dsjdgjrueghdjsofishROREIPjdvszkklzsdorvgh'
x1 = re.findall(r'[aeiou]', word)
print(x1)
print(len(x1))

wsj = sorted(set(nltk.corpus.treebank.words()))
fd = nltk.FreqDist(vs for word in wsj for vs in re.findall(r'[aeiou]{2,}', word))
print(fd.items())

# 2.忽略内部元音
print('/////////////////////////////////////////////')
regexp = r'^[AEIOUaeiou]+|[AEIOUaeiou]+$|[^AEIOUaeiou]'


def compress(word):
    pieces = re.findall(regexp, word)
    return ''.join(pieces)


english_udhr = nltk.corpus.udhr.words('English-Latin1')
x2 = nltk.tokenwrap(compress(w) for w in english_udhr[:75])
print(x2)

# 3.提取辅音元音序列
print('///////////////////////////////////////////////')
rotokas_words = nltk.corpus.toolbox.words('rotokas.dic')
cvs = [cv for w in rotokas_words for cv in re.findall(r'[ptksvr][aeiou]', w)]
cfd = nltk.ConditionalFreqDist(cvs)
cfd.tabulate()

# 4.nltk.Index()转为有用索引
print('///////////////////////////////////////////////')
cv_word_pairs = [(cv, w) for w in rotokas_words for cv in re.findall(r'[ptksvr][aeiou]', w)]
cv_index = nltk.Index(cv_word_pairs)
print(cv_index['ka'])

# 5.查找词干
print('///////////////////////////////////////////////')

# 直接去掉任何看起来像后缀的字符
# def stem(word):
#     for suffix in ['ing', 'ly', 'ed', 'ious', 'ies', 'ive', 'es', 's', 'ment']:
#         if word.endswith(suffix):
#             return word[:-len(suffix)]

# 使用正则表达式的方法
x3 = re.findall(r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)?$', 'language')
print(x3)


# 重新定义词干函数
def stem(word):
    regexp = r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)?$'
    stem, suffix = re.findall(regexp, word)[0]
    return stem


raw = '''it is a good thing,I think we should do it now.
dilicious freshing fucking business.
'''
tokens = nltk.word_tokenize(raw)
print(tokens)

x4 = [stem(t) for t in tokens]
print(x4)

# 6.搜索已分词文本
print('//////////////////////////////////////////////////')
from nltk.corpus import gutenberg, nps_chat

moby = nltk.Text(gutenberg.words('melville-moby_dick.txt'))
x5 = moby.findall(r'<a> (<.*>) <man>')  # 括号()使得只匹配词而不匹配短语
print(x5)
print('///////////////////////////////////////////////////')
chat = nltk.Text(nps_chat.words())
x6 = chat.findall(r'<.*> <.*> <bro>')
print(x6)
print('//////////////////////////////////////////////////')
x7 = chat.findall(r'<l.*>{3,}')
print(x7)

# 小栗子
print('//////////////////////////////////////////////////')
from nltk.corpus import brown

hobbies_learned = nltk.Text(brown.words(categories=['hobbies', 'learned']))
x8 = hobbies_learned.findall(r'<\w*> <and> <other> <\w*s>')
print(x8)

x9 = hobbies_learned.findall(r' <as> <\w*> <as> <\w*>')
print(x9)