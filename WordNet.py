'''
!/usr/bin/env python
 _*_coding:utf-8 _*_
@Time    :2019/11/11 18:50
@Author  :Zhangyunjia
@FileName: WordNet.py
@Software: PyCharm
'''

from nltk.corpus import wordnet as wn
result=wn.synsets('motorcar')
print(result)

result2=wn.synset('car.n.01').lemma_names()
print(result2)

result3=wn.synset('car.n.01').definition()
print(result3)

for synset in wn.synsets('dish'):
    print(synset.lemma_names())

# print(wn.lemmas('car'))

print('///////////////////////////////////////////////')

#下位词
motorcar=wn.synset('car.n.01')
print(motorcar.lemma_names())
types_of_motorcar=motorcar.hyponyms()
# print(types_of_motorcar[26])

result4 = sorted([lemma.name() for synset in types_of_motorcar for lemma in synset.lemmas()])
print(result4)

print('/////////////////////////////////////////////////////////////')
#上位词
hyper=motorcar.hypernyms()
print(hyper)
paths=motorcar.hypernym_paths()
print(paths)
print(len(paths))


path1=[synset.name() for synset in paths[1]]
print(path1)

print(motorcar.root_hypernyms())
















