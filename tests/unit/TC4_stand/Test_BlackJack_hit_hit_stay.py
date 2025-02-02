# important note: to run the test, the user should use -s in the run configuration
# In this test the user has to give inputs to test with 2 hits (2 h) and 1 stay (s)

import unittest
from unittest.mock import patch
from BlackJack_stay import play_blackjack

class TestBlackJackTC4(unittest.TestCase):
    @patch('builtins.input', side_effect=['h', 'h', 's'])
    def test_hit_hit_stay(self, mock_input):
        # Call the function to test
        player_hand, dealer_hand, deck = play_blackjack()

        # Assert that the player's hand has exactly 4 cards after choosing to stay
        self.assertEqual(len(player_hand), 4)

        # Assert that the dealer's hand also has exactly 2 cards
        self.assertEqual(len(dealer_hand), 2)


if __name__ == '__main__':
    unittest.main()
