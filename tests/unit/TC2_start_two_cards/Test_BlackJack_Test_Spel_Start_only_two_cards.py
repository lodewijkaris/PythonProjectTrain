import unittest

from  BlackJack_Spel_Start import play_blackjack

class TestBlackJackTC2(unittest.TestCase):

    def test_two_cards_dealt(self):
        # Call the function to test
        player_hand, dealer_hand = play_blackjack()

        # Assert that player and dealer both have 2 cards
        self.assertEqual(len(player_hand), 2)
        self.assertEqual(len(dealer_hand), 2)

        # Print the cards that player and dealer have 2 cards
        print("")
        print(f"Aantal kaarten speler:{len(player_hand)}, Aantal kaarten deler:{len(dealer_hand)}")
        print(player_hand)
        print(dealer_hand)

if __name__ == '__main__':
    unittest.main()
