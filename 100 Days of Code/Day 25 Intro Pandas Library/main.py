
### Reading a csv file

# with open(r"C:\Users\ronal\OneDrive\Documents\Python\Exercise\Day 25\venv\weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

### Reading a csv file using csv library

# import csv

# with open(r"C:\Users\ronal\OneDrive\Documents\Python\Exercise\Day 25\venv\weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:              
#         """ getting the temp from the data """
#         if row[1] == "temp":
#             continue
        
#         temperature.append(int(row[1]))
#     print(temperature)

### Alternative way of reading a file using pandas library

import pandas

data = pandas.read_csv(r"C:\Users\ronal\OneDrive\Documents\Python\venv\100 Days of Code\Day 25 Intro Pandas Library\weather_data.csv")

# Getting the temperature from the data and converting it to a list
temp_list = data["temp"].to_list()

# Calculating the average temperature 
average_temp = sum(temp_list) / len(temp_list)
print(average_temp)

# Alternative way of calculating the average temperature using a method from the pandas library
average_temp2 = data["temp"].mean()
print(average_temp2)

# Getting the max value from the data using a method from the pandas library
max_temp = data["temp"].max()
print(max_temp)

# How to get specific data in column

# Call the name of the column

print(data["day"])

print(data["temp"])

print(data["condition"])

#or 
# Printing the attributes

print(data.day)

print(data.temp)

print(data.condition)

# How to get data in row

# Call the name of the column and check the row inside the column

print(data[data.day == "Monday"])

# Getting the row with the highest temperature

print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)

# Getting the temperature and converting it from celcius to fahrenheit

monday_temp = int(monday.temp)

monday_temp_F = monday_temp * 1.8 + 32
print(monday_temp_F)

# Creating a dataframe from scratch 

data_dict = {
    "income": ["forex", "kerja", "cuci", "kutip hutang"], 
    "duit": [300, 1500, 400, 350 ]
}

data = pandas.DataFrame(data_dict)

# Converting the data to csv file

data.to_csv("new_data.csv")


