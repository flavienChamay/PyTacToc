"""
This module implements the GUI of the Tic-Tac-Toe game.  It is also the main program of the game.
"""

import GameBoard


def menu_manager():
    """
    This functions manages the menu in the CLI.

    :var waiting_for_input bool:
    :var user_choice str:
    """

    waiting_for_input = True
    print('Welcome to the PyTacToe game, a Tic-Tac-Toe game!')
    while waiting_for_input:
        print("""
        Please choose:
        1: starting a new game with player VS player;
        2: starting a new game with player VS computer;
        3: load a game;
        4: quit the game;
        """)
        user_choice = input('Your choice: ')
        if user_choice == '1':
            game = GameBoard()
            print('Always choose a tuple of coordinates between 0 and 2')

        elif user_choice == '2':
            pass
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
