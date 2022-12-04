from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        """ Creating the food """

        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("white")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """ Randomizing the location of the food """

        random_xcor = random.randint(-320, 320)
        random_ycor = random.randint(-280, 280)
        self.goto(random_xcor, random_ycor)
