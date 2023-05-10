# WarCardGame
This is a digital implementation of the classic card game, War. The game is designed to be played by two players.

## Requirements

### Initialization
At the start of each game, a deck needs to be initialized in a random order.

### Deck Distribution
Once the deck is initialized, it should be split evenly between the two players.

### Gameplay
Players will then take turns drawing the top card from their hand. The player with the higher card takes both cards and adds them to the bottom of their deck. If the cards are the same rank, war is declared.

### War Mechanism 
In a war, each player draws three cards face down and one card face up. The player with the higher face-up card wins all the cards involved in the war. If the face-up cards are again the same rank, the war continues with another set of face-down and face-up cards, until there is a winner.

### End Game 
The game ends when one player has all the cards, or if a player runs out of cards during a war. The player with all the cards is the winner.