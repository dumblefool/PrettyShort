# - *- coding: utf- 8 - *-

import sys
reload(sys)
sys.setdefaultencoding('utf8')
from nltk.tokenize.punkt import PunktSentenceTokenizer 
from sklearn.feature_extraction.text import TfidfTransformer,CountVectorizer
import networkx
import pyperclip
import re

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
    for j in range(0,3):
                print ordered[j][1]

input=str(pyperclip.paste())
r1=re.sub(r'\bMr(?:\.|\b)',"Mr ",input)
r2=re.sub(r'\bMrs(?:\.|\b)',"Mrs ",r1)
r3=re.sub(r'\bDr(?:\.|\b)',"Dr ",r2)
Summarize(r3)

