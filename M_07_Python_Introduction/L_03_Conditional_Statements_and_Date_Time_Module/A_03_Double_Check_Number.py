"""
Activity 3
Title: Double-Check Number
Short description:
Write a Python program to check whether a number entered by the user is greater than 50 or not. If it is greater than 50, then check whether it is odd or even.
"""

num = int(input("Enter number to check :"))

if num > 50:
    print("Number is greater than 50")
    if num % 2 == 0:
        print("And it is even too")
    else:
        print("And it is odd")
else:
    print("Number is less than 50")
