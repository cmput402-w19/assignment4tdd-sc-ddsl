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

    def test_move(self):
        self.cb.init_chessboard()
        self.cb.move(0, 0, "Black")
        self.assertEqual(1, self.cb.chessboard_matrix[0][0])
        self.cb.move(18, 18, "White")
        self.assertEqual(2, self.cb.chessboard_matrix[18][18])
        self.assertRaises(self.cb.IllegalCoordinateException, self.cb.move, 1.6, 0.2, "White")
        self.assertRaises(self.cb.IllegalMoveException, self.cb.move, 0, 0, "White")
        self.assertRaises(self.cb.IllegalCoordinateException, self.cb.move, 19, 0, "White")
        self.assertRaises(self.cb.IllegalPlayerException, self.cb.move, 10, 10, "None")


if __name__ == '__main__':
    unittest.main()
