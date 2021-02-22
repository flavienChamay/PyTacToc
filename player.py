"""
This module manages the players of the Tic-Tac-Toe game. The player can be a human or a computer.

:class Player: The class of the player.
:class DumbComputerPlayer: The class of a computer player with random moves.
:class :
"""


class Player:
    """
    Player class is used to define different types of player: a computer player or a human player.

    :method: __init__(self, symbolPlayer)
    :method: symbolPlayer(self)
    :method: player_plays(self, board)
    """

    def __init__(self, symbolPlayer):
        """
        Initialize the player with input values.

        :param symbolPlayer char: The symbol of the player: an 'X' or an 'O'.
        :returns Player: Yields a Player's instance.
        """

        self._symbolPlayer = symbolPlayer

    @property
    def symbolPlayer(self):
        """
        This function gets the symbol of the player.

        :returns char: The symbol of the player.
        """

        return self._symbolPlayer

    def player_plays(self, board):
        """
        This function lets the player plays.

        :param board GameBoard: The board of the game.
        """

        pass


class DumbComputerPlayer(Player):
    def __init__(self, symbolPlayer):
        super().__init__(symbolPlayer)


class UnbeatableComputerPlayer(Player):
    def __init__(self, symbolPlayer):
        super().__init__(symbolPlayer)


class HumanPlayer(Player):
    """
    HumanPlayer class is used to create a human player, to attribute to him a symbol and to make him play.

    :method: __init__(self, symbolPlayer)
    :method: player_plays(self, board, absX, ordY)
    :method: to_play(self, board)
    """

    def __init__(self, symbolPlayer):
        """
        Initialize the human player with input values.

        :param symbolPlayer char: An 'X' or an 'O' as symbol for the player.
        :returns HumanPlayer: Yields a HumanPlayer's instance.
        """

        super().__init__(symbolPlayer)

    def player_plays(self, board, absX, ordY):
        """
        This functions marks the grid with the player's mark in the given coordinates.

        :param board GameBoard: The board of the game.
        :parma absX int: The x-axis coordinate of the mark of the player.
        :param absY int: The y-axis coordinate of the mark of the player.
        :returns bool: False if there is an error and the player must replay, true if all is ok.
        """

        grid = board.grid
        if not(absX in range(0, 3)) or not(ordY in range(0, 3)):
            print(
                'The coordinates are not in the proper range! Choose another valid coordinates.')
            return False
        elif grid[absX][ordY] != ' ':
            print(
                'This square has already been played! Please choose another valid square.')
            return False
        else:
            grid[absX][ordY] = self.symbolPlayer
            return True

    def to_play(self, board):
        """
        This function tells the player how to play and let the player play until he plays correctly.

        :param board GameBoard: The board of the game.
        :var x int: The x-axis coordinate of the mark of the player.
        :var y int: The y-axis coordinate of the mark of the player.
        :var resultPlay int: 0 if there is an error from the player, 1 if not.
        :returns: None.
        """

        print('Always choose a tuple of coordinates between 0 and 2 like this : "x y"')
        print('Player ' + str(self._symbolPlayer) + ' to play: ')
        while True:  # As long as the player keeps doing mistakes, he has to replay.
            x, y = map(int, input('Your coordinates: ').split())
            resultPlay = self.player_plays(board, x, y)
            board.verify_winning_conditions(self)
            board.display_board()
            if resultPlay:
                break
