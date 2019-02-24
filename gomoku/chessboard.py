class Chessboard:

    def __init__(self):
        self.currentPlayer = "None"
        self.chessboardMatrix = []

    def init_chessboard(self):
        self.currentPlayer = "Black"
        self.chessboardMatrix = []
        for i in range(19):
            aCol = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            self.chessboardMatrix.append(aCol)
