#Test Case geteld, de opgetelde waarde is correct voor speler en deler

import unittest
import time
from BlackJack_count_hands import calculate_hand_value
class TestBlackJackTC5(unittest.TestCase):
    def test_hand_value_no_aces_no_tens(self):
        hand = [('2', 'Hearts'), ('3', 'Diamonds'), ('4', 'Clubs')]
        self.assertEqual(calculate_hand_value(hand), 9)
        print(f"Speler heeft nu :{calculate_hand_value(hand)} punten")
        time.sleep(0.5)
    def test_hand_value_with_face_cards(self):
        hand = [('Jack', 'Hearts'), ('3', 'Diamonds'), ('King', 'Clubs')]
        self.assertEqual(calculate_hand_value(hand), 23)
        print(f"Speler heeft nu :{calculate_hand_value(hand)} punten")
        time.sleep(0.5)
    def test_hand_value_with_aces(self):
        hand = [('Ace', 'Hearts'), ('3', 'Diamonds'), ('Ace', 'Clubs')]
        self.assertEqual(calculate_hand_value(hand), 15)
        print(f"Speler heeft nu :{calculate_hand_value(hand)} punten")
        time.sleep(0.5)
    def test_hand_value_with_ace_adjustment(self):
        hand = [('Ace', 'Hearts'), ('Ace', 'Clubs'), ('10', 'Diamonds')]
        self.assertEqual(calculate_hand_value(hand), 12)
        print(f"Speler heeft nu :{calculate_hand_value(hand)} punten")
        time.sleep(0.5)
    def test_hand_value_busting_with_aces(self):
        hand = [('Ace', 'Hearts'), ('Ace', 'Diamonds'), ('9', 'Clubs'), ('Ace', 'Spades'), ('10', 'Spades')]
        self.assertEqual(calculate_hand_value(hand), 22)
        print(f"Speler heeft nu :{calculate_hand_value(hand)} punten")
if __name__ == '__main__':
    unittest.main()
