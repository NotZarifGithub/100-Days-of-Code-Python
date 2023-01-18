# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet():
  print("Hello.")
  print("My name is Muhammad Zarif.")
  print("You can call me Zarif.")

greet()

#functions with input

def greet_with_name(name): #name == parameters
  print("Hello.")
  print(f"My name is Muhammad {name}.")
  print(f"You can call me {name}.")

greet_with_name("Zarif") #"Zarif" is an argument

def anime(name_of_anime): #name_of_anime == parameters
  print("What's your favourite anime")
  print(f"My favourite anime is {name_of_anime}")
  print(f"{name_of_anime} is also the very first anime that i watched.") 

anime("One Piece") #One Piece is an argument

#Positional vs. Keyword Arguments

def greet_with(name, location): #name & location == parameters
  print(f"Hello {name}")
  print(f"What's it like in {location}")

greet_with("Zarif", "Rawang") #"Zarif" & "Rawang" are arguments 
                              #"Zarif" & "Rawang" are considered as positional arguments
                              # Because the arguments are the exact same position as the parameters

greet_with(location = "PJ", name = "Kedol") #"Kedol" & "PJ" are arguments 
                                            #"Kedol" & "PJ" are considered as keywords arguments
                                            #Because the arguments are the keywords of the parameters

#Paint area calculator 

import math 

def paint_calc(height, width, cover):
    number_of_cans = (height * width) / cover
    number_of_cans = math.ceil(number_of_cans)
    print(f"You'll need {number_of_cans} cans of paint.")

#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

#Prime number checker

#Write your code below this line 👇

def prime_checker(number):
    is_prime = True
    for num in range(2,number):
        if number % num == 0: 
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)

