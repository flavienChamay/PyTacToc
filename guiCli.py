"""
This module implements the GUI of the Tic-Tac-Toe game.  It is also the main program of the game.
"""
from gameBoard import GameBoard


def player_vs_player():
    game = GameBoard()
    result = 0
    print('Always choose a tuple of coordinates between 0 and 2 like this : "x y"')
    player = 1
    while result == 0:
        print('Player ' + str(player) + ' to play: ')
        x, y = map(int, input('Your coordinates: ').split())
        game.playerPlay(player, (x, y))
        game.display_board()
        result = game.verify_winning_conditions()
        if result != 0:
            break
        player += 1
        if player > 2:
            player = 1
    print('The player: ' + str(result) + ' wins!')


def player_vs_computer():
    # TODO: Choosing between two difficulties;
    # TODO: Implement Minimax for unbeatable AI
    print('Choose the computer difficulty: ')
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
        print("""
        Please choose:
        1: starting a new game with player VS player;
        2: starting a new game with player VS computer;
        3: load a game;
        4: quit the game;
        """)
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
