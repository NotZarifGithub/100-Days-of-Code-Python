from msilib.schema import SelfReg
from turtle import Turtle
import random

class Ball(Turtle):
    """ Creating a ball """

    def __init__(self):
        super().__init__()

        self.color("white")
        self.shape("circle")
        self.shapesize(stretch_wid = 1, stretch_len = 1)
        self.penup()
        self.move_speed = 0.1
        self.x_move = 10
        self.y_move = 10

    def move(self):
        """ Moving the ball to  a 45 degree angle """

        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """ Bouncing the ball everytime it hit the wall """
        self.y_move *= -1

    def bounce_x(self):
        """ Bouncing the ball everytime it hit the paddle """

        self.x_move *= -1
        self.move_speed *= 0.01

    def reset_ball(self):
        """ Resetting the ball to the middle of the screen if 
        any of the user didn't caught the ball """

        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()