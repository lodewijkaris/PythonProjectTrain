import unittest
from BlackJack_hit import deal_card

class TestBlackJackTC3(unittest.TestCase):
    def test_deal_card(self):
        # Zet een initieel dek en een hand op
        deck = [
        ('4', 'Clubs'), ('5', 'Spades'),
        ('6', 'Hearts'), ('7', 'Diamonds'), ('8', 'Clubs'), ('9', 'Spades'),
        ('10', 'Hearts'), ('Jack', 'Diamonds'), ('Queen', 'Clubs'), ('King', 'Spades'),
        ('Ace', 'Hearts'), ('2', 'Diamonds'), ('3', 'Clubs'), ('4', 'Spades'),
        ('5', 'Hearts'), ('6', 'Diamonds'), ('7', 'Clubs'), ('8', 'Spades'),
        ('9', 'Hearts'), ('10', 'Diamonds'), ('Jack', 'Clubs'), ('Queen', 'Spades'),
        ('King', 'Hearts'), ('Ace', 'Diamonds'), ('2', 'Clubs'), ('3', 'Spades'),
        ('4', 'Hearts'), ('5', 'Diamonds'), ('6', 'Clubs'), ('7', 'Spades'),
        ('8', 'Hearts'), ('9', 'Diamonds'), ('10', 'Clubs'), ('Jack', 'Spades'),
        ('Queen', 'Hearts'), ('King', 'Diamonds'), ('Ace', 'Clubs'), ('2', 'Spades'),
        ('3', 'Hearts'), ('4', 'Diamonds'), ('5', 'Clubs'), ('6', 'Spades'),
        ('7', 'Hearts'), ('8', 'Diamonds'),
        ('Jack', 'Hearts'), ('Queen', 'Diamonds'), ('King', 'Clubs'), ('Ace', 'Spades')
        ]

        # Spel start met 2 kaarten voor speler en 2 voor deler, 48 kaarten over in dek
        hand = [('2', 'Hearts'), ('3', 'Diamonds')]
        self.assertEqual(len(hand), 2)
        dealer_hand = [('9', 'Clubs'), ('10', 'Spades'),]
        self.assertEqual(len(dealer_hand), 2)

        # Roep de functie aan om de te testen dat de speler 1 kaart neemt
        deal_card(deck, hand)

        # Doe een bewering dat de hand nu 3 kaarten heeft (2+1)
        self.assertEqual(len(hand), 3)
        # Beweer dat het dek 1 kaart minder heeft 48-1
        self.assertEqual(len(deck), 47)
        # Beweer dat de kaart niet langer in het dek is
        self.assertNotIn(hand[0], deck)

        # Roep de functie aan om de te testen dat de speler nog 2 kaarten neemt
        deal_card(deck, hand)
        deal_card(deck, hand)
        # Doe een bewering dat de hand nu 2+3 kaarten heeft
        self.assertEqual(len(hand), 5)
        # Beweer dat het dek 1 kaart minder heeft 47-2
        self.assertEqual(len(deck), 45)

        # Beweer dat de kaart niet langer in het dek is
        self.assertNotIn((hand[0])and(hand[1])and(hand[2]), deck)
        print(f"")
        print(f"Speler heeft nu de volgende vijf kaarten:{hand}")
        print(f"Deler heeft nu de volgende twee kaarten:{dealer_hand}")
        print(f"Aantal kaarten in dek over:{(len(deck))}")
if __name__ == '__main__':
    unittest.main()