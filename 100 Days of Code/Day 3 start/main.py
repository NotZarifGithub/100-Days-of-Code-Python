print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

#if, elif and else statement

if height >= 120:
  print("You are tall enough to ride the rollercoaster")
else:
  print("Unfortunately you are too short for a rollercoaster ride. Comeback again once you are tall enough!")

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

#nested if and elif statements

if height >= 120:
  print("You are tall enough to ride the rollercoaster.")
  age = int(input("How old are you?"))
  if age < 12:
    print("The ticket price will be $5.")
  elif age >= 12 and age <=18:
    print("The ticket price will be $7.")
  else:
    print("The ticket price will be $12.")
else:
  print("Unfortunately you are too short for a rollercoaster ride. Comeback again once you are tall enough!")


#BMI Calculator

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = float(weight) / (float(height) ** 2)
BMI = round(BMI)
BMI = int(BMI)
print(BMI)

if BMI < 18.5:
    print(f"Your BMI is {BMI}, you are underweight.")
elif BMI < 25:
        print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI < 30:
        print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI < 35:
        print(f"Your BMI is {BMI}, you are obese.")
else:
    print(f"Your BMI is {BMI}, you are clinically obese. GO LOSE SOME WEIGHT!!!.")

#Calculating Leap Year
#use "%" to check if the number is evenly disible

#first solution
  
if year % 400 == 0:
    if year % 100 == 0:
        print("Leap Year")
elif year % 100 != 0 and year % 4 == 0 :
        print("Leap Year")
else:
    print("Not Leap Year")

#second solution 

if year % 4 == 0:
    if year % 100 != 0:
        print("Leap Year")
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
else:
    print("Not Leap Year")

#third solution

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")
  
#multiple if condition

height = int(input("What is your height in cm? "))
bill = 0 

if height >= 120:
    print("You are tall enough to ride the rollercoaster.")
    age = int(input("How old are you?"))
    if age < 12:
        bill = 5
        print("The ticket price will be $5.")
    elif age >= 12 and age <=18:
        bill = 7
        print("The ticket price will be $7.")
    else:
        bill = 12
        print("The ticket price will be $12.")
        
    want_picture = input("If you want a set of pictures of the ride enter Y, if no enter N.")
    if want_picture == "Y":
        bill = bill + 3
        print(f"The total price including the pictures will be ${bill}")
    else:
        print(f"The total price will be ${bill}")
else:
    print("Unfortunately you are too short for a rollercoaster ride. Comeback again once you are tall enough!")
    
#Pizza Order Challenge

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#first solution

small_pizza = 15
medium_pizza = 20
large_pizza = 25

if size == "L":
    if add_pepperoni == "Y":
        large_pizza += 3 
    if extra_cheese == "Y":
        large_pizza += 1
        print(f"Your final bill is ${large_pizza}.")
    else:
        print(f"Your final bill is ${large_pizza}.")
elif size == "M":
    if add_pepperoni == "Y":
        medium_pizza += 3 
    if extra_cheese == "Y":
        medium_pizza += 1
        print(f"Your final bill is ${medium_pizza}.")
    else:
        print(f"Your final bill is ${medium_pizza}.")
elif size == "S":
    if add_pepperoni == "Y":
        small_pizza += 2 
    if extra_cheese == "Y":
        small_pizza += 1
        print(f"Your final bill is ${small_pizza}.")
    else:
        print(f"Your final bill is ${small_pizza}.")

#second solution

bill = 0

if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25

if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3
    
if extra_cheese == "Y":
  bill += 1
  
print(f"Your final bill is: ${bill}.")

#Logical Operator "and", "or", "not"

if height >= 120:
    print("You are tall enough to ride the rollercoaster.")
    age = int(input("How old are you?"))
    if age < 12:
        bill = 5
        print("The ticket price will be $5.")
    elif age >= 12 and age <=18:
        bill = 7
        print("The ticket price will be $7.")
    elif age >= 45 and age <= 55:
        bill = 0 
        print("Since you are in a stage of midlife crisis, you will have the oppurtunity to ride the rollercoaster for free!")
    else:
        bill = 12
        print("The ticket price will be $12.")
        
    want_picture = input("If you want a set of pictures of the ride enter Y, if no enter N.")
    if want_picture == "Y":
        bill = bill + 3
        print(f"The total price including the pictures will be ${bill}")
    else:
        print(f"The total price will be ${bill}")
