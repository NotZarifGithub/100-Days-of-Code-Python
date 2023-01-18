############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 20): 
# # range function take two parameters, 'start' and 'end', 'start' includes the number while 'end' ends with the number but not including the number
#     if i == 20:                                  
#       print("You got it")
# my_function()

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1,6)
# #randint function take two parameter, 'start' and 'end', both 'start' and 'end' includes the number 
# print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")
# #if statements only test year 1981 and above, if input == year 1980 and below it will produce bug

# # Fix the Errors
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")
# #if code block under if statement need to be indented
# #if statement only test input age 19 and above, if input == age 18 and below it will produce bug
# parameter in 'print' needs to inlude f-string because the print statement expected {age} as a value. 

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)
# #using print statement to identify the value of the variable
# #found the bug in the variable total_words with the help of print statement
# #variable total_words use '==' instead of '='
# #'==' to check value, '=' to assign value


# # #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)
# #line 52 the for loops needs to be indented if the user expected the for loop to print out every number in the list 

# mutate([1,2,3,5,8,13])