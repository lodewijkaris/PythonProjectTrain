import unittest
#from BlackJack_Check_is_BJ import is_blackjack
#from tests.unit.TC6_BlackJack.BlackJack_Check import is_blackjack
from BlackJack_BJ import play_blackjack, is_blackjack


class TestIsBlackjack(unittest.TestCase):
    def test_blackjack(self):
        hand = [('Ace', 'Hearts'), ('10', 'Diamonds')]
        self.assertTrue(is_blackjack(hand))

        hand = [('King', 'Clubs'), ('Ace', 'Spades')]
        self.assertTrue(is_blackjack(hand))

        hand = [('Ace', 'Hearts'), ('Jack', 'Diamonds')]
        self.assertTrue(is_blackjack(hand))

        hand = [('Queen', 'Hearts'), ('Ace', 'Clubs')]
        self.assertTrue(is_blackjack(hand))

    def test_not_blackjack(self):
        hand = [('2', 'Hearts'), ('10', 'Diamonds')]
        self.assertFalse(is_blackjack(hand))

        hand = [('Ace', 'Hearts'), ('9', 'Diamonds')]
        self.assertFalse(is_blackjack(hand))

        hand = [('Jack', 'Hearts'), ('9', 'Diamonds')]
        self.assertFalse(is_blackjack(hand))

        hand = [('2', 'Hearts'), ('3', 'Diamonds')]
        self.assertFalse(is_blackjack(hand))

        hand = [('2', 'Hearts'), ('10', 'Diamonds'), ('9', 'Diamonds')]
        self.assertFalse(is_blackjack(hand))

        hand = [('Ace', 'Hearts'), ('9', 'Diamonds'),('Ace', 'Spades')]
        self.assertFalse(is_blackjack(hand))

if __name__ == '__main__':
    unittest.main()
