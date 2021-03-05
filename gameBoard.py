"""
This module manages the board of the game. It allows the players and the computer to play on the grid, to save a game or to load a game.

:class GameBoard: The class of the board of the game.
"""
from itertools import cycle
from gui.guicli import save_game


class GameBoard:
    """
    GameBoard class is used to create the board of the game.

    :method: __init__(self)
    :method: grid(self)
    :method: playerWinner(self)
    :method: playerWinner(self, winner)
    :method: number_empty_squares(self)
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

    @grid.setter
    def grid(self, grid):
        """
        This function is the setter of the grid variable.

        :param grid: The new grid of the game.
        :returns: None.
        """

        self._grid = grid

    @property
    def playerWinner(self):
        """
        This function is the getter of the winning player.

        :returns Player: The winner of the game.
        """

        return self._playerWinner

    @playerWinner.setter
    def playerWinner(self, winner):
        """
        This function is the setter of the winning player.

        :param winner: The new winner of the game.
        :returns: None.
        """

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

        :param player Player: The player which needs to be verified.
        :var symbol char: The symbol of the player var.
        :returns int: 1 if the player one wins, 2 if the player two wins, 0 if neither of them wins, prints an error if the two players are winning at the same time.
        :notes: There are 6 conditions for winning, 3 with a line configuration, 3 with a rwo configuration and 2 with a diagonal configuration.
        """

        symbol = player.symbolPlayer
        # Line conditions
        for line in self._grid:
            if all([symbol == square for square in line]):
                self._playerWinner = player.symbolPlayer
        # Row conditions
        if all([self._grid[i][0] == symbol for i in range(3)]) or all([self._grid[i][1] == symbol for i in range(3)]) or all([self._grid[i][2] == symbol for i in range(3)]):
            self._playerWinner = player.symbolPlayer
        # Diagonal conditions
        if all([self._grid[i][i] == symbol for i in range(3)]) or all(self._grid[i][2 - i] == symbol for i in range(3)):
            self._playerWinner = player.symbolPlayer

    def play_on_board(self, listPlayers, typeOfPlay):
        """
        This function takes the players in turn and saves the game after each turn. It prints if the game is a tie or the winner of the game.

        :param listPlayers list: The list of the players of the game.
        :var iterPlayer Player: The iterator of the listPlayers var.
        :var player Player: The player playing at the moment.
        :returns: None.
        """

        iterPlayer = cycle(listPlayers)
        player = next(iterPlayer)

        while True:
            player.to_play(self)
            if self._playerWinner != None:
                break
            save_game(self, player.symbolPlayer, typeOfPlay)
            player = next(iterPlayer)
        if self._playerWinner == 'Tie':
            print('It\'s a tie!')
        else:
            print('The player: ' + str(self._playerWinner) + ' wins!')

    def move_verify_display(self, absX, ordY, player):
        """
        This function makes the move of a player, verify if he wins, verify if there is a tie and displays the board.

        :returns: None.
        """

        self._grid[absX][ordY] = player.symbolPlayer
        self.verify_winning_conditions(player)
        self.verify_tie_conditions()
        self.display_board()

    def verify_tie_conditions(self):
        """
        This function verifies if there is a tie in the game.

        :returns: None.
        """

        if len(self.available_moves()) == 0 and self._playerWinner == None:
            self._playerWinner = 'Tie'
