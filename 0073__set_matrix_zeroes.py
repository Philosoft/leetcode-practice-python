"""
LeetCode: https://leetcode.com/problems/set-matrix-zeroes/

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

## Example 1

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

## Example 2

Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

## Constraints

* m == matrix.length
* n == matrix[0].length
* 1 <= m, n <= 200
* -2^31 <= matrix[i][j] <= 2^31 - 1

## Follow up

* A straightforward solution using O(mn) space is probably a bad idea.
* A simple improvement uses O(m + n) space, but still not the best solution.
* Could you devise a constant space solution?
"""
from typing import List
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
        expected = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
        self.setZeroes(matrix)

        self.assertEqual(expected, matrix)

    def test_example_2(self):
        matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
        expected = [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
        self.setZeroes(matrix)

        self.assertEqual(expected, matrix)

    def test_case_6(self):
        matrix = [[0], [1]]
        expected = [[0], [0]]
        self.setZeroes(matrix)

        self.assertEqual(expected, matrix)

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        should_mark_first_row = False
        for col in range(len(matrix[0])):
            if matrix[0][col] == 0:
                should_mark_first_row = True

        for row in range(1, len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        # now mark everything, but the first row
        for row in range(1, len(matrix)):
            for col in range(len(matrix[row]) - 1, -1, -1):
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0

        # mark first row if necessary
        if should_mark_first_row:
            for col in range(len(matrix[0])):
                matrix[0][col] = 0
