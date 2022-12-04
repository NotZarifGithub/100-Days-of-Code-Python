from turtle import Turtle, position

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:    
    """ Creating the functions of the snake """
    def __init__(self, ):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        """ Spawning the snake at the middle of 
        the screen """

        for position in STARTING_POSITION:
            self.extend_snake(position)

    def extend_snake(self, position):
        """ Creating the body of the snake """

        snake = Turtle()
        snake.penup()
        snake.shape("square")
        snake.color("white")
        snake.goto(position)
        self.snake_body.append(snake)       

    def reset(self):
        for snake in self.snake_body:
            snake.goto(1000, 1000)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]

    def extend(self):
        """ Increasing the length of the snake everytime 
        the snake consume the food """

        self.extend_snake(self.snake_body[-1].position())

    def move(self):
        """
        Allowing the snake to move forward and making sure
        that the body follows the head of the snake
        """ 
        for snake in range(len(self.snake_body) -1, 0, -1):
            new_x = self.snake_body[snake - 1].xcor()
            new_y = self.snake_body[snake - 1].ycor()
            self.snake_body[snake].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        """ Allowing the user to move the snake upward with
        'W' key
        """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """ Allowing the user to move the snake downward with
        'S' key
        """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        """ Allowing the user to move the snake to the right
        with 'D' key
        """
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        """ Allowing the user to move the snake to the left
        with 'A' key
        """
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)