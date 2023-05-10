"""
LeetCode: https://leetcode.com/problems/spiral-matrix-ii/
"""
from typing import List
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        expected = [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
        self.assertEqual(expected, self.generateMatrix(3))

    def test_example_2(self):
        self.assertEqual([[1]], self.generateMatrix(1))

    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        ptr = 1
        left, right, top, bottom = 0, n - 1, 0, n - 1
        while ptr <= n ** 2:
            # left -> right
            row = top
            for col in range(left, right + 1):
                matrix[row][col] = ptr
                ptr += 1
            top += 1

            if ptr > n ** 2:
                break

            # top -> down
            col = right
            for row in range(top, bottom + 1):
                matrix[row][col] = ptr
                ptr += 1
            right -= 1

            if ptr > n ** 2:
                break

            # right -> left
            row = bottom
            for col in range(right, left - 1, -1):
                matrix[row][col] = ptr
                ptr += 1
            bottom -= 1

            if ptr > n ** 2:
                break

            # bottom -> top
            col = left
            for row in range(bottom, top - 1, -1):
                matrix[row][col] = ptr
                ptr += 1
            left += 1

            if ptr > n ** 2:
                break

        return matrix
