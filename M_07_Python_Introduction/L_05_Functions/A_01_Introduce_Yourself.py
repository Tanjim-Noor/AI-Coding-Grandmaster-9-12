"""
Activity 1
Title: Introduce Yourself
Short description:
Write a Python program that takes a name as an input from the user and then creates a function that accepts that name as a parameter and introduces the user.
"""

def intro(name):
    print("Hello, Good morning! I am", name)

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    intro(user_name)
