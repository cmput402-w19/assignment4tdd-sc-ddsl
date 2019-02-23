import unittest
from gomoku.scoreboard import Scoreboard


class TestSetNewResult(unittest.TestCase):

    def setUp(self):
        self.sb = Scoreboard()

    def test_set_new_result(self):
        prev_score = self.sb.current_scoreboard['black']
        new_scoreboard = self.sb.set_new_result('black')
        self.assertEqual(prev_score + 1, new_scoreboard['black'])

        prev_score = self.sb.current_scoreboard['white']
        new_scoreboard = self.sb.set_new_result('white')
        self.assertEqual(prev_score + 1, new_scoreboard['white'])

        prev_score = self.sb.current_scoreboard['tie']
        new_scoreboard = self.sb.set_new_result('tie')
        self.assertEqual(prev_score + 1, new_scoreboard['tie'])

        with self.assertRaises(ValueError) as context:
            _ = self.sb.set_new_result('Sara')
        self.assertEqual('Could not understand Sara as a winner', str(context.exception))

    def test_reset_scoreboard(self):
        expected_scoreboard = {'black': 0, 'white': 0, 'tie': 0}
        self.sb.set_new_result('white')
        self.sb.set_new_result('black')
        self.sb.set_new_result('tie')
        new_scoreboard = self.sb.reset_scoreboard()
        self.assertEqual(new_scoreboard, expected_scoreboard)


if __name__ == '__main__':
    unittest.main()