
#!/usr/bin/python3

import spacy

nlp = spacy.load('en_core_web_sm')
doc = nlp(u"The firm earned $1.5 million in 2017, an increase from $1.2 million in 2016..")
phrases = []
phrase = ''
for token in doc:
    if token.tag_ == '$':
        phrase = token.text
        i = token.i + 1
        while doc[i].tag_ == 'CD': # cardinal number
            phrase += doc[i].text + ' '
            i += 1
        phrases.append(phrase[:-1])
        phrase=''
print(phrases)
