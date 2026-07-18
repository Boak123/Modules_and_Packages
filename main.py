from calculator import divide, add, subtract, multiply

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

try:
    result = divide(num1, num2)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
else:
    print(f"Result: {result}")