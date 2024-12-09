# Lootbox (also called a loot crate or prize crate) is a consumable virtual item
# which can be redeemed to receive a randomised selection of further virtual items,
# or loot, ranging from simple customisation options for a player's avatar or character
# to game-changing equipment such as weapons and armour.

import random

random_number = random.randint(1, 1000)
print(f' Je hebt {random_number} coins en je gaat 1 item van 100 coins kopen')
#print(f' Je hebt {random_number} coins en je gaat 1 item van 100 coins kopen')

class LootBox:
    def __init__(self):
        self.coins = random_number
        self.price = 100
        self.items = {
            "common": ["Common Item 1 hout", "Common Item 2 graan"],
            "rare": ["Rare Item 1 erts", "Rare Item 2 brons"],
            "epic": ["Epic Item 1 zilver", "Epic Item 2 goud"],
            "legendary": ["Legendary Item 1 platina", "Legendary Item 2 diamant"]
        }
        self.probabilities = {
            "common": 0.6,
            "rare": 0.25,
            "epic": 0.1,
            "legendary": 0.05
        }

    def open_box(self):
        if self.coins < self.price:
            print("Not enough coins!")
            return None

        self.coins -= self.price
        roll = random.random()
        cumulative_probability = 0.0
        for rarity, probability in self.probabilities.items():
            cumulative_probability += probability
            if roll < cumulative_probability:
                item = random.choice(self.items[rarity])
                print(f"Congratulations! You got a {rarity} item: {item}")
                return item

        print("Error: No item found")
        return None

    def check_coins(self):
        print(f"You have {random_number-self.price} coins left.")

# Example usage
lootbox = LootBox()
lootbox.open_box()
lootbox.check_coins()