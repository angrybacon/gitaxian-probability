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
    'Act on Impulse':       ('AoI',),
    'Burning Wish':         ('BW',),
    'Doomsday':             ('DD',),
    'Ideas Unbound':        ('IU',),
    'Laboratory Maniac':    (),
    'Lion\'s Eye Diamond':  ('LED',),
    'Three Wishes':         ('TW',),

    # Cantrips
    'Brainstorm':           ('C', 'BS',),
    'Chromatic Sphere':     ('CS',),
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

    'Double Cantrip': [
        {'base': ((1, 'DD',),)},
        ((1, '=DR',), (1, 'L',),       (2, 'LP',),     (2, 'C',),                    ),  # 7
        ((1, '=DR',),                  (3, 'LP',),     (2, 'C',),                    ),  # 7
        ((1, '=DR',), (1, 'L',),       (1, '=LP',),    (1, 'C',),      (1, '=GP',),  ),  # 6
        ((1, '=DR',),                  (2, 'LP',),     (1, 'C',),      (1, '=GP',),  ),  # 6
        ((1, '=DR',), (1, 'L|LP',),                                    (2, 'GP',),   ),  # 5
        ((2, '=DR',), (1, 'L',),       (1, 'LP',),     (1, 'C',),      (1, 'GP|CB',),),  # 7
        ((2, '=DR',),                  (2, 'LP',),     (1, 'C',),      (1, 'GP|CB',),),  # 7
        ((2, '=DR',), (1, 'L|LP',),                    (2, 'GP',),                   ),  # 6
        ((2, '=DR',), (1, 'L|LP',),                    (2, 'CB',),                   ),  # 6
        ((2, '=DR',), (1, 'L|LP',),                    (1, '=CB',),    (1, '=GP',),  ),  # 6
        ((2, '=DR',), (1, 'L|LP',),                    (1, '=C',),     (1, 'CS',),   ),  # 6
        ((2, '=DR',), (1, 'L|LP',),                    (1, '=GP',),    (1, 'CS',),   ),  # 6
        ((3, 'DR',),  (1, 'L|LP',),                    (2, 'GP',),                   ),  # 7
    ],

    'Draw-3 in Hand': [
        {'base': ((1, 'DD',),)},
        ((1, '=DR',), (1, 'L',),       (3, 'LP',),     (1, 'AoI|TW',),               ),  # 7
        ((1, '=DR',),                  (4, 'LP',),     (1, 'AoI|TW',),               ),  # 7
        ((1, '=DR',), (1, 'L',),       (2, 'LP',),     (1, 'AoI|TW',), (1, 'GP',),   ),  # 7
        ((1, '=DR',),                  (3, 'LP',),     (1, 'AoI|TW',), (1, 'GP',),   ),  # 7
        ((2, '=DR',), (1, 'L',),       (1, '=LP|GP',), (1, 'AoI',),                  ),  # 6
        ((2, '=DR',),                  (2, 'LP',),     (1, 'AoI',),                  ),  # 6
        ((2, '=DR',), (1, 'L',),       (2, 'LP',),     (1, 'TW',),                   ),  # 7
        ((2, '=DR',),                  (3, 'LP',),     (1, 'TW',),                   ),  # 7
        ((2, '=DR',), (1, 'L',),       (1, 'LP',),     (1, 'TW',),     (1, 'CS',),   ),  # 7
        ((2, '=DR',),                  (2, 'LP',),     (1, 'TW',),     (1, 'CS',),   ),  # 7
        ((3, 'DR',),  (1, 'L|LP',),                    (1, 'AoI|TW',), (1, 'CS',),   ),  # 7
        ((1, '=DR',), (1, 'L|GP',),    (2, '=LP',),    (1, 'IU',),                   ),  # 6
        ((1, '=DR',),                  (3, 'LP',),     (1, 'IU',),                   ),  # 6
        ((1, '=DR',), (1, 'L|LP',),                    (1, 'IU',),     (2, 'GP'),    ),  # 6
        ((1, '=DR',), (1, 'L',),       (1, '=LP',),    (1, 'IU',),     (1, 'GP'),    ),  # 6
        ((2, 'DR',),  (1, 'L|GP|CS',), (2, 'LP',),     (1, 'IU',),                   ),  # 7
        ((2, 'DR',),  (1, 'L',),       (1, 'LP',),     (1, 'IU',),     (1, 'GP',),   ),  # 7
        ((2, 'DR',),  (1, 'L|LP',),                    (1, 'IU',),     (2, 'GP',),   ),  # 7
        ((2, 'DR',),  (1, 'L|LP',),                    (1, 'IU',),     (1, 'CS',),   ),  # 6
    ],
}
