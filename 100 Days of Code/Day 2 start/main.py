#Data Types

#String 
#Using index to print specific character

print("Hello, today we will be learrning about data types"[0])
print("Hello, today we will be learrning about data types"[14])
print("Hello, today we will be learrning about data types"[3])
print("Hello, today we will be learrning about data types"[2])
print("Hello, today we will be learrning about data types"[8])

name = "zarif"
print(type(name))

#Integer 

print(123)
print(123 + 456)
print(13453 - 323525 +7667)

number = 109080
print(type(number))

#float
print(123.321)
print(8080.6969)

float_1 = 69.69
print(type(float_1))

#boolean
print(True)
print(False)

boolean = True
print(type(boolean))


#type checking, type error, type conversion 
#in order to check a type of a variable, use function "type" in front of the variable
#Example

print(type(name))
print(type(boolean))
print(8080.6969)
print(type(number))

#type conversion
#in order to change a type of a variable, use the function that are provided 
#example of provided functions are "str", "float", "int"

print(int("12345"))
print(float(12345))

#mathematical operation 
#addition "+"
69 + 69 
#subtraction "-"
80 - 80 
#multiplication "*"
549 * 888
#division "/"
9 / 9
#exponent "**"
2 ** 2 
#modulus "%"
50 % 7
#floor division "//"
900 // 90

#round function 
#used for rounding off number to the nearest specific decimal places 
#example

print(9834/34)
print(round(9834/34))

#number after "," is used for a specific decimal point
print(round(9834/34, 5))
print(round(9834/34, 2))
print(round(9834/34, 1))

#f-String 
#f-string is used to input value inside a string 
#Example

name = "zarif"
age = 21

print(f"Hello there, my name is {name} and im {age} years old")

#Day-2 Project : Tip Calculator 

print("Hello there, welcome to Tip Calculator")
print("In order for this calculator to work, user need to answer a few questions")
print("First Question...")
total_bill = (input("What was the total bill?\n"))
tip_percent = (input("What was the percentage you would like to give?\n"))
total_people = (input("How many people to split the bill?\n"))
tip_cost =(float(tip_percent)/100) * float(total_bill) / int(total_people)
bill_for_each_person = (int(total_bill) / int(total_people)) + (float(tip_cost))
print(f"The bill that needed to be paid for each person is ${bill_for_each_person}")                                                              



