"""
This module manages the board of the game. It allows the players and the computer to play on the grid, to save a game or to load a game.

:class GameBoard: The class of the board of the game.
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
        :var playerWinner Player: If a player wins it is stored, None by default when the board is created.
        """

        self.grid = [[' ' for _ in range(3)] for _ in range(3)]
        self.playerWinner = None

    def get_grid(self):
        return self.grid

    def get_playerWinner(self):
        return self.playerWinner

    def playerPlay(self, player, absX, ordY):
        """
        This functions marks the grid with the player's mark in the given coordinates.

        :param player PLayer: The player that plays.
        :parma absX int: The x-axis coordinate of the mark of the player.
        :param absY int: The y-axis coordinate of the mark of the player.
        :returns int: 0 if there is an error and the player must replay, 1 if all is ok.
        """

        if not(absX in range(0, 3)) or not(ordY in range(0, 3)):
            print(
                'The coordinates are not in the proper range! Choose another valid coordinates.')
            return 0
        elif self.grid[absX][ordY] != ' ':
            print(
                'This square has already been played! Please choose another valid square.')
            return 0
        else:
            self.grid[absX][ordY] = player.get_symbol()
            return 1

    def display_board(self):
        """
        This function displays the board of the game in the CLI.

        :var line str: The line of the board to display.
        :returns: None.
        """

        for row in self.grid:
            print(' | '.join(row))

    def verify_winning_conditions(self, player):
        """
        This function verifies if a player wins according to the winning conditions.

        :param player Player:
        :returns int: 1 if the player one wins, 2 if the player two wins, 0 if neither of them wins, prints an error if the two players are winning at the same time.
        :notes: There are 6 conditions for winning, 3 with a line configuration, 3 with a rwo configuration and 2 with a diagonal configuration.
        """

        symbol = player.get_symbol()
        # Line conditions
        for line in self.grid:
            if all([symbol == square for square in line]):
                self.playerWinner = player
        # Row conditions
        if all([self.grid[i][0] == symbol for i in range(3)]) or all([self.grid[i][1] == symbol for i in range(3)]) or all([self.grid[i][2] == symbol for i in range(3)]):
            self.playerWinner = player
        # Diagonal conditions
        if all([self.grid[i][i] == symbol for i in range(3)]) or all(self.grid[i][2 - i] == symbol for i in range(3)):
            self.playerWinner = player
