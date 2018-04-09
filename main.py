#!/usr/bin/env python
# -*- coding: utf-8 -*-
from argparse import ArgumentParser

from deck import Deck
from probability import Probability


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('deck', help='provide a deck file')
    parser.add_argument('-v', '--verbose', help='increase output verbosity', action='store_true')
    arguments = parser.parse_args()
    deck = Deck(file=arguments.deck, verbose=arguments.verbose)
    probability = Probability(deck=deck)
    probability.run()
