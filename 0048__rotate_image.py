"""
LeetCode https://leetcode.com/problems/rotate-image/

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate
another 2D matrix and do the rotation.

## Example 1

Input:
    matrix = [
        [ 1, 2, 3 ],
        [ 4, 5, 6 ],
        [ 7, 8, 9 ]
    ]
Output:
    [
        [ 7, 4, 1 ],
        [ 8, 5, 2 ],
        [ 9, 6, 3 ]
    ]

## Example 2

Input: matrix = [
        [  5,  1,  9, 11 ],
        [  2,  4,  8, 10 ],
        [ 13,  3,  6,  7 ],
        [ 15, 14, 12, 16 ]
    ]
Output: [
        [ 15, 13,  2,  5 ],
        [ 14,  3,  4,  1 ],
        [ 12,  6,  8,  9 ],
        [ 16,  7, 10, 11 ]
    ]

## Constraints

* n == matrix.length == matrix[i].length
* 1 <= n <= 20
* -1000 <= matrix[i][j] <= 1000
"""
from typing import List
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        matrix_for_transpose = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        expected = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        self.rotate(matrix)
        self.rotateViaTranspose(matrix_for_transpose)

        self.assertEqual(expected, matrix)
        self.assertEqual(expected, matrix_for_transpose)

    def test_example_2(self):
        matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
        matrix_for_transpose = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]

        expected = [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]

        self.rotate(matrix)
        self.rotateViaTranspose(matrix_for_transpose)

        self.assertEqual(expected, matrix)
        self.assertEqual(expected, matrix_for_transpose)

    def test_single_cell(self):
        matrix = [[1]]
        matrix_for_transpose = [[1]]
        expected = [[1]]

        self.rotate(matrix)
        self.rotateViaTranspose(matrix_for_transpose)

        self.assertEqual(expected, matrix)
        self.assertEqual(expected, matrix_for_transpose)

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left, right = 0, len(matrix) - 1

        while left < right:
            for i in range(left, right):
                top, bottom = left, right
                # remember top left
                tmp = matrix[top][left + i]

                # bottom left -> top left
                matrix[top][left + i] = matrix[bottom - i][left]

                # bottom right -> bottom left
                matrix[bottom - i][left] = matrix[bottom][right - i]

                # top right -> bottom right
                matrix[bottom][right - i] = matrix[top + i][right]

                # top left -> top right (tmp -> top right)
                matrix[top + i][right] = tmp
            left += 1
            right -= 1

    def rotateViaTranspose(self, matrix: List[List[int]]) -> None:
        # transpose
        for row in range(len(matrix)):
            for col in range(row, len(matrix[row])):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

        # reverse each row
        for row in range(len(matrix)):
            left, right = 0, len(matrix[row]) - 1
            while left < right:
                matrix[row][left], matrix[row][right] = matrix[row][right], matrix[row][left]
                left += 1
                right -= 1
