import random
from pyCardDeck.cards import PokerCard
from pyCardDeck.deck import CardDeck

# Card class implementation 
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        
# Deck class implementation 
class Deck:
    def __init__(self):
        self.deck = CardDeck()
        self.build()

    def build(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
        for suit in suits:
            for rank in ranks:
                self.deck.add_card(PokerCard(rank, suit))

    def shuffle(self):
        self.deck.shuffle()

    def deal(self):
        return self.deck.draw()
