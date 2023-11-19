import turtle
import random


# Function to generate a random RGB color tuple
def random_color():
    return (random.random(), random.random(), random.random())


# Function to draw a spirograph pattern
def draw_spirograph(turtle, radius, color_change_frequency, num_steps):
    for _ in range(num_steps):
        turtle.color(random_color())  # Change color
        turtle.circle(radius)
        turtle.left(360 / num_steps)

    # Check if color change should occur after completing a full circle
    if _ % color_change_frequency == 0:
        turtle.color(random_color())  # Change color again


# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor(random_color())

# Create a turtle
spirograph_turtle = turtle.Turtle()
spirograph_turtle.shape("turtle")

# Define parameters for the spirograph
radius = 69
color_change_frequency = 0  # Set to 0 to change color every step
num_steps = 24

# Draw the spirograph
draw_spirograph(spirograph_turtle, radius, color_change_frequency, num_steps)

# Close the turtle graphics window on click
screen.exitonclick()
