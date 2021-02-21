"""
This module manages the players of the Tic-Tac-Toe game. The player can be a human or a computer.

:class Player: The class of the player.
"""


class Player:

    def __init__(self, symbolPlayer):
        self.symbolPlayer = symbolPlayer

    def get_symbol(self):
        return self.symbolPlayer
