"""
This module implements the CLI of the Tic-Tac-Toe game.  It is also the main program of the game.

:method: human_choose_symbol()
:method: player_vs_player()
:method: player_vs_dumb_computer()
:method: player_vs_unbeatable_computer()n
:method: menu_manager()
:notes: A computer is always X. First human player is always X, second human player is always O.
"""

from gameBoard import GameBoard
from player import HumanPlayer, DumbComputerPlayer, UnbeatableComputerPlayer
import json


def player_vs_player(gameBoard, playerPlay):
    """
    This function manages the game between two human players.

    :param gameBoard GameBoard: The game board.
    :param playerPlay char: X or O for the symbol of the player.
    :var playerList list: The list of all the players involved.
    :returns: None.
    """
    try:
        if playerPlay == 'X':
            playerList = [HumanPlayer('X'), HumanPlayer('O')]
        elif playerPlay == 'O':
            playerList = [HumanPlayer('O'), HumanPlayer('X')]
        else:
            raise IOError('Error in the saved file, wrong type of player!')
        gameBoard.play_on_board(playerList)
    except IOError as io:
        print(io)


def player_vs_dumb_computer(gameBoard, playerPlay):
    """
    This function manages the game between a human player and a dumb computer.

    :param playerPlay char: X or O for the symbol of the player.
    :param gameBoard GameBoard: The game board.
    :var playerList list: The list of all the players involved.
    :returns: None.
    """

    try:
        if playerPlay == 'X':
            playerList = [DumbComputerPlayer('X'), HumanPlayer('O')]
        elif playerPlay == 'O':
            playerList = [HumanPlayer('O'), DumbComputerPlayer('X')]
        else:
            raise IOError('Error in the saved file, wrong type of player!')
        gameBoard.play_on_board(playerList)
    except IOError as io:
        print(io)


def player_vs_unbeatable_computer(gameBoard, playerPlay):
    """
    This function manages the game between a human player and an unbeatable computer.

    :param game GameBoard: The game board.
    :param playerPlay char:
    :var playerList list: The list of all the players involved.
    :returns: None.
    """

    try:
        if playerPlay == 'X':
            playerList = [UnbeatableComputerPlayer('X'), HumanPlayer('O')]
        elif playerPlay == 'O':
            playerList = [HumanPlayer('O'), UnbeatableComputerPlayer('X')]
        else:
            raise IOError('Error in the saved file, wrong type of player!')
        gameBoard.play_on_board(playerList)
    except IOError as io:
        print(io)


def load_game():
    """
    This function manages the load mechanism of the game from a file.

    :var listFile list: The content of the file in a list.
    :var gridLoaded list: The grid loaded from the file.
    :var playerPlay char: The symbol of the player loaded.
    :var typeOfPlay int: The type of play of the loaded game.
    :var game GameBoard: The loaded game.
    :raises IOError: If the file is missing or if wrong infos are on the file.
    :returns: None.
    :notes:
    Structure of a backup file:
    first line -> grid of the game, listed with X or O separated with empty spaces.
    second line -> symbol of the player who must play.
    third line -> type of game: (1) dumb computer vs player (2) unbeatable computer vs player (3) human player vs human player
    """

    try:
        with open("saveGameTTT.txt") as fileSaveGame:
            listFile = fileSaveGame.readlines()
            gridLoaded = json.loads(listFile[0])
            playerPlay = listFile[1].strip()
            typeOfPlay = listFile[2].strip()
        game = GameBoard()
        game.grid = gridLoaded
        # Processing the type of game and the appropriate player
        if typeOfPlay == '1':
            player_vs_dumb_computer(game, playerPlay)
        elif typeOfPlay == '2':
            player_vs_unbeatable_computer(game, playerPlay)
        elif typeOfPlay == '3':
            player_vs_player(game, playerPlay)
        else:
            raise IOError('Error in the saved file, wrong type of play!')
    except IOError as io:
        print(io)


def menu_manager():
    """
    This functions manages the menu in the CLI.

    :var waiting_for_input bool: True if the user wants to play, or to continue to play, or has given a wrong answer.
    :var user_choice str: The choice of the user from 1 to 5.
    :returns: None.
    """

    waiting_for_input = True
    print('Welcome to the PyTacToe game, a Tic-Tac-Toe game!')
    while waiting_for_input:
        print('Please choose:',
              '1: starting a new game player VS player;',
              '2: starting a new game player VS dumb computer (random moves);',
              '3: starting a new game player VS unbeatable computer;',
              '4: load a game;',
              '5: quit the game;', sep='\n')
        user_choice = input('Your choice: ')
        if user_choice == '1':
            player_vs_player()
        elif user_choice == '2':
            player_vs_dumb_computer()
        elif user_choice == '3':
            player_vs_unbeatable_computer()
        elif user_choice == '4':
            # TODO: save/load a game mechanism
            load_game()
            print('No implemented yet!')
        elif user_choice == '5':
            waiting_for_input = False
        else:
            print('Input was invalid, please pick a value from the list!')
    print('You have left the game, see you next time!')


if __name__ == '__main__':
    """
    Main program of the project. Calls the menu manager.
    """

    menu_manager()
