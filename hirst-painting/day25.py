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
# data = pandas.read_csv(weather_data)
# data_dict = data.to_dict()
# temp_list = data["temp"].to_list()


# print(temp_list)

# print(data[data.condition == "Sunny"])

# data_new = {
#     "students": ["Amy", "James", "Angela"],
#     "score":[67,88,99]
    
# }
# data = pandas.DataFrame(data_new)
# data.to_csv("new_data.csv")
data_census = os.path.join(THIS_FOLDER, './2008_Squirrel_census.csv')

data  =  pandas.read_csv(data_census)

gray_squrrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squrrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squrrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squrrels_count)
print(red_squrrels_count)
print(black_squrrels_count)

data_dict= {
    "Fur Color":["Gray", "Cinnamon", "Black"],
    "Count": [gray_squrrels_count,red_squrrels_count,black_squrrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrels_count.csv")