import random
# Input from user
# an array from the user
# Hoeveel spelers
hoeveel_spelers = int(input('Hoeveel spelers doen er mee:  '))
# Defineer reeks gebasseerd op hoeveel spelers
ingevoerde_reeks = list(map(str, input(f"Voeg de {hoeveel_spelers} naam van iedere speler in, gescheiden door een spatie en druk op enter: ").split()))
print("de Spelers zijn :", ingevoerde_reeks)
# Sort the array
gesorteerde_reeks = sorted(ingevoerde_reeks)
print("de Spelers gesorteerd zijn :", gesorteerde_reeks)

# sorteer de reeks randomly
#random_reeks = random.shuffle(ingevoerde_reeks)
#random_reeks = random.shuffle(ingevoerde_reeks)

#shuffled_array = random.sample( gesorteerde_reeks, len(gesorteerde_reeks))

choice_array = random.choice( gesorteerde_reeks)

# Print the sorted array
#print("de Spelers in volgorde zijn randomly gegenereerd :", shuffled_array)
print("de Speler, die als eerste mag beginnen is:", choice_array)
#nieuw = random.shuffle(ingevoerde_reeks)
