
#!/usr/bin/python3

import spacy
import sys

nlp = spacy.load('en_core_web_sm')
doc = nlp(' '.join(sys.argv[1:]))
print(['token.text', 'token.pos_', 'token.tag_', 'spacy.explain(token.tag_)', 'token.dep_', 'spacy.explain(token.dep_)'])
for token in doc:
    print([token.text, token.pos_, token.tag_, spacy.explain(token.tag_), token.dep_, spacy.explain(token.dep_)])
