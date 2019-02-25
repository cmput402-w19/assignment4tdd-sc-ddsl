from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import sys
from gomoku.newQLabel import QLabel_new
from gomoku.chessboard import Chessboard
from gomoku.gameLogic import GameLogic
from gomoku.scoreboard import Scoreboard


class GUI(QtWidgets.QWidget):
    def __init__(self):

        super().__init__()
        self.title = 'Gomoku'
        self.setWindowTitle(self.title)
        self.setFixedSize(1000, 700)
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        self.board_size = (19, 19)
        self.board_pixel_size = 600

        self.label_style = """QLabel {
                                            color: rgba(0, 0, 0, 0.7);
                                            font-size: 20px;}"""
        self.button_style = """QPushButton { 
                                            font-size: 20px;
                                            color: rgba(1, 1, 1, 0.7);
                                            border: 2px solid #8f8f91; 
                                            border-radius: 6px; 
                                            background-color: rgba(255, 255, 255, 0.3); 
                                            min-width: 80px;} 
                                            QPushButton:hover { 
                                            background-color: rgba(255, 255, 255, 0.5);}
                                            QPushButton:pressed { 
                                            background-color: rgba(255, 255, 255, 0.7);} 
                                            QPushButton:flat { 
                                            border: none; /* no border for a flat push button */} 
                                            QPushButton:default { 
                                            border-color: navy; /* make the default button prominent */}"""


        self.board = QtWidgets.QLabel(self)
        self.board.setGeometry(QtCore.QRect(20, 20, self.board_pixel_size, self.board_pixel_size))
        self.board.setText("")
        self.board.setPixmap(QtGui.QPixmap("../pics/board.jpg"))
        self.board.setScaledContents(True)
        self.board.setObjectName("board")

        self.turn_label = QtWidgets.QLabel(self)
        self.turn_label.setGeometry(QtCore.QRect(650, 50, 181, 29))
        self.turn_label.setText("Black's turn ")
        self.turn_label.setObjectName("turn_label")
        self.turn_label.setStyleSheet("""QLabel {
                                            color: rgba(0, 0, 0, 0.7);
                                            font-size: 20px; font-weight: bold}""")

        self.white_Score = QtWidgets.QLabel(self)
        self.white_Score.setGeometry(QtCore.QRect(650, 90, 181, 21))
        self.white_Score.setText("White's Wins: ")
        self.white_Score.setObjectName("white_Score")
        self.white_Score.setStyleSheet(self.label_style)

        self.black_Score = QtWidgets.QLabel(self)
        self.black_Score.setGeometry(QtCore.QRect(650, 130, 181, 29))
        self.black_Score.setText("Black's Wins: ")
        self.black_Score.setObjectName("black_Score")
        self.black_Score.setStyleSheet(self.label_style)

        self.tie_Score = QtWidgets.QLabel(self)
        self.tie_Score.setGeometry(QtCore.QRect(650, 170, 181, 29))
        self.tie_Score.setText("Ties: ")
        self.tie_Score.setObjectName("tie_Score")
        self.tie_Score.setStyleSheet(self.label_style)



        self.int_to_str = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven',
                           8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
                           15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen'}
        self.str_to_int = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7,
                           'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14,
                           'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18}

        width = (self.board_pixel_size / self.board_size[0]) - 0.1

        bias = 0
        for i in range(self.board_size[0]):
            for j in range(self.board_size[1]):
                name = self.int_to_str[i] + '_' + self.int_to_str[j]
                exec('self.' + name + '= QLabel_new(self)')
                exec('self.' + name + '.setGeometry(QtCore.QRect(21+width*j, 21+width*i, width+bias, width+bias))')

        self.reset_button = QtWidgets.QPushButton('Reset Game', self)
        self.reset_button.setGeometry(650, 240, 170, 50)
        self.reset_button.clicked.connect(self.on_reset_click)
        self.reset_button.setStyleSheet(self.button_style)

        self.new_game_button = QtWidgets.QPushButton('New Game', self)
        self.new_game_button.setGeometry(650, 310, 170, 50)
        self.new_game_button.setStyleSheet(self.button_style)

        self.admit_defeat_button = QtWidgets.QPushButton('Admit Defeat', self)
        self.admit_defeat_button.setGeometry(650, 380, 170, 50)
        self.admit_defeat_button.setStyleSheet(self.button_style)

        self.tie_button = QtWidgets.QPushButton('Tie the game', self)
        self.tie_button.setGeometry(650, 450, 170, 50)
        self.tie_button.setStyleSheet(self.button_style)

        self.chessboard = Chessboard()
        self.score_board = Scoreboard()
        self.game_logic = GameLogic()

        self.chessboard.init_chessboard()
        self.current_player = self.chessboard.currentPlayer
        self.board_matrix = self.chessboard.chessboardMatrix
        self.results = self.score_board.reset_scoreboard()

    def on_reset_click(self):
        pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = GUI()
    ex.show()
    sys.exit(app.exec_())
