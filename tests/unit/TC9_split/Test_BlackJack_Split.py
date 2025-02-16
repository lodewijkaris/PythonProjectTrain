import unittest
from BlackJack import create_deck, calculate_hand_value, deal_card

class TestBlackjack(unittest.TestCase):

    def setUp(self):
        self.deck = create_deck()
        self.dealer_hand = []

    def test_dealer_stands_17(self):
        # Dealer's hand starts with a value of 17 and stops
        self.dealer_hand = [('10', 'Hearts'), ('7', 'Spades')]
        print(f"")
        print(f"start waarde: {calculate_hand_value(self.dealer_hand)}")
        while calculate_hand_value(self.dealer_hand) < 17:
            deal_card(self.deck, self.dealer_hand)
        value = calculate_hand_value(self.dealer_hand)
        self.assertGreaterEqual(value, 17, "Dealer should stand with hand value of at least 17.")
        print(f"eind waarde: {calculate_hand_value(self.dealer_hand)}")

        # reset setup, deck and dealer hand
    def setUp(self):
        self.deck = create_deck()
        self.dealer_hand = []

    def test_dealer_stands_19(self):
        # Dealer's hand starts with a value of 17 and stops
        self.dealer_hand = [('10', 'Hearts'), ('9', 'Clubs')]
        print(f"")
        print(f"start waarde: {calculate_hand_value(self.dealer_hand)}")
        while calculate_hand_value(self.dealer_hand) < 17:
            deal_card(self.deck, self.dealer_hand)
        value = calculate_hand_value(self.dealer_hand)
        self.assertGreaterEqual(value, 17, "Dealer should stand with hand value of at least 17.")
        print(f"eind waarde: {calculate_hand_value(self.dealer_hand)}")

        # reset setup, deck and dealer hand
    def setUp(self):
        self.deck = create_deck()
        self.dealer_hand = []

    def test_dealer_hits(self):
        # Dealer's hand starts with a value less than 17
        self.dealer_hand = [('5', 'Hearts'), ('9', 'Spades')]
        print(f"")
        print(f"start waarde:{calculate_hand_value(self.dealer_hand)}")
        while calculate_hand_value(self.dealer_hand) < 17:
            deal_card(self.deck, self.dealer_hand)
        value = calculate_hand_value(self.dealer_hand)
        self.assertGreaterEqual(value, 17, "Dealer should hit until hand value is at least 17.")
        print(f"eind waarde:{calculate_hand_value(self.dealer_hand)}")

        # reset setup, deck and dealer hand
    def setUp(self):
        self.deck = create_deck()
        self.dealer_hand = []

    def test_dealer_busts_23(self):
        # Dealer's hand will bust after hitting
        self.dealer_hand = [('10', 'Hearts'), ('6', 'Spades')]
        print(f"")
        print(f"start waarde:{calculate_hand_value(self.dealer_hand)}")
#       Deal one more specific card to trigger bust
        while calculate_hand_value(self.dealer_hand) <= 21:
            self.dealer_hand.insert(0, ('7', 'Hearts'))
#            deal_card(self.deck, self.dealer_hand)
        value = calculate_hand_value(self.dealer_hand)
        self.assertGreater(value, 21, "Dealer should bust with hand value greater than 21.")
        print(f"eind waarde:{calculate_hand_value(self.dealer_hand)}")

        def setUp(self):
            self.deck = create_deck()
            self.dealer_hand = []

    def test_dealer_busts_26(self):
        # Dealer's hand will bust after hitting
        self.dealer_hand = [('10', 'Hearts'), ('5', 'Spades')]
        print(f"")
        print(f"start waarde:{calculate_hand_value(self.dealer_hand)}")
        #       Deal one more specific card to trigger bust
        while calculate_hand_value(self.dealer_hand) <= 21:
            self.dealer_hand.insert(0, ('10', 'Diamonds'))
        value = calculate_hand_value(self.dealer_hand)
        self.assertGreater(value, 21, "Dealer should bust with hand value greater than 21.")
        print(f"eind waarde:{calculate_hand_value(self.dealer_hand)}")

        # reset setup, deck and dealer hand
    def setUp(self):
        self.deck = create_deck()
        self.dealer_hand = []

    def test_dealer_ace_adjustment_1(self):
        # Dealer's hand includes an Ace
        self.dealer_hand = [('Ace', 'Hearts'), ('6', 'Spades')]
        print(f"")
        print(f"start waarde:{calculate_hand_value(self.dealer_hand)}")
#        deal_card(self.deck, self.dealer_hand)
        while calculate_hand_value(self.dealer_hand) < 17:
#            deal_card(self.deck, self.dealer_hand)
            self.dealer_hand.insert(0, ('10', 'Hearts'))
        value = calculate_hand_value(self.dealer_hand)
        self.assertTrue(17 <= value <= 21, "Dealer hand value should be adjusted correctly with an Ace.")
        print(f"eind waarde:{calculate_hand_value(self.dealer_hand)}")

        # reset setup, deck and dealer hand
    def setUp(self):
        self.deck = create_deck()
        self.dealer_hand = []

    def test_dealer_ace_adjustment_2(self):
        # Dealer's hand includes an Ace
        self.dealer_hand = [('Ace', 'Hearts'), ('5', 'Spades')]
        print(f"")
        print(f"start waarde:{calculate_hand_value(self.dealer_hand)}")
#        deal_card(self.deck, self.dealer_hand)
        while calculate_hand_value(self.dealer_hand) < 17:
#            deal_card(self.deck, self.dealer_hand)
            self.dealer_hand.insert(0, ('Ace', 'Clubs'))
        value = calculate_hand_value(self.dealer_hand)
        self.assertTrue(17 <= value <= 21, "Dealer hand value should be adjusted correctly with two Aces.")
        print(f"eind waarde:{calculate_hand_value(self.dealer_hand)}")

if __name__ == '__main__':
    unittest.main()
