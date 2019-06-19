#!/usr/bin/env python
# -*- coding: utf-8 -*-
# flake8: noqa


"""
The SLATE table contains the corresponding flags to each card that is relevant
to Lands as an archetype.

The FORMS table lists all forms for a Manabond into Marit Lage on the first
turn.
"""


SLATE = {

    # Business
    'Crop Rotation':                    ('CR',),
    'Manabond':                         ('MB',),

    # Mana
    'Mox Diamond':                      ('MD',),

    # Lands
    'Ancient Tomb':                     ('L', '2',),
    'Blast Zone':                       ('L', '1',),
    'Bojuka Bog':                       ('L',),
    'Dark Depths':                      ('L', 'DD',),
    'Forest':                           ('L', 'G',),
    'Ghost Quarter':                    ('L', '1',),
    'Glacial Chasm':                    ('L',),
    "Hall of Heliod's Generosity":      ('L', '1',),
    'Horizon Canopy':                   ('L', '1', 'G', 'W',),
    'Karakas':                          ('L', 'W',),
    'Maze of Ith':                      ('L',),
    'Riftstone Portal':                 ('L', 'RP', '1',),
    'Rishadan Port':                    ('L', '1',),
    'Savannah':                         ('L', 'G', 'W',),
    'The Tabernacle at Pendrell Vale':  ('L',),
    "Thespian's Stage":                 ('L', 'TS', '1',),
    'Tranquil Thicket':                 ('L',),
    'Verdant Catacombs':                ('L', 'G', 'W',),
    'Wasteland':                        ('L', '1',),
    'Windswept Heath':                  ('L', 'G', 'W',),
    'Wooded Foothills':                 ('L', 'G', 'W',),
}

FORMS = {

    'No Mox Diamond, no Crop Rotation, no Ancient Tomb': [
        {'base': ((1, 'MB',), (1, 'DD',), (1, 'TS',), (0, '=MD',), (0, '=CR'), (0, '=2'))},
        ((1, '=G',), (2, '1|W',),),
        ((2, '=G',), (1, '1|W',),),
        ((3, 'G',),),
    ],

    'No Mox Diamond, no Crop Rotation, with Ancient Tomb': [
        {'base': ((1, 'MB',), (1, 'DD',), (1, 'TS',), (0, '=MD',), (0, '=CR'))},
        ((1, '2'), (1, 'G',),),
    ],
}
