#!/usr/bin/env python3

from ldtn import split, evaluate, classifier, bow_vector, Predictors, fit, tokenizer


train_test = split(
    size_of_test=0.4,
    dataset_filename='training_sets/product_reviews.tsv',
)

stats = evaluate(train_test, Predictors, bow_vector, fit, tokenizer)

for label, value in stats:
    print(f'{label}: \t{value}')
