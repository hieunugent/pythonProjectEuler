#list comprehension 
# code shorter and easier to read
#  nameofnewlist = [new_item for item in list]
#  new_list = [n+1 for n in [1,2,3,4]]
#  short_names =[new_item for item in list if test]
#  dictionary comprehension new_dict = {new_key:new_value for item in list}

import os
import csv
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
file1 = os.path.join(THIS_FOLDER, './file1.txt')
file2 = os.path.join(THIS_FOLDER,"./file2.txt")

with open(file1) as f1:
    file1_data = f1.readlines()
with open(file2) as f2:
    file2_data = f2.readlines()

result =[int(num) for num in file1_data if num in file2_data ]
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result1 ={word:len(word) for word in sentence.split()}



print(result1)