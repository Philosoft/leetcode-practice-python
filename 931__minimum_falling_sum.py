"""
Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.
A falling path starts at any element in the first row and chooses the element in the next row that is either directly
below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1),
(row + 1, col), or (row + 1, col + 1).

## Example 1:

Input:
    matrix = [
        [ 2, 1, 3 ],
        [ 6, 5, 4 ],
        [ 7, 8, 9 ],
    ]
Output: 13
Explanation:
    Two possible paths with minimum sum (13) are:
    * 1 -> 4 -> 8
    * 1 -> 5 -> 7

## Example 2:

Input:
    matrix = [
        [ -19, 57 ],
        [ -40, -5 ],
    ]
Output: -59
Explanation: -19 -> -40

## Constraints:

* n == matrix.length == matrix[i].length
* 1 <= n <= 100
* -100 <= matrix[i][j] <= 100
"""
from typing import List
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        matrix = [
            [2, 1, 3],
            [6, 5, 4],
            [7, 8, 9],
        ]

        self.assertEqual(13, self.minFallingPathSum(matrix))

    def test_example_2(self):
        matrix = [
            [-19, 57],
            [-40, -5],
        ]

        self.assertEqual(-59, self.minFallingPathSum(matrix))

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        falling_row = matrix[0]

        for r in range(1, len(matrix)):
            row_copy = falling_row.copy()
            for c in range(len(matrix[r - 1])):
                candidates = []
                for dc in [-1, 0, 1]:
                    upper_cell = c + dc
                    if 0 <= upper_cell < len(falling_row):
                        candidates.append(row_copy[upper_cell])
                falling_row[c] = min(candidates) + matrix[r][c]

        return min(falling_row)
