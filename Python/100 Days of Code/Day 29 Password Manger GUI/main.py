from re import L
from tkinter import *
from tkinter import messagebox
from webbrowser import get
import random, pyperclip, json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
        
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
               'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
               'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
               'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [random.choice(letters) for char in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for char in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for char in range(random.randint(2, 4))]

    password_list = password_letter + password_symbols + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)
    password_input.insert(0, f"{password}")
    pyperclip.copy(password)

# ---------------------------- FUNCTIONS ------------------------------- #

# A function that allowed "command" use multiple func
# URL = https://stackoverflow.com/questions/5839517/tkinter-call-two-functions
def sequence(*functions):
    def func(*args, **kwargs):
        return_value = None
        for function in functions:
            return_value = function(*args, **kwargs)
        return return_value
    return func

# Save function
def save():

    website = website_input.get()
    email = email_username_input.get()
    password = password_input.get()
    clicking_ok = True

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0:
        messagebox.showerror(title = "Error", message = "Enter a website")
    elif len(email) == 0:
        messagebox.showerror(title = "Error", message = "Enter an email or username")
    elif len(password) == 0:
        messagebox.showerror(title = "Error", message = "Enter a password")
    else:
        if clicking_ok:       
            try:
                with open('data.json', mode='r') as data_file:
                    data = json.load(data_file)
            except (FileNotFoundError, json.JSONDecodeError):
                data = new_data
            else:
                data.update(new_data)
            
            with open('data.json', mode='w') as data_file:
                json.dump(data, data_file, indent=4)
        else:
            delete_entry()

# Delete function 
def delete_entry():

    website_input.delete(0, END)
    password_input.delete(0, END)

def search_password():
    website = website_input.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title = "Error", message = "No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title = website, message = f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title = "Error", message = f"No details for {website} exists.")

# ---------------------------- UI SETUP ------------------------------- #

# Setting up the window 

window = Tk()
window.config(padx = 20, pady = 20, bg = "white smoke")
window.title("Password Manager")

# Setting up the image "my_pass.png" and canvas

lock_image = PhotoImage(file = r"C:\Users\ronal\OneDrive\Documents\Python\venv\100 Days of Code\Day 29 Password Manger GUI\my_pass.png")
canvas = Canvas(width = 200, height = 200, bg = "white smoke", highlightthickness = 0)
canvas.create_image(100, 100, image = lock_image)
canvas.grid(row = 0, column = 1)

# Label "Website"

label_website = Label()
label_website.config(text = "Website:", bg = "white smoke")
label_website.grid(row = 1, column = 0)

# Label "Email/Username"

label_email_username = Label()
label_email_username.config(text = "Email/Username:", bg = "white smoke")
label_email_username.grid(row = 2, column = 0)

# Label "Password"

label_password = Label()
label_password.config(text = "Password:", bg = "white smoke")
label_password.grid(row = 3, column = 0)

# Entry "Website"

website_input = Entry()
website_input.config(width = 20)
website_input.focus()
website_input.grid(row = 1, column = 1, sticky = "EW", pady = 5)

# Entry "Email/Username"

email_username_input = Entry()
email_username_input.config(width = 35)
email_username_input.insert(0, "ronaldo7zarif@gmail.com")
email_username_input.grid(row = 2, column = 1, columnspan = 2, sticky = "EW", pady = 5)

# Entry "Password"

password_input = Entry()
password_input.config(width = 20)
password_input.grid(row = 3, column = 1, sticky = "EW", pady = 5)

# Button "Generate Password"

button_generate_password = Button(bg = "white smoke", command = generate_password)
button_generate_password.config(text = "Generate Password", padx = 5)
button_generate_password.grid(row = 3, column = 2)

# Button "Add"

button_add = Button(bg = "white smoke", command = sequence(save, delete_entry))
button_add.config(text = "Add", width = 36)
button_add.grid(row = 4, column = 1, columnspan = 2, sticky = "EW", pady = 5)

# Button "Search"

button_search = Button(bg = "white smoke", command = search_password)
button_search.config(text = "Search", width = 15)
button_search.grid(row = 1, column = 2)

window.mainloop()