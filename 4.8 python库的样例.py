'''
!/usr/bin/env python
 _*_coding:utf-8 _*_
@Time    :2019/11/19 16:35
@Author  :Zhangyunjia
@FileName: 4.8 python库的样例.py
@Software: PyCharm
'''
from __future__ import division
import nltk, re, pprint

# 1.布朗语料库中不同部分的情态动词频率
colors = 'rgbcmyk'


def bar_chart(categories, words, counts):
    'Plot a bar chart showing counts for each word by category'
    import pylab
    ind = pylab.arange(len(words))
    width = 1 / (len(categories) + 1)
    bar_groups = []
    for c in range(len(categories)):
        bars = pylab.bar(ind + c * width, counts[categories[c]], width, color=colors[c % len(colors)])
        bar_groups.append(bars)

    pylab.xticks(ind + width, words)
    pylab.legend([b[0] for b in bar_groups], categories, loc='upper left')
    pylab.ylabel('Frequency')
    pylab.title('Frequency of Six Modal Verbs by Genre')
    pylab.show()


genres = ['news', 'religion', 'hobbies', 'government', 'adventure']
modals = ['can', 'could', 'may', 'might', 'must', 'will']
cfdist = nltk.ConditionalFreqDist(
    (genre, word) for genre in genres for word in nltk.corpus.brown.words(categories=genre) if word in modals)
counts = {}
for genre in genres:
    counts[genre] = [cfdist[genre][word] for word in modals]

bar_chart(genres, modals, counts)

# 2.动态地产生数据的可视化图像

import matplotlib, pylab

matplotlib.use('Agg')
pylab.savefig('modals.png')
print('Content-Type: text/html')
print()
print('<html><body>')
print('<img src="modals.png"/>')
print('</body></html>')

# 3.NetworkX
import networkx as nx
import matplotlib
from nltk.corpus import wordnet as wn


def traverse(graph, start, node):
    graph.depth[node.name] = node.shortest_path_distance(start)
    for child in node.hyponyms():
        graph.add_edge(node.name, child.name)
        traverse(graph, start, child)


def hyponym_graph(start):
    G = nx.Graph()
    G.depth = {}
    traverse(G, start, start)
    return G


def graph_draw(graph):
    nx.draw_graphviz(graph,
                     node_size=[16 * graph.degree(n) for n in graph],
                     node_color=[graph.depth[n] for n in graph],
                     with_labels=False)
    matplotlib.pyplot.show()
dog = wn.synset('dog.n.01')
graph = hyponym_graph(dog)
graph_draw(graph)