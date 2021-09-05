#!/usr/bin/python3

import spacy

nlp = spacy.load('en_core_web_sm')
doc = nlp(u'The Golden Gate Bridge is an iconic landmark in San Francisco.')
with doc.retokenize() as retokenizer:
    attrs = {"LEMMA": "Golden Gate Bridge"}
    retokenizer.merge(doc[1:4], attrs=attrs)
    retokenizer.merge(doc[9:11], attrs={"LEMMA":"San Francisco"})
for token in doc:
    print(token.text, token.lemma_, token.pos_, token.dep_)
