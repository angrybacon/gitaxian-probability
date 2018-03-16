#!/usr/bin/env python
# -*- coding: utf-8 -*-
from binomial import binomial


"""
The following functions expect a well-formed deck as implemented in deck.Deck.

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

Functions:

  DOUBLE_CANTRIP
  A double cantrip pile needs the following starting hand:
  DR, DD, C, C
"""


class Probability:

    def __init__(self, deck=None):
        self.deck = deck
        flags = (
            'BZ', 'BW', 'DD', 'LED',  # Business
            'C', 'BS', 'CB', 'GP',    # Cantrips
            'L', 'U', 'B', 'R', 'G',  # Lands
            'DR', 'LP',               # Mana
        )
        self.data = {flag: 0 for flag in flags}
        for it in self.deck.library:
            for flag in flags:
                self.data[flag] += 1 if flag in it['flags'] else 0

    def double_cantrip(self):
        """Return the probability of a double cantrip pile.
        """

        return binomial(3, 1) * binomial(4, 1) * binomial(16, 2) * binomial(60, 3) / binomial(60, 7)
