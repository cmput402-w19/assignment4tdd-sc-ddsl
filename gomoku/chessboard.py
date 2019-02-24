class Chessboard:

    def __init__(self):
        self.current_player = "None"
        self.chessboard_matrix = []

    def init_chessboard(self):
        """

        Initialize the chessboard as a zero matrix and set Black as the sente player.
        """
        self.current_player = "Black"
        self.chessboard_matrix = []
        for i in range(19):
            a_row = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            self.chessboard_matrix.append(a_row)
