from turtle import Turtle

FONT = ("Helvetica", 18, "normal")


class Scoreboard(Turtle):
   
    def __init__(self):
        """ Crete a scoreboard to check the current level """

        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(-280, 250)
        self.level = 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level : {self.level}", move=False, align='left', font=(FONT))

    def increase_level(self):
        """ Increasing the level everytime the turtle
        reach the end """

        self.level += 1
        self.update_score()

    def game_over(self):
        """ End the game if the turtle hit the cars"""

        self.goto(0, 0)
        self.write(f"GAME OVER", move=False, align='center', font=(FONT))
        