#Write your code below this line 👇

import math
def paint_calc(height, width, cover):
    canneed = height* width / cover
    print("you need "+ str(math.ceil(canneed)) + " cans "+" to cover "+ str(height) + " feet hight "+ str(width) +" feet weight")




#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
def paintcalculate():
    test_h = int(input("Height of wall: "))
    test_w = int(input("Width of wall: "))
    coverage = 5
    paint_calc(height=test_h, width=test_w, cover=coverage)

#Write your code below this line 👇
def prime_checker(number):
    if (number <= 1):
        print("this is not prime number")
        return
    for i in range(2,number-1):
        if (number % i == 0):
            print("This is not prime number")
            return
    print("this is prime number")



#Write your code above this line 👆
    
#Do NOT change any of the code below👇
def doprime():
    n = int(input("Check this number: "))
    prime_checker(number=n)

import art

def cipher():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    print(art.logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    cipher_text=""
    for letter in text:
        index = alphabet.index(letter)
        if direction== "encode":
            newindex = (index + shift)%len(alphabet)
        elif direction == "decode":
            newindex = (index - shift)%len(alphabet)
        else:
            print("direction is not right")
        cipher_text +=alphabet[newindex]

    print("my new code is "+ cipher_text)
#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HiNT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
  
#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
# ceacar(direction, text, shift)
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.

student_grades={}
#TODO-2: Write your code below to add the grades to student_grades.👇
for a in student_scores:
    if student_scores[a] >= 80:
        student_grades[a]="A"
    elif student_scores[a] >=70:
        student_grades[a]="B"
    elif (student_scores[a] >=60):
        student_grades[a]="C"
    elif (student_scores[a]>=50):
        student_grades[a]="D"
    

# 🚨 Don't change the code below 👇
print(student_grades)





