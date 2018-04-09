#!/usr/bin/env python
# -*- coding: utf-8 -*-
from deck import Deck
from probability import Probability


if __name__ == '__main__':
    deck = Deck(file='')
    probability = Probability(deck=deck)
    for method in (
            m for m in dir(probability)
            if callable(getattr(probability, m)) and m.startswith('get_')
    ):
        print('{}: {}%'.format(
            method[4:].replace('_', ' ').title(),
            round(getattr(probability, method)() * 100, 2)),
        )
