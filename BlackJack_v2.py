#########################################################################################
#Lodewijk Aris  version 2, date 16 februari  2025                                       #
#               version 1, date 30 januari  2025                                        #
#De verbeterde BlackJack code na testen en leren                                        #
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

# Functionaliteit om kaart(en) te laten zien van de hand
def display_hand(hand, name, hide_second_card=False):
    print(f"{name}'s hand:")
    for i, card in enumerate(hand):
        rank, suit = card
        if hide_second_card and i == 1:
            print("Hidden")
        else:
            print(f"{rank} of {suit}")
    if not hide_second_card:
        print(f"Value: {calculate_hand_value(hand)}")
    print()

# Function to deal a card
def deal_card(deck, hand):
    card = random.choice(deck)
    deck.remove(card)
    hand.append(card)

# Functie om de speluitkomst te bepalen
def determine_outcome(dealer_value, player_value):
    if dealer_value > 21:
        return "Dealer busts! Player wins."
    elif dealer_value > player_value:
        return "Dealer wins."
    elif dealer_value < player_value:
        return "Player wins."
    else:
        return "It's a tie!"

# Main function to play blackjack
def play_blackjack():
    deck = create_deck()
    random.shuffle(deck)

    player_hand = []
    dealer_hand = []

    for _ in range(2):
        deal_card(deck, player_hand)
        deal_card(deck, dealer_hand)

    # Player's turn met verborgen kaart deler
    while True:
        display_hand(dealer_hand, "Dealer", hide_second_card=True)
        display_hand(player_hand, "Player")
        if calculate_hand_value(player_hand) > 21:
            print("Player busts! Dealer wins.")
            return
        choice = input("Do you want to hit or stand? (h/s): ").lower()
        if choice == 'h':
            deal_card(deck, player_hand)
        elif choice == 's':
            break
        else:
            print("Invalid choice. Please enter 'h' to hit or 's' to stand.")

    # Dealer's turn
    while calculate_hand_value(dealer_hand) < 17:
        deal_card(deck, dealer_hand)

    display_hand(dealer_hand, "Dealer")

    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)

    outcome = determine_outcome(dealer_value, player_value)
    print(outcome)

# Run the game
play_blackjack()