from art import logoHL
from game_data import data
import random

def resultfun(win, score):
    prompt=""
    resultstring=""
    if not win:
        prompt = "Sorry your are lose."
        resultstring = " Final score " + str(score)
    else:
        prompt = "Your are right. "    
        resultstring = " Current score "+ str(score)
    print(prompt + resultstring)


print(logoHL)
resultfun(True, 8)
print(len(data))
alreadydone =[]
isyes = "y"
while isyes== "y":
    a = random.randint(0,len(data))
    while (alreadydone.index(a) in list):
        a = random.randint(0,len(data))
    while (alreadydone.index(b) in list):
        b = random.randint(0,len(data))
        while (a == b):
            b=random.randint(0,len(data))
    alreadydone.append(a)
    alreadydone.append(b)
    print(a)
    print(b)
    isyes = input("is more input")
