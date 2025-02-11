#########################################################################################
#Lodewijk Aris version 1, date 31 jan 2025                                              #
#This sourcecode is part of the code BlackJack and covers Test Case Spel initialisatie  #
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
