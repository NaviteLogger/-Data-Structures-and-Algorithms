import collections
from random import choice, shuffle

Card = collections.namedtuple('Card', ['rank','suit'])

class PolishDeck:
    ranks = [str(n) for n in range (2,11)] + list('WDKA')
    suits = 'spades diamonds clubs hearts'.split()
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
        
    def __len__(self):
        return len(self._cards)
    def __getitem__(self, position):
        return self._cards[position]
    
exempler_card = Card('7','diamonds')
print(exempler_card)

deck = PolishDeck()
print(len(deck))

print(deck[0])
print(deck[-1])
print(deck[:3])

print(choice(deck))
print(choice(deck))
print(choice(deck))

print(deck[:3])
print(deck[12::13])

for card in deck:
    print(card)
    
for card in reversed(deck):
    print(card)
    
suit_values = dict(spades = 3, hearts = 2, diamonds = 1, clubs = 0)

def spades_high(card):
    rank_value = PolishDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key = spades_high):
    print(card)
    
deck = PolishDeck()

def set_card(deck, position, card):
    deck._cards[position] = card
    
PolishDeck.__setitem__ = set_card
shuffle(deck)
print(deck[:5])