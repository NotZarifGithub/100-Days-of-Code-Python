from turtle import Turtle, Screen
import random
import turtle as t

arrow = Turtle()
screen = Screen()

color_list =[(233, 233, 232), (231, 233, 237), (236, 231, 233), (224, 233, 227),
(207, 160, 82), (54, 88, 130), (145, 91, 40), (140, 26, 49), (221, 207, 105),
(132, 177, 203), (158, 46, 83), (45, 55, 104), (169, 160, 39), (129, 189, 143),
(83, 20, 44), (37, 43, 67), (186, 94, 107), (187, 140, 170), (85, 120, 180),
(59, 39, 31), (88, 157, 92), (78, 153, 165), (194, 79, 73), (45, 74, 78),
(80, 74, 44), (161, 201, 218), (57, 125, 121), (219, 175, 187), (169, 206, 172),
(219, 182, 169), (179, 188, 212), (48, 74, 73), (147, 37, 35), (43, 62, 61)]

screen.colormode(255)
turtle, screen  = t .Turtle(),  t .Screen()

Width, Height  = 800, 500
screen.setworldcoordinates(-1, -1, screen.window_width() - 1, screen.window_height() - 1)

on = True
x = 0
y = 0

while on:
    arrow.goto(x , y)

    for i in range(10):
        arrow.color(random.choice(color_list))
        arrow.dot(20)
        arrow.penup()
        arrow.forward(50)
    y += 50
    if y == 500:
        on = False

screen.exitonclick()