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


# Function to split a hand
def split(hand):
    if len(hand) == 2 and hand[0][0] == hand[1][0]:
        hand1 = [hand[0]]
        hand2 = [hand[1]]
        return hand1, hand2
    else:
        raise ValueError("Cannot split hand")


# Main function to play blackjack
def play_blackjack():
    deck = create_deck()
    random.shuffle(deck)

    player_hand = []
    dealer_hand = []

    for _ in range(2):
        deal_card(deck, player_hand)
        deal_card(deck, dealer_hand)

    # Player's turn
    while True:
        display_hand(player_hand, "Player")
        if calculate_hand_value(player_hand) > 21:
            print("Player busts! Dealer wins.")
            return
        choice = input("Do you want to hit, stand, or split? (h/s/sp): ").lower()
        if choice == 'h':
            deal_card(deck, player_hand)
        elif choice == 's':
            break
        elif choice == 'sp':
            try:
                player_hand1, player_hand2 = split(player_hand)
                print("Hand split!")
                display_hand(player_hand1, "Player Hand 1")
                display_hand(player_hand2, "Player Hand 2")
            except ValueError as e:
                print(e)
        else:
            print("Invalid choice. Please enter 'h' to hit, 's' to stand, or 'sp' to split.")

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
