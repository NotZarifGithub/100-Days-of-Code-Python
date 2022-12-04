# For Loop
numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)

# List Comprehension
# list = [new_items for items in list]

new_list = [n + 1 for n in numbers]

# String as List
name = "Angela"
letters_list = [letter for letter in name]

# Range as List
# list = [new_items for items in list]

range_list = [n * 2 for n in range(1, 5)]

# Conditional List Comprenhension
# list = [new_items for items in list if test]

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]

upper_case_names = [name.upper() for name in names if len(name) > 4]

# Dictionary Comprehension
# dict = {new_key:new_value for items in list}

import random

student_grades = {name: random.randint(1, 100) for name in names}
print(student_grades)

# Conditional Dictionary Comprehension
# dict = {new_key:new_value for (key, value) in dict.items() if test} 

passed_students = {student:score for (student, score) in student_grades.items() if score >= 60}
print(passed_students)

# Coding Room Challenge 

days_list = ["monday", "Tuesday", 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
temp_list = [12, 14, 15, 14, 21, 22, 24]
 
 
def check_values(weather_f_dict):
    check_list = [53.6, 57.2, 59.0, 57.2, 69.8, 71.6, 75.2]
    for i in range(len(check_list)):
        dict_val = list(weather_f.values())[i]
        list_val = check_list[i]
        if dict_val == list_val:
            print(f"Your value at index {i} is correct. {dict_val}")
        else:
            print(f"Your value at index {i} is incorrect. {dict_val} should be ")
 
 
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15, 
    "Thursday": 14,
    "Friday": 21, 
    "Saturday": 22, 
    "Sunday": 24,
}
 
# WRITE YOUR CODE BELOW. The function above will do the checking.
#######################################
 
weather_f = {day:temp * 1.8 + 32 for (day, temp) in weather_c.items()}
 
#######################################
# Don't change the function call below.
check_values(weather_f)