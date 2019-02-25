import unittest
from gomoku.scoreboard import Scoreboard


class TestSetNewResult(unittest.TestCase):

    def setUp(self):
        self.sb = Scoreboard()

    def test_set_new_result(self):
        prev_score = self.sb.current_scoreboard['Black']
        new_scoreboard = self.sb.set_new_result('Black')
        self.assertEqual(prev_score + 1, new_scoreboard['Black'])

        prev_score = self.sb.current_scoreboard['White']
        new_scoreboard = self.sb.set_new_result('White')
        self.assertEqual(prev_score + 1, new_scoreboard['White'])

        prev_score = self.sb.current_scoreboard['Tie']
        new_scoreboard = self.sb.set_new_result('Tie')
        self.assertEqual(prev_score + 1, new_scoreboard['Tie'])

        with self.assertRaises(ValueError) as context:
            _ = self.sb.set_new_result('Sara')
        self.assertEqual('Could not understand Sara as a winner', str(context.exception))

    def test_reset_scoreboard(self):
        expected_scoreboard = {'Black': 0, 'White': 0, 'Tie': 0}
        self.sb.set_new_result('White')
        self.sb.set_new_result('Black')
        self.sb.set_new_result('Tie')
        new_scoreboard = self.sb.reset_scoreboard()
        self.assertEqual(new_scoreboard, expected_scoreboard)


if __name__ == '__main__':
    unittest.main()