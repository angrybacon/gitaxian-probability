#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pprint import pprint

from deck import Deck
from probability import Probability


if __name__ == '__main__':
    deck = Deck(file='')
    probability = Probability(deck=deck)
    pprint(probability.double_cantrip())
