"""
The constants module holds global variables for the cell game
"""
from arcade import key
SCREEN_TITLE = "Conway's Game of Life"

# I recommend having the ratio between screen and board be 1:1 so you get squares.
# It functions just fine either way but it will look weird
# If your screen is small, I recommend making the screen width and screen height smaller,
#   especially if your display settings are set to show higher than 100% scale
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
BOARD_WIDTH = 35
BOARD_HEIGHT = 35

ESCAPE_KEY = key.ESCAPE

# If it gets 1 from this random range, it creates a cell. Larger ranges mean less cells
RANDOM_CELL_CREATION_RANGE = (0, 5)

# frame time in seconds
FRAME_TIME = 0.1