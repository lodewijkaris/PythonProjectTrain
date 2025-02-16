#########################################################################################
#Lodewijk Aris version 1, date 1 feb 2025                                               #
#This sourcecode is part of the code BlackJack and covers Test Case Hit                 #
#########################################################################################

import random

# The function to be tested
def deal_card(deck, hand):
    card = random.choice(deck)
    deck.remove(card)
    hand.append(card)

