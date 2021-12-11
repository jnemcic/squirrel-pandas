# with open("weather_data.csv", "r") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
print(data)
print(type(data))
print(type(data["temp"]))
dictionary_data = data.to_dict()
print(dictionary_data)
temp_list = data["temp"].to_list()
print(temp_list)
average = sum(temp_list)/len(temp_list)
print("{:.2f}".format(average))
print(data["temp"].mean())
print(data["temp"].max())
print(data["condition"]) # We're treating data like dictionary.
print(data.condition) # We're treating data like object.
print(data[data.day == "Wednesday"])
print(data[data.temp == max(data.temp)])
monday = data[data.day == "Monday"]
print(monday.condition)
print(int(monday.temp) * 1.8 + 32)

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 63]
}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("student_scores.csv")