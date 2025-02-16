1  import random
2
3
4  # Function to create a deck of cards
5  def create_deck():
6      deck = []
7      suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
8      ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
9      for suit in suits:
10         for rank in ranks:
11             deck.append((rank, suit))
12     return deck
13
14
15 # Function to calculate the value of a hand
16 def calculate_hand_value(hand):
17     value = 0
18     ace_count = 0
19     for card in hand:
20         rank, suit = card
21         if rank in ['Jack', 'Queen', 'King']:
22             value += 10
23         elif rank == 'Ace':
24             ace_count += 1
25             value += 11
26         else:
27             value += int(rank)
28
29     # Adjust for aces
30     while value > 21 and ace_count:
31         value -= 10
32         ace_count -= 1
33
34     return value
35
36
37 # Function to display the hand
38 def display_hand(hand, name):
39     print(f"{name}'s hand:")
40     for card in hand:
41         rank, suit = card
42         print(f"{rank} of {suit}")
43     print(f"Value: {calculate_hand_value(hand)}")
44     print()
45
46
47 # Function to deal a card
48 def deal_card(deck, hand):
49     card = random.choice(deck)
50     deck.remove(card)
51     hand.append(card)
52
53
54 # Main function to play blackjack
55 def play_blackjack():
56     deck = create_deck()
57     random.shuffle(deck)
58
59     player_hand = []
60     dealer_hand = []
61
62     for _ in range(2):
63         deal_card(deck, player_hand)
64         deal_card(deck, dealer_hand)
65
66     # Player's turn
67     while True:
68         display_hand(player_hand, "Player")
69         if calculate_hand_value(player_hand) > 21:
70             print("Player busts! Dealer wins.")
71             return
72         choice = input("Do you want to hit or stand? (h/s): ").lower()
73         if choice == 'h':
74             deal_card(deck, player_hand)
75         elif choice == 's':
76             break
77         else:
78             print("Invalid choice. Please enter 'h' to hit or 's' to stand.")
79
80     # Dealer's turn
81     while calculate_hand_value(dealer_hand) < 17:
82         deal_card(deck, dealer_hand)
83
84     display_hand(dealer_hand, "Dealer")
85
86     player_value = calculate_hand_value(player_hand)
87     dealer_value = calculate_hand_value(dealer_hand)
88
89     if dealer_value > 21:
90         print("Dealer busts! Player wins.")
91     elif dealer_value > player_value:
92         print("Dealer wins.")
93     elif dealer_value < player_value:
94         print("Player wins.")
95     else:
96         print("It's a tie!")
97
98
99 # Run the game
100play_blackjack()