class GameLogic:

    def __init__(self):
        self.winner = "None"

    def check_horizontal(self, chessboard_matrix, last_move_row, last_move_col):
        """

        Check five-in-a-row horizontally
        :param chessboard_matrix: Current chessboard matrix, last_move_row: Row number of the last move, last_move_col: Column number of the last move
        :return: True or False
        """
        left_count = 0
        right_count = 0
        stone = chessboard_matrix[last_move_row][last_move_col]
        if stone == 0:
            return False
        for i in range(1, 5):
            if last_move_col - i >= 0:
                if chessboard_matrix[last_move_row][last_move_col - i] == stone:
                    left_count = left_count + 1
                else:
                    break
            else:
                break
        for i in range(1, 5):
            if last_move_col + i <= 18:
                if chessboard_matrix[last_move_row][last_move_col + i] == stone:
                    right_count = right_count + 1
                else:
                    break
            else:
                break
        if left_count + right_count + 1 >= 5:
            return True
        else:
            return False

    def check_vertical(self, chessboard_matrix, last_move_row, last_move_col):
        """

        Check five-in-a-row vertically
        :param chessboard_matrix: Current chessboard matrix, last_move_row: Row number of the last move, last_move_col: Column number of the last move
        :return: True or False
        """
        up_count = 0
        down_count = 0
        stone = chessboard_matrix[last_move_row][last_move_col]
        if stone == 0:
            return False
        for i in range(1, 5):
            if last_move_row - i >= 0:
                if chessboard_matrix[last_move_row - i][last_move_col] == stone:
                    up_count = up_count + 1
                else:
                    break
            else:
                break
        for i in range(1, 5):
            if last_move_row + i <= 18:
                if chessboard_matrix[last_move_row + i][last_move_col] == stone:
                    down_count = down_count + 1
                else:
                    break
            else:
                break
        if up_count + down_count + 1 >= 5:
            return True
        else:
            return False

    def check_lower_diagonal(self, chessboard_matrix, last_move_row, last_move_col):
        """

        Check five-in-a-row in the lower diagonal direction
        :param chessboard_matrix: Current chessboard matrix, last_move_row: Row number of the last move, last_move_col: Column number of the last move
        :return: True or False
        """
        left_count = 0
        right_count = 0
        stone = chessboard_matrix[last_move_row][last_move_col]
        if stone == 0:
            return False
        for i in range(1, 5):
            if last_move_row + i <= 18 and last_move_col - i >= 0:
                if chessboard_matrix[last_move_row + i][last_move_col - i] == stone:
                    left_count = left_count + 1
                else:
                    break
            else:
                break
        for i in range(1, 5):
            if last_move_row - i >= 0 and last_move_col + i <= 18:
                if chessboard_matrix[last_move_row - i][last_move_col + i] == stone:
                    right_count = right_count + 1
                else:
                    break
            else:
                break
        if left_count + right_count + 1 >= 5:
            return True
        else:
            return False

    def check_upper_diagonal(self, chessboard_matrix, last_move_row, last_move_col):
        """

        Check five-in-a-row in the upper diagonal direction
        :param chessboard_matrix: Current chessboard matrix, last_move_row: Row number of the last move, last_move_col: Column number of the last move
        :return: True or False
        """
        left_count = 0
        right_count = 0
        stone = chessboard_matrix[last_move_row][last_move_col]
        if stone == 0:
            return False
        for i in range(1, 5):
            if last_move_row - i >= 0 and last_move_col - i >= 0:
                if chessboard_matrix[last_move_row - i][last_move_col - i] == stone:
                    left_count = left_count + 1
                else:
                    break
            else:
                break
        for i in range(1, 5):
            if last_move_row + i <= 18 and last_move_col + i <= 18:
                if chessboard_matrix[last_move_row + i][last_move_col + i] == stone:
                    right_count = right_count + 1
                else:
                    break
            else:
                break
        if left_count + right_count + 1 >= 5:
            return True
        else:
            return False

    def has_winner(self, chessboard_matrix, last_move_row, last_move_col):
        """

        Check if the game has a winner. If there is a winner, change the winner variable to "Black" or "White".
        :param chessboard_matrix: Current chessboard matrix, last_move_row: Row number of the last move, last_move_col: Column number of the last move
        :return: True or False
        """
        if (self.check_horizontal(chessboard_matrix, last_move_row, last_move_col)
                or self.check_vertical(chessboard_matrix, last_move_row, last_move_col)
                or self.check_upper_diagonal(chessboard_matrix, last_move_row, last_move_col)
                or self.check_lower_diagonal(chessboard_matrix, last_move_row, last_move_col)):
            self.winner = "Black" if chessboard_matrix[last_move_row][last_move_col] == 1 else "White"
            return True
        else:
            return False
