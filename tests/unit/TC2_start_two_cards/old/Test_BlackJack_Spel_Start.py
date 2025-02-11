import unittest

from BlackJack_Spel_Start import play_blackjack

class TestBlackjack(unittest.TestCase):
    def test_play_blackjack(self):
        # Mock player and dealer hands
        player_hand = []
        dealer_hand = []

        # Call the function to test
        play_blackjack()

        #Store and print the number of cards dealt to each hand
#        items1 = player_hand
#        items2 = dealer_hand
#        number_of_items_player = len(player_hand)
#        number_of_items_dealer = len(dealer_hand)
#        print(number_of_items_player)
#        print(number_of_items_dealer)

        # Assert that player and dealer both have 2 cards
        self.assertEqual(len(player_hand), 2)
        self.assertEqual(len(dealer_hand), 2)

#        self.assertEqual(number_of_items_player, 2)
#        self.assertEqual(number_of_items_dealer, 2)

#        assertEqual(len(player_hand), 2)
#        assertEqual(len(dealer_hand), 2)



if __name__ == '__main__':
    unittest.main()

