student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
import os
import csv
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
nato_data = os.path.join(THIS_FOLDER, './nato_phonetic_alphabet.csv')

data= pandas.read_csv(nato_data)

print(data)
# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter : row.code for (index, row) in data.iterrows()}

{"A": "Alfa", "B": "Bravo"}
print(phonetic_dict)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.




def phonetic_code():
    word = input("Enter the word:").upper()
    try:
         output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("This is not a valid word")
        phonetic_code()
    else:
      print(output_list)

phonetic_code()