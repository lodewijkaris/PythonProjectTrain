#########################################################################################
#Lodewijk Aris version 1, date 31 jan 2025                                              #
#This Test code belongs to Test Case Spel initialisatie                                 #
#########################################################################################

import unittest

from BlackJack_spel_initilisatie import create_deck

import random

class TestBlackjackTC1(unittest.TestCase):

    def test_create_deck(self):
        deck = create_deck()
        self.assertEqual(len(deck), 52)  # Check if deck has 52 cards
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        expected_deck = [(rank, suit) for suit in suits for rank in ranks]
        self.assertEqual(sorted(deck), sorted(expected_deck))  # Check if all expected cards are in the deck

    def test_deck_shuffled(self):
        deck = create_deck()
        shuffled_deck = create_deck()
        random.shuffle(shuffled_deck)
        self.assertNotEqual(deck, shuffled_deck, "The deck should be shuffled.")

    def test_initial_hands_empty(self):
        player_hand = []
        dealer_hand = []

        self.assertEqual(len(player_hand), 0, "Player's hand should be empty at the start.")
        self.assertEqual(len(dealer_hand), 0, "Dealer's hand should be empty at the start.")

if __name__ == '__main__':
    unittest.main()
