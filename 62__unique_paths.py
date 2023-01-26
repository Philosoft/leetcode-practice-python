"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot
tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any
point in time.
Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the
bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 10^9.

## Example 1:

Input: m = 3, n = 7
Output: 28

## Example 2:

Input: m = 3, n = 2
Output: 3
Explanation:
    From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
        1. Right -> Down -> Down
        2. Down -> Down -> Right
        3. Down -> Right -> Down

## Constraints:

1 <= m, n <= 100
"""
from unittest import TestCase


class Solution(TestCase):
    def test_all(self):
        options = [
            ('example 1', 28, 3, 7),
            ('example 2', 3, 3, 2),
            ('2 x 3', 3, 2, 3),
            ('1 x 1', 1, 1, 1),
            ('1 x 100', 1, 1, 100),
            ('2 x 2', 2, 2, 2),
            ('3 x 3', 6, 3, 3),
        ]

        for name, expected, m, n in options:
            with self.subTest(name):
                self.assertEqual(expected, self.uniquePaths(m, n))

    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1

        dp = []
        for r in range(m):
            row = []
            for c in range(n):
                row.append(0)
            dp.append(row)

        for col in range(n):
            dp[-1][col] = 1
        for row in range(m):
            dp[row][-1] = 1

        for row in range(m - 2, -1, -1):
            for col in range(n - 2, -1, -1):
                dp[row][col] = dp[row][col + 1] + dp[row + 1][col]

        return dp[0][0]
