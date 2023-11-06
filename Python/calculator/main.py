import graphics


# Function for addition
def add(a, b):
    return a + b


# Function for subtraction
def subtract(a, b):
    return a - b


# Function for multiplication
def multiply(a, b):
    return a * b


# Function for division
def divide(a, b):
    return a / b


# Main calculator loop
while True:
    print("Hello, and welcome to the calculator!")
    print(graphics.logo)
    print("Choose the operator (+, -, *, /) or 'q' to quit:")
    operator = input("Operator: ")

    if operator == 'q':
        break

    if operator not in ('+', '-', '*', '/'):
        print("Invalid operator. Please enter a valid operator.")
        continue

    first_operand = input("Enter the first operand: ")
    second_operand = input("Enter the second operand: ")

    first_operand = float(first_operand)
    second_operand = float(second_operand)

    result = 0

    if operator == '+':
        result = add(first_operand, second_operand)
    elif operator == '-':
        result = subtract(first_operand, second_operand)
    elif operator == '*':
        result = multiply(first_operand, second_operand)
    elif operator == '/':
        if second_operand == 0:
            print("Error: Division by zero")
            continue
        else:
            result = divide(first_operand, second_operand)

    print(f"The result of {first_operand} {operator} {second_operand} is: {result}\n")
    print(input("Press enter to continue"))

print("Calculator closed. Thank you for using it!")
