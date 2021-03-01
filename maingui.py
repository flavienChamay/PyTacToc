from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget, QDesktopWidget
import sys


class WindowGame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("PyTacToe Game")

        self.button1 = QtWidgets.QPushButton(self)
        self.button1.setText("Button to click!")
        self.button1.clicked.connect(self.clicked)

        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText("Welcome to the PyTacToe game!")
        self.label1.move(50, 50)
        self.update()

    def clicked(self):
        self.label1.setText("You pressed the button")
        self.update()

    def update(self):
        self.label1.adjustSize()

    def center(self):
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())


def main_window():
    app = QApplication(sys.argv)
    win = WindowGame()

    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main_window()
