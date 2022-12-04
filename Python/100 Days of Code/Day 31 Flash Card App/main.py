from tkinter import *
import pandas, random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
word_dict = {}

try:
    data = pandas.read_csv(r"data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv(r"C:\Users\ronal\OneDrive\Documents\Python\venv\100 Days of Code\Day 31 Flash Card App\data\french_words.csv")
    word_dict = original_data.to_dict(orient = "records")
else:
    word_dict = data.to_dict(orient = "records")
# ------------------------------ FUNCTIONS ---------------------------- #

# Creating function to change the words

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(word_dict)
    canvas_image.itemconfig(card_title, text = "French", fill = "black")
    canvas_image.itemconfig(card_word, text = current_card["French"], fill = "black")
    canvas_image.itemconfig(card_background, image = card_front_image)
    flip_timer = window.after(3000, func = flip_card)

def flip_card():
    canvas_image.itemconfig(card_title, text = "English", fill = "white")
    canvas_image.itemconfig(card_word, text = current_card["English"], fill = "white")
    canvas_image.itemconfig(card_background, image = card_back_image)

def is_known():
    word_dict.remove(current_card)
    data = pandas.DataFrame(word_dict)
    data.to_csv("data/words_to_learn.csv", index = False)
    next_card()

# Window 


window = Tk()
window.title("Flashy Card App")
window.config(bg = BACKGROUND_COLOR, padx = 40, pady = 40)

flip_timer = window.after(3000, func = flip_card)
# Canvas "card_front.png"

canvas_image = Canvas(width = 800, height = 526)
card_front_image = PhotoImage(file = r"C:\Users\ronal\OneDrive\Documents\Python\venv\100 Days of Code\Day 31 Flash Card App\images\card_front.png")
card_back_image = PhotoImage(file = r"C:\Users\ronal\OneDrive\Documents\Python\venv\100 Days of Code\Day 31 Flash Card App\images\card_back.png")

#Creating image
card_background = canvas_image.create_image(400, 263, image = card_front_image)
#Creating text "Word"
card_word = canvas_image.create_text(400, 263, fill = "black", font = ("Ariel 35 bold"))
#Creating text "Title"
card_title = canvas_image.create_text(400, 200, font = ("Ariel 20 italic"))

canvas_image.config(bg = BACKGROUND_COLOR, highlightthickness = 0)
canvas_image.grid(row = 0, column = 0, columnspan = 2)

# Button "Correct"

button_correct = Button(text = "Right", command = is_known)
button_correct_image = PhotoImage(file = r"C:\Users\ronal\OneDrive\Documents\Python\venv\100 Days of Code\Day 31 Flash Card App\images\right.png")
button_correct.config(image = button_correct_image, highlightthickness = 0)
button_correct.grid(row = 1, column = 1)

# Button "Wrong"

button_wrong = Button(text = "Wrong", command = next_card)
button_wrong_image = PhotoImage(file = r"C:\Users\ronal\OneDrive\Documents\Python\venv\100 Days of Code\Day 31 Flash Card App\images\wrong.png")
button_wrong.config(image = button_wrong_image, highlightthickness = 0)
button_wrong.grid(row = 1, column = 0)


next_card( )

window.mainloop()
