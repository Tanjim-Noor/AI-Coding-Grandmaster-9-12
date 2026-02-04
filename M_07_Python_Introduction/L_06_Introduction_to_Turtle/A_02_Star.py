"""
Activity 2
Title: Star
Short description:
Set the screen for turtle graphics, including its size and title. Set the screen colour as per your choice and create a star using turtle.
"""

import turtle

sc = turtle.Screen()
sc.bgcolor("Orange")
board = turtle.Turtle()

# first triangle for star
board.forward(100) # draw base
board.left(120)
board.forward(100)

board.left(120)
board.forward(100)

board.penup()
board.right(150)
board.forward(50)

# second triangle for star
board.pendown()
board.right(90)
board.forward(100)

board.right(120)
board.forward(100)

board.right(120)
board.forward(100)

board.right(120)
board.forward(100)

board.right(120)
board.forward(100)

# end drawing
turtle.done()
