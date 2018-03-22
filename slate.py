#!/usr/bin/env python
# -*- coding: utf-8 -*-
# flake8: noqa


"""
The following table contains the corresponding flags to each card that is
relevant to Doomsday as an archetype.

Why?

  This is useful to count a given "kind" of cards accross the library.

Notation:

  BZ  --  Pile business
          This can be any of the elligible business pieces to put back with a
          Brainstorm.
  C   --  Cantrip
          We are assuming the cantrip is castable by itself or with other cards
          from the current hand. eg. 2 life or a U land or a Lotus Petal for a
          Gitaxian Probe.
  L   --  Land
  Z   --  Unused card
"""


SLATE = {

    # Business
    'Act on Impulse':      ('BZ',),
    'Burning Wish':        ('BZ', 'BW',),
    'Doomsday':            ('BZ', 'DD',),
    'Laboratory Maniac':   ('BZ',),
    "Lion's Eye Diamond":  ('BZ', 'LED',),

    # Cantrips
    'Brainstorm':          ('C', 'BS',),
    "Conjurer's Bauble":   ('C', 'CB',),
    'Gitaxian Probe':      ('C', 'GP',),
    'Ponder':              ('C',),
    'Preordain':           ('C',),

    # Mana
    'Badlands':            ('L', 'B', 'R',),
    'Dark Ritual':         ('DR',),
    'Island':              ('L', 'U',),
    'Lotus Petal':         ('LP', 'W', 'U', 'B', 'R', 'G',),
    'Polluted Delta':      ('L', 'U', 'B', 'R', 'G',),
    'Scalding Tarn':       ('L', 'U', 'B', 'R', 'G',),
    'Swamp':               ('L', 'B',),
    'Tropical Island':     ('L', 'U', 'G',),
    'Underground Sea':     ('L', 'U', 'B',),
    'Verdant Catacombs':   ('L', 'U', 'B', 'R', 'G',),
    'Volcanic Island':     ('L', 'U', 'R',),
}
