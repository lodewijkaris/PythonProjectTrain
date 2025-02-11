import unittest

from BlackJack_deck import create_deck

class TestCreateDeck(unittest.TestCase):

    def test_create_deck(self):
        deck = create_deck()
        self.assertEqual(len(deck), 52)  # Check if deck has 52 cards
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        expected_deck = [(rank, suit) for suit in suits for rank in ranks]
        self.assertEqual(sorted(deck), sorted(expected_deck))  # Check if all expected cards are in the deck

if __name__ == '__main__':
    unittest.main()
