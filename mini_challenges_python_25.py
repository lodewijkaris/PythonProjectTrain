#installed numpy
import numpy as np

## van internet https://www.tutorialspoint.com/data_structures_algorithms/quick_sort_algorithm.htm
def partition(arr, low, high):
   i = low - 1
   pivot = arr[high]  # pivot element
   for j in range(low, high):
      if arr[j] <= pivot:
         # increment
         i = i + 1
         arr[i], arr[j] = arr[j], arr[i]
   arr[i + 1], arr[high] = arr[high], arr[i + 1]
   return i + 1

def quickSort(arr, low, high):
   if low < high:
      pi = partition(arr, low, high)
      quickSort(arr, low, pi - 1)
      quickSort(arr, pi + 1, high)

#Vraag gebruiker om aantal nummers tussen 0 en 100 voor de willekeurige reeks
hoeveel_nummers = int(input('Hoeveel willekeurige nummers tussen 0 en 100 wil je opgeven?:  '))
# Define the size of the array
size = hoeveel_nummers  # You can change this to any number you want

# Generate a 1-D array containing random integers from 0 to 100
random_array = np.random.randint(0, 100, size=(size))
print("Random gegenereerde reeks:", random_array)

n = len(random_array)
print("Inhoud van de gegeneerde random reeks van getallen tussen 0 en 100: ")
for i in range(n):
   print(random_array[i], end=" ")
quickSort(random_array, 0, n - 1)
print("\nInhoud van de reeks gesorteerd van laag naar hoog : ")
for i in range(n):
   print(random_array[i], end=" ")

#old code...
# Create a 1D array with random values
#random_array = np.random.rand(size)
#print(random_array)
#arr = [2, 5, 3, 8, 6, 5, 4, 7]