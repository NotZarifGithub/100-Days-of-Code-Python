from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self):
        """ Creating the turtle """

        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def move_up(self):
        """ Allow the turtle to move forward """

        self.forward(MOVE_DISTANCE)

    def move_down(self):
        """ Allow the turtle to move backward """

        self.backward(MOVE_DISTANCE)
    
    def is_at_finished_line(self):
        """ Checking wether the turtle reach the end """
        if self.ycor() > 280:
            return True

    def go_to_start(self):
        """ Move the turtle to the start point """
        self.goto(0, -280)
