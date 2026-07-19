import calculator

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

try:
    for operation in [calculator.add, calculator.subtract, calculator.multiply, calculator.divide]:
        result = operation(num1, num2)
        print(f"Result of {operation.__name__}: {result}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter valid numbers.")