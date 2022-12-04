from turtle import Turtle, Screen
import random
import turtle as t
arrow = Turtle()
arrow.shape("arrow")
arrow.color("red4", "black")

#Drawing a square

# for i in range(4):
#     arrow.forward(150)
#     arrow.right(90) 

#Drawing a dashed line 

# for i in range(10):
#     arrow.forward(10)
#     arrow.penup()
#     arrow.forward(10)
#     arrow.pendown()
 
#Drawing multiple shapes in 1 go
 
# on = True
# num = 3
# angle = 360

# while on:

#     for i in range(num):
#         arrow.forward(100)
#         arrow.right(angle / num)
#     num += 1
#     if num == 11:
#         on = False

#Drawing a random walk 
#Generate random color

t.colormode(255)

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)

#     color = (r, g, b)
#     return color

# directions = [0, 90, 180, 270]
# arrow.pensize(15)

# on = True

# while on:
#     arrow.color(random_color())
#     arrow.forward(30)
#     arrow.setheading(random.choice(directions))

#Draw Spirograph

# t.colormode(255)

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)

#     color = (r, g, b)
#     return color

# arrow.speed("fastest")
# arrow.pensize(3)

# for i in range(36):
#     arrow.color(random_color())
#     arrow.circle(150)
#     arrow.right(10)

screen = Screen()
screen.exitonclick()

