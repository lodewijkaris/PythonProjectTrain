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

# Function to deal a card
def deal_card(deck, hand):
    card = random.choice(deck)
    deck.remove(card)
    hand.append(card)

def play_blackjack():
    deck = create_deck()
    random.shuffle(deck)

    player_hand = []
    dealer_hand = []
#    number_of_items_player = []
#    number_of_items_dealer = []
    for _ in range(2):
        deal_card(deck, player_hand)
        deal_card(deck, dealer_hand)
        continue
    # Return the hands for testing
    return player_hand, dealer_hand
# Run the game
play_blackjack()