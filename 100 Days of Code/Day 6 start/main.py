#function 
#examples of built-in functions

#print()
#len()
#int()
#float()
#sum()
#max()
#min()

#creating our own function

def function():
  #do something
  pass

#call the function
  
#example

def function1(): #defining the function
  print("YOLO")  #doing something
  print("Baby")  #doing something
  print("zyzz")  #doing something

function1()      #calling the fucntion

#Reebog's World

#Hurdle 1 
#solution 1 

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
for steps in range(6):
    jump()
#or 

#while loop 

while number_of_walls > 0:
  jump()
  number_of_walls -= 1

#hurdle 3 

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    jump()

#or 

while at_goal != True:
  jump()

#hurdle 3 

#my solution

while not at_goal():
    if wall_in_front():
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()
    else:
        move()

  #best solution

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
  
while not at_goal():
    if wall_in_front():
      jump()       
    else:
        move()

#hurdle 4

def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    move()
    while front_is_clear():
        move()
    turn_left()
        
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()

#Reebog's World Maze

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if not wall_on_right():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
    
  