#!/usr/bin/env python
import random
import re


RE = re.compile(r'^([0-9]+)[\t ]+(.+)$')


class Deck:

    def __init__(self, name=None, file=None):
        self.name = name
        self.file = file
        self.mainboard = []
        self.sideboard = []
        self.get_decklist()
        self.library = self.mainboard[:]
        self.shuffle()

    def get_decklist(self):
        with open(self.file, 'r') as file:
            is_sideboard = False
            for line in file:
                line = line.strip()
                if is_sideboard is False and 'sideboard' in line.lower():
                    is_sideboard = True
                match = RE.match(line)
                card = match.groups() if match is not None else None
                if card is not None:
                    container = self.sideboard if is_sideboard else self.mainboard
                    container.extend((card[1],) * int(card[0]))

    def shuffle(self):
        random.shuffle(self.library)

    def draw(self, size=1):
        return (self.library.pop(0) for _ in range(size))


if '__main__':
    deck = Deck(file='doomsday.ubrg.dec')
    hand = []
    hand.extend(deck.draw(7))
    print(hand)
