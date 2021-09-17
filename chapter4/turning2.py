
#!/usr/bin/python3

import spacy

def swap(doc_, oldorder, neworder):
    oldtags=[];
    ordermap=[];

    for n in neworder:
        for i,o in enumerate(oldorder):
            if o==n:
                ordermap.append(i)
    for token in doc_:
        oldtags.append(token.tag_)
    for i, tag in enumerate(oldtags):
        if oldtags[i:i+len(oldorder)]==oldorder:
            newdoc = '' 
            for k, j in enumerate(ordermap):
                if k==0:
                    newdoc = newdoc + doc_[i+j].text.capitalize() + ' '
                else:
                    newdoc = newdoc + doc_[i+j].text + ' '
            newdoc = newdoc + doc_[i+len(ordermap):].text
            return nlp(newdoc)

def substitute(doc_, tag, old, new):
    subbed = True
    while (subbed):
        subbed = False
        for i, token in enumerate(doc_):
            if token.tag_ == tag and token.text == old:
                sent = doc_[:i].text + ' ' + new + ' ' + doc_[i+1:].text
                subbed = True
        doc_ = nlp(sent)
    return(doc_)


nlp = spacy.load('en_core_web_sm')

doc = nlp(u"I can promise it is worth your time.")

#explain sentence, if needed
#for token in doc:
#    print(token.text, token.pos_, token.tag_, spacy.explain(token.tag_))

#swap order of words to make a question; pronound, modal, verb to modal, prp, verb
doc = swap(doc, ['PRP','MD','VB'], ['MD', 'PRP', 'VB'])

#invert pronouns
doc = substitute(doc,'PRP','I','you')
doc = substitute(doc,'PRP$','your','my')
#Invert pronoun

for i, token in enumerate(doc):
    if token.tag_ == 'VB':
        sent = doc[:i].text + ' really ' + doc[i:].text
        break
#change punctuation
doc=nlp(sent)
sent = doc[:len(doc)-1].text + '?'
print(sent)