else:
    print("Unfortunately you are too short for a rollercoaster ride. Comeback again once you are tall enough!")

#Love Calculator Challenge

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1 = name1.lower()
name2 = name2.lower()

t = name1.count("t")
r = name1.count("r")
u = name1.count("u")
e = name1.count("e")

t1 = name2.count("t")
r1 = name2.count("r")
u1 = name2.count("u")
e1 = name2.count("e")

l = name1.count("l")
o = name1.count("o")
v = name1.count("v")
e = name1.count("e")

l1 = name2.count("l")
o1 = name2.count("o")
v1 = name2.count("v")
e2 = name2.count("e")

loves_scores = str(int(t + r + u + e + t1 + r1 + u1 + e1)) + str(int(l + o + v + e + l1 + o1 + v1 + e2))
loves_scores = int(loves_scores)

if loves_scores < 10 or loves_scores > 90:
    print(f"Your score is {loves_scores}, you go together like coke and mentos.")
elif loves_scores >= 40 and loves_scores <= 50:
    print(f"Your score is {loves_scores}, you are alright together.")
else:
    print(f"Your score is {loves_scores}.")


#second solution 

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combined_names = name1 + name2
lower_names = combined_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))

if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")


#Treasure Island Project 

print("Hello there, welcome Treasure Island!!")
print("Before you start the game, it is necessary to introduce yourself first.")
name = input("Please enter your name\n.")

print(f"Welcome to the game {name}")
print("Today you will be playing a newly created game called treasure island with one goal in mind, to find the hidden treasure!!")
input("Once you are ready enter 'p'.")

print("You will be relocated in a middle of a deep forest located far from civilization.")

direction = input("You can enter a direction to start your journey either south, west, north or east.")

if direction == "south":
    print("You found a weapon.")
    print("This weapon can be used to protect yourself from the danger of the jungle.")
    print("You can now choose wether to go with straight forward or choose  a new direction.")
    new_direction1 = input("type go to go straight forward or enter a new direction.")
    if new_direction1 == "go":
        print("Nooooo, you encounter a beast of the jungle")
        print("You need run towards the direction of your choice.")
    else:
        print("You enter the alam bunian.")
        print("You had no chance to get out from this world.")
        print("Game Over.")
        new_direction = input("Enter a new direction other than west and south to escape yourself from the beast.")
        if new_direction1 == "north":
            print("You found a mysterious temple covered with moss and surrounded with trees.")
            print("You can now choose wether to enter the mysterious temple.")
            enter_temple = input("type 'enter' to enter the temple.")
            if enter_temple == "enter":
                print("YOU FOUND THE HIDDEN TREASURE!!!!!!!!!")
                print("CONGRATULATIONS YOU SUCCESSFULLY FINISHED AND WON THE GAME.")
                print("Thank You for playing.")
        else:
            print("The beast found you and devour you alive, you had no chance to survive")
            print("Game Over")                 
if direction == "north":
    print("You found a river.")
    print("This river will help you in finding food as well as keeping you hydrated.")
    print("After camping and supplied yourself with tons of food and water supplies, it is time to find the hiddent treasure.")
    new_direction3 = input("Choose wether to stay for a little bit more time or enter a new direction.")
    if new_direction3 == "stay":
        print("A group of cannibal found you and kept you captive")
        print("After a few days, the cannibal kills you.")
        print("Game Over.")
    else:
            print("You found a mysterious temple covered with moss and surrounded with trees.")
            print("You can now choose wether to enter the mysterious temple.")
            enter_temple = input("type 'enter' to enter the temple.")
            if enter_temple == "enter":
                print("YOU FOUND THE HIDDEN TREASURE!!!!!!!!!")
                print("CONGRATULATIONS YOU SUCCESSFULLY FINISHED AND WON THE GAME.")
                print("Thank You for playing.")
