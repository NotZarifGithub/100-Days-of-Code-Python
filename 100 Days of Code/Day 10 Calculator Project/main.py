#Creating operators functions 

from art import logo
import subprocess
import platform

#Clear function

def clear():
    subprocess.Popen( "cls" if platform.system() == "Windows" else "clear", shell=True)
  
#Add function
  
def add(n1, n2):
  return n1 + n2

#subtract function

def subtract(n1, n2):
  return n1 - n2

#multiply function

def multiply(n1, n2):
  return n1 * n2

#Division function

def division(n1, n2):
  return n1 / n2

operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : division,
}

#def calculator recursive function

def calculator():
  print(logo)
  n1 = float(input("What's the first number?: "))
  for operators in operations:
    print(operators)
  
  continue_calc = True
  
  while continue_calc:
    operators_symbols = input("Choose an operation: ")
    n2 = float(input("What's the next number?: "))
    calculation_function = operations[operators_symbols]
    answer = calculation_function(n1, n2)
    
    print(f"{n1} {operators_symbols} {n2} = {answer}")
    
    yes_no = input("Type 'y' to continue, type 'n' to stop, type 's' to start a new calculation: ")
    if yes_no == "y":
      n1 = answer
    elif yes_no == "s":
      clear()
      calculator()
    elif yes_no == "n":
      continue_calc = False
      clear()
    
calculator()