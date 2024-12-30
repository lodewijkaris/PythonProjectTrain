# Python program for simple calculator

# Function to add two numbers
def add(num1, num2):
    return num1 + num2

# Function to subtract two numbers
def subtract(num1, num2):
    return num1 - num2

# Function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2

# Function to divide two numbers
def divide(num1, num2):
    return num1 / num2

print("The defined operation \n" \
        "1. + (Add)\n" \
        "2. - (Subtract)\n" \
        "3. * (Multiply)\n" \
        "4. / (Divide)\n" \
        "5. = (Result)\n")

# Take input from the user

number_1 = float(input("Enter first number (and hit enter): "))
select_operation = int(input("Select operations form 1, 2, 3, 4 (and hit enter):"))
number_2 = float(input("Enter second number (and hit enter): "))
select_result = int(input("Enter number 5 (and hit enter) to get the Result:"))

if select_operation == 1 and select_result ==5:
    print(number_1, "+", number_2, "=",
                    add(number_1, number_2))

elif select_operation == 2 and select_result ==5:
    print(number_1, "-", number_2, "=",
                    subtract(number_1, number_2))

elif select_operation == 3 and select_result ==5:
    print(number_1, "*", number_2, "=",
                    multiply(number_1, number_2))

elif select_operation == 4 and select_result ==5:
    print(number_1, "/", number_2, "=",
                    divide(number_1, number_2))
else:
    print("Invalid input")