################### Scope ####################

#local scope 

def drink_potion():  
  strength = 0      #local scope
  strength += 1     #local scope 
  print(strength)

drink_potion()

#global scope 

muscle_gain = 0      #global scope 

def gain_muscle():
  muscle = 0         #local scope
  muscle += 1        #local scope
  print(muscle_gain)

gain_muscle()

iq_gain = 0          #global scope 

def start():
  def iq():          #local scope
    iq = 0           #local scope 
    iq += 1          #local scope
    print(iq)
    
#modifying global scope

#modify the global scope by using the global funtion inside the chosen scope
#avoid using this method because it led to bugs and errors

enemies = 1

def increase_enemies():
  global enemies        #using global function
  enemies += 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

#use return instead

enemies = 1

def increase_enemies():
  print(f"enemies inside function: {enemies}")
  return enemies + 2
  
increase_enemies()
print(f"enemies outside function: {enemies}")

#Global Constants

#Constants are immutable, which value cannot be changed or updated
#variables are mutable, whihc value can be changed and updated
#It is best to all upper case the constant to remind that constant is immutable

#Examples of constants

PI = 3.14159
URL = "https://www.google.com"

