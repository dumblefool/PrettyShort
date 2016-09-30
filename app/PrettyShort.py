# - *- coding: utf- 8 - *-

import sys
reload(sys)
sys.setdefaultencoding('utf8')
from nltk.tokenize.punkt import PunktSentenceTokenizer
from sklearn.feature_extraction.text import TfidfTransformer,CountVectorizer
import networkx
import re
from bs4 import BeautifulSoup
import requests


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
    for j in range(0,1):
                return ordered[j][1]

def prest():
    output=u" "
    url="http://www.dailymail.co.uk/sport/football/article-3814060/Jurgen-Klopp-sets-standards-Liverpool-players-wake-Mamadou-Sakho-social-media-slip-up.html"
    soup=BeautifulSoup(requests.get(url).text,"lxml")
    page=max(soup.find_all(),key=lambda x:len(x.find_all('p',recursive=False)))
    data=u" "
    input=page.find_all('p')
    for p in input:
        data=data+p.text
        output=Summarize(data)
    return output
