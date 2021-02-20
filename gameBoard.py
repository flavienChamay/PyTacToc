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
        # TODO: Do not authorize to play on a square already chosen by another player.
        # TODO: Verify the coordinates [0; 2]

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
                    line = line + self.grid[i][j]
                else:
                    line = line + self.grid[i][j] + "|"
            if i == 2:
                print(line)
            else:
                print(line, "-----", sep="\n")

    def verify_winning_conditions(self):
        """
        This function verifies if a player wins and returns the player number.

        :notes: There are 6 conditions for winning, 3 with a line configuration, 3 with a rwo configuration and 2 with a diagonal configuration.
        """
        # TODO: Simplify with list capture or for loops ?

        # Verification for player1:
        condPlayerOne = False
        # Line conditions
        for line in self.grid:
            if all(['X' == square for square in line]):
                condPlayerOne = True
        # Row conditions
        if (self.grid[0][0] == 'X' and self.grid[1][0] == 'X' and self.grid[2][0] == 'X') or (self.grid[0][1] == 'X' and self.grid[1][1] == 'X' and self.grid[2][1] == 'X') or (self.grid[0][2] == 'X' and self.grid[1][2] == 'X' and self.grid[2][2] == 'X'):
            condPlayerOne = True
        # Diagonal conditions
        if (self.grid[0][0] == 'X' and self.grid[1][1] == 'X' and self.grid[2][2] == 'X') or (self.grid[0][2] == 'X' and self.grid[1][1] == 'X' and self.grid[2][0] == 'X'):
            condPlayerOne = True
        # Verification for player2:
        condPlayerTwo = False
        # Line conditions
        for line in self.grid:
            if all(['O' == square for square in line]):
                condPlayerTwo = True
        # Row conditions
        if (self.grid[0][0] == 'O' and self.grid[1][0] == 'O' and self.grid[2][0] == 'O') or (self.grid[0][1] == 'O' and self.grid[1][1] == 'O' and self.grid[2][1] == 'O') or (self.grid[0][2] == 'O' and self.grid[1][2] == 'O' and self.grid[2][2] == 'O'):
            condPlayerTwo = True
        # Diagonal conditions
        if (self.grid[0][0] == 'O' and self.grid[1][1] == 'O' and self.grid[2][2] == 'O') or (self.grid[0][2] == 'O' and self.grid[1][1] == 'O' and self.grid[2][0] == 'O'):
            condPlayerTwo = True

        if condPlayerOne and condPlayerTwo:
            print('ERROR: The two players wins this game, which is impossible!')
        if condPlayerOne and not condPlayerTwo:
            return 1
        if not condPlayerOne and condPlayerTwo:
            return 2
        if not condPlayerOne and not condPlayerTwo:
            return 0
