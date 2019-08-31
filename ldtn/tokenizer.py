import string

import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from spacy.lang.en import English

punctuations = string.punctuation
nlp = spacy.load('en')

# Load English tokenizer, tagger, parser, NER and word vectors
parser = English()

def lemma(sentence):
    for word in parser(sentence):
        if word.lemma_ == "-PRON-":
            yield word.lower_
        else:
            yield word.lemma_.lower().strip()

def tokenizer(sentence):
    for word in lemma(sentence):
        if word in STOP_WORDS or word in punctuations:
            continue
        yield word
