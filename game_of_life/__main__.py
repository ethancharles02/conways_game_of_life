"""
The entry point to run the cell game
"""

# Possible additions:
#   add mouse click and drag to create cells
#   save cell configurations as files
#   import cell configs
#   update constants in menu
#   pause mechanic
#   adjust size of the board for cells leaving the screen space to make it an infinite size board

import arcade
import os

file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

from data import constants
from data.game_creation_view import GameCreationView
# from data.game_view import GameView

def main():
    """ Main method """
    window = arcade.Window(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
    game_creation_view = GameCreationView(window)
    window.show_view(game_creation_view)
    # game_view = GameView(window)
    # window.show_view(game_view)
    arcade.run()

if __name__ == "__main__":
    main()