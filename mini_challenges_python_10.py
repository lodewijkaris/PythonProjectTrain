import random
hoeveel_ds = int(input('Hoeveel dobbelstenen wil je gooien?:  '))
i= hoeveel_ds
while i > 0:
    roll = random.randint(1,6)
    #print (random.randint(1,6))
    print (roll)
    i -= 1
#prijs = float(input('Wat is de prijs: '))
#print(f'jouw naam is {naam}')
#print(f'de prijs is {prijs}')