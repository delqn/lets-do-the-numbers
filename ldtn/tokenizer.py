import string

import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from spacy.lang.en import English

punctuations = string.punctuation
nlp = spacy.load('en')
stop_words = spacy.lang.en.stop_words.STOP_WORDS
parser = English()
def tokenizer(sentence):
    lemmai = (word.lemma_.lower().strip() if word.lemma_ != "-PRON-" else word.lower_ for word in parser(sentence))
    for word in lemmai:
        if word in stop_words or word in punctuations:
            continue
        yield word
