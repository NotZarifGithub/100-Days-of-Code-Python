from turtle import Turtle, Screen, title
import pandas

screen = Screen()
screen.setup(700, 500)
screen.title("U.S.A Quiz Game")
screen.bgpic(r"C:\Users\ronal\OneDrive\Documents\Python\venv\100 Days of Code\Day 25 USA Quiz Game\blank_states_img.gif")

score = 0
is_game_on = True

while is_game_on:
    user_answer = screen.textinput(title = f"{score}/50 States Correct", prompt = "What's another states name? ").title()

    data = pandas.read_csv(r"C:\Users\ronal\OneDrive\Documents\Python\venv\100 Days of Code\Day 25 USA Quiz Game\50_states.csv")

    state = data.state
    state_list = state.to_list()

    for state_name in state_list:
        if score > 50 or user_answer == "Exit":
            is_game_on = False

        elif user_answer == state_name:
            score += 1
            state = Turtle()
            state.hideturtle()
            state.penup()
            state_data = data[data.state == user_answer]
            state.goto(int(state_data.x), int(state_data.y))
            state.write(user_answer)


