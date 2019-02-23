import unittest
from gomoku.scoreboard import Scoreboard


class TestSetNewResult(unittest.TestCase):

    def setUp(self):
        self.sb = Scoreboard()

    def test_set_new_result(self):
        prev_score = self.sb.result['black']
        new_result = self.sb.set_new_result('black')
        self.assertEqual(prev_score + 1, new_result['black'])

        prev_score = self.sb.result['white']
        new_result = self.sb.set_new_result('white')
        self.assertEqual(prev_score + 1, new_result['white'])

        prev_score = self.sb.result['tie']
        new_result = self.sb.set_new_result('tie')
        self.assertEqual(prev_score + 1, new_result['tie'])

        with self.assertRaises(ValueError) as context:
            _ = self.sb.set_new_result('Sara')
        self.assertEqual('Could not understand Sara as a winner', str(context.exception))


if __name__ == '__main__':
    unittest.main()