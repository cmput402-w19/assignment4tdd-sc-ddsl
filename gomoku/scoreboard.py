class Scoreboard:

    def __init__(self):
        self.result = {'black': 0, 'white': 0, 'tie': 0}

    def set_new_result(self, winner):
        if winner == 'black':
            self.result['black'] += 1
        elif winner == 'white':
            self.result['white'] += 1
        elif winner == 'tie':
            self.result['tie'] += 1
        else:
            raise ValueError('Could not understand ' + winner + ' as a winner')

        return self.result