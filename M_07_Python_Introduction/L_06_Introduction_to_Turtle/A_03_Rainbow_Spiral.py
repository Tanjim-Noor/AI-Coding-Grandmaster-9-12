"""
Activity 3
Title: Rainbow Spiral
Short description:
Write a Python program to create a spiral web of rainbow colours using the turtle library.
"""

import turtle

t = turtle.Turtle()
s = turtle.Screen()
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
s.bgcolor('black')
t.speed('fastest')
t.hideturtle()

while True:
    for x in range(200):
        t.pencolor(colors[x % len(colors)])
        t.width(x/100 + 1)
        t.forward(x)
        t.left(59)
        t.right(239)
    for x in range(200, 0, -1):
        t.pencolor('black')
        t.width(x/100 + 7)
        t.forward(x)
        t.right(59)

# Note: this program runs until the window is closed by the user
