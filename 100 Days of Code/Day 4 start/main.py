#Random Module 
import random
import new_module

#Importing other module from other file by using import

print(new_module.pi)
print(new_module.name)
print(new_module.random_number)

#Random Integer 

random_integer = random.randint(0,100)
print(random_integer)

random_integer1 = random.randint(0,100)
print(random_integer1)

random_integer2 = random.randint(0,100)
print(random_integer2)

#Random Float
#Random function takes no argument 

random_float = random.random()
print(random_float)

random_float1 = random.random()
print(random_float1)

random_float2 = random.random()
print(random_float2)

#Random function randomize number from 0.0000000 - 0.9999999
#In order to get random float number more than 1, multiply the number
#Example 

new_float = random_float * 23
print(new_float)

new_float1 = random_float1 * 90
print(new_float1)

new_float2 = random_float2 *463
print(new_float2)

#List 

pc = ["graphic card", "CPU", "case", "fan", "storage", "ram", "power supply", "motherboard", "monitor", "mouse", "mousepad", "monitor tangan"]

#Using index number to pick a value from a list 

first_pc_components = pc[0]
print(first_pc_components)

first_pc_components1 = pc[2]
print(first_pc_components1)

first_pc_components2 = pc[-1]
print(first_pc_components2)

#modifying a list  

pc[-1] = "monitor arm"
print(pc)

pc[-3] = "XTRFY mouse"
print(pc)

#appending a list 

pc.append("headset")
print(pc)

pc.append("keyboard")
print(pc)

#Banker roulette challenge

#first solution

import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

length_of_names = len(names)

random_number = random.randint(0, (len(names) - 1))

print(f"{names[random_number]} is going to buy the meal today!")

#second solution

#Get the total number of items in list.
num_items = len(names)
#Generate random numbers between 0 and the last index. 
random_choice = random.randint(0, num_items - 1)
#Pick out random person from list of names using the random number.
person_who_will_pay = names[random_choice]

print(person_who_will_pay + " is going to buy the meal today!")

#easier solution
#by using choice function

random_names = random.choice(names)
print(f"{random_names} is going to buy the meal today!")

#nested list or list inside a list

smartphone = ["samsung", "iphone", "oppo", "xiaomi", "nokia" ]
computer = ["dell", "hp", "alienware", "asus", "macbook"]

combined_list = [smartphone, computer]
print(combined_list)

#Treasure Map Challenge

row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")

horizontal = int(position[0])
vertical = int(position[1])

map[vertical - 1][horizontal - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")

#Day 4 : rock-paper-scissors project 
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


import random 

choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

if choice == "0":
    print(rock)
elif choice == "1":
    print(paper)
elif choice == "2":
    print(scissors)

computer_random = random.randint(0,2)

if computer_random == 0:
    print(rock)
if computer_random == 1:
    print(paper)
if computer_random == 2:
    print(scissors)
    
if choice == "0":
    if computer_random == 0:
        print("Tie")
    if computer_random == 1:
        print("You Lose")
    if computer_random == 2:
        print("You Win")
elif choice == "1":
    if computer_random == 0:
        print("You Win")
    if computer_random == 1:
        print("Tie")
    if computer_random == 2:
        print("You Lose")
elif choice == "2":
    if computer_random == 0:
        print("You Lose")
    if computer_random == 1:
        print("You Win")
    if computer_random == 2:
        print("Tie")

#second solution
      
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")

####### Debugging challenge: #########
#Try running this code and type 5.
#It will give you an IndexError and point to line 32 as the issue.
#But on line 38 we are trying to prevent a crash by detecting
#any numbers great than or equal to 3 or less than 0.
#So what's going on?
#Can you debug the code and fix it?
#Solution: https://repl.it/@appbrewery/rock-paper-scissors-debugged-end

