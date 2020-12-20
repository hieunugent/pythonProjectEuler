#TODO: Create a letter using starting_letter.docx 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
        
import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

invited_names = os.path.join(THIS_FOLDER, './Input/Names/invited_names.txt')
PLACEHOLDER = "[name]"
with open(invited_names, mode="r") as data:
    names = data.readlines()
staring_letter = os.path.join(THIS_FOLDER, './Input/Letters/starting_letter.docx')
with open(staring_letter) as letter:
    letter_contents = letter.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        letterform = os.path.join(THIS_FOLDER, f"./Output/ReadyToSend/letter_for_{stripped_name}.docx")
        with open(letterform, mode="w") as completed_letter:
            completed_letter.write(new_letter)
            
        
