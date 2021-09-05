#!/usr/bin/python3

import spacy

nlp = spacy.load('en_core_web_sm')
doc = nlp(u'There once was a man from Nantucket. The rest of this poem is not good. That\'s never stopped me before.')
for sent in doc.sents:
    print([sent[i] for i in range(len(sent))])
