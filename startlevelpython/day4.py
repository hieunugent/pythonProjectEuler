rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random


def fun(action):
    if (action == 1):
        print(rock)
    elif action == 2:
        print(paper)
    elif action == 3:
        print(scissors)

a = input("enter your number from 1 -3 which is 1 for rock , 2 for paper, 3 for scissors \n")
def iswin(a, b ):
    if (a == 1 and b == 3 ):
        return True
    elif (a == 2 and b == 1):
        return True
    elif (a == 3 and b == 2):
        return True
    else:
        return False
    
myoutcome = int(a)

machineoutcome =random.randint(1,3)

print("My Our come is the \n")
fun(myoutcome)
print("Computer Our Come \n")
fun(machineoutcome)

print("WIN DECISION")
if (iswin(myoutcome, machineoutcome)):
    print ("You are Winning")
elif myoutcome==machineoutcome:
    print (" Draw")
else:
    print("You are losing")

