'''
!/usr/bin/env python
 _*_coding:utf-8 _*_
@Time    : 2019/11/29 11:29
@Author  :Zhangyunjia
@FileName:  7.3 开发和评估分块器.py
@Software: PyCharm
'''
import nltk

# 1.IOB格式转NLTK树状图
text = '''
he PRP B-NP
accepted VBD B-VP
the DT B-NP
position NN I-NP
of IN B-PP
vice NN B-NP
chairman NN I-NP
of IN B-PP
Carlyle NNP B-NP
Group NNP I-NP
, , O
a DT B-NP
merchant NN I-NP
banking NN I-NP
concern NN I-NP
. . O
'''

# nltk.chunk.conllstr2tree(text, chunk_types=['NP']).draw()

# 2.读取CoNLL2000分块语料库
from nltk.corpus import conll2000

print(conll2000.chunked_sents('train.txt', chunk_types=['NP'])[99])

# 3.为琐碎的不创建任何块的块分析器建立一个标准
print('\n为琐碎的不创建任何块的块分析器建立一个标准:')
cp3 = nltk.RegexpParser('')
test_sents3 = conll2000.chunked_sents('test.txt', chunk_types=['NP'])
x3 = cp3.evaluate(test_sents3)
print('x3: ', x3)

# 4.查找以名词短语标记的特征字母开头的标记
print('\n查找以名词短语标记的特征字母开头的标记:')
grammar4 = r'NP: {<[CDJNP].*>+}'
cp4 = nltk.RegexpParser(grammar4)
x4 = cp4.evaluate(test_sents3)
print('x4: ', x4)

# 5.用 unigram 标注器对名词短语分块
print('\n用 unigram 标注器对名词短语分块:')


class gramChunker(nltk.ChunkParserI):
    def __init__(self, train_sents):
        train_data = [[(t, c) for w, t, c in nltk.chunk.tree2conlltags(sent)] for sent in train_sents]
        # self.tagger = nltk.UnigramTagger(train_data)
        self.tagger = nltk.BigramTagger(train_data)

    def parse(self, sentence):
        pos_tags = [pos for (word, pos) in sentence]
        tagged_pos_tags = self.tagger.tag(pos_tags)
        chunktags = [chunktag for (pos, chunktag) in tagged_pos_tags]
        conlltags = [(word, pos, chunktag) for ((word, pos), chunktag) in zip(sentence, chunktags)]
        return nltk.chunk.conlltags2tree(conlltags)


test_sents5 = test_sents3
train_sents5 = conll2000.chunked_sents('train.txt', chunk_types=['NP'])
gram_chunker = gramChunker(train_sents5)
x5 = gram_chunker.evaluate(test_sents5)
print('x5: ', x5)

# 使用 unigram 标注器分配一个标记给每个语料库中出现的词性标记
postags = sorted(set(pos for sent in train_sents5 for (word, pos) in sent.leaves()))
x5_2 = gram_chunker.tagger.tag(postags)
print('x5_2: ', x5_2)

# 6.用连续分类器对名词短语分块
print('\n用连续分类器对名词短语分块: ')


def tags_since_dt(tagged_sent, i):
    tags = set()
    for word, pos in tagged_sent[:i]:
        if pos == 'DT':
            tags = set()
        else:
            tags.add(pos)

    return '+'.join(sorted(tags))


def npchunk_features(tagged_sent, i, history):
     word, pos = tagged_sent[i]
     if i == 0:
         prevword, prevpos = "<START>", "<START>"
     else:
         prevword, prevpos = tagged_sent[i-1]
     if i == len(tagged_sent)-1:
         nextword, nextpos = "<END>", "<END>"
     else:
         nextword, nextpos = tagged_sent[i+1]
     return {"pos": pos,
             "word": word,
             "prevpos": prevpos,
             "nextpos": nextpos,
             "prevpos+pos": "%s+%s" % (prevpos, pos),
             "pos+nextpos": "%s+%s" % (pos, nextpos),
             "tags-since-dt": tags_since_dt(tagged_sent, i)}

class ConsecutiveNPChunkTagger(nltk.TaggerI):
    def __init__(self, train_sents):
        train_set = []
        for tagged_sent in train_sents:
            tagged_unchunked_sent = nltk.tag.untag(tagged_sent)
            # print('untagged_sent: ',tagged_unchunked_sent)
            history = []
            for i, (word_tag, chunk) in enumerate(tagged_sent):
                featureset = npchunk_features(tagged_unchunked_sent, i, history)
                train_set.append( (featureset, chunk) )
                history.append(chunk)
        self.classifier = nltk.MaxentClassifier.train(
            train_set, trace=0)

    def tag(self, tagged_unchunked_sent):
        history = []
        for i, word in enumerate(tagged_unchunked_sent):
            featureset = npchunk_features(tagged_unchunked_sent, i, history)
            chunk = self.classifier.classify(featureset)
            history.append(chunk)
        return zip(tagged_unchunked_sent, history)

class ConsecutiveNPChunker(nltk.ChunkParserI):
    def __init__(self, train_sents):
        tagged_chunked_sents = [[((w,t),c) for (w,t,c) in
                         nltk.chunk.tree2conlltags(sent)]
                        for sent in train_sents]
        # print('tagged_sents: ',tagged_sents)
        self.tagger = ConsecutiveNPChunkTagger(tagged_chunked_sents)

    def parse(self, tagged_unchunked_sent):
        tagged_sents = self.tagger.tag(tagged_unchunked_sent)
        conlltags = [(w,t,c) for ((w,t),c) in tagged_sents]
        return nltk.chunk.conlltags2tree(conlltags)

train_sents6 = conll2000.chunked_sents('train.txt',chunk_types=['NP'])
test_sents6 =  conll2000.chunked_sents('test.txt',chunk_types=['NP'])
# print(test_sents6)
chunker = ConsecutiveNPChunker(train_sents6[:200])
x6 = chunker.evaluate(test_sents6[:20])
print('x6: ', x6)
