############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt
from art import logoBJ
import random
import os

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
    return random.choice(cards)


#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().

def calculate_score(list):
    if len(list) == 2 and sum(list)== 21:
        return 0 
    if sum(list) > 21:
        for card in list:
            if card == 11:
                list.remove(card)
                list.append(1)  
    return sum(list)
def isgameover(user, comp):
    if calculate_score(user) == 0 or calculate_score(comp)==0:
        return True
    return False


def isWin(user, comp):
    if calculate_score(user) == 0:
        return "win"
    elif calculate_score(comp) == 0:
        return "lose"
    elif (calculate_score(user) > calculate_score(comp) and calculate_score(user) <= 21 ) :
        return "win"
    elif calculate_score(comp) < 22 and calculate_score(comp) > 16 and calculate_score(user) > calculate_score(comp):
        return "lose"
    elif calculate_score(user) < calculate_score(comp) and calculate_score(comp) >21:
        return "win"
    elif calculate_score(user) == calculate_score(comp):
        return "draw"
    return "lose"


def dealerplay(list):
    while calculate_score(list) < 17 and calculate_score(list) < 22:
        list.append(deal_card())



users =[11,10]
compu = [10,9]

print(isWin(users, compu))


def play_game():
    print(logoBJ)
    user_cards = []
    computer_cards = [1,4] 
    for init in range(0, 2):
        user_cards.append(deal_card())
        # computer_cards.append(deal_card())
    print("Dealer card is: " + str(computer_cards[0]))
    print("Your Cards: " + str(user_cards) +
          " Total cards: " + str(calculate_score(user_cards)))
    gameover = isgameover(user_cards, computer_cards)
    while not gameover:
        drawnext = input("do you want to draw another card ? y/n: ")
        if drawnext == "n":
            gameover = True
        else:
            user_cards.append(deal_card())
            print("Dealer card is: " + str(computer_cards[0]) )
            print("Your Cards: " + str(user_cards) + " Total cards: "+ str(calculate_score(user_cards)))
            if calculate_score(user_cards) > 21:
                gameover= True
  
    dealerplay(computer_cards)

    if isWin(user_cards, computer_cards) == "win":
        print("Your card " + " Total cards: " +
              str(calculate_score(user_cards)))
        print(user_cards)
        print("Dealer Card" + " Total cards: " +
              str(calculate_score(computer_cards)))
        print(computer_cards)
        print("User Win")
    elif isWin(user_cards, computer_cards) == "lose":
        print("Your card " + " Total cards: " +
              str(calculate_score(user_cards)))
        print(user_cards)
        print("Dealer Card" + " Total cards: " +
              str(calculate_score(computer_cards)))
        print(computer_cards)
        print("User Lose")
    elif isWin(user_cards, computer_cards) == "draw":
        print("Your card " + " Total cards: " +
              str(calculate_score(user_cards)))
        print(user_cards)
        print("Dealer Card" + " Total cards: " +
              str(calculate_score(computer_cards)))
        print(computer_cards)
        print("Draw")
#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.




while input("Do you want to play a game of Blackjack? Type 'y' or 'n':") == 'y':
    os.system('clear')
    play_game()
