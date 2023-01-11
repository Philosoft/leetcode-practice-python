import unittest
from typing import List


class Solution(unittest.TestCase):
    def test_example_1(self):
        matrix = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
        self.assertEqual(8, self.countNegatives(matrix))

    def test_example_2(self):
        matrix = [[3, 2], [1, 0]]

        self.assertEqual(0, self.countNegatives(matrix))

    def test_single_column_negative(self):
        self.assertEqual(2, self.countNegatives([[-1], [-2]]))

    def test_single_column_positive(self):
        self.assertEqual(0, self.countNegatives([[1], [1]]))

    def test_all_negative(self):
        self.assertEqual(100, self.countNegatives([[-1] * 10] * 10))

    def countNegatives(self, grid: List[List[int]]) -> int:
        right_boundary = len(grid[0]) - 1
        length = len(grid[0])
        count = 0
        for row in range(len(grid)):
            # edge case 1. leftmost value is negative
            if grid[row][0] < 0:
                count += length
                continue

            # edge case 2. rightmost value is positive
            if grid[row][length - 1] >= 0:
                continue

            # general case. binary search for negative
            # keep track of right boundary
            left, right = 0, right_boundary
            while left <= right:
                mid = left + (right - left) // 2

                if grid[row][mid] >= 0:
                    left = left + 1
                else:
                    right = right - 1

            if grid[row][left] < 0:
                right_boundary = left
                count += length - left

        return count
