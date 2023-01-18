#Functions with output 

def format_name(f_name, l_name):
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  return f"{formated_f_name} {formated_l_name}"
  
name = format_name("MuHammAD", "ZARif") 
print(name)


def anime_author(anime, author):
  formated_anime_name = anime.title()
  formated_author_name = author.title()
  return formated_anime_name + " " + formated_author_name

print(anime_author("ONE pIECe", "eIChIRO oDA"))

#Functions with multiple return

def anime_author(anime, author):
  if anime == "" or author == "":
    return "You entered an invalid inputs!"
  formated_anime_name = anime.title()
  formated_author_name = author.title()
  return formated_anime_name + formated_author_name

print(anime_author(input("What is the name of the anime?: "), input(f"What is the name of the author of the anime?: ")))

#Docstrings 
#Pretty much the same as comments
#Use docstrings to provide documentations about functions, classes, etc
#Use comments to leave simple notes
#Docstrings start with 3 ' " ' or """ and end with """
#Doctsrings start right on the 2nd line
#Example 

def anime_author(anime, author):
  """ Takes the name of the anime and the author and concatenate them together """ #THIS LINE
  if anime == "" or author == "":
    return "You entered an invalid inputs!"
  formated_anime_name = anime.title()
  formated_author_name = author.title()
  return formated_anime_name + formated_author_name

print(anime_author(input("What is the name of the anime?: "), input(f"What is the name of the author of the anime?: ")))

#Days in month Challenge

#solution 1

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True 
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
    if is_leap(year) == True:     #DIFFERENCEDIFFERENCEDIFFERENCEDIFFERENCE
        month_days[1] = 29        #DIFFERENCEDIFFERENCEDIFFERENCEDIFFERENCE
    return month_days[month - 1]
  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

#Solution 2 

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True 
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
    if is_leap(year) and month == 2:   #DIFFERENCEDIFFERENCEDIFFERENCEDIFFERENCE
        return 29                      #DIFFERENCEDIFFERENCEDIFFERENCEDIFFERENCE
    return month_days[month - 1]

#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

