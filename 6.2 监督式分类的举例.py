'''
!/usr/bin/env python
 _*_coding:utf-8 _*_
@Time    : 2019/11/25 10:06
@Author  :Zhangyunjia
@FileName:  6.2 监督式分类的举例.py
@Software: PyCharm
'''

import nltk

# 1.句子分割
sents = nltk.corpus.treebank_raw.sents()
print('sents: ', sents)
tokens = []
boundaries = set()
offset = 0
for i, sent in enumerate(nltk.corpus.treebank_raw.sents()):
    tokens.extend(sent)
    offset += len(sent)
    boundaries.add(offset - 1)  # 不是按照顺序添加


# print('tokens: ',tokens)
# print('offset: ',offset)
# print('boundaries: ',boundaries)

# 指定用于决定标点是否表示句子边界的数据特征
# 构建特征提取器
def punct_features(tokens, i):
    return {'next-word-capitalized': tokens[i + 1][0].isupper(),
            'prevword': tokens[i - 1].lower(),
            'punct': tokens[i],
            'prev-word-is-one-char': len(tokens[i - 1]) == 1}


# 特征集
featuresets = [(punct_features(tokens, i), (i in boundaries))
               for i in range(1, len(tokens) - 1)
               if tokens[i] in '.?!']

size = int(len(featuresets) * 0.1)
train_set, test_set = featuresets[size:], featuresets[:size]
classifier = nltk.NaiveBayesClassifier.train(train_set)
score = nltk.classify.accuracy(classifier, test_set)
print('score: ', score)


# 基于分类的断句器
def segment_sentences(words):
    start = 0
    sents = []
    for i, word in words:
        if word in '.?!' and classifier.classify(punct_features(words, i)) == True:
            sents.append(words[start:i + 1])
            start = i + 1

    if start < len(words):
        sents.append(words[start:])
        return sents


# 2.识别对话行为类型
print('\n识别对话行为类型:')
posts = nltk.corpus.nps_chat.xml_posts()[:10000]
print('posts: ', posts)


# 特征提取器
def dialogue_act_features(post):
    features = {}
    for word in nltk.word_tokenize(post):
        features['contains(%s)' % word.lower()] = True
    return features


# 特征集
featuresets = [(dialogue_act_features(post.text), post.get('class')) for post in posts]
# print(featuresets[:100])
size = int(len(featuresets) * 0.1)
train_set, test_set = featuresets[size:], featuresets[:size]
# for i in range(10):
#     print('train_set: ', train_set[i])

classifier = nltk.NaiveBayesClassifier.train(train_set)
score = nltk.classify.accuracy(classifier, test_set)
print('score: ', score)


# 3.识别文字蕴含
print('\n识别文字蕴含: ')
# 认识文字蕴含的特征提取器
def rte_features(rtepair):
    extractor = nltk.RTEFeatureExtractor(rtepair)
    features = {}
    features['word_overlap']=len(extractor.overlap('word'))
    features['word_hyp_extra']=len(extractor.hyp_extra('word'))
    features['ne_overlap']=len(extractor.overlap('ne'))
    features['ne_hyp_extra']=len(extractor.hyp_extra('ne'))
    return features


rtepair=nltk.corpus.rte.pairs(['rte3_dev.xml'])[33]
extractor = nltk.RTEFeatureExtractor(rtepair)
print('extractor.text_words: ',extractor.text_words)

print('extractor.hyp_words: ',extractor.hyp_words)
print('extractor.overlap_word: ',extractor.overlap('word'))
print('extractor.overlap_ne: ',extractor.overlap('ne'))

print('extractor.hyp_extra_word: ',extractor.hyp_extra('word'))
















