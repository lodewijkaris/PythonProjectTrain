import random
from array import array

hoeveel_ds = int(input('Hoeveel dobbelstenen wil je gooien?:  '))
i= hoeveel_ds

numbers = []

while i > 0:
#    def main():
#        mySum = 0
#        amountOfThrows = 0
    roll = random.randint(1,6)
    #print (random.randint(1,6))
    print (roll)
    numbers.append(roll)
#    extend(roll)
    i -= 1
#    extend(roll)
#    list.append(roll)
print(numbers)
total = sum(numbers)

print(f'De som van de gegooide dobbelstenen is {total}')
