#Oni H
#this will implement the actual screen so user can see what is happening

from tkinter import *
import logic

#set colors for each number
COLORS = {0: "#f0e9da",
          2: "#eee4da",
          4: "#ede0c8",
          8: "#f2b179",
          16: "#f59563",
          32: "#f67c5f",
          64: "#f65e3b",
          128: "#edcf72",
          256: "#edcc61",
          512: "#edc850",
          1024: "#edc53f",
          2048: "#edc22e"
          }


def drawGrid(): 
    #draws the 4x4 grid for the game from current board

    for i in range(4):
        for j in range(4):
            value = board[i][j] #get the value of the current cell from the board
            cells[i][j].config(text = str(value) 
                               if value != 0 else "",
                               bg = COLORS.get(value, "#bbada0")) #set background color for the cell
    scoreLabel.config(text = "Score: " + str(logic.score))

def newGame():
    #resets all for new game button
    global board, gameOver

    board = logic.startGame() #rests score to 0
    gameOver = False
    statusLabel.config(text = "Lets Play 2048!")
    drawGrid()


def keyPressed(event):
    #key presses for moving tiles in the game
    
    global board, gameOver #declares board and gameOver as global variables

    #if they wanna quit
    if event.keysym in ("q", "Q"):
        statusLabel.config(text = "Quitting...Goodbye!", bg = "#df691a", fg = "white")
        gameOver = True
        window.after(1500, window.destroy)
        return

    if gameOver: #if game is over (true) do not return any keys
        return 

    #key presses to coressponding moves
    moves = {"Up": logic.moveUp,
             "Down": logic.moveDown,
             "Left": logic.moveLeft,
             "Right": logic.moveRight,}
    

    #checks if key pressed is a valid move
    if event.keysym not in moves:
        return

    #performs the move based on the key pressed
    board, changed = moves[event.keysym](board)
    if changed:
        logic.addsNewTwo(board)
    drawGrid()

    #updates the status label based on the current state of the game
    status = logic.getCurrentState(board)
    if status == "WON":
        statusLabel.config(text = "You Won!")
        gameOver = True
    elif status == "LOST":
        statusLabel.config(text = "Game Over!")
        gameOver = True

#creates game window
window = Tk()
window.title("2048 Game")
window.geometry("800x600")
window.resizable(True, True)
window.config(background = "#fff4db")

#top bar with score and new game button
topFrame = Frame(window, bg = "#dfb11a")
topFrame.pack(pady = 10)

#score label
scoreLabel = Label(topFrame, text = "Score: 0", font = ("Helvetica", 20, "bold"), bg = "#dfb11a", fg = "white")
scoreLabel.pack(side = LEFT, padx = 20)

#new game button
newGameButton = Button(topFrame, text = "New Game", font = ("Helvetica", 20, "bold"), bg = "#dfb11a", fg = "white", command = newGame, takefocus = 0)
newGameButton.pack(side = RIGHT, padx = 0)

#creates label for game status
statusLabel = Label(window, text = "Lets Play 2048!", font = ("Helvetica", 20, "bold"), bg = "#dfb11a", fg = "white")
statusLabel.pack(pady=20)

#makes board frame
boardFrame = Frame(window, bg = "#5c5849")
boardFrame.pack(padx = 10, pady = 10)

#grid of cells for game board
cells = []
for i in range(4):
    row = []
    for j in range(4):
        label = Label(boardFrame, text = "", width = 5, height = 2,
                      font = ("Helvetica", 30, "bold"))
        label.grid(row = i, column = j, padx = 5, pady = 5)
        row.append(label)
    cells.append(row)

#initializes game board, draws it on screen
board = logic.startGame()
gameOver = False
drawGrid()

#binds key presses to the keyPressed function
window.bind("<Up>", keyPressed)
window.bind("<Down>", keyPressed)
window.bind("<Left>", keyPressed)
window.bind("<Right>", keyPressed)
window.bind("<q>", keyPressed)
window.bind("<Q>", keyPressed)


#starts the game loop
window.mainloop()






