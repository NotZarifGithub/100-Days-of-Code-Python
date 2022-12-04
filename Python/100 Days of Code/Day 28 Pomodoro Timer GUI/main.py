from distutils.cmd import Command
from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 30  
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text = "00:00")
    label_timer.config(text = "Timer")
    label_mark.config(text = "")
    global reps 
    reps = 0 
# ---------------------------- TIMER MECHANISM ------------------------------- # 

#Start func

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0: 
        count_down(long_break_sec)
        label_timer.config(text = "Go Have a Break", fg = "red3")
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label_timer.config(text = "Short 5 Min Break", fg = "grey1")
    else:
        count_down(work_sec)
        label_timer.config(text = "Work Now", fg = "green2")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# Countdown func

def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec  < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for i in range(work_sessions):
            marks += "✔"
        label_mark.config(text = marks)

# ---------------------------- UI SETUP ------------------------------- #

# Window Setup

window = Tk()
window.title("Pomodoro Timer")
window.config(padx = 100, pady = 50, bg = PINK)

# Tomato IMG 

tomato_img = PhotoImage(file = r"C:\Users\ronal\OneDrive\Documents\Python\venv\100 Days of Code\Day 28 Pomodoro Timer GUI\tomato.gif")
canvas = Canvas(width = 200, height = 224, bg = PINK, highlightthickness = 0)
canvas.create_image(100, 112, image = tomato_img)
timer_text = canvas.create_text(100, 130, text = "00:00", fill = "white", font = (FONT_NAME, 25, "bold"))
canvas.grid(row = 2, column = 2)

# Label "Timer"

label_timer = Label()
label_timer.config(text = "Timer", bg = PINK, fg = GREEN, font = (FONT_NAME, 35, "bold"))
label_timer.grid(row = 1, column = 2)

# Label "Check Mark"

label_mark = Label()
label_mark.config(bg = PINK, fg = "black", font = (FONT_NAME, 13, "bold"), pady = 15)
label_mark.grid(row = 3, column = 2)

# Start Button 

button_start = Button()
button_start.config(text = "Start", padx = 7, command = start_timer)
button_start.grid(row = 3, column = 1)

# Reset Button

button_reset = Button()
button_reset.config(text = "Reset", padx = 7, command = reset_timer)
button_reset.grid(row = 3, column = 3)

window.mainloop()

