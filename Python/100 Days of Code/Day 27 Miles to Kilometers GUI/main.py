from tkinter import *

window = Tk()

#Window 

window.title("Mile to Kilometer Converter")
window.minsize(250, 100)
window.config(padx = 10, pady = 10)

# Button Function

def miles_to_kilometers():
    answer = int(user_input.get()) * 1.609
    label_answer.config(text = answer)

# Label "is equal to"

label_is_equal_to = Label(text = "is equal to", font = ("Arial", 10))
label_is_equal_to.grid(row = 2, column = 1)

# Label "Miles"

label_miles = Label(text = "Miles", font = ("Arial", 10))
label_miles.config(padx = 5, pady = 5)
label_miles.grid(row = 1, column = 3)

# Label "answer"

label_answer = Label(text = 0)
label_answer.grid(row = 2, column = 2)

# Label "KM"

label_km = Label(text = "Km")
label_km.config(padx = 5, pady = 5)
label_km.grid(row = 2 , column = 3)

# Button Calculate

calculate_button = Button(text = "Calculate", command =  miles_to_kilometers)
calculate_button.grid(row = 3, column = 2)

# Entry number

user_input = Entry(width = 10)
user_input.grid(row = 1, column = 2)



window.mainloop()
