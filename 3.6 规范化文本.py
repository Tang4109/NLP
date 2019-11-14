'''
!/usr/bin/env python
 _*_coding:utf-8 _*_
@Time    :2019/11/14 11:18
@Author  :Zhangyunjia
@FileName: 3.6 规范化文本.py
@Software: PyCharm
'''
from __future__ import division
import nltk, re, pprint

# 1.定义数据
raw = '''It so chanced, that after the Parsee's disappearance, I was he whom
the Fates ordained to take the place of Ahab's bowsman, when that
bowsman assumed the vacant post; the same, who, when on the last day
the three men were tossed from out of the rocking boat, was dropped
astern.  So, floating on the margin of the ensuing scene, and in full
sight of it, when the halfspent suction of the sunk ship reached me,
I was then, but slowly, drawn towards the closing vortex.  When I
reached it, it had subsided to a creamy pool.  Round and round, then,
and ever contracting towards the button-like black bubble at the axis
of that slowly wheeling circle, like another Ixion I did revolve.
Till, gaining that vital centre, the black bubble upward burst; and
now, liberated by reason of its cunning spring, and, owing to its
great buoyancy, rising with great force, the coffin life-buoy shot
lengthwise from the sea, fell over, and floated by my side.  Buoyed
up by that coffin, for almost one whole day and night, I floated on a
soft and dirgelike main.  The unharming sharks, they glided by as if
with padlocks on their mouths; the savage sea-hawks sailed with
sheathed beaks.  On the second day, a sail drew near, nearer, and
picked me up at last.  It was the devious-cruising Rachel, that in
her retracing search after her missing children, only found another
orphan.
'''
tokens = nltk.word_tokenize(raw)

# 2.词干提取器
porter = nltk.PorterStemmer()
lancaster = nltk.LancasterStemmer()

x1 = [porter.stem(t) for t in tokens]
print(x1)

# 3.使用词干提取器索引文本
print('/////////////////////////////////////////////')


class IndexedText(object):
    def __init__(self, stemmer, text):
        self._text = text
        self._stemmer = stemmer
        self._index = nltk.Index((self._stem(word), i) for (i, word) in enumerate(text))

    def concordance(self, word, width=40):
        key = self._stem(word)
        wc = int(width / 4)
        # print(wc)
        for i in self._index[key]:
            # print(i)
            # print(self._text[i - wc:i])
            lcontext = ' '.join(self._text[i - wc:i])
            print(lcontext)
            rcontext = ' '.join(self._text[i:i + wc])
            print(rcontext)
            ldisplay = '%*s' % (width, lcontext[-width:])
            rdisplay = '%-*s' % (width, rcontext[:width])
            print(ldisplay, rdisplay)
            print('//////////////////////////////////////')

    def _stem(self, word):
        return self._stemmer.stem(word).lower()


porter = nltk.PorterStemmer()
grail = nltk.corpus.webtext.words('grail.txt')
text = IndexedText(porter, grail)
text.concordance('lie')

# 4.WordNet词形归并器
wnl = nltk.WordNetLemmatizer()
x2 = [wnl.lemmatize(t) for t in tokens]
print(x2)
