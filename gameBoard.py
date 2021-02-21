"""
This module manages the board of the game. It allows the players and the computer to play on the grid, to save a game or to load a game.

:class GameBoard: The class of the board of the game
"""


class GameBoard:
    """
    GameBoard class is used to create the board of the game.

    :method: __init__(self)
    :method: playerPlay(self, playerNumber, coord)
    :method: display_board(self)
    :method: verify_winning_conditions(self)
    """

    def __init__(self):
        """
        Initialize the board of the game with start values.

        :var grid: The grid of the game initialized with 'E' values for empty.
        :var condPlayerOne bool: True if the player one wins, false if not. Initialized at False.
        :var condPlayerTwo bool: True if the player two wins, false if not. Initialized at False.
        """

        self.grid = [['E', 'E', 'E'], ['E', 'E', 'E'], ['E', 'E', 'E']]
        self.condPlayerOne = False
        self.condPlayerTwo = False

    def playerPlay(self, playerNumber, coord):
        """
        This functions marks the grid with the player's mark in the given coordinates.

        :param playerNumber int: The number of the player, 1 or 2.
        :param coord (int, int): Tuple of integers representing, in order, the x-axis coordinates and the y-axis coordinates.
        :var absX int: The x-axis coordinate of the mark of the player.
        :var absY int: The y-axis coordinate of the mark of the player.
        :returns int: 0 if there is an error, 1 if all is ok.
        """

        absX, ordY = coord
        if not(absX in range(1, 3)) or not(ordY in range(1, 3)):
            print(
                'The coordinates are not in the proper range! Choose another valid coordinates.')
            return 0
        elif self.grid[absX][ordY] != 'E':
            print(
                'This square has already been played! Please choose another valid square.')
            return 0
        elif playerNumber == 1:
            self.grid[absX][ordY] = 'X'
            return 1
        elif playerNumber == 2:
            self.grid[absX][ordY] = 'O'
            return 1
        else:
            print('Not a proper player number! Please choose a valid player number.')
            return 0

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
                    line = line + self.grid[i][j]
                else:
                    line = line + self.grid[i][j] + "|"
            if i == 2:
                print(line)
            else:
                print(line, "-----", sep="\n")

    def verify_winning_conditions(self):
        """
        This function verifies if a player wins according to the winning conditions.

        :returns int: 1 if the player one wins, 2 if the player two wins, 0 if neither of them wins, prints an error if the two players are winning at the same time.
        :notes: There are 6 conditions for winning, 3 with a line configuration, 3 with a rwo configuration and 2 with a diagonal configuration.
        """

        # Line conditions
        for line in self.grid:
            if all(['X' == square for square in line]):
                self.condPlayerOne = True
            if all(['O' == square for square in line]):
                self.condPlayerTwo = True
        # Row conditions
        if all([self.grid[i][0] == 'X' for i in range(3)]) or all([self.grid[i][1] == 'X' for i in range(3)]) or all([self.grid[i][2] == 'X' for i in range(3)]):
            self.condPlayerOne = True
        if all([self.grid[i][0] == 'O' for i in range(3)]) or all([self.grid[i][1] == 'O' for i in range(3)]) or all([self.grid[i][2] == 'O' for i in range(3)]):
            self.condPlayerTwo = True
        # Diagonal conditions
        if all([self.grid[i][i] == 'X' for i in range(3)]) or all(self.grid[i][2 - i] == 'X' for i in range(3)):
            self.condPlayerOne = True
        if all([self.grid[i][i] == 'O' for i in range(3)]) or all(self.grid[i][2 - i] == 'O' for i in range(3)):
            self.condPlayerTwo = True

        if self.condPlayerOne and not self.condPlayerTwo:
            return 1
        elif not self.condPlayerOne and self.condPlayerTwo:
            return 2
        elif not self.condPlayerOne and not self.condPlayerTwo:
            return 0
        else:
            print('ERROR: The two players wins this game, which is impossible!')
