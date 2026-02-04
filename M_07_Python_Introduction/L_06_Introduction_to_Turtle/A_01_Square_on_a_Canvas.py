"""
Activity 1
Title: Square on a Canvas
Short description:
Write a Python program to set the screen size, colour and title for turtle graphics and draw a square using turtle.
"""

import turtle

# creating canvas
sc = turtle.Screen()
sc.bgcolor("Orange")
sc.setup(400, 300)

turtle.title("Welcome to Turtle Window")

# turtle object creation
board = turtle.Turtle()

# creating a square
for i in range(4):
    board.forward(100)
    board.left(90)

# keep the window open until closed by user
turtle.done()
