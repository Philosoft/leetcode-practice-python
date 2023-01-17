"""
Given a 2D matrix matrix, handle multiple queries of the following type:

Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and
lower right corner (row2, col2).
Implement the NumMatrix class:

NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle
defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
You must design an algorithm where sumRegion works on O(1) time complexity.

Example:

Input
    ["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
    [[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
Output
    [null, 8, 11, 12]

Explanation
    NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
    numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangle)
    numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green rectangle)
    numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the blue rectangle)

Constraints:

* m == matrix.length
* n == matrix[i].length
* 1 <= m, n <= 200
* -10^4 <= matrix[i][j] <= 10^4
* 0 <= row1 <= row2 < m
* 0 <= col1 <= col2 < n
* At most 10^4 calls will be made to sumRegion.
"""
from typing import List
from unittest import TestCase


class TestNumMatrix(TestCase):
    def test(self):
        matrix_v1 = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
        self.assertEqual(8, matrix_v1.sumRegion(2, 1, 4, 3))
        self.assertEqual(11, matrix_v1.sumRegion(1, 1, 2, 2))
        self.assertEqual(12, matrix_v1.sumRegion(1, 2, 2, 4))

        matrix_v2 = NumMatrixV2([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
        self.assertEqual(8, matrix_v2.sumRegion(2, 1, 4, 3))
        self.assertEqual(11, matrix_v2.sumRegion(1, 1, 2, 2))
        self.assertEqual(12, matrix_v2.sumRegion(1, 2, 2, 4))


class NumMatrixV2:
    def __init__(self, matrix: List[List[int]]):
        self.prefix = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]

        for row in range(len(matrix)):
            prefix = 0
            for col in range(len(matrix[row])):
                prefix += matrix[row][col]
                above = self.prefix[row][col + 1]
                self.prefix[row + 1][col + 1] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        main = self.prefix[row2 + 1][col2 + 1]
        top = self.prefix[row1][col2 + 1]
        left = self.prefix[row2 + 1][col1]
        top_left = self.prefix[row1][col1]

        return main - top - left + top_left


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.prefixes = []
        for row in range(len(matrix)):
            prefix_row = []
            s = 0
            for col in range(len(matrix[row])):
                prefix_row.append(matrix[row][col] + s)
                s += matrix[row][col]
            self.prefixes.append(prefix_row)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        answer = 0
        for row in range(row1, row2 + 1):
            answer += self.prefixes[row][col2] - (self.prefixes[row][col1 - 1] if col1 > 0 else 0)

        return answer
