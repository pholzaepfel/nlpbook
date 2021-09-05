#!/usr/bin/python3

import spacy

nlp = spacy.load('en_core_web_sm')
doc = nlp(u'I want a spicy green apple.')
print ([w for w in doc[5].children]) # children are all relatives of a word
print ([w for w in doc[5].lefts]) # lefts are adjectives, etc
print ([w for w in doc[1].rights]) # rights are objects, etc

