def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

# Example usage
print(f'de eerste 15 getallen van de Fibonacci reeks:  {fibonacci(15)}') # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]


#print(f'De som van de gegooide dobbelstenen is {total}')