"""
This module manages the players of the Tic-Tac-Toe game. The player can be a human or a computer.

:class Player: The class of the player.
"""


class Player:

    def __init__(self, symbolPlayer):
        self._symbolPlayer = symbolPlayer

    @property
    def symbolPlayer(self):
        return self._symbolPlayer

    def player_plays(self, gameBoard):
        pass


class DumbComputerPlayer(Player):
    def __init__(self, symbolPlayer):
        super().__init__(symbolPlayer)


class HumanPlayer(Player):
    def __init__(self, symbolPlayer):
        super().__init__(symbolPlayer)

    def player_plays(self, gameBoard, absX, ordY):
        """
        This functions marks the grid with the player's mark in the given coordinates.

        :param:
        :parma absX int: The x-axis coordinate of the mark of the player.
        :param absY int: The y-axis coordinate of the mark of the player.
        :returns int: 0 if there is an error and the player must replay, 1 if all is ok.
        """

        grid = gameBoard.grid
        if not(absX in range(0, 3)) or not(ordY in range(0, 3)):
            print(
                'The coordinates are not in the proper range! Choose another valid coordinates.')
            return 0
        elif grid[absX][ordY] != ' ':
            print(
                'This square has already been played! Please choose another valid square.')
            return 0
        else:
            grid[absX][ordY] = self.symbolPlayer
            return 1

    def to_play(self, board):
        print('Always choose a tuple of coordinates between 0 and 2 like this : "x y"')
        print('Player ' + str(self._symbolPlayer) + ' to play: ')
        while True:  # As long as the player keeps doing mistakes, he has to replay.
            x, y = map(int, input('Your coordinates: ').split())
            resultPlay = self.player_plays(board, x, y)
            board.verify_winning_conditions(self)
            board.display_board()
            if resultPlay != 0:
                break
