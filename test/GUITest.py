import unittest
from unittest.mock import patch
import sys
from PyQt5 import QtWidgets, QtTest, QtCore
from gomoku.GUI import GUI
import numpy as np

class TestGUI(unittest.TestCase):
    def setUp(self):
        self.zero_board = np.zeros((19, 19), dtype=int)
        self.zero_board = self.zero_board.tolist()
        self.zero_result = {'Black': 0, 'White': 0, 'Tie': 0}
        self.none_zero_result = {'Black': 3, 'White': 2, 'Tie': 4}

    @patch('gomoku.GUI.Scoreboard')
    @patch('gomoku.GUI.Chessboard')
    def test_on_reset_click(self, mock_chessboard, mock_scoreboard):
        app = QtWidgets.QApplication(sys.argv)
        self.ex = GUI()

        mock_chessboard_instance = mock_chessboard.return_value
        mock_chessboard_instance.chessboard_matrix = self.zero_board
        mock_chessboard_instance.current_player = 'Black'

        mock_scoreboard_instance = mock_scoreboard.return_value
        mock_scoreboard_instance.reset_scoreboard.return_value = self.zero_result

        QtTest.QTest.mouseClick(self.ex.reset_button, QtCore.Qt.LeftButton)

        self.assertEqual(self.ex.current_player, 'Black')
        self.assertEqual(self.ex.board_matrix, self.zero_board)
        self.assertEqual(self.ex.results, self.zero_result)
        self.assertEqual(self.ex.turn_label.text(), "Black's turn ")

    @patch('gomoku.GUI.Scoreboard')
    @patch('gomoku.GUI.Chessboard')
    def test_setup_new_game(self, mock_chessboard, mock_scoreboard):
        # test current_player = 'Black'
        app = QtWidgets.QApplication(sys.argv)
        self.ex = GUI()

        mock_chessboard_instance = mock_chessboard.return_value
        mock_chessboard_instance.chessboard_matrix = self.zero_board
        mock_chessboard_instance.current_player = 'Black'

        mock_scoreboard_instance = mock_scoreboard.return_value
        mock_scoreboard_instance.reset_scoreboard.return_value = self.zero_result

        self.ex.setup_new_game()
        self.assertEqual(self.ex.current_player, 'Black')
        self.assertEqual(self.ex.board_matrix, self.zero_board)
        self.assertEqual(self.ex.turn_label.text(), "Black's turn ")

        # test current_player = 'White'
        mock_chessboard_instance.current_player = 'White'
        self.ex.setup_new_game()
        self.assertEqual(self.ex.current_player, 'White')
        self.assertEqual(self.ex.turn_label.text(), "White's turn ")

        # test current_player = 'Sara'
        with self.assertRaises(ValueError) as context:
            mock_chessboard_instance.current_player = 'Sara'
            self.ex.setup_new_game()
        self.assertEqual('invalid color', str(context.exception))

    @patch('gomoku.GUI.Chessboard')
    def test_on_new_game_click(self, mock_chessboard):
        app = QtWidgets.QApplication(sys.argv)
        self.ex = GUI()

        mock_chessboard_instance = mock_chessboard.return_value
        mock_chessboard_instance.chessboard_matrix = self.zero_board
        mock_chessboard_instance.current_player = 'Black'

        self.ex.results = self.none_zero_result
        prev_result = self.ex.results
        QtTest.QTest.mouseClick(self.ex.new_game_button, QtCore.Qt.LeftButton)

        self.assertEqual(self.ex.current_player, 'Black')
        self.assertEqual(self.ex.board_matrix, self.zero_board)
        self.assertEqual(self.ex.results, prev_result)

    @patch('gomoku.GUI.Scoreboard')
    @patch('gomoku.GUI.Chessboard')
    @patch('gomoku.GUI.GUI.show_winner')
    def test_on_admit_defeat_click(self, mock_show_winner, mock_chessboard, mock_scoreboard):
        app = QtWidgets.QApplication(sys.argv)
        self.ex = GUI()

        mock_chessboard_instance = mock_chessboard.return_value
        mock_chessboard_instance.chessboard_matrix = self.zero_board
        mock_chessboard_instance.current_player = 'Black'

        mock_scoreboard_instance = mock_scoreboard.return_value
        mock_scoreboard_instance.reset_scoreboard.return_value = self.zero_result
        mock_scoreboard_instance.set_new_result.return_value = {'Black': 0, 'White': 1, 'Tie': 0}

        mock_show_winner.return_value = True

        self.ex.current_player = 'Black'
        QtTest.QTest.mouseClick(self.ex.admit_defeat_button, QtCore.Qt.LeftButton)

        self.assertEqual(self.ex.current_player, 'Black')
        self.assertEqual(self.ex.board_matrix, self.zero_board)
        self.assertEqual(self.ex.results, {'Black': 0, 'White': 1, 'Tie': 0})
        self.assertEqual(self.ex.turn_label.text(), "Black's turn ")

    @patch('gomoku.GUI.Scoreboard')
    @patch('gomoku.GUI.Chessboard')
    @patch('gomoku.GUI.GUI.show_winner')
    def test_on_tie_click(self, mock_show_winner, mock_chessboard, mock_scoreboard):
        app = QtWidgets.QApplication(sys.argv)
        self.ex = GUI()

        mock_chessboard_instance = mock_chessboard.return_value
        mock_chessboard_instance.chessboard_matrix = self.zero_board
        mock_chessboard_instance.current_player = 'Black'

        mock_scoreboard_instance = mock_scoreboard.return_value
        mock_scoreboard_instance.reset_scoreboard.return_value = self.zero_result
        mock_scoreboard_instance.set_new_result.return_value = {'Black': 0, 'White': 0, 'Tie': 1}

        mock_show_winner.return_value = True

        self.ex.current_player = 'Black'
        QtTest.QTest.mouseClick(self.ex.tie_button, QtCore.Qt.LeftButton)

        self.assertEqual(self.ex.current_player, 'Black')
        self.assertEqual(self.ex.board_matrix, self.zero_board)
        self.assertEqual(self.ex.results, {'Black': 0, 'White': 0, 'Tie': 1})
        self.assertEqual(self.ex.turn_label.text(), "Black's turn ")

    @patch('gomoku.GUI.Scoreboard')
    @patch('gomoku.GUI.Chessboard')
    @patch('gomoku.GUI.GameLogic')
    @patch('gomoku.GUI.GUI.show_winner')
    def test_player_clicked(self, mock_show_winner, mock_game_logic, mock_chessboard, mock_scoreboard):
        app = QtWidgets.QApplication(sys.argv)
        self.ex = GUI()

        # testing with black on 0,0
        new_board = np.zeros((19, 19), dtype=int).tolist()
        new_board[0][0] = 1
        self.ex.current_player = 'Black'
        self.ex.board_matrix = self.zero_board
        self.ex.results = {'Black': 0, 'White': 0, 'Tie': 0}
        mock_chessboard_instance = mock_chessboard.return_value
        mock_chessboard_instance.chessboard_matrix = new_board
        mock_chessboard_instance.get_current_player.return_value = 'White'

        mock_game_logic_instance = mock_game_logic.return_value
        mock_game_logic_instance.has_winner.return_value = False

        mock_scoreboard_instance = mock_scoreboard.return_value
        mock_scoreboard_instance.set_new_result.return_value = {'Black': 0, 'White': 0, 'Tie': 0}

        mock_show_winner.return_value = True

        QtTest.QTest.mouseClick(self.ex.zero_zero, QtCore.Qt.LeftButton)

        self.assertEqual(self.ex.current_player, 'White')
        self.assertEqual(self.ex.board_matrix, new_board)
        self.assertEqual(self.ex.results, {'Black': 0, 'White': 0, 'Tie': 0})
        self.assertEqual(self.ex.turn_label.text(), "White's turn ")

        # testing with white on 18,18
        new_board = np.zeros((19, 19), dtype=int).tolist()
        new_board[18][18] = 1
        self.ex.current_player = 'White'
        self.ex.board_matrix = self.zero_board
        self.ex.results = {'Black': 0, 'White': 0, 'Tie': 0}
        mock_chessboard_instance = mock_chessboard.return_value
        mock_chessboard_instance.chessboard_matrix = new_board
        mock_chessboard_instance.current_player = 'Black'
        mock_chessboard_instance.get_current_player.return_value = 'Black'

        mock_game_logic_instance = mock_game_logic.return_value
        mock_game_logic_instance.has_winner.return_value = True
        mock_game_logic_instance.winner = 'White'

        mock_scoreboard_instance = mock_scoreboard.return_value
        mock_scoreboard_instance.set_new_result.return_value = {'Black': 0, 'White': 1, 'Tie': 0}

        mock_show_winner.return_value = True

        QtTest.QTest.mouseClick(self.ex.eighteen_eighteen, QtCore.Qt.LeftButton)

        self.assertEqual(self.ex.current_player, 'Black')
        self.assertEqual(self.ex.board_matrix, new_board)
        self.assertEqual(self.ex.results, {'Black': 0, 'White': 1, 'Tie': 0})
        self.assertEqual(self.ex.turn_label.text(), "Black's turn ")

        # test num 3
        new_board = np.zeros((19, 19), dtype=int).tolist()
        new_board[0][18] = 1
        self.ex.current_player = 'White'
        self.ex.board_matrix = self.zero_board
        self.ex.results = {'Black': 0, 'White': 0, 'Tie': 0}
        mock_chessboard_instance = mock_chessboard.return_value
        mock_chessboard_instance.chessboard_matrix = new_board
        mock_chessboard_instance.current_player = 'Black'
        mock_chessboard_instance.get_current_player.return_value = 'Black'

        mock_game_logic_instance = mock_game_logic.return_value
        mock_game_logic_instance.has_winner.return_value = True
        mock_game_logic_instance.winner = 'White'

        mock_scoreboard_instance = mock_scoreboard.return_value
        mock_scoreboard_instance.set_new_result.return_value = {'Black': 0, 'White': 1, 'Tie': 0}

        mock_show_winner.return_value = True

        QtTest.QTest.mouseClick(self.ex.zero_eighteen, QtCore.Qt.LeftButton)

        self.assertEqual(self.ex.current_player, 'Black')
        self.assertEqual(self.ex.board_matrix, new_board)
        self.assertEqual(self.ex.results, {'Black': 0, 'White': 1, 'Tie': 0})
        self.assertEqual(self.ex.turn_label.text(), "Black's turn ")

        # testing with white on 18,0
        new_board = np.zeros((19, 19), dtype=int).tolist()
        new_board[18][0] = 1
        self.ex.current_player = 'White'
        self.ex.board_matrix = self.zero_board
        self.ex.results = {'Black': 0, 'White': 0, 'Tie': 0}
        mock_chessboard_instance = mock_chessboard.return_value
        mock_chessboard_instance.chessboard_matrix = new_board
        mock_chessboard_instance.current_player = 'Black'
        mock_chessboard_instance.get_current_player.return_value = 'Black'

        mock_game_logic_instance = mock_game_logic.return_value
        mock_game_logic_instance.has_winner.return_value = True
        mock_game_logic_instance.winner = 'White'

        mock_scoreboard_instance = mock_scoreboard.return_value
        mock_scoreboard_instance.set_new_result.return_value = {'Black': 0, 'White': 1, 'Tie': 0}

        mock_show_winner.return_value = True

        QtTest.QTest.mouseClick(self.ex.eighteen_zero, QtCore.Qt.LeftButton)

        self.assertEqual(self.ex.current_player, 'Black')
        self.assertEqual(self.ex.board_matrix, new_board)
        self.assertEqual(self.ex.results, {'Black': 0, 'White': 1, 'Tie': 0})
        self.assertEqual(self.ex.turn_label.text(), "Black's turn ")

        # test current_player = 'Sara'
        with self.assertRaises(ValueError) as context:
            mock_chessboard_instance.current_player = 'Sara'
            self.ex.setup_new_game()
        self.assertEqual('invalid color', str(context.exception))


if __name__ == '__main__':
    unittest.main()
