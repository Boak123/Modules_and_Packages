import calculator

while True:
    try:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        result = calculator.divide(a, b)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Invalid input. Please enter valid numbers.")
    else:
        print(f"Result: {result}")
        break