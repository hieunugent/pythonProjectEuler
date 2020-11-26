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




alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text, shift):
    cipher_text=""
    for letter in text:
        index = alphabet.index(letter)
        newindex = (index + shift)%len(alphabet)
        cipher_text +=alphabet[newindex]

    print("my new code is "+ cipher_text)
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HiNT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
def decrypt(text, shift):
    cipher_text = ""
    for letter in text:
        index = alphabet.index(letter)
        
        newindex = (index - shift)%len(alphabet)
        cipher_text +=alphabet[newindex]
    print("my new code is "+ cipher_text)   
#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
if (direction == "encode"):
    encrypt(text, shift)
elif (direction == "decode"):
    decrypt(text,shift)
else:
    print("your direction not right")