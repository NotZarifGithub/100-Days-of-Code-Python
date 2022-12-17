from turtle import Turtle

class Paddle(Turtle):
    """ Creating a paddle """

    def __init__(self, position):
        super().__init__()

        self.Turtle = Turtle()
        self.speed("fastest")
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid = 5, stretch_len = 1)
        self.penup()
        self.goto(position)    
    
    def move_up(self):
        """ Allow the paddle to move upward """

        if self.ycor() < 250:
            new_y = self.ycor() + 50
            self.goto(self.xcor(), new_y)

    def move_down(self):
        """ Allow the paddle to move downward """

        if self.ycor() > -250:
            new_y = self.ycor() - 50
            self.goto(self.xcor(), new_y)




