"""
This module implements the GUI of the Tic-Tac-Toe game.  It is also the main program of the game.
"""
from gameBoard import GameBoard
from player import HumanPlayer, DumbComputerPlayer, UnbeatableComputerPlayer


def human_choose_symbol():
    """
    """

    print('Choose the symbol you want:', 'X: for the X player',
          'O: for the O player', sep='\n')
    symbol = input('Your choice: ')
    return HumanPlayer(symbol)


def player_vs_player():
    """
    This function manages the game between two human players.

    ::
    :returns: None.
    """

    playerList = [human_choose_symbol(), human_choose_symbol()]
    game = GameBoard()
    game.play_on_board(playerList)


def player_vs_dumb_computer():
    """
    """

    playerList = [DumbComputerPlayer('X'), HumanPlayer('O')]
    print('Computer is X and you are O.')
    game = GameBoard()
    game.play_on_board(playerList)


def player_vs_unbeatable_computer():
    """
    """

    playerList = [UnbeatableComputerPlayer('X'), HumanPlayer('O')]
    print('Computer is X and you are O.')
    game = GameBoard()
    game.play_on_board(playerList)


def menu_manager():
    """
    This functions manages the menu in the CLI.

    :var waiting_for_input bool:
    :var user_choice str:
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
            print('No implemented yet!')
        elif user_choice == '5':
            waiting_for_input = False
        else:
            print('Input was invalid, please pick a value from the list!')
    print('You have left the game, see you next time!')


if __name__ == '__main__':
    """
    Main program of the project.
    """
    menu_manager()
