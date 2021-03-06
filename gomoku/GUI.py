from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import sys
import re
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
                exec('self.' + name + ".clicked.connect(lambda self=self: self.player_clicked('" + name + "'))")

        self.reset_button = QtWidgets.QPushButton('Reset Game', self)
        self.reset_button.setGeometry(650, 240, 170, 50)
        self.reset_button.clicked.connect(self.on_reset_click)
        self.reset_button.setStyleSheet(self.button_style)

        self.new_game_button = QtWidgets.QPushButton('New Game', self)
        self.new_game_button.setGeometry(650, 310, 170, 50)
        self.new_game_button.clicked.connect(self.on_new_game_click)
        self.new_game_button.setStyleSheet(self.button_style)

        self.admit_defeat_button = QtWidgets.QPushButton('Admit Defeat', self)
        self.admit_defeat_button.setGeometry(650, 380, 170, 50)
        self.admit_defeat_button.clicked.connect(self.on_admit_defeat_click)
        self.admit_defeat_button.setStyleSheet(self.button_style)

        self.tie_button = QtWidgets.QPushButton('Tie the game', self)
        self.tie_button.setGeometry(650, 450, 170, 50)
        self.tie_button.clicked.connect(self.on_tie_click)
        self.tie_button.setStyleSheet(self.button_style)

        self.chessboard = Chessboard()
        self.score_board = Scoreboard()
        self.game_logic = GameLogic()

        self.chessboard.init_chessboard()
        self.current_player = self.chessboard.current_player
        self.board_matrix = self.chessboard.chessboard_matrix
        self.results = self.score_board.reset_scoreboard()
        self.show_scores()

    def setup_new_game(self):
        self.chessboard.init_chessboard()
        self.board_matrix = self.chessboard.chessboard_matrix
        self.current_player = self.chessboard.current_player
        if self.current_player == 'Black':
            self.turn_label.setText("Black's turn ")
        elif self.current_player == 'White':
            self.turn_label.setText("White's turn ")
        else:
            raise ValueError('invalid color')

    def on_reset_click(self):
        self.setup_new_game()
        self.results = self.score_board.reset_scoreboard()
        self.show_game(self.board_matrix)
        self.show_scores()

    def on_new_game_click(self):
        self.setup_new_game()
        self.show_game(self.board_matrix)

    def on_admit_defeat_click(self):
        winner = "White" if self.current_player == "Black" else "Black"
        message = winner + ' won!'
        if self.show_winner(message):
            self.setup_new_game()
            self.results = self.score_board.set_new_result(winner)
            self.show_game(self.board_matrix)
            self.show_scores()

    def on_tie_click(self):
        if self.show_winner('Game ended in a tie!'):
            self.setup_new_game()
            self.results = self.score_board.set_new_result('Tie')
            self.show_game(self.board_matrix)
            self.show_scores()

    def player_clicked(self, label_name):
        pattern = re.compile(r'(.*)_(.*)')
        result = pattern.match(label_name)
        row = self.str_to_int[result.group(1)]
        column = self.str_to_int[result.group(2)]
        if self.board_matrix[row][column] == 0:
            self.chessboard.move(row, column, self.current_player)
            self.board_matrix = self.chessboard.chessboard_matrix
            self.current_player = self.chessboard.get_current_player()
            if self.current_player == 'Black':
                self.turn_label.setText("Black's turn ")
            elif self.current_player == 'White':
                self.turn_label.setText("White's turn ")
            else:
                raise ValueError('invalid color')

            if self.game_logic.has_winner(self.board_matrix, row, column):
                message = self.game_logic.winner + ' won!'
                self.results = self.score_board.set_new_result(self.game_logic.winner)
                self.show_scores()
                if self.show_winner(message):
                    self.setup_new_game()
                    self.show_game(self.board_matrix)
                    return
            self.show_game(self.board_matrix)

    def show_winner(self, message):
        self.buttonReply = QtWidgets.QMessageBox.information(self, "Result", message,
                                                        QtWidgets.QMessageBox.Ok)
        return self.buttonReply == QtWidgets.QMessageBox.Ok

    def show_scores(self):
        self.white_Score.setText("White's Wins: " + str(self.results['White']))
        self.black_Score.setText("Black's Wins: " + str(self.results['Black']))
        self.tie_Score.setText("Ties: " + str(self.results['Tie']))

    def show_game(self, board_matrix):
        black_pixmap = QPixmap('../pics/black.png')
        white_pixmap = QPixmap('../pics/white.png')
        self.clear_board()
        for i in range(self.board_size[0]):
            for j in range(self.board_size[1]):
                name = self.int_to_str[i] + '_' + self.int_to_str[j]
                if board_matrix[i][j] == 1:
                    exec('pixmap_smaller = QPixmap.scaled(black_pixmap, self.' + name + '.width()-2, self.'
                         + name + '.height()-2)')
                    exec('self.' + name + '.setAlignment(QtCore.Qt.AlignCenter)')
                    exec('self.' + name + '.setPixmap(pixmap_smaller)')
                elif board_matrix[i][j] == 2:
                    exec(
                        'pixmap_smaller = QPixmap.scaled(white_pixmap, self.' + name + '.width()-4, self.' + name + '.height()-4)')
                    exec('self.' + name + '.setAlignment(QtCore.Qt.AlignCenter)')
                    exec('self.' + name + '.setPixmap(pixmap_smaller)')

    def clear_board(self):
        for i in range(self.board_size[0]):
            for j in range(self.board_size[1]):
                name = self.int_to_str[i] + '_' + self.int_to_str[j]
                exec('self.' + name + '.clear()')
