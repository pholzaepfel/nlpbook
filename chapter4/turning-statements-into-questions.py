
#!/usr/bin/python3

import spacy

nlp = spacy.load('en_core_web_sm')

#doc = nlp(u"I can promise it is worth your time.")
doc = nlp(u"I can drink an unhealthy amount of beer.")

#explain sentence, if needed
#for token in doc:
#    print(token.text, token.pos_, token.tag_, spacy.explain(token.tag_))

sent = ''

#invert the order of the modal and pronoun
for i,token in enumerate(doc):
    if doc[i].tag_ == 'PRP' and doc[i+1].tag_ == 'MD' and doc[i+2].tag_ == 'VB':
        sent = doc[i+1].text.capitalize() + ' ' + doc[i].text
        sent = sent + ' ' + doc[i+2:].text
        break
#retokenize
#Invert pronoun
doc=nlp(sent)
for i, token in enumerate(doc):
    if token.tag_ == 'PRP' and token.text == 'I':
        sent = doc[:i].text + ' you ' + doc[i+1:].text
        break
doc=nlp(sent)
#invert posessive pronoun
for i, token in enumerate(doc):
    if token.tag_ == 'PRP$' and token.text == 'your':
        sent = doc[:i].text + ' my ' + doc[i+1:].text
        break
#add emphasis to the verb
doc=nlp(sent)
for i, token in enumerate(doc):
    if token.tag_ == 'VB':
        sent = doc[:i].text + ' really ' + doc[i:].text
        break
#change punctuation
doc=nlp(sent)
sent = doc[:len(doc)-1].text + '?'
print(sent)
