#########################################################################################
#Lodewijk Aris version 2, date 11 feb 2025                                              #
#      Initial version 1, date 4 feb 2025                                               #
#This sourcecode is part of the code BlackJack and covers Test Case Dealer Turn         #
#########################################################################################

import random

# Function to create a deck of cards
def create_deck():
    deck = []
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    for suit in suits:
        for rank in ranks:
            deck.append((rank, suit))
    return deck


# Function to calculate the value of a hand
def calculate_hand_value(hand):
    value = 0
    ace_count = 0
    for card in hand:
        rank, suit = card
        if rank in ['Jack', 'Queen', 'King']:
            value += 10
        elif rank == 'Ace':
            ace_count += 1
            value += 11
        else:
            value += int(rank)

    # Adjust for aces
    while value > 21 and ace_count:
        value -= 10
        ace_count -= 1

    return value


# Function to deal a card
def deal_card(deck, hand):
    card = random.choice(deck)
    deck.remove(card)
    hand.append(card)
