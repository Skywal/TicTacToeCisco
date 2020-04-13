#
# -- Cisco python course project --
#   Tic-tac-toe game
#
from random import randrange

# values in the cells
board = [
    [1, 2, 3],
    [4, "X", 6],
    [7, 8, 9]
    ] 

# free cels
free_cells = []

circke_player = "O"
cross_player = "X"

width = 25 # number of columns in console board
height = 13 # number of rows in console board


def PlayerInput():
    player_input = 0
    
    while True:
        player_input = input("Enter your move: ")
        
        if player_input: 
            try:
                player_input = int(player_input)

                if player_input > 0 and player_input < 10:
                    return player_input
                else:
                    print("It must be a digit between 0 and 10!")
            except ValueError:
                print("It must be a digit!")
        else:
            print("Pleace enter your move!")

def MakeMove(board, move, player):
    for i in range(len(free_cells)):
        row, col = free_cells[i]

        # if there is a free cell chosen by the player
        if board[row][col] == move:
            
            board[row][col] = player

            return True  # don't continue, got into free cell

    return False  # continue to input while get into free cell


def DisplayBoard(board):
    #
    # the function accepts one parameter containing the board's current status
    # and prints it out to the console
    #

    row_b_count = 0  # current board row to display
    
    for row in range(height):
        col_b_count = 0  # current board column to display

        for col in range(width):
            
            if row % 4 == 0:
                if col % 8 == 0:
                    print("+", end="")    
                else:
                    print("-", end="")
            else:
                if col % 8 == 0:
                    print("|", end="")
                elif col % 4 == 0 and row % 2 == 0: # вивід циферки
                    print(board[row_b_count][col_b_count], end="")

                    col_b_count += 1 # move in board columns forward
                else:
                    print(" ", end="")
        
        # move in board rows forward at each cell end
        if row != 0 and row % 4 == 0 and row != (height-1):
            row_b_count += 1 

        print()

def EnterMove(board):
    #
    # the function accepts the board current status, asks the user about their move, 
    # checks the input and updates the board according to the user's decision
    #
    
    if len(free_cells) > 0:
        while True:
            _input = PlayerInput()
            # do we get into free cell
            isFree = MakeMove(board, _input, circke_player)
            
            if isFree:
                break
    
    DisplayBoard(board)
        
def MakeListOfFreeFields(board):
    #
    # the function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers
    #
     
    free_cells = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            if type(board[row][col]) == int:
                tup = row, col,
                free_cells.append(tup)
    return free_cells

def VictoryFor(board, sign):
    #
    # the function analyzes the board status in order to check if 
    # the player using 'O's or 'X's has won the game
    #
    
    # check rows for win
    for row in board:
        if row.count(sign) == 3:
            return True

    # check columns for win
    for col in range(len(board[0])):
        lst = []
        for j in range(len(board)):
            lst.append(board[j][col])

        if lst.count(sign) == 3:
            return True
    
    lst_left = []  # diagonal from left to right
    lst_right = []  # diagonal from right to left
    for i in range(len(board)):
        lst_left.append(board[i][i])
        lst_right.append(board[i][2-i])

    if lst_left.count(sign) == 3:
        return True
    if lst_right.count(sign) == 3:
        return True
    
    return False

def DrawMove(board):
    #
    # the function draws the computer's move and updates the board
    #
    if len(free_cells) > 0:
        while True:
            _input = randrange(1, 10)
            # do AI gets into free cell
            isFree = MakeMove(board, _input, cross_player)

            if isFree:
                break

    DisplayBoard(board)

if __name__ == "__main__":
    DisplayBoard(board)
    while True:
        
        isVictory = VictoryFor(board, circke_player)
        if isVictory:
            print("You win!! Congrats!!")
            break
        
        isVictory = VictoryFor(board, cross_player)
        if isVictory:
            print("You lost!! Fail!!")
            break

        free_cells = MakeListOfFreeFields(board)
        
        EnterMove(board)

        DrawMove(board)
