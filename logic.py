#Oni H
#implements game logic, tile movement, merging, random tile generation, game state checks

import random #for generating random tiles


def startGame():
    # initialize the game board 4x4
    global score
    score = 0

    board = []
    for i in range(4):
        board.append([0] * 4)

    print("Starting the game...")

    addsNewTwo(board) #place the first tile
    return board

def findEmptyCell(board):
    #finds first empty (0) cell in the board
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return (i, j)
    return None, None #if no empty cell is found

def addsNewTwo(board):
    #adds a new 2 to a random empty cell in grid

    if all(all(cell != 0 for cell in row) for row in board): #checks if the board is full
        return

    tries = 0
    while tries < 30:
        r = random.randint(0, 3) #random row
        c = random.randint(0, 3) #random column
        if board[r][c] == 0: #if the cell is empty
            board[r][c] = 2 #place a new 2 in the empty cell
            return
        tries += 1 #increment num of attempts

    r, c = findEmptyCell(board)
    if r is not None and c is not None:
        board[r][c] = 2 #place a new 2 in the empty cell

#function that asses the current state of game 
def getCurrentState(board):

    #check if game has been won by looking for a 2048 tile
    for i in range(4):
        for j in range(4):
            if(board[i][j] == 2048):
                return 'WON'

    #check if there are any empty cells, if so then game not over
    for i in range(4):
        for j in range(4):
            if(board[i][j] == 0):
                return 'GAME NOT OVER'

    #checks if there are possible moves left 
    for i in range(3):
        for j in range(3):
            if(board[i][j] == board[i + 1][j] or board[i][j] == board[i][j + 1]):
                return 'GAME NOT OVER'

    #checks last row for any horizontal moves
    for j in range(3):
        if(board[3][j] == board[3][j + 1]):
                return 'GAME NOT OVER'

    #checks last column for any vertical moves
    for i in range(3):
        if(board[i][3] == board[i + 1][3]):
                return 'GAME NOT OVER'

    #if no more moves are possible then game is lost
    return 'LOST'

def compress(board):
    #compresses the tiles in the board by moving all non-zero tiles to the left

    changed = False
    newBoard = []
    for i in range(4):
        newBoard.append([0] * 4)

    for i in range(4):
        pos = 0
        for j in range(4):
            if(board[i][j] != 0):
                newBoard[i][pos] = board[i][j]

                if(j != pos):
                    changed = True
                pos += 1
    return newBoard, changed

def merge(board):
    #merges tiles in board by combining tiles equal to each other

    global score
    changed = False

    for i in range(4):
        for j in range(3):
            if(board[i][j] == board[i][j + 1] and board[i][j] != 0): #if two adjacent tiles are equal and non-zero
                board[i][j] = board[i][j] * 2 #merge the two tiles into one with double the value
                score += board[i][j] #update score by adding value of merged tiles
                board[i][j + 1] = 0 #clear the second tile after merging
                changed = True

    return board, changed


def reverseBoard(board):
    #reverses order of tiles in each row of board
    newBoard = []
    for i in range(4):
        newBoard.append([])
        for j in range(4):
            newBoard[i].append(board[i][3 - j]) #reverse the order of tiles in the row
    return newBoard

def transposeBoard(board):
    #swaps rows and columns of the board
    newBoard = []
    for i in range(4):
        newBoard.append([])
        for j in range(4):
            newBoard[i].append(board[j][i]) #swaps rows and columns
    return newBoard

#NOW TIME FOR MOVING---------------------------------------------------------

def moveLeft(grid):
    #moves all tiles to the left
    newGrid, changed1 = compress(grid) #compress grid by moving all non 0s to left
    newGrid, changed2 = merge(newGrid) #merge tiles in compressed grid

    changed = changed1 or changed2

    newGrid, temp = compress(newGrid) #compress grid again after merging

    #binding left key for left arrow key to move tiles left


    return newGrid, changed #return the new grid and any changes occurred


def moveRight(grid):
    #moves all tiles to right
    newGrid = reverseBoard(grid) #reverse the grid to move tiles to the right
    newGrid, changed = moveLeft(newGrid) #move tiles to the left in the reversed grid

    newGrid = reverseBoard(newGrid)
    return newGrid, changed

def moveUp(grid):
    #moves all tiles up
    newGrid = transposeBoard(grid) #transpose grid to move tiles up
    newGrid, changed = moveLeft(newGrid) #move tiles to left in transposed grid
    newGrid = transposeBoard(newGrid) #transpose grid back to original orientation

    return newGrid, changed

def moveDown(grid):
    #moves all the tiles down
    newGrid = transposeBoard(grid) #transpose grid to move tiles down
    newGrid, changed = moveRight(newGrid) #move tiles to the right in transposed grid
    
    newGrid = transposeBoard(newGrid) #transpose grid back to original orientation
    return newGrid, changed

