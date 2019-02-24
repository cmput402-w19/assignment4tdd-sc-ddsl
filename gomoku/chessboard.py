class Chessboard:

    class IllegalCoordinateException(Exception):
        def __init__(self):
            Exception.__init__(self)

    class IllegalPlayerException(Exception):
        def __init__(self):
            Exception.__init__(self)

    class IllegalMoveException(Exception):
        def __init__(self):
            Exception.__init__(self)

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

    def get_current_player(self):
        """

        Rotate players
          :return: current player
        """
        self.current_player = "White" if self.current_player == "Black" else "Black"
        return self.current_player

    def move(self, x, y, player):
        if type(x) != int or type(y) != int:
            raise self.IllegalCoordinateException
        if x < 0 or x > 18 or y < 0 or y > 18:
            raise self.IllegalCoordinateException
        if not (player == "White" or player == "Black"):
            raise self.IllegalPlayerException
        if self.chessboard_matrix[x][y] != 0:
            raise self.IllegalMoveException
        if player == "Black":
            self.chessboard_matrix[x][y] = 1
        elif player == "White":
            self.chessboard_matrix[x][y] = 2
