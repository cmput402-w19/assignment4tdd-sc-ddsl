class Scoreboard:

    def __init__(self):
        self.current_scoreboard = {'black': 0, 'white': 0, 'tie': 0}

    def set_new_result(self, winner):
        """
        :param winner: A string showing the winner
        :return: Changed scoreboard
        """
        if winner == 'black':
            self.current_scoreboard['black'] += 1
        elif winner == 'white':
            self.current_scoreboard['white'] += 1
        elif winner == 'tie':
            self.current_scoreboard['tie'] += 1
        else:
            raise ValueError('Could not understand ' + winner + ' as a winner')

        return self.current_scoreboard

    def reset_scoreboard(self):
        """
          :return: The scoreboard in its initial state
        """
        self.current_scoreboard = {'black': 0, 'white': 0, 'tie': 0}
        return self.current_scoreboard
