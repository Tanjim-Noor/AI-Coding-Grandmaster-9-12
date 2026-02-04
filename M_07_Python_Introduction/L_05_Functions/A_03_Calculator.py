"""
Activity 3
Title: Calculator
Short description:
Write a Python program to create a calculator. Create individual functions for different operators - addition, subtraction, division, multiplication and return the output value.
"""

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

if __name__ == "__main__":
    num1 = int(input("Enter Number 1: "))
    num2 = int(input("Enter Number 2: "))

    print("Sum :", add(num1, num2))
    print("Difference :", subtract(num1, num2))
    print("Product :", multiply(num1, num2))
    print("Quotient :", divide(num1, num2))
