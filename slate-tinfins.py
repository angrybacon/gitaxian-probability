#!/usr/bin/env python
# -*- coding: utf-8 -*-
# flake8: noqa


"""
The SLATE table contains the corresponding flags to each card that is relevant
to Tin Fins as an archetype.

The FORMS table lists all forms for a first turn draw 21.
"""


SLATE = {

    # Business
    'Corpse Dance':              ('CD',),
    # 'Emrakul, the Aeons Torn':   ('Em'),
    'Entomb':                    ('En',),
    'Griselbrand':               ('Gr'),
    'Lion\'s Eye Diamond':       ('LED',),
    # 'Magus of the Mind':         ('MM',),
    # 'Mastermind\'s Acquisition': ('MA',),
    # 'Past in Flames':            ('PiF',),
    'Shallow Grave':             ('SG',),

    # Cantrips
    # 'Brainstorm':                ('C', 'BS',),
    # 'Gitaxian Probe':            ('GP',),
    # 'Ponder':                    ('C',),

    # Discard
    # 'Cabal Therapy':             ('D',),
    # 'Collective Brutality':      ('CoBr',),
    # 'Thoughtseize':              ('D',),

    # Mana
    'Badlands':                  ('L', 'B', 'R',),
    # 'Cabal Ritual':              ('CR',),
    'Dark Ritual':               ('DR',),
    'Island':                    ('L', 'U',),
    'Lotus Petal':               ('LP',),
    'Marsh Flats':               ('L', 'W', 'U', 'B', 'R', 'G',),
    'Plains':                    ('L', 'W',),
    'Polluted Delta':            ('L', 'W', 'U', 'B', 'R', 'G',),
    'Scalding Tarn':             ('L', 'W', 'U', 'B', 'R', 'G',),
    'Swamp':                     ('L', 'B',),
    'Tropical Island':           ('L', 'U', 'G',),
    'Tundra':                    ('L', 'W', 'U',),
    'Underground Sea':           ('L', 'U', 'B',),
    'Verdant Catacombs':         ('L', 'W', 'U', 'B', 'R', 'G',),
    'Volcanic Island':           ('L', 'U', 'R',),
}

FORMS = {

    'Entomb in Hand': [
        ((1, 'B|LP'),    (1, 'DR'),      (1, 'En'),      (1, 'SG'),                      ),  # 4
    ],

}
