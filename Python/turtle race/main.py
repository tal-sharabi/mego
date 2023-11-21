import turtle
import random

# Set up the screen with a canvas size of 600x600
turtle.setup(width=800, height=600)

# Create a list of colors
colors = ["red", "green", "blue", "yellow"]

# Create a list of initials for each color
initials = ["R", "G", "B", "Y"]

# Create a list of turtle objects with different colors
turtles = []

# Initial Y positions for the turtles
y_positions = [180, 60, -60, -180]

# Create turtle objects with specified colors and positions
for the_color, y_position in zip(colors, y_positions):
    t = turtle.Turtle(shape="turtle")
    t.color(the_color)
    t.penup()
    t.goto(-390, y_position)
    t.pendown()
    turtles.append(t)

# Create a pop-up window to input the user's guess
user_guess = turtle.textinput(title="Guess the Turtle", prompt="Which turtle do you think will win? (R/G/B/Y)").upper()

# Race simulation
winner = None

# Simulate the race until a turtle crosses the finish line
while True:
    for t in turtles:
        distance = random.randint(1, 10)
        t.forward(distance)

        # Check if a turtle has crossed the finish line
        if t.xcor() > 370:
            winner = t
            break

    if winner:
        break

# Check if the user guessed correctly
if user_guess and user_guess.upper() == initials[colors.index(winner.color()[0])]:
    turtle.textinput("Result", f"Congratulations! You guessed right. The winner is the "
                               f"{winner.color()[0]} turtle!\nEnter your name:")
else:
    turtle.textinput("Result", f"Sorry, you guessed wrong. The winner is the "
                               f"{winner.color()[0]} turtle.\nEnter your name:")

# End the program by clicking on the screen
turtle.exitonclick()
