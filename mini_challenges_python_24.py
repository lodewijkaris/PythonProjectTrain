#define aantal dobbelstenen A en vlakken X
hoeveel_ds = int(input('Hoeveel dobbelstenen wil je gooien?:  '))
A= hoeveel_ds
hoeveel_vlakken = int(input('Hoeveel vlakken heeft de dobbelsteen?:   '))
X = hoeveel_vlakken

#Gooi willekeurig het aantal dobbelstenen A met X vlakken
import random

def roll_dice(notation):
    try:
        num_dice, dice_type = notation.lower().split('d')
        num_dice = int(num_dice)
        dice_type = int(dice_type)
        rolls = [random.randint(1, dice_type) for _ in range(num_dice)]
        return rolls
    except ValueError:
        return "Invalid notation. Use the format 'AdX' where A is the number of dice and X is the number of sides."

# Example usage
#notation = '3d6'
notation = f'{A}'+'d'+f'{X}'
result = roll_dice(notation)
print(f"Rolling {notation}: {result}")
total_sum = sum(result)
print(f"Total score: {total_sum}" )