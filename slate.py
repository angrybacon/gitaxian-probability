#!/usr/bin/env python
# -*- coding: utf-8 -*-
# flake8: noqa


"""
The SLATE table contains the corresponding flags to each card that is relevant
to Doomsday as an archetype.

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
  ?   --  Unused card

  See the more common abbreviations at
  http://ddft.wiki/pages-output/ch1/basics/.

Lastly, list all forms for a first turn kill. Scenarii can be written using a
custom-made syntax:

  |  --  Use this character as a separator for flags to consider on the slot.
  =  --  Prefix a flag with this character to indicate that the requirement count
         should be exact.
"""


SLATE = {

    # Business
    'Act on Impulse':       ('BZ', 'AoI',),
    'Burning Wish':         ('BZ', 'BW',),
    'Doomsday':             ('BZ', 'DD',),
    'Laboratory Maniac':    ('BZ',),
    'Lion\'s Eye Diamond':  ('BZ', 'LED',),

    # Cantrips
    'Brainstorm':           ('C', 'BS',),
    'Conjurer\'s Bauble':   ('C', 'CB',),
    'Gitaxian Probe':       ('GP',),
    'Ponder':               ('C',),
    'Preordain':            ('C',),

    # Mana
    'Badlands':             ('L', 'B', 'R',),
    'Dark Ritual':          ('DR',),
    'Island':               ('L', 'U',),
    'Lotus Petal':          ('LP',),
    'Polluted Delta':       ('L', 'U', 'B', 'R', 'G',),
    'Scalding Tarn':        ('L', 'U', 'B', 'R', 'G',),
    'Swamp':                ('L', 'B',),
    'Tropical Island':      ('L', 'U', 'G',),
    'Underground Sea':      ('L', 'U', 'B',),
    'Verdant Catacombs':    ('L', 'U', 'B', 'R', 'G',),
    'Volcanic Island':      ('L', 'U', 'R',),
}

FORMS = {

    'Double Cantrip': (
        ((1, 'DR',), (1, 'DD',), (1, 'L',),    (2, 'LP',),  (2, 'C',),             ),
        ((1, 'DR',), (1, 'DD',),               (3, 'LP',),  (2, 'C',),             ),
        ((1, 'DR',), (1, 'DD',), (1, 'L',),    (1, '=LP',), (1, 'C',), (1, '=GP',),),
        ((1, 'DR',), (1, 'DD',),               (2, 'LP',),  (1, 'C',), (1, '=GP',),),
        ((1, 'DR',), (1, 'DD',), (1, 'L|LP',),                         (2, 'GP',), ),
    ),

    'Draw-3 in Hand': (
        ((1, 'DR',), (1, 'DD',), (1, 'L',),    (3, 'LP',),     (1, 'AoI',)              ),
        ((1, 'DR',), (1, 'DD',),               (4, 'LP',),     (1, 'AoI',)              ),
        ((1, 'DR',), (1, 'DD',), (1, 'L',),    (2, 'LP',),     (1, 'AoI',), (1, 'GP',), ),
        ((1, 'DR',), (1, 'DD',),               (3, 'LP',),     (1, 'AoI',), (1, 'GP',), ),
        ((2, 'DR',), (1, 'DD',), (1, 'L',),    (1, '=LP|GP',), (1, 'AoI',),             ),
        ((2, 'DR',), (1, 'DD',),               (2, 'LP',),     (1, 'AoI',),             ),
        ((2, 'DR',), (1, 'DD',), (1, 'L|LP',),                 (1, 'AoI',), (2, '=GP',),),
    ),
}
