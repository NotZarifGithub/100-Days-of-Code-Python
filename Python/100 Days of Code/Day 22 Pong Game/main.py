from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

import time

# Creating the screen

screen = Screen()
screen.bgcolor("black")
screen.setup(width = 800, height = 600)
screen.title("Pong Game")
screen.tracer(0)

# Creating the paddle
    
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# Creating the ball

ball = Ball()

# Creating the scoreboard

score = Scoreboard()

screen.listen()

screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")

screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()
    
    # Detect collision with the wall

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Detect collision with the paddle

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() <  -320:
        ball.bounce_x()

    # Detect score 

    if ball.xcor() > 380:
        score.clear()
        score.add_point_right()
        ball.reset_ball()

    if ball.xcor() < -380:
        score.clear()
        score.add_point_left()   
        ball.reset_ball()
        
screen.exitonclick()  