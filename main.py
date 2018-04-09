#!/usr/bin/env python
# -*- coding: utf-8 -*-
from deck import Deck
from probability import Probability


if __name__ == '__main__':
    deck = Deck(file='')
    probability = Probability(deck=deck)
    probability.run()
