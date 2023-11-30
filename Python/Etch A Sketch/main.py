from turtle import Turtle, Screen


def move_forward():
    Tal.forward(10)


def move_backward():
    Tal.backward(10)


def turn_left():
    Tal.left(15)


def turn_right():
    Tal.right(15)


def clear_drawing():

    Tal.clear()
    Tal.penup()
    Tal.goto(0, 0)
    Tal.pendown()


screen = Screen()
screen.screensize(555, 444)
screen.title("Eyal is a classic man")

Tal = Turtle()

# Bind keys to functions
screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear_drawing, "c")

screen.exitonclick()
