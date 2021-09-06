#!/usr/bin/python3

import spacy
from spacy import util

out = util.get_package_path('en_core_web_sm')
print(out)
