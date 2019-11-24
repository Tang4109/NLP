'''
!/usr/bin/env python
 _*_coding:utf-8 _*_
@Time    :2019/11/22 21:59
@Author  :Zhangyunjia
@FileName: 5.7 如何确定一个词的分类.py
@Software: PyCharm
'''
from __future__ import division
import nltk, re, pprint

# 1.性别鉴定

# 特征提取器
from sklearn.model_selection import train_test_split


def gender_features(word):
    return {'last_letter': (word[-2], word[-1])}
    # return {'suffix1': word[-1:],'suffix2': word[-2:]}


from nltk.corpus import names
import random

# 数据
names = ([(name, 'male') for name in names.words('male.txt')] +
         [(name, 'female') for name in names.words('female.txt')])

# 洗牌
random.shuffle(names)

# 数据划分
featuresets = [(gender_features(n), g) for (n, g) in names]
# print('featuresets: ',featuresets[:10])
X_train, X_test = train_test_split(featuresets, random_state=0)
# X_train = featuresets[500:]
# X_test = featuresets[:500]
# 训练
classifier = nltk.NaiveBayesClassifier.train(X_train)

# 预测单个数据
x_Neo = classifier.classify(gender_features('Neo'))
print('x_Neo: ', x_Neo)

x_Trinity = classifier.classify(gender_features('Trinity'))
print('x_Trinity: ', x_Trinity)

# 系统评估分类器
ratio = nltk.classify.accuracy(classifier, X_test)
print('准确率： ', ratio)

# 最有效特征
classifier.show_most_informative_features(5)

from nltk.classify import apply_features

train_set = apply_features(gender_features, names[500:])
print('train_set: ', train_set)
print('X_train: ', X_train)

# 2.选择正确的特征
# 特征提取器过拟合性别特征
print('\n特征提取器过拟合性别特征:')


def gender_features2(name):
    features = {}
    features['firstletter'] = name[0].lower()
    features['lastletter'] = name[-1].lower()
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        features['count(%s)' % letter] = name.lower().count(letter)
        features['has(%s)' % letter] = (letter in name.lower())
    return features


features2 = gender_features2('John')
print('features2: ', features2)
train_sets2 = apply_features(gender_features2, names)
print('train_sets2: ', train_sets2)
X_train, X_test = train_test_split(train_sets2, random_state=0)
classifier2 = nltk.NaiveBayesClassifier.train(X_train)
score = nltk.classify.accuracy(classifier2, X_test)
print('score: ', score)

# 3.验证集
print('\n验证集： ')
print('数据集的大小: ', len(names))

train_sets = apply_features(gender_features, names)
train_set_ = train_sets[1500:]
devtest_set_ = train_sets[500:1500]
test_set_ = train_sets[:500]
classifier3 = nltk.NaiveBayesClassifier.train(train_set_)
score_dev = nltk.classify.accuracy(classifier3, devtest_set_)
print('验证集得分： ', score_dev)

# 4. 错误列表
print('\n错误列表：')
errors = []
devtest_names = names[500:1500]

for (name, tag) in devtest_names:
    guess = classifier3.classify(gender_features(name))
    if guess != tag:
        errors.append((tag, guess, name))

print('errors: ', errors)
print('len(errors): ', len(errors))

# for (tag,guess,name) in sorted(errors):
#     print('correct=%-8s guess=%-8s name=%-30s' % (tag,guess,name))


# 5.文档分类
print('\n文档分类：')
from nltk.corpus import movie_reviews

documents = [(list(movie_reviews.words(fileid)), category) for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

print('document0: ', documents[0])
print('document1: ', documents[1])

# 文档分类的特征提取器
print('\n文档分类的特征提取器:')
all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
# print('all_words: ', all_words)
# print('all_words.items(): ', all_words.items())
# print('all_words.keys(): ', all_words.keys())
from operator import itemgetter

fd_items = sorted(all_words.items(), key=itemgetter(1), reverse=True)[:2000]
# print('fd_items: ',fd_items)
word_features = [word[0] for word in fd_items]
print('word_features: ', word_features)


def document_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features


df = document_features(movie_reviews.words('pos/cv957_8737.txt'))
print('df: ', df)

# 训练和测试分类器以进行文档分类
featuresets = [(document_features(d), c) for (d, c) in documents]
train_set5, test_set5 = featuresets[100:], featuresets[:100]
classifier5 = nltk.NaiveBayesClassifier.train(train_set5)
test_set5_score = nltk.classify.accuracy(classifier5, test_set5)
print('test_set5_score: ', test_set5_score)
classifier5.show_most_informative_features(5)

# 6.词性标注
# 找出最常见的后缀
print('\n找出最常见的后缀:')
from nltk.corpus import brown
suffix_fdist=nltk.FreqDist()
for word in brown.words():
    word=word.lower()
    suffix_fdist[word[-1:]] += 1
    suffix_fdist[word[-2:]] += 1
    suffix_fdist[word[-3:]] += 1
# print(suffix_fdist.items())
# print(suffix_fdist.keys())
suffix_fdist_items = sorted(suffix_fdist.items(), key=itemgetter(1), reverse=True)[:100]
common_suffixes = [word[0] for word in suffix_fdist_items]
print('common_suffixes: ',common_suffixes)
