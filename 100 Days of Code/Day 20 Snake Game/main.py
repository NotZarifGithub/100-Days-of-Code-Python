from turtle import Screen
from food import Food
from scoreboard import Scoreboard
import time
import random
from snake import Snake

# Screen Setup

screen = Screen()
screen.setup(width=700, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")
screen.onkey(snake.left, "a")

is_game_over = False

while not is_game_over:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.clear()
        score.add_point()

    # Detect collision with wall

    if snake.head.xcor() > 350 or snake.head.xcor() < -350 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.reset()
        snake.reset()

    # Detect collision with tail

    for body in snake.snake_body[1:]:
        if snake.head.distance(body) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()
