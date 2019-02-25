class Scoreboard:

    def __init__(self):
        self.current_scoreboard = {'Black': 0, 'White': 0, 'Tie': 0}

    def set_new_result(self, winner):
        """
        :param winner: A string showing the winner
        :return: Changed scoreboard
        """
        if winner == 'Black':
            self.current_scoreboard['Black'] += 1
        elif winner == 'White':
            self.current_scoreboard['White'] += 1
        elif winner == 'Tie':
            self.current_scoreboard['Tie'] += 1
        else:
            raise ValueError('Could not understand ' + winner + ' as a winner')

        return self.current_scoreboard

    def reset_scoreboard(self):
        """
          :return: The scoreboard in its initial state
        """
        self.current_scoreboard = {'Black': 0, 'White': 0, 'Tie': 0}
        return self.current_scoreboard
