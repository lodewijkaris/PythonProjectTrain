#Test Case Kapot; is waar als waarde hand groter is dan 21 voor speler en deler

import unittest

from BlackJack_kapot import calculate_hand_value

class TestBlackjackBusts(unittest.TestCase):
    def test_player_busts_with_3_cards(self):
        hand = [('10', 'Hearts'), ('10', 'Diamonds'), ('2', 'Clubs')]
        self.assertGreater(calculate_hand_value(hand), 21)
        print(f"Waarde Hand:{calculate_hand_value(hand)} punten")
    def test_player_busts_with_4_cards(self):
        hand = [('5', 'Hearts'), ('6', 'Diamonds'), ('7', 'Clubs'), ('4', 'Spades')]
        self.assertGreater(calculate_hand_value(hand), 21)
        print(f"Waarde Hand:{calculate_hand_value(hand)} punten")
    def test_dealer_busts_with_3_cards(self):
        hand = [('9', 'Hearts'), ('9', 'Diamonds'), ('4', 'Clubs')]
        self.assertGreater(calculate_hand_value(hand), 21)
        print(f"Waarde Hand:{calculate_hand_value(hand)} punten")
    def test_dealer_busts_with_5_cards(self):
        hand = [('3', 'Hearts'), ('4', 'Diamonds'), ('5', 'Clubs'), ('6', 'Spades'), ('5', 'Diamonds')]
        self.assertGreater(calculate_hand_value(hand), 21)
        print(f"Waarde Hand:{calculate_hand_value(hand)} punten")
    def test_dealer_busts_with_4_cards_and_face_card(self):
        hand = [('3', 'Hearts'), ('4', 'Diamonds'), ('5', 'Clubs'), ('6', 'Spades'), ('Queen', 'Diamonds')]
        self.assertGreater(calculate_hand_value(hand), 21)
        print(f"Waarde Hand:{calculate_hand_value(hand)} punten")
if __name__ == '__main__':
    unittest.main()
