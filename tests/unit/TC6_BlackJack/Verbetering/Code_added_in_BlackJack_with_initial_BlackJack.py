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


# Function to display the hand
def display_hand(hand, name):
    print(f"{name}'s hand:")
    for card in hand:
        rank, suit = card
        print(f"{rank} of {suit}")
    print(f"Value: {calculate_hand_value(hand)}")
    print()


# Function to deal a card
def deal_card(deck, hand):
    card = random.choice(deck)
    deck.remove(card)
    hand.append(card)


# Functionaliteit om blackjack te herkennen
def is_blackjack(hand):
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
              'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

    # Check dat het aantal in de hand precies 2 kaarten is
    if len(hand) != 2:
        return False

    # Reken de total waarde uit van de hand

    total_value = sum(values[card[0]] for card in hand)

    # Check voor blackjack (een aas en een 10-punten kaart
    if total_value == 21 and any(card[0] == 'Ace' for card in hand):
        return True

    return False


# Main function to play blackjack
def play_blackjack():
    deck = create_deck()
    random.shuffle(deck)

    player_hand = []
    dealer_hand = []

    for _ in range(2):
        deal_card(deck, player_hand)
        deal_card(deck, dealer_hand)

    # Check voor initieel blackjack
    if is_blackjack(player_hand):
        display_hand(player_hand, "Player")
        display_hand(dealer_hand, "Dealer")
        print("Player has Blackjack! Player wins.")
        return
    elif is_blackjack(dealer_hand):
        display_hand(player_hand, "Player")
        display_hand(dealer_hand, "Dealer")
        print("Dealer has Blackjack! Dealer wins.")
        return

    # Player's turn
    while True:
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

    if dealer_value > 21:
        print("Dealer busts! Player wins.")
    elif dealer_value > player_value:
        print("Dealer wins.")
    elif dealer_value < player_value:
        print("Player wins.")
    else:
        print("It's a tie!")

# Run the game
play_blackjack()
