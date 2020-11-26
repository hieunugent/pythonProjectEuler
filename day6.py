#Step 1
import random
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chooseword = random.choice(word_list)
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
display=[]
word_length = len(chooseword)
for _ in range(word_length):
    display += "_"
def game(guess):
    count = 0
    for pos in range(word_length):
        letter = chooseword[pos]
        if letter == guess:
            display[pos] = letter
          
  

gameover= False
while(not gameover):
    guess = input(
        "guess a letter and assign their answer to a variable called guess. Make guess lowercase.").lower()
    game(guess)
    print(display)
    if "_" not in display:
        print("You are WIn")
        gameover=True






