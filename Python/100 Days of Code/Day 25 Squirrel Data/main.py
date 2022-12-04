import pandas 

# Reading the data

data = pandas.read_csv(r"C:\Users\ronal\OneDrive\Documents\Python\venv\100 Days of Code\Day 25 Squirrel Data\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# Getting the squirrel count for each color 

grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])

cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])

black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

# Creating dict for the data

squirrel_data_dict = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"], 
    "Count" : [grey_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

# Creting a datafrom for the "squirrel_data_dict"

data = pandas.DataFrame(squirrel_data_dict)

# Converting the dict file to csv file

data.to_csv("Number of Squirrel per Color.csv")