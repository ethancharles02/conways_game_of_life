"""
The GameView module combines all of the modules to create the 
frame of the game, deciding where everything goes. It comes 
from arcade.View and overrides methods to draw the game, update it, etc.
"""

import arcade
import time
from random import randint
from data import constants
from data.board import Board
# from data.game_creation_view import GameCreationView


class GameView(arcade.View):
    """
    The game is in charge of bringing everything together and putting it into the arcade window        
    """

    def __init__(self, window: arcade.Window, game_creation_view = None, board: Board = None):
        """
        The class constructor
        """
        super().__init__(window=window)

        self.game_creation_view = game_creation_view

        self.board = board

    def on_show(self):
        """
        Set up the cell board and initialize the variables.
        """
        if self.board == None:
            self.board = Board(constants.BOARD_WIDTH, constants.BOARD_HEIGHT)

            for x in range(self.board.width):
                for y in range(self.board.height):
                    if randint(*constants.RANDOM_CELL_CREATION_RANGE) == 1:
                        self.board.add_cell((x, y), True)

        self.board_dx = constants.SCREEN_WIDTH / self.board.width
        self.board_dy = constants.SCREEN_HEIGHT / self.board.height
        # arcade.set_background_color(constants.BACKGROUND_COLOR)

    def on_draw(self):
        """
        Render the screen.
        """

        arcade.start_render()

        for cell in self.board.cells:
            arcade.draw_lrtb_rectangle_filled(cell[0] * self.board_dx, cell[0] * self.board_dx + self.board_dx, cell[1] * self.board_dy + self.board_dy, cell[1] * self.board_dy, arcade.color.WHITE)

    def on_key_press(self, key, modifiers):
        """
        Called whenever a key is pressed
        """
        if key == constants.ESCAPE_KEY:
            if self.game_creation_view != None:
                self.window.show_view(self.game_creation_view)
            else:
                self.window.close()
            
        if key == arcade.key.R:
            self.board.clear(True)
            for x in range(self.board.width):
                for y in range(self.board.height):
                    if randint(*constants.RANDOM_CELL_CREATION_RANGE) == 1:
                        self.board.add_cell((x, y), True)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """
        Called whenever a mouse key is pressed
        """

        pass

    def on_update(self, delta_time):
        """
        Movement and game logic
        """
        time.sleep(constants.FRAME_TIME)

        self.board.update()
