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
player1_hand = deck[0:26]
player2_hand = deck[26:]

war_list =[]
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
def play_round(player1_hand, player2_hand,war_list):
    """Play a single round of the game.
		That is, each player flips a card, and the winner is determined using the card_comparison function
		if both players flip the same value card, call the war function
	"""
    # Your code here
    p1_card = player1_hand.pop(0)
    p2_card = player2_hand.pop(0)
    print(p1_card)
    print(p2_card)
    result = card_comparison(p1_card,p2_card)
    if result == 1:
        player1_hand.append(p1_card)
        player1_hand.append(p2_card)
    elif result == 2:
        player2_hand.append(p2_card)
        player2_hand.append(p1_card)
    else:
        war(player1_hand,player2_hand,war_list,p1_card,p2_card)
    print(len(player1_hand))
    print(len(player2_hand))
    return player1_hand, player2_hand
def war(player1_hand, player2_hand,war_list,p1_card,p2_card):
    """Handle the 'war' scenario when cards are equal.
		recall the rules of war, both players put 3 cards face down, 
		then both players flip face up a 4th card. The player with the stronger
		card takes all the cards.		
	"""
    # Your code here
    war_list = []
    result = 0
    war_list.insert(0,p2_card)
    war_list.insert(0,p1_card)
    while result != 1 and result != 2:
        if len(player1_hand) <5:
            player2_hand.extend(player1_hand)
            player2_hand.append(p1_card)
            player2_hand.append(p2_card)
            player1_hand = []
            result = 0
            return player1_hand, player2_hand
        elif len(player2_hand) <5:
            player1_hand.append(p1_card)
            player1_hand.append(p2_card)
            player1_hand.extend(player2_hand)
            player2_hand = []
            result = 0
            return player2_hand, player1_hand
        else:
            war_list += [player1_hand.pop(0) for _ in range(3)]
            war_list += [player2_hand.pop(0) for _ in range(3)]
            p1_card = player1_hand.pop(0)
            print(p1_card)
            p2_card = player2_hand.pop(0)
            print(p2_card)
            result = card_comparison(p1_card,p2_card)
            if result == 1:
                player1_hand.append(p1_card)
                player1_hand.append(p2_card)
                player1_hand.extend(war_list)
            elif result == 2:
                player2_hand.append(p1_card)
                player2_hand.append(p2_card)
                player2_hand.extend(war_list)
            else:
                war_list.append(p1_card)
                war_list.append(p2_card)
    return war_list, player1_hand, player2_hand
def play_game():
    """Main function to run the game."""
    # Your code here
    while len(player1_hand)>0 and len(player2_hand)>0:
        play_round(player1_hand,player2_hand,war_list)
    if len(player1_hand) == 0:
        print("Player 2 wins")
    else:
        print("Player 1 wins")
# Call the main function to start the game
play_game()
