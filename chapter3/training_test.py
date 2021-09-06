#!/usr/bin/python3
# page 42
#The Language.update method now takes a batch of Example objects instead of the raw texts and annotations or Doc and GoldParse objects. An Example streamlines how data is passed around. It stores two Doc objects: one for holding the gold-standard reference data, and one for holding the predictions of the pipeline.
# For most use cases, you shouldn’t have to write your own training scripts anymore. Instead, you can use spacy train with a config file and custom registered functions if needed. See the training documentation for details.
import spacy
from spacy.tokens import Doc
from spacy.training import Example

nlp = spacy.load('en_core_web_sm')

doc = nlp(u'I need a taxi to Iwefh.') # the example org Festy doesn't register as an org anymore
for ent in doc.ents:
    print(ent.text, ent.label_)
vocab = doc.vocab # yuck
examples = []

ner = nlp.get_pipe('ner')
ner.add_label('DISTRICT') # haven't gotten this working correctly yet; TODO

words = ['We', 'need', 'to', 'deliver', 'it', 'to', 'Iwefh','.'] # I've tried a few random 5-letter strings here and... the most bizarre thing is that this isn't deterministic. I've run this same code repeatedly with different results. what the *hell*. It usually works but not always.

doc = Doc(vocab, words=words)
entities = [(25,30, 'GPE')] # geo-political entity, this seems like a fit since district is being painful
example = Example.from_dict(doc, {'words': words, "entities": entities})
nlp.update([example])

words = ['I','like','red','oranges']
doc = Doc(vocab, words=words)
entities = []
example = Example.from_dict(doc, {'words': words, "entities": entities})
nlp.update([example])


doc = nlp(u'I need a taxi to Iwefh.') # the example org Festy doesn't register as an org anymore

for ent in doc.ents:
    print(ent.text, ent.label_)

