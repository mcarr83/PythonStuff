'''Name: Michael Carr
Date: 7/31/2019
Description: Tic-Tac-Toe to be played with another human or by yourself if you have split personalities. Just an
             exercise to see if I could make a simple game with python. No known bugs as of now but it could change.'''

#Only needed to import 2 libraries for small things
import time
import sys

def userInput():
    '''
    Function used ask for an input and then determine if the input is valid, an integer. Doesn't take any args in
    but returns one if it is valid.
    '''

    choice = 0
    while True:
        try:
            choice = int(input('Pick any open square numbers 1 through 9: '))

        except:
            print('Only numbers are allowed, try again')
            continue
        finally:
            return choice


def moveValid(move, mlist):
    '''
    Function is used to check if a number is in a list of moves already made
    '''

    #Users input
    move = int(move)
    for i in mlist:
        #Had to convert over to an int to compare it to move that was an arg coming in
        i = int(i)
        if i == move:
            return False
    #Checks to make sure the number is between 1 and 9
    if move < 1 or move > 9:
        return False
    return True

def makeMove(gameboard, moveNumber, x):
    '''
    This function determines if the player is X or O depending on if the turn is odd or even. Next takes the gameboard
    list and modifies the gameboard lists inside a list to establish a visual representation of where the player went.

    Game Board Layout using x as var:
    7 | 8 | 9
    ---------
    4 | 5 | 6
    ---------
    1 | 2 | 3
    '''

    person = ''
    x = int(x)

    #Depending on the moveNumber, determines if the move is X or O. X for even, O for odd
    if moveNumber%2 == 0:
        person = 'X'

    else:
        person = 'O'

    #Modifies the game board and returns it
    if x == 1:
        gameboard[4][0] = person
        return gameboard

    elif x == 2:
        gameboard[4][2] = person
        return gameboard

    elif x == 3:
        gameboard[4][4] = person
        return gameboard

    elif x == 4:
        gameboard[2][0] = person
        return gameboard

    elif x == 5:
        gameboard[2][2] = person
        return gameboard

    elif x == 6:
        gameboard[2][4] = person
        return gameboard

    elif x == 7:
        gameboard[0][0] = person
        return gameboard

    elif x == 8:
        gameboard[0][2] = person
        return gameboard

    elif x == 9:
        gameboard[0][4] = person
        return gameboard




def print_Board(gameboard):

    '''
    Print the game board
    '''

    for i in range(len(gameboard)):
        for j in range(len(gameboard[i])):
            print(gameboard[i][j], end=' ')
        print()
    print()

def intro():

    '''
    Intro to game displayed before game startes
    '''

    print('Welcome to Tic-Tac-Toe')
    print('First person with a 3 in a row horizontally, vertically, ')
    print('or diagonally wins.')
    gameboard = [['7', '|', '8', '|', '9'], ['---------'], ['4', '|', '5', '|', '6'], ['---------'],
                 ['1', '|', '2', '|', '3']]
    print('Here is the board sections by the numbers:')
    print_Board(gameboard)
    time.sleep(5)
    print('X goes first')
    time.sleep(1)
    print('Ready,')
    time.sleep(1)
    print('GO!!!')
    time.sleep(1)

def Winner(board, moveNumber):

    '''
    This function determines if a player is a winner by checking the board in all directions for a 3 in a row match
    '''

    #Assigns person based on even or odd turn
    person = ''
    if moveNumber%2 == 0:
        person = 'X'

    else:
        person = 'O'

    #Downward checks (probably a better way of doing this)
    if board[0][0] == person and board[2][0] == person and board[4][0] == person:
        return True

    elif board[0][2] == person and board[2][2] == person and board[4][2] == person:
        return True

    elif board[0][4] == person and board[2][4] == person and board[4][4] == person:
        return True

    #Left to right checks
    elif board[0][0] == person and board[0][2] == person and board[0][4] == person:
        return True

    elif board[2][0] == person and board[2][2] == person and board[2][4] == person:
        return True

    elif board[4][0] == person and board[4][2] == person and board[4][4] == person:
        return True

    #Checks diagonal
    elif board[0][0] == person and board[2][2] == person and board[4][4] == person:
        return True

    elif board[0][4] == person and board[2][2] == person and board[4][0] == person:
        return True

    #Else nothing is found, return False
    else:
        return False

def tie(mlist):
    '''
    This function is used to check if there is a tie of not
    '''

    #If the move list has 9 elements in it the game has no more move and the game is then tied
    if len(mlist) == 9:
        return True

def main():
    '''
    Heart and soul, controller of the game.
    '''

    intro()

    #moveNumber used manly to figure out what to print on screen. Even moveNumber used to indicate
    #an X move and odd to indicate an O move
    moveNumber = 0

    #used to store the places a roll has been
    move_list = []

    #game board list used to be modified and passed to functions
    gameboard = [[' ', '|', ' ', '|', ' '], ['---------'], [' ', '|', ' ', '|', ' '], ['---------'], [' ', '|', ' ', '|', ' ']]
    print_Board(gameboard)

    Valid = True
    while Valid == True:
        #Function call with return of user input
        x = userInput()

        #checks to see if the move can be made
        if moveValid(x, move_list) == True:

            #If True:
            #Add move to move_list
            move_list.append(x)

            #Modify game board list of lists
            gameboard = makeMove(gameboard, moveNumber, x)
            print_Board(gameboard)

            #Checks to see if the move made the user a winner
            if Winner(gameboard, moveNumber) == True:
                # Assigns person based on even or odd turn
                person = ''
                if moveNumber % 2 == 0:
                    person = 'X'

                else:
                    person = 'O'

                #If a winner print:
                print(person, 'you won!!!!')
                print('Congrats')

                #Exit
                sys.exit()

            #If there is a tie:
            if tie(move_list) == True:
                print('Tie!!! No one won.')
                sys.exit()

            #else increment moveNumber
            moveNumber += 1

        else:
            #If move is not allowed, ask for another move.
            print('That move is not allowed')
            Valid == True

main()