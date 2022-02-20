from typing import List


class Matrix:
    def __init__(self, matrix: List[List[int]]):
        row_length = len(matrix[0])
        for row in matrix:
            if len(row) != row_length:
                raise ValueError("fail initialization matrix")
        self.matrix = matrix

    def __str__(self):
        out_string = ""
        for row in self.matrix:
            out_string += "|"
            for column in row:
                out_string += f' {column}'
            out_string += " |\n"
        return out_string

    def __add__(self, other):
        # check if matrixes addition is possible (they have same dimensions)
        if len(self.matrix) != len(other.matrix):
            raise ValueError("Can't add matrixes of different height")
        if len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError("Can't add matrixes of different width")
        return Matrix([
            [cell_1 + cell_2 for cell_1, cell_2 in zip(row_1, row_2)]
            for row_1, row_2 in zip(self.matrix, other.matrix)
        ])


if __name__ == '__main__':
    first_matrix = Matrix([[1, 2], [3, 4], [5, 6]])
    second_matrix = Matrix([[6, 5], [4, 3], [2, 1]])
    print(first_matrix)
    """
    | 1 2 |
    | 3 4 |
    | 5 6 |
    """
    print(first_matrix + second_matrix)
    """
    | 7 7 |
    | 7 7 |
    | 7 7 |
    """
    fail_matrix = Matrix([[1, 2], [3, 4, 7], [5, 6]])
    """
    Traceback (most recent call last):
      ...
    ValueError: fail initialization matrix
    """
