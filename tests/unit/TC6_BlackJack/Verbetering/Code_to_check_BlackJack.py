
# Functionaliteit om blackjack te testen
def is_blackjack(hand):
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
              'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

    # Check if the hand has exactly two cards
    if len(hand) != 2:
        return False

    # Calculate the total value of the hand
    total_value = sum(values[card[0]] for card in hand)

    # Check for blackjack (an ace and a 10-value card)
    if total_value == 21 and any(card[0] == 'Ace' for card in hand):
        return True

    return False

