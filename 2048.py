#Oni H
#implements game, accepts user input, displays game board

import logic

#main game loop
if __name__ == "__main__":
    board = logic.startGame()

#while the game is not over(false), keep running game loop
while(True):
    userInput = input("Press the command : ")

    #if user pressed W go up-------------------------------------
    if(userInput == 'W' or userInput == 'w'):
        board, changed = logic.moveUp(board)
        status = logic.getCurrentState(board)
        print(status)

        if(status == 'GAME NOT OVER'):
            logic.addsNewTwo(board)
        else:
            break

    #if user pressed S go down-------------------------------------
    elif(userInput == 'S' or userInput == 's'):
        board, changed = logic.moveDown(board)
        status = logic.getCurrentState(board)
        print(status)
        
        if(status == 'GAME NOT OVER'):
            logic.addsNewTwo(board)
        else:
            break

    #if user pressed A go left-------------------------------------
    elif(userInput == 'A' or userInput == 'a'):
            board, changed = logic.moveLeft(board)
            status = logic.getCurrentState(board)
            print(status)
            
            if(status == 'GAME NOT OVER'):
                logic.addsNewTwo(board)
            else:
                break

    #if user pressed D go right-------------------------------------
    elif(userInput == 'D' or userInput == 'd'):
            board, changed = logic.moveRight(board)
            status = logic.getCurrentState(board)
            print(status)
            
            if(status == 'GAME NOT OVER'):
                logic.addsNewTwo(board)
            else:
                break

    #if user pressed q end game
    elif(userInput == 'Q' or userInput == 'q'):
        print("Game ended. GOODBYE!")
        break

    #if user pressed any other key-------------------------------------
    else:
        print("Invalid command. Please try again.")

    print(board)