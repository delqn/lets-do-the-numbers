#!/usr/bin/env python

import unittest

from ldtn import split, evaluate, predict, train, lemma, tokenizer

class TestIt(unittest.TestCase):
    def setUp(self):
        pass

    def test_lemma(self):
        l = list(lemma('It is now possible to teach a machine to excel a human endeavors, when in the past it may have not been possible.'))
        expected = ['it', 'be', 'now', 'possible', 'to', 'teach', 'a', 'machine',
                    'to', 'excel', 'a', 'human', 'endeavor', ',', 'when',
                    'in', 'the', 'past', 'it', 'may', 'have', 'not', 'be', 'possible', '.',
        ]
        self.assertEqual(l, expected)

    def test_tokenizer(self):
        l = list(tokenizer('It is now possible to teach a machine to excel a human endeavors, when in the past it may have not been possible.'))
        expected = ['possible','teach','machine','excel','human','endeavor','past','possible']
        self.assertEqual(l, expected)

if __name__ == '__main__':
    unittest.main()
