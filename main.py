#!/usr/bin/env python
# -*- coding: utf-8 -*-
from argparse import ArgumentParser

from deck import Deck
from probability import Probability


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('slate', help='provide a slate file')
    parser.add_argument('deck', help='provide a deck file')
    parser.add_argument('-c', '--count', help='output the count of hands', action='store_true')
    parser.add_argument('-p', '--precise', help='round less', action='store_true')
    parser.add_argument('-v', '--verbose', help='increase output verbosity', action='store_true')
    p = parser.parse_args()
    deck = Deck(file=p.deck, slate=p.slate, verbose=p.verbose)
    probability = Probability(count=p.count, deck=deck, precise=p.precise, slate=p.slate)
    probability.run()
