# 2048 Game

A desktop version of the classic 2048 puzzle game, built with Python and tkinter.



## Features 
- Play with arrow keys
- Live score counter
- New Game button
- Win and Game-over detection
- Press Q to quit

## How to Play
1. Install Python 3
2. Download or clone this repo
3. Run:

'''
python gui.py
'''

No extra libraries needed, since tkinter comes with Python.

## How it works
The game logic (`logic.py`) is separate from the display (`gui.py`).
Every move is built from one "slide left" operation. Right, up and down
are done by reversing or transposing the board, sliding left, then
flipping it back.

## What I learned
- Separating game logic from the GUI
- Working with 2D lists
- Handling keyboard events in tkinter

## Future improvements
- Best score that saves between sessions
- Tile slide animations
- Undo button

## Credits
Game logic adapted from the GeeksforGeeks 2048 tutorial. The tkinter
GUI, scoring, and New Game features were added by me.
