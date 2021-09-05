#!/usr/bin/python3

import spacy
from spacy.symbols import ORTH, LEMMA, NORM

nlp = spacy.load('en_core_web_sm')
doc = nlp(u'I am flying to Frisco')
print([w.text for w in doc])

#the following get_pipe method replaces the following olde stuff
#special_case = [{ORTH: u'Frisco', LEMMA: u'San Francisco'}]
#nlp.tokenizer.add_special_case(u'Frisco',special_case)

nlp.get_pipe("attribute_ruler").add([[{"TEXT": "Frisco"}]], {"LEMMA": "San Francisco"})
print([w.lemma_ for w in nlp(u'I am flying to Frisco')])
