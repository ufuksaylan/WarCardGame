import random

# Card class implementation 
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"
        
# Deck class implementation 
from pyCardDeck import Deck
from pyCardDeck.cards import PokerCard

class Deck:
    def __init__(self):
        self.cards = [Card(suit, value) for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']
                                        for value in range(2, 15)]  # Values 2-14 represent 2-Ace
    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()


# player class implementation 
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
    

class Game:
    def __init__(self, player1_name, player2_name):
        self.deck = Deck()
        self.deck.shuffle()
        self.players = [Player(player1_name), Player(player2_name)]

    def distribute_cards(self):
        while len(self.deck.cards) != 0:
            self.players[0].hand.append(self.deck.draw_card())
            self.players[1].hand.append(self.deck.draw_card())

    def play(self):
        self.distribute_cards()
        round_number = 1
        while len(self.players[0].hand) > 0 and len(self.players[1].hand) > 0:
            card1 = self.players[0].hand.pop(0)
            card2 = self.players[1].hand.pop(0)
            print(f"Round {round_number}:")
            print(f"{self.players[0].name} plays {card1.value} of {card1.suit}")
            print(f"{self.players[1].name} plays {card2.value} of {card2.suit}")
            if card1.value > card2.value:
                self.players[0].hand.append(card1)
                self.players[0].hand.append(card2)
                print(f"{self.players[0].name} wins the round\n")
            else: # In case of a tie, player 1 wins
                self.players[1].hand.append(card1)
                self.players[1].hand.append(card2)
                print(f"{self.players[1].name} wins the round\n")
            round_number += 1
        
        if len(self.players[0].hand) > 0:
            return self.players[0].name
        else:
            return self.players[1].name


def main():
    game = Game("Player 1", "Player 2")
    winner = game.play()
    print(f"The winner is {winner}")

if __name__ == "__main__":
    main()