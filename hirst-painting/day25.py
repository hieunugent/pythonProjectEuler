import os
import csv
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
weather_data = os.path.join(THIS_FOLDER, './weather_data.csv')


with open(weather_data) as data_file:
    data = csv.reader(data_file)
    temperature =[]
    for row in data:
        if row[1] != "temp":
            temperature.append(row[1])
    print(temperature)   