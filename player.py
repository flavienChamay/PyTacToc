"""
This module manages the players of the Tic-Tac-Toe game. The player can be a human or a computer.

:class Player: The class of the player.
:class DumbComputerPlayer: The class of a computer player with random moves.
:class UnbeatableComputerPlayer: The class of a computer player that is unbeatable.
:class HumanPlayer: The class of a human player.
"""

import random
from math import inf
from gui import guicli


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

    @symbolPlayer.setter
    def symbolPlayer(self, symbol):
        """
        This function sets the symbol of the player.

        :returns: None.
        """

        self._symbolPlayer = symbol

    def to_play(self, board):
        """
        This function lets the player plays.

        :param board GameBoard: The board of the game.
        :returns: None.
        """

        pass


class DumbComputerPlayer(Player):
    """
    DumbComputerPlayer class is used to define a computer that plays at random.

    :method: __init__(self, symbolPlayer)
    :method: to_play(self, board)
    """

    def __init__(self, symbolPlayer):
        """
        Initializes the dumb computer with input values.

        :returns DumbComputerPlayer: Yields a DumbComputerPlayer's instance.
        """

        super().__init__(symbolPlayer)

    def to_play(self, board):
        """
        This function makes the dumb computer play.

        :param board GameBoard: The game board on which the player plays.
        :var grid GameBoard: The grid of the game.
        :var moveX int: x-axis coordinate of the mark of the computer.
        :var moveY int: y-axis coordinate of the mark of the computer.
        :returns: None.
        """

        print('Computer plays...')
        grid = board.grid
        moveX, moveY = random.choice(board.available_moves())
        board.move_verify_display(moveX, moveY, self)


class UnbeatableComputerPlayer(Player):
    """
    UnbeatableComputerPlayer class is used to define a computer that is unbeatable.

    :method: __init__(self, symbolPlayer)
    :method: to_play(self, board)
    :method: minimax(self, currentBoard, currentPlayer)
    """

    def __init__(self, symbolPlayer):
        """
        Initializes the unbeatable computer with input values.

        :param symbolPlayer char: The symbol of the player, X or O.
        :returns UnbeatableComputerPlayer: Yields a UnbeatableComputerPlayer's instance 
        """

        super().__init__(symbolPlayer)

    def to_play(self, board):
        """
        This function lets the unbeatable computer plays on the board.

        :var grid list: The grid of the game board.
        :var moves int: All the available moves.
        :var moveX int: The x-axis coordinate of the move of the computer.
        :var moveY int: The y-axis coordinate of the move of the computer.
        :returns: None.
        :notes: If all squares on the board are available (meaning that it plays first), then it chooses a random square. If not, it uses the minimax algorithm to play.
        """

        print('Computer plays...')
        grid = board.grid
        moves = board.available_moves()
        if len(moves) == 9:
            moveX, moveY = random.choice(moves)
        else:
            moveX, moveY = self.minimax(board, self._symbolPlayer)['position']
        board.move_verify_display(moveX, moveY, self)

    def minimax(self, currentBoard, currentPlayer):
        """

        :notes: The utility function is positive if it is valuable for user of the minimax algorithm, negative if not. Its formulae is h = (±1) * (number_of_possible_moves + 1). The minimax algo modifies the board when it tries to figure out the best move, so we must undo its move each time we iterate.
        """
        maxPlayer = self._symbolPlayer
        minPlayer = 'X' if currentPlayer == 'O' else 'O'

        # Base case:
        if currentBoard.playerWinner == minPlayer:
            return {'position': None,
                    'score': 1 * (currentBoard.number_empty_squares() + 1) if minPlayer == maxPlayer else -1 * (currentBoard.number_empty_squares() + 1)
                    }

        # Terminal case:
        if not currentBoard.available_moves():
            return {'position': None, 'score': 0}

        # Core of the Minimax Algo
        # Maximizer tries to have the greater value so we need the lowest value possible to be sure to replace it.
        if currentPlayer == maxPlayer:
            bestMove = {
                'position': None,
                'score': -inf
            }
        # Minimizer tries to have the lowest value so we need the greater value possible to be sure to replace it.
        else:
            bestMove = {
                'position': None,
                'score': inf
            }

        grid = currentBoard.grid
        for possibleMoveX, possibleMoveY in currentBoard.available_moves():
            # Play the possible move
            grid[possibleMoveX][possibleMoveY] = currentPlayer
            virtualScore = self.minimax(currentBoard, minPlayer)

            # Undoing the move:
            grid[possibleMoveX][possibleMoveY] = ' '
            currentBoard.playerWinner = None
            virtualScore['position'] = (possibleMoveX, possibleMoveY)

            if currentPlayer == maxPlayer and virtualScore['score'] > bestMove['score']:
                bestMove = virtualScore
            if virtualScore['score'] < bestMove['score']:
                bestMove = virtualScore

        return bestMove


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
            board.move_verify_display(absX, ordY, self)
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
        # As long as the player keeps doing mistakes, he has to replay.
        while True:
            x, y = map(int, input('Your coordinates: ').split())
            resultPlay = self.player_plays(board, x, y)
            if resultPlay:
                break
