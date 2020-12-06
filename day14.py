from art import logoHL, vs
from game_data import data
import random
import os

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
def printinfo(data, who):
    print("Choice "+ who +" is " + data.get("name")+" is a "+ data.get("description")+" in " + data.get("country"))



# alreadydone =[]
gameover = False
score =0
iswin = True
while not gameover:
    os.system("clear")
    print(logoHL)
    if (score > 0):
        resultfun(iswin, score)
    a = random.randint(0,len(data)-1)
    b = random.randint(0,len(data)-1)
    while (a == b):
        b=random.randint(0,len(data)-1)
    
    printinfo(data[a], "A")
    print(vs)
    printinfo(data[b], "B")
   
    winner =""
    if (data[a].get("follower_count") > data[b].get("follower_count")):
            winner = "a"
    elif (data[a].get("follower_count") < data[b].get("follower_count")):
            winner = "b"q
    print(winner)
    yourchoice = input("Who has higher follower A or B ? ").lower()
    if winner == yourchoice:
        score+=1
    else:
        iswin=False
        gameover = True
        os.system("clear")
        print(logoHL)
        resultfun(iswin, score)
        

        
