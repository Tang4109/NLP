'''
!/usr/bin/env python
 _*_coding:utf-8 _*_
@Time    :2019/11/21 17:04
@Author  :Zhangyunjia
@FileName: 5.4 自动标注.py
@Software: PyCharm
'''
from __future__ import division
import nltk, re, pprint
from nltk.corpus import brown

brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news')
print(brown_tagged_sents)
# for sent in brown_tagged_sents:
#     for words in sent:
#         print(words[0],end=' ')

print(brown_sents)

# 1.默认标注器
# 找出最有可能的标记
print('\n找出最有可能的标记：')
tags = [tag for (word, tag) in brown.tagged_words(categories='news')]
print('tags: ', tags)
tag_max = nltk.FreqDist(tags).max()
print('tag_max: ', tag_max)
# 创建一个将所有词都标注成tag_max的标注器
raw = 'I do not like green eggs and ham, I do not like them Sam I am!'
tokens = nltk.word_tokenize(raw)
default_tagger = nltk.DefaultTagger(tag_max)
tokens_tagged = default_tagger.tag(tokens)
print('tokens_tagged: ', tokens_tagged)

# 评估
print('评估brown_tagged_sents: ', default_tagger.evaluate(brown_tagged_sents))

# 2.正则表达式标注器
print('\n正则表达式标注器：')

patterns = [
    (r'.*ing$', 'VBG'),  # gerunds
    (r'.*ed$', 'VBD'),  # simple past
    (r'.*es$', 'VBZ'),  # 3rd singular present
    (r'.*ould$', 'MD'),  # modals
    (r'.*\'s$', 'NN$'),  # possessive nouns
    (r'.*s$', 'NNS'),  # plural nouns
    (r'^-?[0-9]+(.[0-9]+)?$', 'CD'),  # cardinal numbers
    (r'.*', 'NN')  # nouns (default)
]
regexp_tagger = nltk.RegexpTagger(patterns)
brown_sent3_tagged = regexp_tagger.tag(brown_sents[3])
print(brown_sent3_tagged)
# 评估
print('regexp_tagger 评估 brown_tagged_sents: ', regexp_tagger.evaluate(brown_tagged_sents))

# 3.查询标注器
print('\n查询标注器：')
fd = nltk.FreqDist(brown.words(categories='news'))
from operator import itemgetter

# print('fd.keys(): ',fd.keys())
fd_items = sorted(fd.items(), key=itemgetter(1), reverse=True)[:100]
most_freq_words = [word[0] for word in fd_items]
print('most_freq_words: ', most_freq_words)

cfd = nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))
print('cfd: ', cfd.items())
likely_tags = dict((word, cfd[word].max()) for word in most_freq_words)
print('likely_tags: ', likely_tags)
baseline_tagger = nltk.UnigramTagger(model=likely_tags, backoff=nltk.DefaultTagger('NN'))
# 评估
print('baseline_tagger 评估 brown_tagged_sents: ', baseline_tagger.evaluate(brown_tagged_sents))

# 未标注的输入文本是如何处理的
print('\n未标注的输入文本是如何处理的：')

sent = brown.sents(categories='news')[3]
print('sent: ', sent)
sent_tagged = baseline_tagger.tag(sent)
print('sent_tagged: ', sent_tagged)

# 4.使用不同大小的模型，查找标注器的性能不同
print('\n\n使用不同大小的模型，查找标注器的性能不同：')


def performance(cfd, wordlist):
    lt = dict((word, cfd[word].max()) for word in wordlist)
    baseline_tagger = nltk.UnigramTagger(model=lt, backoff=nltk.DefaultTagger('NN'))
    # 对新数据进行标注
    return baseline_tagger.evaluate(brown.tagged_sents(categories='fiction'))


def display():
    import pylab
    fd_items = sorted(nltk.FreqDist(brown.words(categories='news')).items(), key=itemgetter(1), reverse=True)
    print('words_by_freq: ', fd_items[:100])
    words_by_freq = [word[0] for word in fd_items]
    cfd = nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))
    sizes = 2 ** pylab.arange(15)
    print('sizes: ', sizes)
    perfs = [performance(cfd, words_by_freq[:size]) for size in sizes]
    print('perfs: ', perfs)
    pylab.plot(sizes, perfs, '-bo')
    pylab.title('Lookup Tagger Performance with Varying Model Size')
    pylab.xlabel('Model Size')
    pylab.ylabel('Performance')
    pylab.show()


display()

