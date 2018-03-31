#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pprint import pprint

from deck import Deck
from probability import Probability


if __name__ == '__main__':
    deck = Deck(file='')
    probability = Probability(deck=deck)
    print('Double cantrip: {}%'.format(round(probability.double_cantrip() * 100, 2)))
