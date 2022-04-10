import random


board = ["."] * 9
def resetboard(board):
    for i in range(9):
        board[i] = "."
def printBoard(board):
    for i in range(0, 9, 3):
        print(board[i] + "|" + board[i+1] + "|" + board[i+2])
        

def xiswinner(board):
    if board[0] == board[1] == board[2] == "x" or board[0] == board[3] == board[6] == "x" or board[0] == board[4] == board[8] == "x" or board[1] == board[4] == board[7] == "x" or board[2] == board[5] == board[8] == "x" or board[2] == board[4] == board[6] == "x" or board[3] == board[4] == board[5] == "x" or board[6] == board[7] == board[8] == "x":
        return True
def oiswinner(board):
    if board[0] == board[1] == board[2] == "o" or board[0] == board[3] == board[6] == "o" or board[0] == board[4] == board[8] == "o" or board[1] == board[4] == board[7] == "o" or board[2] == board[5] == board[8] == "o" or board[2] == board[4] == board[6] == "o" or board[3] == board[4] == board[5] == "o" or board[6] == board[7] == board[8] == "o":
        return True
def isfull(board):
    if "." not in board:
        return True
def inputPlayerLetter():
    letter = ""
    while not (letter == "x" or letter == "o"):
        letter = input("Do you want to be x or o? ").lower()
    if letter == "x":
        return ["x", "o"]
    else:
        return ["o", "x"]
def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return "computer"
    else:
        return "player"
def playAgain():
    
    return input("Do you want to play again? (yes or no) ").lower().startswith("y")
def makeMove(board, letter, move):
    board[move] = letter
def isSpaceFree(board, move):   
    if board[move] == ".":
        return True
    else:
        return False

while True:
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print("The " + turn + " will go first.")
    gameIsPlaying = True
    resetboard(board)
    while gameIsPlaying:
        if turn == "player":
            move = int(input("Please select a number between 1 and 9: "))
            if isSpaceFree(board, move-1):
                makeMove(board, playerLetter, move-1)
            else:
                print("Sorry, this space is occupied.")
            if xiswinner(board):
                print("X wins!")
                gameIsPlaying = False
            else:
                if isfull(board):
                    print("The game is a tie!")
                    break
                else:
                    turn = "computer"
        
        else:
            print("The computer is thinking...")
            move = random.randint(0, 8)
            if isSpaceFree(board, move):
                makeMove(board, computerLetter, move)
            else:
                move = random.randint(0, 8)
            if oiswinner(board):
                print("O wins!")
                gameIsPlaying = False
            else:
                if isfull(board):
                    print("The game is a tie!")
                    break
                else:
                    turn = "player"
        printBoard(board)
    if not playAgain():
        break

