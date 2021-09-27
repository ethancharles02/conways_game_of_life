"""
The Game Creation View module creates a view for placing cells for Conway's Game of Life
"""

import arcade
from data import constants
from data.game_view import GameView
from data.board import Board
from random import randint

class GameCreationView(arcade.View):
    """
    The Game Creation View is used to create the initial setup for Conway's Game of Life
    """
    def __init__(self, window: arcade.Window):
        """
        The class constructor
        """
        super().__init__(window=window)

        self.window = window

        self.board = Board(constants.BOARD_WIDTH, constants.BOARD_HEIGHT)

        self.board_dx = constants.SCREEN_WIDTH / self.board.width
        self.board_dy = constants.SCREEN_HEIGHT / self.board.height
        self.text_shown = True

    def on_show(self):
        """
        Designs the grid for cell placement
        """
        self.board.reset()

    def on_draw(self):
        """
        Displays the grid for cell placement or the hint text
        """
        arcade.start_render()

        if not self.text_shown:
            for cell in self.board.initial_cells:
                arcade.draw_lrtb_rectangle_filled(cell[0] * self.board_dx, cell[0] * self.board_dx + self.board_dx, cell[1] * self.board_dy + self.board_dy, cell[1] * self.board_dy, arcade.color.GREEN_YELLOW)

            for x in range(constants.BOARD_WIDTH + 1):
                x_pos = x * self.board_dx
                arcade.draw_lrtb_rectangle_filled(x_pos - 0.5, x_pos + 0.5, constants.SCREEN_HEIGHT - 1, 0, arcade.color.WHITE)
            for y in range(constants.BOARD_HEIGHT + 1):
                y_pos = y * self.board_dy
                arcade.draw_lrtb_rectangle_filled(0, constants.SCREEN_WIDTH - 1, y_pos + 0.5, y_pos - 0.5, arcade.color.WHITE)
        
        else:
            arcade.draw_text('Press "R" to randomize the cell creation\nPress "ESC" to exit or return to the creation menu if in game\nPress "Enter" to start\nPress "X" to clear all cells\nPress "H" to hide/show this text and show/hide grid for cell placement', 0, 0, arcade.color.WHITE, bold=True, font_size=15)

    def on_key_press(self, key, modifiers):
        """
        Called whenever a key is pressed

        Args:
            key: Library used in the constant module
        """
        if key == constants.ESCAPE_KEY:
            self.window.close()
        
        if key == arcade.key.ENTER:
            self.window.show_view(GameView(self.window, self, self.board))

        if key == arcade.key.X:
            self.board.clear(True)
        
        if key == arcade.key.R:
            self.board.clear(True)
            for x in range(self.board.width):
                for y in range(self.board.height):
                    if randint(*constants.RANDOM_CELL_CREATION_RANGE) == 1:
                        self.board.add_cell((x, y), True)
        
        if key == arcade.key.H:
            self.text_shown = not self.text_shown

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """
        Determines the cell placement
        
        Args:
            _x: x axis position of the mouse press
            _y: y axis position of the mouse press
            _button: Conditions created from button press
        """
        
        if not self.text_shown:
            board_x = int(_x // self.board_dx)
            board_y = int(_y // self.board_dy)

            self.board.flip_cell((board_x, board_y))