from turtle import Turtle, Screen

arrow = Turtle()
screen = Screen()

def move_forwards():
    arrow.forward(10)

def move_backwards():
    arrow.back(10)

def move_left():
    new_direction = arrow.heading() + 10
    arrow.setheading(new_direction)

def move_right():
    new_direction = arrow.heading() - 10
    arrow.setheading(new_direction)

def clear():
    arrow.clear()

screen.listen()
screen.onkey(move_forwards ,"w")
screen.onkey(move_backwards ,"s")
screen.onkey(move_left , "a")
screen.onkey(move_right , "d")
screen.onkey(clear, "c")

screen.exitonclick()  


