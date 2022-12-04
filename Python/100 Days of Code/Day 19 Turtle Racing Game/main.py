from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()

screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title = "Make a bet", prompt = "Which one of these turtles will win the race? Choose a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

num = -100

for color in colors:
    turtle = Turtle(shape = "turtle")
    turtle.color(color)
    turtle.penup()
    turtle.goto(x = -230, y = num)
    num += 40
    all_turtles.append(turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            if user_bet == turtle.pencolor():
                print(f"Congratulation ur bet on turtle {user_bet} won the race!")
            else:
                print(f"Turtle {turtle.pencolor()} won the race!")
                print(f"Sorry ur bet on turtle {user_bet} lost the race.")
            
        random_speed = random.randint(0, 10)
        turtle.forward(random_speed)
    
screen.exitonclick()