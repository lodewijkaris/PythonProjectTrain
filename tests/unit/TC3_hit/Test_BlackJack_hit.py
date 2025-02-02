import unittest
from BlackJack_hit import deal_card

class TestBlackJackTC3(unittest.TestCase):
    def test_deal_card(self):
        # Setup initial deck and hand
        deck = [
        ('4', 'Clubs'), ('5', 'Spades'),
        ('6', 'Hearts'), ('7', 'Diamonds'), ('8', 'Clubs'), ('9', 'Spades'),
        ('10', 'Hearts'), ('Jack', 'Diamonds'), ('Queen', 'Clubs'), ('King', 'Spades'),
        ('Ace', 'Hearts'), ('2', 'Diamonds'), ('3', 'Clubs'), ('4', 'Spades'),
        ('5', 'Hearts'), ('6', 'Diamonds'), ('7', 'Clubs'), ('8', 'Spades'),
        ('9', 'Hearts'), ('10', 'Diamonds'), ('Jack', 'Clubs'), ('Queen', 'Spades'),
        ('King', 'Hearts'), ('Ace', 'Diamonds'), ('2', 'Clubs'), ('3', 'Spades'),
        ('4', 'Hearts'), ('5', 'Diamonds'), ('6', 'Clubs'), ('7', 'Spades'),
        ('8', 'Hearts'), ('9', 'Diamonds'), ('10', 'Clubs'), ('Jack', 'Spades'),
        ('Queen', 'Hearts'), ('King', 'Diamonds'), ('Ace', 'Clubs'), ('2', 'Spades'),
        ('3', 'Hearts'), ('4', 'Diamonds'), ('5', 'Clubs'), ('6', 'Spades'),
        ('7', 'Hearts'), ('8', 'Diamonds'),
        ('Jack', 'Hearts'), ('Queen', 'Diamonds'), ('King', 'Clubs'), ('Ace', 'Spades')
        ]

        # Game starts with 2 cards player and 2 card dealer, 48 cards left in deck

        hand = [('2', 'Hearts'), ('3', 'Diamonds')]
        self.assertEqual(len(hand), 2)
        dealer_hand = [('9', 'Clubs'), ('10', 'Spades'),]
        self.assertEqual(len(dealer_hand), 2)

        # Call the function to test hit 1 card by player
        deal_card(deck, hand)

        # Assert that the hand has 3 cards (2+1)

        self.assertEqual(len(hand), 3)
        # Assert that the deck has 1 less card 48-1
        self.assertEqual(len(deck), 47)
        # Assert that the card in the hand is no longer in the deck
        self.assertNotIn(hand[0], deck)

        # Call the function two times to test hitting 2 other cards
        deal_card(deck, hand)
        deal_card(deck, hand)
        # Assert that the hand has now 2+3 card
        self.assertEqual(len(hand), 5)
        # Assert that the deck has 2 less card 47-2
        self.assertEqual(len(deck), 45)

        # Assert that the card in the hand is no longer in the deck
        self.assertNotIn((hand[0])and(hand[1])and(hand[2]), deck)
        print(f"")
        print(f"Speler heeft nu de volgende vijf kaarten:{hand}")

if __name__ == '__main__':
    unittest.main()