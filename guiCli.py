"""
This module implements the GUI of the Tic-Tac-Toe game.  It is also the main program of the game.
"""
from gameBoard import GameBoard
from player import HumanPlayer, DumbComputerPlayer
from itertools import cycle


def player_vs_player():
    """
    This function manages the game between two human players.

    ::
    :returns: None.
    """
    playerList = [HumanPlayer('X'), HumanPlayer('O')]
    game = GameBoard()
    iterPlayer = cycle(playerList)
    player = next(iterPlayer)

    while True:  # As long as there is no winner the game continues.
        player.to_play(game)
        if game.playerWinner != None:
            break
        player = next(iterPlayer)
    print('The player: ' + str(player.symbolPlayer) + ' wins!')


def player_vs_computer():
    # TODO: Implement Minimax for unbeatable AI.
    print('Choose the computer difficulty: ', '1: for a dumb difficulty (random moves)',
          '2: for unbeatable difficulty', sep='\n')
    user_choice = input('Your choice: ')
    if user_choice == '1':
        playerList = [DumbComputerPlayer('X'), HumanPlayer('O')]
        print('Computer is X and you are O.')
        game = GameBoard()
        iterPlayer = cycle(playerList)
        player = next(iterPlayer)

        while True:
            player.to_play(game)
            if game.playerWinner != None:
                break
            player = next(iterPlayer)
        print('The player: ' + str(player.symbolPlayer) + ' wins!')
    else:
        pass


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
              '1: starting a new game with player VS player;',
              '2: starting a new game with player VS computer;',
              '3: load a game;',
              '4: quit the game;', sep='\n')
        user_choice = input('Your choice: ')
        if user_choice == '1':
            player_vs_player()
        elif user_choice == '2':
            player_vs_computer()
        elif user_choice == '3':
            # TODO: Implement all read and write file functionnalities.
            pass
        elif user_choice == '4':
            waiting_for_input = False
        else:
            print('Input was invalid, please pick a value from the list!')
    print('You have left the game, see you next time!')


if __name__ == '__main__':
    """
    Main program of the project.
    """
    menu_manager()
