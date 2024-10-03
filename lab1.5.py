# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 11:41:11 2024

@author: s223287
"""

import collections
import random

Card = collections.namedtuple('Card', ['rank', 'suit'])

class PolishDeck:
    
    ranks = [str(n) for n in range(2,11)] + list('WDKA')
    suits = 'spades diamonds clubs hearts'.split()
    
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
        
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position: int):
        return self._cards[position]
    

sampleCard = Card('7', 'diamonds')
print(sampleCard)

deck = PolishDeck()
print(f"Dlugosc decku: {len(deck)}")
print(deck[0])
print(deck[-1])
print(deck[:3])

print("\nLosowe karty")
print(random.choice(deck))
print(random.choice(deck))
print(random.choice(deck))

for card in deck:
    print(f"Karta: {card}")
    

print("\nOdwrocona talia")
for card in reversed(deck):
    print(f"Karta: {card}")
    
print('')
print("Czy karta jets w talii?")
print(Card('D', 'hearts') in deck)

suit_values: dict = dict(
    spades = 3,
    hearts = 2,
    diamonds = 1,
    clubs = 0
)

def spades_high(card):
    rank_value = PolishDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):
    print(card)
    
nowyDeck = PolishDeck()

def set_card(deck, position, card):
    deck._cards[position] = card
    
PolishDeck.__setitem__ = set_card
random.shuffle(deck)
print (deck[:5])