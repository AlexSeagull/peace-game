# Import necessary modules
import random

# Define the ranks and suits
ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
suits = ("hearts", "diamonds", "clubs", "spades")

# Create a deck of cards
deck = [(rank,suit) for rank in ranks for suit in suits]

# Shuffle the deck 
random.shuffle(deck)

# Split the deck into two hands
hand1 = deck[0:26]
hand2 = deck[26:]
def card_comparison(p1_card, p2_card):
    """This is the logic that compares two cards to find the stronger card
		Return 1 if player 1's card is strong, 2 for player 2
		if the cards are equal, return 0.

		Hint, using the index function will make this very simple (one liner)"""
    # Your code here
    if ranks.index(p1_card[0])>ranks.index(p2_card[0]):
        return 1
    elif ranks.index(p1_card[0])<ranks.index(p2_card[0]):
        return 2
    else:
        return 0
def play_round(player1_hand, player2_hand):
    """Play a single round of the game.
		That is, each player flips a card, and the winner is determined using the card_comparison function
		if both players flip the same value card, call the war function
	"""
    # Your code here
    p1_card = player1_hand.pop(0)
    p2_card = player2_hand.pop(0)
    result = card_comparison(p1_card,p2_card)
    if result == 1:
        player1_hand.append(p1_card)
        player1_hand.append(p2_card)
    elif result == 2:
        player2_hand.append(p2_card)
        player2_hand.append(p1_card)
    else:
        player1_hand.append(p1_card)
        player2_hand.append(p2_card)
        war(player1_hand,player2_hand)
def war(player1_hand, player2_hand):
    """Handle the 'war' scenario when cards are equal.
		recall the rules of war, both players put 3 cards face down, 
		then both players flip face up a 4th card. The player with the stronger
		card takes all the cards.		
	"""
    # Your code here
    p1_card = player1_hand[-1]
    p2_card = player2_hand[-1]
def play_game():
    """Main function to run the game."""
    # Your code here
    while len(hand1)>0 and len(hand2)>0:
        play_round(player1_hand,player2_hand)
# Call the main function to start the game
play_game()
