# Overview

### Conway's Game of Life
Conway's Game of Life is setup on a grid of infinite cells, certain cells on the grid are alive
while others are dead. 
For this version, the grid is finite instead of infinite
Everything is decided at the beginning based on 3 rules:
* Any live cell that has 2-3 nearby live cells (within one cell radius) will survive.
* A dead cell with 3 nearby live cells will become a live cell.
* Any other cell dies.

# Development Environment
VS Code was used to create this game/program

### Dependancies
* Python 3.9.4
* Arcade 2.5.7 module

# Useful Websites
* [The Python Arcade Library](https://api.arcade.academy/en/latest/)
* [W3 Schools Python Documentation](https://www.w3schools.com/python/default.asp)
* [Original Python Documentation](https://docs.python.org/3/)
* [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)

# Future Work
Here are some of the things I am interested in adding later
* Dragging the mouse to create cells
* Saving cell configurations as files
* Importing cell configurations
* Changing settings in the menu
* Pausing the game
* Adjusting the size of the board for cells outside of the screen space (they get killed right now if they are off screen)





















<!-- Old version of the readme 

# Conway's Game of Life
Conway's Game of Life is setup on a grid of infinite cells, certain cells on the grid are alive
while others are dead. Everything is decided at the beginning based on 3 rules:
* Any live cell that has 2-3 nearby (within one cell radius) live cells will survive.
* A dead cell with 3 nearby live cells will become a live cell.
* Any other cell dies.

## Getting Started
---
Make sure you have Python 3.8.0 or newer, arcade 2.5.7 or newer
and running on your machine. You can install arcade by opening a terminal 
and running the following command.
```
python3 -m pip install arcade
```
After you've installed the required libraries, open a terminal and browse to the 
project's root folder. Start the program by running either of these commands (depending 
on your python installation)
```
python3 game_of_life
python game_of_life
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE 
and open the project folder. Select the main module inside the lightbike folder and 
click the "run" icon.

## Project Structure
---
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- game_of_life        (src code files - game_of_life)
  +-- data              (program data files)
    +-- __init__.py
    +-- board.py
    +-- constants.py
    +-- game_creation_view.py
    +-- game_view.py
  +-- __init__.py       (python package file)
  +-- __main__.py       (entry point for program)
+-- LICENSE             (license file)
+-- README.md           (general info)
```

## Required Technologies
---
* Python 3.8.0 or later
* arcade 2.5.7 or later

## Author
---
* Ethan Charles: ethan.charles02@gmail.com -->