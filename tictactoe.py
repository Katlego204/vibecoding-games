#I am going to create a tictactoe game to try to grasp how to make games
#I am watching a tutorial from "Code Coach"
#https://youtu.be/dK6gJw4-NCo?si=8uNzCQ41HDJjPIcl

'''Before starting we need to think about what features do I need to make this functional
-> printing the game board
-> take player input
-> check for win or tie
-> switch the player
-> check for win or tie again'''

#_________IMPORTS_________#
import random


#_________________________GLOBAL VARIABLES__________________________#
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
currentPlayer = "X" #This means the first person to play will always be "X"
winner = None
gameRunning = True


#______PRINTING THE GAME BOARD______#
def printBoard(board):
    
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])
#printBoard(board=board) #here we are calling the function while passing the global variable "board" as a argument


#__________PLAYER INPUT__________#
def playerInput(board):
    
    inp = int(input("Enter a number 1-9: "))
    if inp>=1 and inp<=9 and board[inp-1]=="-": #we use the board[inp-1]=="-" to check whether the space we are indexing to is free
        board[inp-1] = currentPlayer
    else:
        print("Oops, player is already in that spot!")
        exit()


#______CHECK FOR WIN OR TIE______#
#Here we are going to check for every WIN possibility and TIE possibility
def checkHorizontal(board):
    global winner #the global variable basically means we are altering not just the value of the variable inside the function but the GLOBAL variable,(the variable as a whole on every function)
    if board[0]==board[1]==board[2] and board[1]!="-": #Here we check if the the first horizontal row has the same charecter and is not "-"
        winner = board[0]
        return True #returning true helps us when we are using the functions in a if statement and we can say "if checkHorizontal==True" break out of the gameloop or summ'
    elif board[3]==board[4]==board[5] and board[3]!="-":
        winner = board[3]
        return True
    elif board[6]==board[7]==board[8] and board[6]!="-":
        winner = board[6]
        return True
    # else:
    #     print("Oops, ran into a problem in the checkHorizontal function")
    
def checkRow(board):
    global winner #by initialising it here, we say "we are going to alter this variable as a whole. not just in this function"
    
    if board[0]==board[3]==board[6] and board[0] != "-":
        winner = board[0]
        return True
    
    elif board[1]==board[4]==board[7] and board[1] != "-":
        winner = board[1]
        return True
    
    elif board[2]==board[5]==board[8] and board[2] != "-":
        winner = board[2]
        return True
    # else:
    #     print("Oops, there is a problem at the checkRow function")
        
def checkDiag(board):
    global winner
    
    if board[0]==board[4]==board[8] and board[0]!="-":
        winner  = board[0]
        return True
    
    elif board[2]==board[4]==board[6] and board!="-":
        winner = board[2]
        return True    
    
    # else:
    #     print("Oops there is a problem at the checkRow function")

def checkTie(board):
    global gameRunning
    
    if "-" not in board:
        printBoard(board=board)
        print("It is a tie!")
        gameRunning  = False


#________SWITCH THE PLAYER________#
def switchPlayer():
    global currentPlayer
    
    if currentPlayer=="X":
        currentPlayer="O"
    else:
        currentPlayer = "X"


#_________CHECK FOR WIN__________#
def checkWin():
    global gameRunning
    
    if checkDiag(board=board) or checkHorizontal(board=board) or checkRow(board=board):
        print(f"The winner is {winner}")
        if winner!="-":
            gameRunning = False


#__________VS COMPUTER__________#
def computer(board):
    
    while currentPlayer=="O":
        position = random.randint(0,8)
        if board[position] == "-":
            board[position]= "O"
            switchPlayer()
            
            
#___________GAME LOOP___________#
while gameRunning:
    printBoard(board=board)
    playerInput(board=board)
    checkWin()
    checkTie(board=board)
    switchPlayer()
    checkWin()
    checkTie(board=board)
printBoard(board)
        