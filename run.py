#!/usr/bin/env python3

from ldtn import split, stats, classifier, bow_vector, Predictors, fit, tokenizer


train_test = split(
    size_of_test=0.4,
    dataset_filename='training_sets/product_reviews.tsv',
)

print(
    stats(
        train_test, Predictors, bow_vector, classifier, fit, tokenizer
    ))
