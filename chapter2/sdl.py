#!/usr/bin/python3

import spacy

nlp = spacy.load('en_core_web_sm')
doc = nlp(u'I have flown to LA. Now I am flying to Frisco.')
for token in doc:
    print(token.head.text, token.dep_, token.text, token.pos_, token.tag_)
