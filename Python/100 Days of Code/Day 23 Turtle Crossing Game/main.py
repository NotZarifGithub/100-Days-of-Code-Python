import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Creating the screen 

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

# Spawning the turtle

turtle = Player()

screen.listen()
screen.onkey(turtle.move_up, "w")
screen.onkey(turtle.move_down, "s")

# Spawning random cars

cars = CarManager()

# Create a scoreboard

score = Scoreboard()

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move_cars()

    # Detect collisions with the cars

    for car in cars.all_cars:
        if turtle.distance(car) < 30:
            score.game_over()
            game_is_on = False

    # Detect if turtle reach the end
    
    if turtle.is_at_finished_line():
        turtle.go_to_start()
        cars.increase_speed()
        score.increase_level()
        
screen.exitonclick()