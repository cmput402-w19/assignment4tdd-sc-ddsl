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


if __name__ == '__main__':
    unittest.main()