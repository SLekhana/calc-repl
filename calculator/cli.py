# calculator/cli.py

import sys
from calculator import operations

def main():
    print("Welcome to the Interactive Calculator!")
    print("Available operations: add, subtract, multiply, divide, exit")

    while True:
        op = input("Enter operation: ").strip().lower()

        if op == "exit":
            print("Goodbye!")
            sys.exit(0)

        if op not in ["add", "subtract", "multiply", "divide"]:
            print("Invalid operation. Try again.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid number entered.")
            continue

        if op == "add":
            result = operations.add(num1, num2)
        elif op == "subtract":
            result = operations.subtract(num1, num2)
        elif op == "multiply":
            result = operations.multiply(num1, num2)
        elif op == "divide":
            try:
                result = operations.divide(num1, num2)
            except ZeroDivisionError:
                print("Cannot divide by zero")
                continue

        print(f"Result: {result}")

if __name__ == "__main__":
    main()
