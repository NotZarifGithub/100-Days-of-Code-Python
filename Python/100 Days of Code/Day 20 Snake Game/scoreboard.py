from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        """ Creating a scoreboard to check the score 
        of the user everytime the snake consume the food """
        super().__init__()
        self.penup()
        self.score = 0
        with open(r"C:\Users\ronal\OneDrive\Documents\Python\venv\100 Days of Code\Day 20 Snake Game\data.txt", "rt") as file:
            self.highscore = int(file.read())

        self.goto(0, 270)
        self.hideturtle()
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score : {self.score}       High Score : {self.highscore} ",
                   align="center", font=('Arial', 15, 'normal'))

    def add_point(self):
        """ Add a point everytime the snake consume the food """

        self.score += 1
        self.update_scoreboard()

    def reset(self):
        """ Reset the game if the snake hit the wall or 
        itself """

        if self.score > self.highscore:
            self.highscore = self.score
            with open(r"C:\Users\ronal\OneDrive\Documents\Python\venv\100 Days of Code\Day 20 Snake Game\data.txt", "w") as file:
                file.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     """ A method to stop the game if the snake collide
    #     with the wall or itself """

    #     self.goto(0, 0)
    #     self.write(arg = "GAME OVER.", align = "center", font = ('Arial', 15, 'normal'))
