"""
Activity 4
Title: Number Swap
Short description:
Take two numbers from the user, store them in variables x and y, respectively. Write a Python program to swap the values present inside x and y and display the results.
"""

# Take input values from user
x = input("Enter Value of x:")
y = input("Enter Value of y:")

# Swapping
temp = x
x = y
y = temp

# Displaying results after swapping
print("value of x after swapping", x)
print("value of y after swapping", y)
