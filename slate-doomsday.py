#!/usr/bin/env python
# -*- coding: utf-8 -*-
# flake8: noqa


"""
The SLATE table contains the corresponding flags to each card that is relevant
to Doomsday as an archetype.

The FORMS table lists all forms for a first turn kill.
"""


SLATE = {

    # Business
    'Act on Impulse':       ('AoI',),
    # 'Burning Wish':         ('BW',),
    'Doomsday':             ('DD',),
    'Ideas Unbound':        ('IU',),
    # 'Laboratory Maniac':    ('LM',),
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
    # 'Cabal Ritual':         ('CR',),
    'Dark Ritual':          ('DR',),
    'Island':               ('L', 'U',),
    'Lotus Petal':          ('LP',),
    'Marsh Flats':          ('L', 'W', 'U', 'B', 'R', 'G',),
    'Plains':               ('L', 'W',),
    'Polluted Delta':       ('L', 'W', 'U', 'B', 'R', 'G',),
    'Scalding Tarn':        ('L', 'W', 'U', 'B', 'R', 'G',),
    'Swamp':                ('L', 'B',),
    'Tropical Island':      ('L', 'U', 'G',),
    'Tundra':               ('L', 'W', 'U',),
    'Underground Sea':      ('L', 'U', 'B',),
    'Verdant Catacombs':    ('L', 'W', 'U', 'B', 'R', 'G',),
    'Volcanic Island':      ('L', 'U', 'R',),
}

FORMS = {

    'Double Cantrip': [
        {'base': ((1, 'DD'), (0, '=AoI'), (0, '=IU'), (0, '=LED'), (0, '=TW'),)},
        ((1, '=DR'),     (1, 'L'),       (2, 'LP'),      (2, 'C'),                                       ),  # 7
        ((1, '=DR'),                     (3, 'LP'),      (2, 'C'),                                       ),  # 7
        ((1, '=DR'),     (1, 'L'),       (1, '=LP'),     (1, 'C'),       (1, '=GP'),                     ),  # 6
        ((1, '=DR'),                     (2, 'LP'),      (1, 'C'),       (1, '=GP'),                     ),  # 6
        ((1, '=DR'),     (1, 'L|LP'),    (2, 'GP'),                                                      ),  # 5
        ((2, '=DR'),     (1, 'L'),       (1, 'LP'),      (1, 'C'),       (1, 'GP|CB'),                   ),  # 7
        ((2, '=DR'),                     (2, 'LP'),      (1, 'C'),       (1, 'GP|CB'),                   ),  # 7
        ((2, '=DR'),     (1, 'L|LP'),                    (2, 'GP'),                                      ),  # 6
        ((2, '=DR'),     (1, 'L|LP'),                    (2, 'CB'),                                      ),  # 6
        ((2, '=DR'),     (1, 'L|LP'),                    (1, '=CB'),     (1, '=GP'),                     ),  # 6
        ((2, '=DR'),     (1, 'L|LP'),                    (1, '=C'),      (1, 'CS'),                      ),  # 6
        ((2, '=DR'),     (1, 'L|LP'),                    (1, '=GP'),     (1, 'CS'),                      ),  # 6
        ((3, 'DR'),      (1, 'L|LP'),                    (2, 'GP'),                                      ),  # 7
    ],

    'Draw-3 in Hand': [
        {'base': ((1, 'DD'), (0, '=LED'),)},
        ((1, '=DR'),     (1, 'L'),       (3, 'LP'),      (1, 'AoI|TW'),                                  ),  # 7
        ((1, '=DR'),                     (4, 'LP'),      (1, 'AoI|TW'),                                  ),  # 7
        ((1, '=DR'),     (1, 'L'),       (2, 'LP'),      (1, 'AoI|TW'),  (1, 'GP'),                      ),  # 7
        ((1, '=DR'),                     (3, 'LP'),      (1, 'AoI|TW'),  (1, 'GP'),                      ),  # 7
        ((2, '=DR'),     (1, 'L'),       (1, '=LP|GP'),  (1, 'AoI'),                                     ),  # 6
        ((2, '=DR'),                     (2, 'LP'),      (1, 'AoI'),                                     ),  # 6
        ((2, '=DR'),     (1, 'L'),       (2, 'LP'),      (1, 'TW'),                                      ),  # 7
        ((2, '=DR'),                     (3, 'LP'),      (1, 'TW'),                                      ),  # 7
        ((2, '=DR'),     (1, 'L'),       (1, 'LP'),      (1, 'TW'),      (1, 'CS'),                      ),  # 7
        ((2, '=DR'),                     (2, 'LP'),      (1, 'TW'),      (1, 'CS'),                      ),  # 7
        ((3, 'DR'),      (1, 'L|LP'),                    (1, 'AoI|TW'),  (1, 'CS'),                      ),  # 7
        ((1, '=DR'),     (1, 'L|GP'),    (2, '=LP'),     (1, 'IU'),                                      ),  # 6
        ((1, '=DR'),                     (3, 'LP'),      (1, 'IU'),                                      ),  # 6
        ((1, '=DR'),     (1, 'L|LP'),                    (1, 'IU'),      (2, 'GP'),                      ),  # 6
        ((1, '=DR'),     (1, 'L'),       (1, '=LP'),     (1, 'IU'),      (1, 'GP'),                      ),  # 6
        ((2, 'DR'),      (1, 'L|GP|CS'), (2, 'LP'),      (1, 'IU'),                                      ),  # 7
        ((2, 'DR'),      (1, 'L'),       (1, 'LP'),      (1, 'IU'),      (1, 'GP'),                      ),  # 7
        ((2, 'DR'),      (1, 'L|LP'),                    (1, 'IU'),      (2, 'GP'),                      ),  # 7
        ((2, 'DR'),      (1, 'L|LP'),                    (1, 'IU'),      (1, 'CS'),                      ),  # 6
    ],

    'LED in Hand': [
        {'base': ((1, 'DD'),)},
        ((1, 'DR'),      (1, 'L|LP'),                    (1, 'LED'),     (1, 'GP'),                      ),  # 5
        ((1, 'DR'),      (1, '=L'),      (1, '=LP'),     (1, 'LED'),     (1, '=C'),      (0, 'GP'),      ),  # 6
        ((1, 'DR'),                      (2, '=LP'),     (1, 'LED'),     (1, '=C'),      (0, 'GP'),      ),  # 6
    ],

}
