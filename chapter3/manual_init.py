#!/usr/bin/python3

import spacy

lang = 'en' # derived from the model metadata
pipeline = ['tagger','parser','ner'] # there's more enabled by default now
model_data_path = '/home/gibeath/.local/lib/python3.9/site-packages/en_core_web_sm/en_core_web_sm-3.1.0'
lang_cls = spacy.util.get_lang_class(lang)
nlp = lang_cls()
for name in pipeline:
    #component = nlp.create_pipe(name) #this has changed :)
    nlp.add_pipe(name)
nlp.from_disk(model_data_path)

#this is broken as-is, but I'm neither downgrading the version of spacy to be able to use the examples
#nor sweating figuring this out right this second
