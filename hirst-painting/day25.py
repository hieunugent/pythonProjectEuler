import os
import csv
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
weather_data = os.path.join(THIS_FOLDER, './weather_data.csv')


# with open(weather_data) as data_file:
#     data = csv.reader(data_file)
#     temperature =[]
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(row[1])
#     print(temperature)   

import pandas 
data = pandas.read_csv(weather_data)
data_dict = data.to_dict()
temp_list = data["temp"].to_list()


print(temp_list)

print(data[data.condition == "Sunny"])

data_new = {
    "students": ["Amy", "James", "Angela"],
    "score":[67,88,99]
    
}
data = pandas.DataFrame(data_new)
data.to_csv("new_data.csv")