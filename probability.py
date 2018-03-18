#!/usr/bin/env python
# -*- coding: utf-8 -*-
from itertools import chain

from cache import cache
from binomial import binomial as b
from starsnbars import starsnbars


"""
The following functions expect a well-formed deck as implemented in deck.Deck.

Prelude:

  We are assuming cards are castable either by themselves for no mana (eg.
  Gitaxian Probe) or from a land and/or Lotus Petal.

Notation:

  DD -- Doomsday
  DR -- Dark Ritual
        We are assuming the Dark Ritual is castable from either a land or a
        Lotus Petal.
  C  -- Cantrip
        We are assuming the cantrip is castable by itself or with other cards
        from the current hand. eg. 2 life or a U land or a Lotus Petal for a
        Gitaxian Probe.
  BZ -- Pile business
        This can be any of the elligible business pieces to put back with a
        Brainstorm.
  Z  -- Unused card

Functions:

  These functions basically divide the count of plausible hands by the count of
  total hands. Furthermore, each function implements a customized handling of
  mana costs.

  DOUBLE_CANTRIP
  A double cantrip hand consists of 2 cantrips, usually to consume a pile
  starting with LED and GP.
"""


b = cache(b)


class Probability:

    def __init__(self, deck=None):
        self.deck = deck
        self.counts = self.count_flags()

    def count_flags(self):
        """Count copies of each relevant flags.
        """

        counts = {flag: 0 for flag in (
            'BZ', 'BW', 'DD', 'LED',                   # Business
            'C', 'BS', 'CB', 'GP',                     # Cantrips
            'DR', 'LP', 'L', 'W', 'U', 'B', 'R', 'G',  # Mana
        )}
        for it in self.deck.library:
            for flag in counts:
                counts[flag] += 1 if flag in it['flags'] else 0
        return counts

    def double_cantrip(self):
        """Return the probability of a double cantrip hand.

        A double cantrip hand looks like [DR, DD, C, C, Z, Z, Z].
        """

        return (
            sum(chain(

                # # Scenario 1: [DR, DD, C, C, Z, Z, Z]
                # (
                #     b(self.counts['DR'], 1 + DR) *
                #     b(self.counts['DD'], 1 + DD) *
                #     b(self.counts['C'], 2 + C) *
                #     b(
                #         len(self.deck.library) -
                #         self.counts['DR'] - self.counts['DD'] - self.counts['C'],
                #         Z
                #     )
                #     for DR, DD, C, Z in starsnbars(3, 3)
                # ),

                # Scenario 2: [DR, DD, GP, GP, B, Z, Z]
                (
                    b(self.counts['DR'], 1 + DR) *
                    b(self.counts['DD'], 1 + DD) *
                    b(self.counts['GP'], 2 + GP) *
                    b(self.counts['B'], 1 + B) *
                    b(
                        len(self.deck.library) -
                        self.counts['DR'] - self.counts['DD'] - self.counts['GP'] - self.counts['B'],
                        Z
                    )
                    for DR, DD, GP, B, Z in starsnbars(2, 4)
                ),

            )) / b(60, 7)
        )
