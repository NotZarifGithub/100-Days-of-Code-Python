
#Dictionary

programming_dictionary = {
"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again.",
"Loop": "The action of doing something over and over again.",
}

#How to retrieve items from dictionary?
#by getting the "key" of the items
#example

print(programming_dictionary["Bug"])
print(programming_dictionary["Loop"])

#How to add items in dictionary?
#by adding a new key with values
#example

programming_dictionary["List"] = "List is one of the data types in function used to store data"
programming_dictionary["Variable"] = "Variable in python are a containers used to store data value"

print(programming_dictionary)

#How to update a dictionary

programming_dictionary.update({"String" : "String is an immutable sequence data type"})

print(programming_dictionary)

#Creating an empty dictionary

dictionary_1 = {}

#Emptying an existing dictionary 

#programming_dictionary = {}
#print(programming_dictionary)

#Edit an item in dictionary

programming_dictionary["String"] = "String is a collection of alphabets, words or other characters."
print(programming_dictionary)

#Looping through dictionary
#retrieving keys

for keys in programming_dictionary:
  print(keys)

#retrieving value

for keys in programming_dictionary:
  print(programming_dictionary[keys])

#Grading Program challenge

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.

student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇

for keys in student_scores:
    if student_scores[keys] >= 91:
         student_grades[keys] = "Outstanding"
    elif student_scores[keys] >= 81:
        if student_scores[keys] <= 90:
            student_grades[keys] = "Exceeds Expectations"
    elif student_scores[keys] >= 71:
        if student_scores[keys] <= 80:
            student_grades[keys] = "Acceptable"
    else: 
        student_grades[keys] = "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)

#Nesting 

capitals = {
  "United Kingdom" : "London",
  "Turkey" : "Istanbul",
  "Indonesia" : "Bali",
}

#Nesting a list inside dictionary

travel_log = {
"United Kingdom" : ["London", "Manchester", "Liverpool", "Birmingham"],
"Turkey" : ["Istanbul", "Ankara", "Izmir"]}

print(travel_log)
print(travel_log["United Kingdom"])

#Nesting dictionary inside dictionary 

travel_log = {
"United Kingdom" : {"cities_visited" : ["London", "Manchester", "Liverpool", "Birmingham"], "total visits": 1 },
"Turkey": {"cities_visited" : ["Istanbul", "Ankara", "Izmir"], "total visits" : 1},
}

#Nesting dictionary inside a list 

travel_log = [
  {
    "country" : "United Kingdom",
    "cities_visited" : ["London", "Manchester", "Liverpool", "Birmingham"],
    "total visits": 1,
  },
  {
    "country" : "Turkey",
    "cities_visited": ["Istanbul", "Ankara", "Izmir"],
    "total visits": 1,
  }
]

#Adding dictionary in list

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country, visits, cities):
  new_country = {}
  new_country["country"] = country
  new_country["visits"] = visits
  new_country["cities"] = cities
  travel_log.append(new_country)

#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

#Secret Auction Challenge

from replit import clear
from art import logo

print(logo)

name_and_price = {}
bidding_finished = False

def finding_highest_bidder(name_and_price):
  highest_bid = 0
  winner = ""
  for bidder in name_and_price:
    bid_amount = name_and_price[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}!!")
    
while not bidding_finished:
  bidders_name = input("What is your name?: ")
  bid_price = int(input("What is the bidding price?: $"))
  name_and_price[bidders_name] = bid_price
  any_bidders = input("Are there any bidders left?: ")
  if any_bidders == "no":
    bidding_finished = True
    clear()
    print(logo)
    finding_highest_bidder(name_and_price)
  elif any_bidders == "yes":
    clear()
    print(logo)
                 
                 
                
    