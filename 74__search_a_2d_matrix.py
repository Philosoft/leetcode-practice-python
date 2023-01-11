import unittest
from typing import List

"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.


Example 1:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
"""

class Solution(unittest.TestCase):
    def test_example_1(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        target = 3

        self.assertTrue(self.searchMatrix(matrix, target))

    def test_example_2(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        target = 13

        self.assertFalse(self.searchMatrix(matrix, target))

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix) - 1
        line = []
        while left <= right:
            m = left + (right - left) // 2
            line = matrix[m]

            c = line[0]
            if c < target:
                if line[-1] >= target:
                    break
                left = m + 1
            elif c > target:
                right = m - 1
            else:
                return True

        left, right, = 0, len(line) - 1
        while left <= right:
            m = left + (right - left) // 2

            if line[m] < target:
                left = m + 1
            elif line[m] > target:
                right = m - 1
            else:
                return True

        return False
