#!/usr/bin/env python
# -*- coding: utf-8 -*-
from functools import reduce
from itertools import chain

from cache import cache
from binomial import binomial as b
from starsnbars import starsnbars


b = cache(b)


"""
The following functions expect a well-formed deck as implemented in deck.Deck.

Prelude:

  We are assuming cards are castable either by themselves for no mana (eg.
  Gitaxian Probe) or from a land and/or Lotus Petal.

Notation:

  See slate.py.

Functions:

  These functions basically divide the count of plausible hands by the count of
  total hands. Furthermore, each function implements a customized handling of
  mana costs.

  DOUBLE_CANTRIP
  A double cantrip hand consists of 2 cantrips, usually to consume a pile
  starting with LED and GP.
"""


HAND_SIZE = 7


class Probability:

    def __init__(self, deck=None):
        self.deck = deck
        self.counts = self.count_flags()

    def count_flags(self):
        """Count copies of each relevant flags.
        """

        counts = {flag: 0 for flag in (
            'BZ', 'BW', 'DD', 'LED',                        # Business
            'C', 'BS', 'CB', 'GP',                          # Cantrips
            'DR', 'LP', 'L', '1', 'W', 'U', 'B', 'R', 'G',  # Mana
        )}
        for it in self.deck.library:
            for flag in counts:
                counts[flag] += 1 if flag in it['flags'] else 0
        return counts

    def count_hands(self, flags):
        """Count all the unordered hands that respect the specified flags.

        Essentially, this means that it will return the number of different
        ways to draw each of the requirements according to
        self.deck.library.

        A well-formed iterable of flags is as follow:
          {'key': 'DR', 'requirements': 1},
          {'key': 'DD', 'requirements': 1},

        These flags each contain the key for a given flag to account for
        and its corresponding requirement as a positive integer.
        """

        requirement_count = sum(flag['requirements'] for flag in flags)
        return sum(
            reduce(lambda x, y: x * y, (
                b(self.counts[flag['key']], flag['requirements'] + ktuple[i])
                for i, flag in enumerate(flags)
            )) *
            b(
                reduce(
                    lambda x, y: x - y,
                    (len(self.deck.library),) +
                    tuple(self.counts[flag['key']] for flag in flags),
                ),
                ktuple[-1]
            ) for ktuple in starsnbars(7 - requirement_count, len(flags))
        )

    def get_double_cantrip(self):
        """Return the probability of a double cantrip hand.
        """

        return (
            sum((

                self.count_hands((
                    {'key': 'B', 'requirements': 1},
                    {'key': 'DR', 'requirements': 1},
                    {'key': 'DD', 'requirements': 1},
                    {'key': 'GP', 'requirements': 2},
                )),

            )) / b(len(self.deck.library), HAND_SIZE)
        )
