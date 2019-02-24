import unittest
from gomoku.chessboard import Chessboard


class TestChessboard(unittest.TestCase):
    def setUp(self):
        self.cb = Chessboard()

    def test_init_chessboard(self):
        self.cb.init_chessboard()
        self.assertEqual("Black", self.cb.currentPlayer)
        self.assertEqual(19, len(self.cb.chessboardMatrix))
        for i in range(19):
            self.assertEqual(19, len(self.cb.chessboardMatrix[i]))
            self.assertEqual(0, sum(self.cb.chessboardMatrix[i]))


if __name__ == '__main__':
    unittest.main()
