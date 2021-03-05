from gui.guicli import menu_manager
from gameBoard import GameBoard

if __name__ == '__main__':
    """
    Main program of the project. Calls the menu manager.
    """
    game = GameBoard()
    menu_manager(game)
