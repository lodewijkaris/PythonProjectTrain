import numpy as np

## from https://www.w3schools.com/dsa/dsa_algo_bubblesort.php

#Vraag gebruiker om aantal nummers tussen 0 en 100 voor de willekeurige reeks
hoeveel_nummers = int(input('Hoeveel willekeurige nummers tussen 0 en 100 wil je opgeven?:  '))
# Define the size of the array
size = hoeveel_nummers  # You can change this to any number you want

# Generate a 1-D array containing random integers from 0 to 100
random_array = np.random.randint(0, 100, size=(size))
print("Random gegenereerde reeks:", random_array)

#my_array = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(random_array)
for i in range(n-1):
    for j in range(n-i-1):
        if random_array[j] > random_array[j+1]:
            random_array[j], random_array[j+1] = random_array[j+1], random_array[j]

print("Gesorteerde reeks methode 1:", random_array)

#my_array = [7, 3, 9, 12, 11]

n = len(random_array)
for i in range(n-1):
    swapped = False
    for j in range(n-i-1):
        if random_array[j] > random_array[j+1]:
            random_array[j], random_array[j+1] = random_array[j+1], random_array[j]
            swapped = True
    if not swapped:
        break

print("Gesorteerde reeks methode 2:", random_array)