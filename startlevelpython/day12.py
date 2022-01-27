stillplay = True
import random
from art import logoGTN
def playGuessgame():
    print(logoGTN)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    guessnum = int(random.randint(0,100))
    print(guessnum)

    difficulty = input("Choose a difficulty.Type 'easy' or 'hard: ")
    attemp = 0
    if difficulty == "easy":
        attemp = 10
        print("you have "+ str(attemp)+ " attemps remaining to guess the number.")
    elif difficulty == "hard":
        attemp = 5
        print("you have " + str(attemp) +
              " attemps remaining to guess the number.")
    while attemp > 0:
        attemp -= 1
        yourguess = int(input("Make a guess: "))
        if yourguess == guessnum:
            print("Your Guess is Correct!")
            break
        elif yourguess < guessnum:
            print("Too low \nGuess again")
            print("you have " + str(attemp) +
                  " attemps remaining to guess the number.")
        else:
            print("Too high \nGuess again")
            print("you have " + str(attemp) +
                  " attemps remaining to guess the number.")
        
    if attemp == 0:
        print("You run out of guess")

while stillplay:
    playGuessgame()
    yourdecision = input("Do you want to play again? y/n: ")
    if yourdecision =="y":
        stillplay = True
    else:
        stillplay = False
