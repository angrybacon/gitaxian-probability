#!/usr/bin/env python
# -*- coding: utf-8 -*-
from functools import reduce
from itertools import chain

from cache import cache
from binomial import binomial as b
from slate import FORMS
from starsnbars import starsnbars


b = cache(b)


"""
The following functions expect a well-formed deck as implemented in deck.Deck.

Prelude:

  We are assuming cards are castable either by themselves for no mana (eg.
  Gitaxian Probe) or from a land and/or Lotus Petal.

  These features basically divide the count of matching hands by the count of
  total hands.

Notation:

  See slate.py.

Mathematics:

  Below is an example picturing the algorithm chosen to describe the probability
  to obtain a specific given hand.

  The following expression counts the total number of different unordered hands
  that are exactly:
  - 1 copy of Dark Ritual
  - 1 copy of Doomsday
  - 5 cards that are neither Dark Ritual nor Doomsday

      count = b(4, 1) * b(3, 1) * b(53, 5)

  Therefore, the probability of drawing these exact specific hands, out of
  b(60, 7) total different unordered hands, is:

      probability = count / b(60, 7)

  However, what if we allowed the 5 last cards to be anything? Where anything is
  any of the 3 remaining copies of Dark Ritual, the 2 remaining copies of
  Doomsday or the 53 other cards.

  Let x be the allowed count of extra copies of Dark Ritual.
  Let y be the allowed count of extra copies of Doomsday.
  Let z be the allowed count of cards that are neither Dark Ritual nor Doomsday.

      count = b(4, 1 + x) * b(3, 1 + y) * b(53, z)

  Furthermore, 1 + x + 1 + y + z must add up to exactly 7 since we don't take
  mulligan actions into account. Therefore, we now know that we need to sum all
  the counts of hands for each permutation of the 3-tuples (x, y, z) following
  the Stars and Bars aid.
"""


HAND_SIZE = 7


class Probability:

    def __init__(self, count=False, deck=None, precise=False):
        self.count_only = count
        self.deck = deck
        self.precise = precise
        self.counts = self.count_flags()

    def count_flags(self):
        """Count copies of each relevant flags.
        """

        counts = {flag: 0 for flag in (
            'AoI', 'BZ', 'BW', 'DD', 'LED',                 # Business
            'C', 'BS', 'CB', 'GP',                          # Cantrips
            'DR', 'LP', 'L', '1', 'W', 'U', 'B', 'R', 'G',  # Mana
        )}
        for it in self.deck.library:
            for flag in counts:
                counts[flag] += 1 if flag in it['flags'] else 0
        return counts

    def count_flag(self, query):
        """Return the count of cards for a given query of flags.

        Ill-support for the separator `|` was added. However, since we draw
        cards with no replacement, you should not write a scenario form that
        uses the same flag with and without a `|` seperator. For instance:

          The following C is not equivalent to A+B:
          - 'A': ((4, 'DR',), (1, 'DD',), (1, 'L',), (3, 'LP',)),
          - 'B': ((4, 'DR',), (1, 'DD',), (1, 'LP',), (3, 'LP',)),
          - 'C': ((4, 'DR',), (1, 'DD',), (1, 'L|LP',), (3, 'LP',)),

          The following C is equivalent to A+B:
          - 'A': ((4, 'DR',), (1, 'DD',), (1, 'L',),),
          - 'B': ((4, 'DR',), (1, 'DD',), (1, 'LP',),),
          - 'C': ((4, 'DR',), (1, 'DD',), (1, 'L|LP',),),
        """

        return sum(self.counts[flag] for flag in query.split('|'))

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

        flags = tuple(flags)
        requirement_count = sum(flag['requirements'] for flag in flags)
        return sum(
            reduce(lambda x, y: x * y, (
                b(self.count_flag(flag['key']), flag['requirements'] + ktuple[i])
                for i, flag in enumerate(flags)
            )) *
            (b(
                reduce(
                    lambda x, y: x - y,
                    (len(self.deck.library),) +
                    tuple(self.count_flag(flag['key']) for flag in flags),
                ),
                ktuple[-1]
            ) if requirement_count < HAND_SIZE else 1)  # NOTE: There is no remainder.
            for ktuple in starsnbars(HAND_SIZE - requirement_count, len(flags))
        )

    def run(self):
        """Compute the scenarii found in slate.FORMS.
        """

        results = {}
        for label, forms in FORMS.items():
            results[label] = sum(
                self.count_hands(chain(
                    {'key': key, 'requirements': amount} for amount, key in form,
                )) for form in forms
            )
        for label, result in results.items():
            if self.count_only:
                print('{}: {} hands'.format(label, result))
            else:
                print('{}: {}%'.format(
                    label,
                    round(
                        result / b(len(self.deck.library), HAND_SIZE) * 100,
                        6 if self.precise else 2,
                    ),
                ))
