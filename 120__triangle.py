from math import inf
from typing import List
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        self.assertEqual(11, self.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for row in range(1, len(triangle)):
            for col in range(row + 1):
                smallest_above = inf
                if col > 0:
                    smallest_above = triangle[row - 1][col - 1]
                if col < row:
                    smallest_above = min(smallest_above, triangle[row - 1][col])
                triangle[row][col] += smallest_above

        return min(triangle[-1])

    def minimumTotalOriginal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]

        dp = [inf] * len(triangle[-1])
        dp[0] = triangle[0][0]
        for row in range(1, len(triangle)):
            row_copy = triangle[row].copy()
            for col in range(len(row_copy)):
                row_copy[col] += min(
                    dp[col] if col < len(dp) else dp[col - 1],
                    dp[col - 1] if col - 1 >= 0 else dp[col]
                )
            dp = row_copy.copy()

        return min(dp)
