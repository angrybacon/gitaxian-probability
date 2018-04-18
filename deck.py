#!/usr/bin/env python
# -*- coding: utf-8 -*-
from importlib import import_module
import random
import re


class Deck:

    RE_CARD = re.compile(r'^([0-9]+)[\t ]+(.+)$')

    def __init__(self, name=None, file=None, slate=None, verbose=False):
        self.name = name
        self.file = file
        self.slate = import_module('slate-' + slate).SLATE
        self.verbose = verbose
        self.mainboard = []
        self.sideboard = []
        self.get_decklist()
        self.library = self.mainboard[:]
        self.shuffle()

    def get_decklist(self):
        """Read a deck from a text-based deck file.

        Anything past a line containing "Sideboard" in it will be considered
        sideboard content.
        """

        with open(self.file, 'r') as file:
            is_sideboard = False
            for line in file:
                line = line.strip()
                if is_sideboard is False and 'sideboard' in line.lower():
                    is_sideboard = True
                match = self.RE_CARD.match(line)
                card = match.groups() if match is not None else None
                if card is not None:
                    container = self.sideboard if is_sideboard else self.mainboard
                    flags = self.slate.get(card[1])
                    if self.verbose and flags is None and not is_sideboard:
                        print('Ignoring {}'.format(card[1]))
                    container.extend(({
                        'card': card[1],
                        'flags': flags or (),
                    },) * int(card[0]))

    def shuffle(self):
        random.shuffle(self.library)

    def draw(self, size=1):
        return (self.library.pop(0) for _ in range(size))
