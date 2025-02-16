########################################################################################
#Lodewijk Aris version 2, date  14 feb 2025: print kaarten deler en speler toegevoegd  #
#              version 1, date  5 feb 2025                                             #
#This Test code belongs to Test Case Stand                                             #
#                                                                                      #
# belangrijke opmerking: Om de test uit te voeren moet de gebruiker de -s gebruiken    #
# in de run configuration                                                              #
# In deze test moet de tester 1 keer s (stand) ingeven                                 #
# Door de patch functie gaan er toch 2 hits en 1 stand worden ingevoerd;               #
# dat resulteert in 4 kaarten speler en 2 kaarten deler                                #
#########################################################################################

import unittest
from unittest.mock import patch
from BlackJack_stand import play_blackjack

class TestBlackJackTC4(unittest.TestCase):
    @patch('builtins.input', side_effect=['h', 'h', 's'])
    def test_hit_hit_stand(self, mock_input):
        # Roep de functie op om te testen
        player_hand, dealer_hand, deck = play_blackjack()

        # Beweer dat de spelers hand precies 4 kaarten is na input
        self.assertEqual(len(player_hand), 4)
        print(f"lengte van spelers hand is: {len(player_hand)}")
        print(player_hand)

        # Beweer dat de deler nog precies 2 kaarten heeft na het spel van de speler
        self.assertEqual(len(dealer_hand), 2)
        print(f"lengte van delers hand is: {len(dealer_hand)}")
        print(dealer_hand)
if __name__ == '__main__':
    unittest.main()
