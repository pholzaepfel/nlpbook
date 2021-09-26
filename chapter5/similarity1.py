#!/usr/bin/python3

import spacy

nlp = spacy.load('en_core_web_md')
doc=nlp('I want a green apple.')
print(doc[2:5].similarity(doc[2:5]))
doc2=nlp('I crave a juicy orange.')
for i,token in enumerate(doc):
    print(doc[i],doc2[i],doc[i].similarity(doc2[i]))
