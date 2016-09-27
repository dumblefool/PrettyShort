# - *- coding: utf- 8 - *-

import sys
reload(sys)
sys.setdefaultencoding('utf8')
from nltk.tokenize.punkt import PunktSentenceTokenizer
from sklearn.feature_extraction.text import TfidfTransformer,CountVectorizer
import networkx
import pyperclip
import re
from bs4 import BeautifulSoup
import urllib2

def Summarize(data):
    data=' '.join(data.strip().split('\n'))
    st=PunktSentenceTokenizer()
    tokens=st.tokenize(data)
    n=CountVectorizer()
    m=n.fit_transform(tokens)
    normalized=TfidfTransformer().fit_transform(m)
    graph=normalized*normalized.T
    rank=networkx.from_scipy_sparse_matrix(graph)
    scores=networkx.pagerank(rank)
    ordered=sorted(((scores[i],s) for i,s in enumerate(tokens)),reverse=True)
    for j in range(0,2):
                print ordered[j][1]

url=raw_input()
page=urllib2.urlopen(url)
soup=BeautifulSoup(page,"lxml")
input=soup.find_all('p')
data=u" "
for p in input:
    data=data+p.text
Summarize(data)
