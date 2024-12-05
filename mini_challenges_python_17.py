#input user
woord = input('Wat is jouw woord:  ')
#define variabelen
woord_spiegel = woord[::-1]
#check = woord gespiegeld is woord
if woord_spiegel == woord:
    print(f'het woord {woord} is een palindroom')
else:
    print(f'het woord {woord} is een geen palindroom')


#print het is een palindroom
#    anders niet
#print het is geen palindroom


#prijs = float(input('Wat is de prijs: '))
#print(f'jouw naam is {naam}')
#print(f'de prijs is {prijs}')