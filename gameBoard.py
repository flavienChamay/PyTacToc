"""
This module manages the board of the game. It allows the players and the computer to play on the grid, to save a game or to load a game. 

:class GameBoard: The class of the board of the game
"""


class GameBoard:
    """
    GameBoard class is used to create the board of the game.

    :method :
    """

    def __init__(self):
        """
        Initialize the board of the game with start values.

        :var grid: The grid of the game initialized with 'E' values for empty.
        :var winner: True if we have a winner of the game, false if not. Initialized at False for starting the game.
        """

        self.grid = [['E', 'E', 'E'], ['E', 'E', 'E'], ['E', 'E', 'E']]
        self.winner = False

    def playerPlay(self, playerNumber, coord):
        """
        This functions marks the grid with the player's mark in the given coordinates.

        :param playerNumber int:
        :param coord (int, int): Tuple of integers representing, in order, the x-axis coordinates and the y-axis coordinates.
        :var absX int:
        :var absY int: 
        """

        absX, ordY = coord
        if playerNumber == 1:
            self.grid[absX][ordY] = 'X'
        elif playerNumber == 2:
            self.grid[absX][ordY] = 'O'
        else:
            print('Not a proper player number, please choose a valid player number')

    def display_board(self):
        """
        This function displays the board of the game in the CLI.

        :var line str: The line of the board to display.
        :returns: None.
        """

        for i in range(3):
            line = ""
            for j in range(3):
                if j == 2:
                    line = line + "|" + self.grid[i][j]
                else:
                    line = line + self.grid[i][j] + "|"
            if i == 2:
                print(line)
            else:
                print(line, "- - -", sep="\n")

    def verify_winning_conditions():
        """
        This function verifies if a player wins and returns the player number.


        """
        for line in self.grid:
            if all()
