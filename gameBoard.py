"""
This module manages the board of the game. It allows the players and the computer to play on the grid, to save a game or to load a game.

:class GameBoard: The class of the board of the game.
"""
from itertools import cycle


class GameBoard:
    """
    GameBoard class is used to create the board of the game.

    :method: __init__(self)
    :method: grid(self)
    :method: playerWinner(self)
    :method: available_moves(self)
    :method: display_board(self)
    :method: verify_winning_conditions(self, player)
    """

    def __init__(self):
        """
        Initialize the board of the game with start values.

        :var grid: The grid of the game initialized with 'E' values for empty.
        :var playerWinner Player: If a player wins it is stored, None by default when the board is created.
        """

        self._grid = [[' ' for _ in range(3)] for _ in range(3)]
        self._playerWinner = None

    @property
    def grid(self):
        """
        This function is the getter of the grid attribute.

        :returns list: The grid of the game board.
        """
        return self._grid

    @property
    def playerWinner(self):
        """
        This function is the getter of the winning player.

        :returns Player: The winner of the game.
        """
        return self._playerWinner

    @playerWinner.setter
    def playerWinner(self, winner):
        self._playerWinner = winner

    def available_moves(self):
        """
        This function indicates all of the avaible moves for a game board.

        :var l list: The list of coordinates of the game.
        :var absX int: The x-axis coordinate of a square of the game.
        :var ordY int: The y-axis coordinate of a square of the game.
        :var row list: A line of the grid.
        :returns list: A list of tuple containing the x-axis and y-axis coordinates avaible to play.
        """

        l = []
        for absX, row in enumerate(self._grid):
            for ordY, letter in enumerate(row):
                if letter == ' ':
                    l.append((absX, ordY))
        return l

    def number_empty_squares(self):
        """
        This function indicates the number of empty squares for the game board.

        :returns int: The number of empty squares.
        """

        return len(self.available_moves())

    def display_board(self):
        """
        This function displays the board of the game in the CLI.

        :var line str: The line of the board to display.
        :returns: None.
        """

        for row in self._grid:
            print(' | '.join(row))

    def verify_winning_conditions(self, player):
        """
        This function verifies if a player wins according to the winning conditions.

        :param player Player:
        :returns int: 1 if the player one wins, 2 if the player two wins, 0 if neither of them wins, prints an error if the two players are winning at the same time.
        :notes: There are 6 conditions for winning, 3 with a line configuration, 3 with a rwo configuration and 2 with a diagonal configuration.
        """

        symbol = player.symbolPlayer
        # Line conditions
        for line in self._grid:
            if all([symbol == square for square in line]):
                self._playerWinner = player
        # Row conditions
        if all([self._grid[i][0] == symbol for i in range(3)]) or all([self._grid[i][1] == symbol for i in range(3)]) or all([self._grid[i][2] == symbol for i in range(3)]):
            self._playerWinner = player
        # Diagonal conditions
        if all([self._grid[i][i] == symbol for i in range(3)]) or all(self._grid[i][2 - i] == symbol for i in range(3)):
            self._playerWinner = player

    def play_on_board(self, listPlayers):
        """
        """

        iterPlayer = cycle(listPlayers)
        player = next(iterPlayer)

        while True:
            player.to_play(self)
            if self._playerWinner != None:
                break
            player = next(iterPlayer)
        print('The player: ' + str(player.symbolPlayer) + ' wins!')

    def move_verify_display(self, absX, ordY, player):
        """
        """

        self._grid[absX][ordY] = player.symbolPlayer
        self.verify_winning_conditions(player)
        self.display_board()
