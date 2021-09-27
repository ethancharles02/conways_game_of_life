"""
The Board class holds all information for the cells in the game
It also provides the service of updating itself based on the cells within it based on the game's rules
"""

class Board:
    """
    Board holds information for the cells in Conway's Game of Life

    and provides an update method for each frame of change
    
    Methods:
        __init__(): Assigns attributes, creates initial board based on arguments

        add_cell(): Appends a cell to a queue to be added to the board

        delete_cell(): Appends a cell to a queue to be deleted from the board

        flip_cell(): Flips a cell from dead to live or live to dead

        update(): Updates all contents of the board based on the rules

        clear(): Clears all cells from the board

        reset(): Resets the active board to its initial state

        __analyze_cells(): Performs most of the work for the update method
            Adds necessary cells to creation and deletion queues

        __clear_queues(): Removes all cells from the queues

        __get_nearby_cells(): Returns nearby cells relative to a cell

        __in_bounds(): Checks if a position is within the bounds of the board

        __append_cell(): Used by add_cell() in the event that the queue needs to be skipped

        __remove_cell(): Used by delete_cell() in the event that the queue needs to be skipped

    """
    def __init__(self, width:int, height:int):
        """
        Assigns attributes, creates initial board based on arguments

        Parameters:
            width (int): The width of the board

            height (int): The height of the board

        Attributes:
            width (int): Width of the board

            height (int): Height of the board

            cells (list): List of live cells by position
                ie. [(0, 0)] would indicate one live cell in the bottom left corner

            cell_board (list): Organized so that dead cells are false and live cells are true
                ie. a two by two board would look like [[True, False], [False, False]] with one live cell at (0, 0)

            __add_queue (list): The queue for adding cells. Each spot holds a tuple position, ie. (0, 0)

            __delete_queue (list): The queue for deleting cell. Each spot holds a tuple position, ie. (0, 0)
        """
        self.width = width
        self.height = height

        self.initial_cells = []
        self.initial_cell_board = [[False for y in range(self.height)] for x in range(self.width)]

        self.cells = []
        self.cell_board = [[False for y in range(self.height)] for x in range(self.width)]

        self.__add_queue = []
        self.__delete_queue = []

    def add_cell(self, position:tuple, skip_queue:bool = False):
        """
        Appends a cell to a queue to be added to the board

        Queue can also be skipped for immediate adding

        Queue will apply upon update()


        Parameters:
            position (tuple): The position to add the cell, (0, 0) is bottom left

            skip_queue (bool): Skip the queue to immediately add the cell to the board instead of waiting for update()
        """
        if not skip_queue:
            self.__add_queue.append(position)
        else:
            self.__append_cell(position, True)

    def delete_cell(self, position:tuple, skip_queue:bool = False):
        """
        Appends a cell to a queue to be deleted from the board

        Queue can be skipped for immediate deletion

        Queue applies upon update()

        Parameters:
            position (tuple): The position to delete the cell, (0, 0) is bottom left

            skip_queue (bool): Skip the queue to immediately delete the cell from the board instead of waiting for update()
        """
        if not skip_queue:
            self.__delete_queue.append(position)
        else:
            self.__remove_cell(position, True)
    
    def flip_cell(self, position:tuple):
        """
        Flips the state of a cell, dead to alive, alive to dead
        
        This is only used in the creation portion so there is no queue for it

        Parameters:
            position (tuple): position to flip the cell
        """
        if position in self.cells:
            self.__remove_cell(position, True)
        else:
            self.__append_cell(position, True)

    def update(self):
        """
        Updates all contents of the board based on the rules
        """
        for cell in self.__add_queue:
            self.__append_cell(cell)
        self.__add_queue.clear()

        for cell in self.__delete_queue:
            self.__remove_cell(cell)
        self.__delete_queue.clear()

        self.__analyze_cells()

    def clear(self, initial: bool = False):
        """
        Clears all cells from the board

        Parameters:
            initial (bool): If it is initial, it will clear both the active and inital board
        """
        self.cell_board = [[False for y in range(self.height)] for x in range(self.width)]
        self.cells.clear()
        self.__clear_queues()

        if initial:
            self.initial_cell_board = [[False for y in range(self.height)] for x in range(self.width)]
            self.initial_cells.clear()

    def reset(self):
        """
        Resets the active board to its initial state
        """
        self.clear()

        for cell in self.initial_cells:
            self.__append_cell(cell)

    def __analyze_cells(self):
        """
        Performs most of the work for the update method
        Adds necessary cells to creation and deletion queues
        """
        dead_cells = []
        for cell in self.cells:
            nearby_live_cells = 0
            for nearby_cell in self.__get_nearby_cells(cell):
                if self.cell_board[nearby_cell[0]][nearby_cell[1]]:
                    nearby_live_cells += 1
                else:
                    dead_cells.append(nearby_cell)

            if nearby_live_cells > 3 or nearby_live_cells < 2:
                self.delete_cell(cell)
        
        # print(dead_cells)
        while dead_cells:
            # print(dead_cells.count(dead_cells[0]))
            if dead_cells.count(dead_cells[0]) == 3:
                self.add_cell(dead_cells[0])

            temp_dead_cell = dead_cells[0]
            while temp_dead_cell in dead_cells:
                dead_cells.remove(temp_dead_cell)
            
            # print(dead_cells)
    
    def __clear_queues(self):
        """
        Removes all cells from the queues
        """
        self.__add_queue.clear()
        self.__delete_queue.clear()

    def __get_nearby_cells(self, position:tuple):
        """
        Returns nearby cells relative to a cell

        Parameters:
            position (tuple): The position to check and get nearby cells
        """
        nearby_cells = []

        # Starts at bottom left relative (-1, -1), goes counter-clockwise
        temp_position = (position[0] - 1, position[1] - 1)
        if self.__in_bounds(temp_position):
            nearby_cells.append(temp_position)
        
        temp_position = (position[0], position[1] - 1)
        if self.__in_bounds(temp_position):
            nearby_cells.append(temp_position)

        temp_position = (position[0] + 1, position[1] - 1)
        if self.__in_bounds(temp_position):
            nearby_cells.append(temp_position)
        
        temp_position = (position[0] + 1, position[1])
        if self.__in_bounds(temp_position):
            nearby_cells.append(temp_position)
        
        temp_position = (position[0] + 1, position[1] + 1)
        if self.__in_bounds(temp_position):
            nearby_cells.append(temp_position)
        
        temp_position = (position[0], position[1] + 1)
        if self.__in_bounds(temp_position):
            nearby_cells.append(temp_position)

        temp_position = (position[0] - 1, position[1] + 1)
        if self.__in_bounds(temp_position):
            nearby_cells.append(temp_position)
        
        temp_position = (position[0] - 1, position[1])
        if self.__in_bounds(temp_position):
            nearby_cells.append(temp_position)
        
        return nearby_cells

    def __in_bounds(self, position: tuple):
        """
        Checks if a position is within the bounds of the board

        Parameters:
            position (tuple): The position to check if in bounds
        """
        return position[0] >= 0 and position[0] < self.width and position[1] >= 0 and position[1] < self.height

    def __append_cell(self, position: tuple, initial: bool = False):
        """
        Used by add_cell() in the event that the queue needs to be skipped

        Parameters:
            position (tuple): The position to add a cell

            initial (bool): Adds to the initial portion as well if True
        """
        self.cells.append(position)
        self.cell_board[position[0]][position[1]] = True

        if initial:
            self.initial_cells.append(position)
            self.initial_cell_board[position[0]][position[1]] = True

    def __remove_cell(self, position: tuple, initial: bool = False):
        """
        Used by delete_cell() in the event that the queue needs to be skipped

        Parameters:
            position (tuple): The position to remove a cell

            initial (bool): Removes from the initial portion as well if True
        """
        self.cells.remove(position)
        self.cell_board[position[0]][position[1]] = False

        if initial:
            self.initial_cells.remove(position)
            self.initial_cell_board[position[0]][position[1]] = False