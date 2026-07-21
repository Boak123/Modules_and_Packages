from utils import calculator
from utils import validator


def main():
    x = validator.get_number("Enter the first number: ")
    y = validator.get_number("Enter the second number: ")
       
    print(f"Addition: {calculator.add(x, y)}")
    print(f"SUbtraction: {calculator.subtract(x, y)}")
    print(f"Multiplication: {calculator.multiply(x, y)}")
    try:
        print(calculator.divide(x, y))
    except ZeroDivisionError as error:
        print(error)
    else:
        print('calculation successful')

if __name__ == "__main__":
    main()