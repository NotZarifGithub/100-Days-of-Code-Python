#for loop 

#for items in list_of_items:
#  do something inside here

#Example:

import random
new_string = "zarif"

for i in new_string:
  print(i)

for i in new_string:
  print("new_string")

for i in new_string:
  print(new_string)
  

pc = ["graphic card", "CPU", "case", "fan", "storage", "ram", "power supply", "motherboard", "monitor", "mouse", "mousepad", "monitor arm"]

for components in pc:
  print(components)

for components in pc:
  pc[-1] = "Hello"
  print(pc)

valorant = ["phoenix","neon", "jett","skye"]
valorant1 = ["cypher","viper","brim","reyna"]

for agents in valorant:
  print(agents, random.randint(0,100))
  for agents in valorant1:
    print(agents, random.randint(0,100))
    
for no in range(1):
  print(valorant, random.randint(0,100))
  
bart = "no one is interested in my pants."

for reps in range(5):
  print(bart)

#range function 
#range function has 3 arguments start, stop, step

for numbers in range(1,11):
  print(numbers)

for numbers in range(1,100,10):
  print(numbers)

for numbers in range(0,100,10):
  print(numbers)

for numbers in range(15):
  print(numbers)

total_numbers = 0 
for numbers in range(1,101):
  total_numbers += numbers
print(total_numbers)
  
#Calculating average height using for loops 

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

average_heights = 0
count = 0

for height in student_heights:
    average_heights += height
for num in student_heights:
    count += 1 
average_heights /= count
average_heights = round(average_heights, 0)
average_heights = int(average_heights)
print(average_heights)

#finding teh highest score

# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

highest_scores = 0

for scores in student_scores:
    if scores > highest_scores:
        highest_scores = scores
print(f"The highest score in the class is: {highest_scores}")

#Adding even number

#first solution 

even_numbers_sum = 0 

for num in range(2,101,2):
    even_numbers_sum += num 
print(even_numbers_sum)

#second solution 

even_numbers_sum = 0

for num in range(101):
    if num %2 == 0:
        even_numbers_sum += num
print(even_numbers_sum)

#FizzBuzz Challenge

for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)    


#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#first solutiion 

password = ''

password = random.choices(letters, k=nr_letters) + random.choices(symbols, k=nr_symbols) + random.choices(numbers, k=nr_numbers)
password = "".join(password)
print(password)

#second solution 

passwords = ""

for num in range(nr_letters):
    passwords += random.choice(letters)
for num in range(nr_symbols):
    passwords += random.choice(symbols)
for num in range(nr_numbers):
    passwords += random.choice(numbers)
print(passwords)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

#first solution 

passwords = []

for num in range(nr_letters):
    passwords += random.choice(letters)
for num in range(nr_symbols):
    passwords += random.choice(symbols)
for num in range(nr_numbers):
    passwords += random.choice(numbers)

random.shuffle(passwords)
passwords = "".join(passwords)
print(passwords)

#second solution 

passwords = []

for num in range(nr_letters):
    passwords.append(random.choice(letters))
for num in range(nr_symbols):
    passwords.append(random.choice(symbols))
for num in range(nr_numbers):
    passwords.append(random.choice(numbers))

random.shuffle(passwords)
passwords = "".join(passwords)
print(passwords)

