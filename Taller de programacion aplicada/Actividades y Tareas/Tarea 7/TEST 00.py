import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QGridLayout
from PyQt6.QtGui import QIcon, QFont

class TicTacToe(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Tic Tac Toe')
        self.setWindowIcon(QIcon('icon.png'))
        self.setGeometry(100, 100, 300, 300)
        self.font = QFont('Arial', 20)

        self.turn = 'X'
        self.board = [' '] * 9

        self.buttons = []
        for i in range(9):
            button = QPushButton(' ', self)
            button.setFont(self.font)
            button.clicked.connect(lambda _, index=i: self.buttonClicked(index))
            self.buttons.append(button)

        layout = QGridLayout()
        layout.addWidget(self.buttons, 0, 0)
        layout.addWidget(self.buttons[1], 0, 1)
        layout.addWidget(self.buttons[2], 0, 2)
        layout.addWidget(self.buttons[3], 1, 0)
        layout.addWidget(self.buttons[4], 1, 1)
        layout.addWidget(self.buttons[5], 1, 2)
        layout.addWidget(self.buttons, 2, 0)
        layout.addWidget(self.buttons, 2, 1)
        layout.addWidget(self.buttons, 2, 2)

        self.label = QLabel('Turn: ' + self.turn, self)
        self.label.setFont(self.font)
        layout.addWidget(self.label, 3, 0, 1, 3)

        self.setLayout(layout)

    def buttonClicked(self, index):
        if self.board[index] == ' ':
            self.board[index] = self.turn
            self.buttons[index].setText(self.turn)
            if self.turn == 'X':
                self.turn = 'O'
            else:
                self.turn = 'X'
            self.label.setText('Turn: ' + self.turn)
            winner = self.checkWinner()
            if winner:
                self.label.setText('Winner: ' + winner)
                for button in self.buttons:
                    button.setEnabled(False)

    def checkWinner(self):
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] != ' ':
                return self.board[i]
        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6] != ' ':
                return self.board[i]
        if self.board == self.board[4] == self.board != ' ':
            return self.board
        if self.board[2] == self.board[4] == self.board != ' ':
            return self.board[2]
        if ' ' not in self.board:
            return 'Tie'

if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = TicTacToe()
    game.show()
    sys.exit(app.exec())