if direction == "west":
    print("Nooooo, you encounter a beast of the jungle")
    print("You need run towards the direction of your choice.")
    new_direction = input("Enter a new direction other than west to escape yourself from the beast.")
    if new_direction == "south":
        print("You escaped from the beast.")
        print("You are hiding behind a huge tree, waiting for the beast to vanish.")
        print("The beast is now gone, now choose a direction to keep playing.")
        new_direction2 = input("enter a new direction")
        if new_direction2 == "north":
            print("You found a mysterious temple covered with moss and surrounded with trees.")
            print("You can now choose wether to enter the mysterious temple.")
            enter_temple = input("type 'enter' to enter the temple.")
            if enter_temple == "enter":
                print("YOU FOUND THE HIDDEN TREASURE!!!!!!!!!")
                print("CONGRATULATIONS YOU SUCCESSFULLY FINISHED AND WON THE GAME.")
                print("Thank You for playing.")
        else:
            print("The beast found you and devour you alive, you had no chance to survive")
            print("Game Over")       
    if new_direction == "north":
        print("You ran towards a cliff!!")
        print("You can now choose wether to jump into the deep jungle or pretend to be dead.")
        option = input("enter jump or pretend")
        if option == "jump":
            print("You are heavily injured!!")
            print("You are screaming for help while redting your back behind a tree.")
            print("After a few days waiting for help, starvation finally got to you.")
            print("Game Over")
        if option == "pretend":
            print("The beast thought you were dead.")
            print("It is now your chance to run")
            runnning_away_from_the_beast = input("Choose wether to run away or stay.")
            if running_away_from_the_beast == "run away":
                print("You are lucky!!! You found the map to the hidden treasure.") 
                hidden_treasure_map = input("follow the direction of the map or stay for a rest.")
                if hidden_treasure_map == "follow":
                    print("You found a mysterious temple covered with moss and surrounded with trees.")
                    print("You can now choose wether to enter the mysterious temple.")
                    enter_temple = input("type 'enter' to enter the temple.")
                    if enter_temple == "enter":
                        print("YOU FOUND THE HIDDEN TREASURE!!!!!!!!!")
                        print("CONGRATULATIONS YOU SUCCESSFULLY FINISHED AND WON THE GAME.")
                        print("Thank You for playing.")
                if hidden_treasure_map == "stay":
                    print("The beast came back and devour you alive, you had no chance to survive")
                    print("Game Over")     
            if running_away_from_the_beast == "stay":
                print("The beast came back and devour you alive, you had no chance to survive")
                print("Game Over")
    if new_direction == "east":
        print("After succefully escaped from the beast, you found a mysterious temple covered with moss and surrounded with trees.")
        print("You can now choose wether to enter the mysterious temple or go straight forward or choose a new direction.")
        found_temple = input("type enter to enter the temple or type go to go straight forward or choose a new direction.")
        if found_temple == "enter":
            print("YOU FOUND THE HIDDEN TREASURE!!!!!!!!!")
            print("CONGRATULATIONS YOU SUCCESSFULLY FINISHED AND WON THE GAME.")
            print("Thank You for playing.")
        else:
            print("The beast found you and devour you alive, you had no chance to survive")
            print("Game Over")    
if direction == "east":
    print("You found a map of the hidden treasure.")
    print("This map will help you locate the treasure in no time.")
    follow_map = input("enter follow to follow the direction of the hidden treasure in the map or enter enter new direction.")
    if follow_map == "follow":
        print("You found a mysterious temple covered with moss and surrounded with trees.")
        print("You can now choose wether to enter the mysterious temple.")
        enter_temple = input("type 'enter' to enter the temple.")
        if enter_temple == "enter":
            print("YOU FOUND THE HIDDEN TREASURE!!!!!!!!!")
            print("CONGRATULATIONS YOU SUCCESSFULLY FINISHED AND WON THE GAME.")
            print("Thank You for playing.")
    else:
        print("You enter the alam bunian.")
        print("You had no chance to get out from this world.")
        print("Game Over.")

      

