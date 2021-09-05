#!/usr/bin/python3

import spacy

nlp = spacy.load('en_core_web_sm')
doc = nlp(u'A noun chunk is a phrase that has a noun as its head.')
for chunk in doc.noun_chunks: # automagic
    print(chunk)

for token in doc: #manual and it doesn't work lol
    if token.pos_=='NOUN':
        chunk=''
        for w in token.lefts:
            chunk = chunk + w.text + ' '
        chunk = chunk + token.text
        print(chunk)
