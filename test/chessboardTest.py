import unittest
from gomoku.chessboard import Chessboard


class TestChessboard(unittest.TestCase):
    def setUp(self):
        self.cb = Chessboard()

    def test_init_chessboard(self):
        self.cb.init_chessboard()
        self.assertEqual("Black", self.cb.current_player)
        self.assertEqual(19, len(self.cb.chessboard_matrix))
        for i in range(19):
            self.assertEqual(19, len(self.cb.chessboard_matrix[i]))
            self.assertEqual(0, sum(self.cb.chessboard_matrix[i]))

    def test_get_current_player(self):
        self.cb.current_layer = "White"
        self.assertEqual("Black", self.cb.get_current_player())
        self.assertEqual("White", self.cb.get_current_player())


if __name__ == '__main__':
    unittest.main()
