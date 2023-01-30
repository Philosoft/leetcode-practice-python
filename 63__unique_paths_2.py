"""
You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]).
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or
right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square
that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 10^9.

## Example 1

Input:
    obstacleGrid = [
        [0,0,0],
        [0,1,0],
        [0,0,0]
    ]
Output:
    2
Explanation:
    There is one obstacle in the middle of the 3x3 grid above.
    There are two ways to reach the bottom-right corner:
    1. Right -> Right -> Down -> Down
    2. Down -> Down -> Right -> Right

## Example

Input: obstacleGrid = [[0,1],[0,0]]
Output: 1

## Constraints

* m == obstacleGrid.length
* n == obstacleGrid[i].length
* 1 <= m, n <= 100
* obstacleGrid[i][j] is 0 or 1.
"""
from typing import List
from unittest import TestCase


class Solution(TestCase):
    def test_all(self):
        options = [
            ('example 1', 2, [[0, 0, 0], [0, 1, 0], [0, 0, 0]]),
            ('example 2', 1, [[0, 1], [0, 0]]),
            ('no obstacles for 3 x 3', 6, [[0] * 3] * 3),
            ('no way in line 1 x 10', 0, [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0]]),
            ('exit is blocked', 0, [[0, 0], [0, 1]]),
            ('whole row is blocked', 0, [[0, 0, 0], [1, 1, 1], [0, 0, 0]]),
            ('whole row is blocked 2', 0, [[0, 0], [1, 1], [0, 0]]),
            ('diagonal is blocked', 0, [[0, 0, 0, 0, 0], [0, 0, 0, 0, 1], [0, 0, 0, 1, 0], [0, 0, 1, 0, 0]]),
        ]

        for name, expected, grid in options:
            with self.subTest(name):
                self.assertEqual(expected, self.uniquePathsWithObstacles(grid))

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1] == 1:
            return 0

        dp = [0] * len(obstacleGrid[0])
        dp[-1] = 1

        for row in range(len(obstacleGrid) - 1, -1, -1):
            row_below = dp.copy()

            # check if row is blocked
            if sum(obstacleGrid[row]) == len(obstacleGrid[row]):
                return 0

            for col in range(len(obstacleGrid[row]) - 1, -1, -1):
                # check for obstacle
                if obstacleGrid[row][col] == 1:
                    dp[col] = 0
                else:
                    dp[col] = (dp[col + 1] + row_below[col]) if col + 1 < len(obstacleGrid[row]) else row_below[col]

        return dp[0]
