"""
Activity 1
Title: Odd Even
Short description:
Write a Python program to take a number as input from the user, then check whether that number is even or odd and print the result.
"""

number = int(input("Enter Number to check: "))
print("Number to be checked :", number)

if number % 2 == 0:
    print("This is an even number")
else:
    print("This is an odd number")
