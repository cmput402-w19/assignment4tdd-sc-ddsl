class GameLogic:

    def __init__(self):
        self.winner = "None"

    def check_horizontal(self, chessboardMatrix, lastMoveRow, lastMoveCol):
        leftCount = 0
        rightCount = 0
        stone = chessboardMatrix[lastMoveRow][lastMoveCol]
        if stone == 0:
            return False
        for i in range(1, 5):
            if lastMoveCol - i >= 0:
                if chessboardMatrix[lastMoveRow][lastMoveCol - i] == stone:
                    leftCount = leftCount + 1
                else:
                    break
            else:
                break
        for i in range(1, 5):
            if lastMoveCol + i <= 18:
                if chessboardMatrix[lastMoveRow][lastMoveCol + i] == stone:
                    rightCount = rightCount + 1
                else:
                    break
            else:
                break
        if leftCount + rightCount + 1 >= 5:
            return True
        else:
            return False
