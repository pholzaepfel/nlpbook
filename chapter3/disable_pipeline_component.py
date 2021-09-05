#!/usr/bin/python3

import spacy

nlp = spacy.load('en_core_web_sm', disable=['parser'])
print (nlp.pipe_names) #show enabled pipes

doc = nlp(u'I want a green apple.')
for token in doc:
    print(token.text,token.pos_,token.dep_)
