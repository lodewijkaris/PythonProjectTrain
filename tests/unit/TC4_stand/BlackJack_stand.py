#########################################################################################
#Lodewijk Aris version 2, date 14 feb 2025, print verwijderd, verplaatst naar test code #
#              version 1, date 2 feb 2025                                               #
#This sourcecode is part of the code BlackJack and covers Test Case Stand               #
#########################################################################################

import random
print("Tester geeft meteen s voor stand op (,please insert 1 stand to let the test run smoothly")
# Functie om dek kaarten te creeeren
def create_deck():
    deck = []
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    for suit in suits:
        for rank in ranks:
            deck.append((rank, suit))
    return deck

# Functie om kaart te delen
def deal_card(deck, hand):
    card = random.choice(deck)
    deck.remove(card)
    hand.append(card)

# Hoofdfunctie om blackjack te spelen
def play_blackjack():
    deck = create_deck()
    random.shuffle(deck)

    player_hand = []
    dealer_hand = []

    for _ in range(2):
        deal_card(deck, player_hand)
        deal_card(deck, dealer_hand)

    # Spelers beurt
    while True:
        choice = input("Do you want to hit or stand? (h/s): ").lower()
        if choice == 'h':
            deal_card(deck, player_hand)
        elif choice == 's':
            break
        else:
            print("Invalid choice. Please enter 'h' to hit or 's' to stand.")
    print("")
#    print(player_hand)
#    print(dealer_hand)

    return player_hand, dealer_hand, deck


# Run the game
play_blackjack()