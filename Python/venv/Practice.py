import turtle

# Function to move the turtle forward
def move_forward():
    etch_a_sketch.forward(10)

# Function to move the turtle backward
def move_backward():
    etch_a_sketch.backward(10)

# Function to turn the turtle left
def turn_left():
    etch_a_sketch.left(10)

# Function to turn the turtle right
def turn_right():
    etch_a_sketch.right(10)

# Function to clear the drawing
def clear_drawing():
    etch_a_sketch.clear()
    etch_a_sketch.penup()
    etch_a_sketch.goto(0, 0)
    etch_a_sketch.pendown()

# Set up the screen
screen = turtle.Screen()
screen.title("Etch A Sketch")

# Create the turtle
etch_a_sketch = turtle.Turtle()
etch_a_sketch.speed(1)  # Adjust the speed as needed

# Bind keys to functions
screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear_drawing, "c")

# Keep the window open
turtle.done()
