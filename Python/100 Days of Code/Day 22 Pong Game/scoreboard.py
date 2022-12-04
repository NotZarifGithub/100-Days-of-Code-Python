from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        """ Creating a scoreboard to check the score 
        of the user """
        super().__init__()
        self.penup()
        self.score_right = 0
        self.score_left = 0
        self.goto(0, 250)
        self.hideturtle()
        self.color("white")
        self.write(arg = f"{self.score_left} : {self.score_right}", align = "center", font = ('Lato', 30, 'normal'))
    
    def add_point_right(self):
        """ Adding a point to the right user """

        self.score_right += 1
        self.write(arg = f"{self.score_left} : {self.score_right}", align = "center", font = ('Lato', 30, 'normal'))

    def add_point_left(self):
        """ Adding a point to the left user """

        self.score_left += 1
        self.write(arg = f"{self.score_left} : {self.score_right}", align = "center", font = ('Lato', 30, 'normal'))