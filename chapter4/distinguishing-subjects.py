
#!/usr/bin/python3

import spacy

nlp = spacy.load('en_core_web_sm')
doc = nlp(u"I can promise it is worth your time.")
for token in doc:
    print(token.text, token.pos_, token.tag_, spacy.explain(token.tag_), token.dep_, spacy.explain(token.dep_))

doc = nlp(u"I know you. You know me.")
for token in doc:
    print(token.text, token.pos_, token.tag_, spacy.explain(token.tag_), token.dep_, spacy.explain(token.dep_))
