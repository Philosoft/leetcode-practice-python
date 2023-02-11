"""
LeetCode link: https://leetcode.com/problems/as-far-from-land-as-possible/

Given an n x n grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell
such that its distance to the nearest land cell is maximized, and return the distance. If no land or water exists in
the grid, return -1.

The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is
|x0 - x1| + |y0 - y1|.

## Example 1

Input:
    grid = [
        [ 1, 0, 1 ],
        [ 0, 0, 0 ],
        [ 1, 0, 1 ]
    ]
Output: 2
Explanation: The cell (1, 1) is as far as possible from all the land with distance 2.

## Example 2

Input:
    grid = [
        [ 1, 0, 0 ],
        [ 0, 0, 0 ],
        [ 0, 0, 0 ]
    ]
Output: 4
Explanation: The cell (2, 2) is as far as possible from all the land with distance 4.

## Constraints

* n == grid.length
* n == grid[i].length
* 1 <= n <= 100
* grid[i][j] is 0 or 1
"""
from collections import deque
from typing import List
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        self.assertEqual(2, self.maxDistance([[1, 0, 1], [0, 0, 0], [1, 0, 1]]))

    def test_example_2(self):
        self.assertEqual(4, self.maxDistance([[1, 0, 0], [0, 0, 0], [0, 0, 0]]))

    def test_leetcode_36(self):
        grid = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
        self.assertEqual(-1, self.maxDistance(grid))

    def maxDistance(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        mapped_grid = []

        q = deque()
        for row in range(len(grid)):
            mapped_row = []
            for col in range(len(grid[row])):
                mapped_row.append(-1)
                if grid[row][col] == 1:
                    q.append((row, col))
            mapped_grid.append(mapped_row)

        steps = 0
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()

                if mapped_grid[row][col] != -1:
                    continue

                if grid[row][col] != 1:
                    mapped_grid[row][col] = steps
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    new_row, new_col = row + dr, col + dc

                    if -1 < new_row < ROWS and -1 < new_col < COLS and grid[new_row][new_col] != 1 and \
                        mapped_grid[new_row][new_col] == -1:
                        q.append((new_row, new_col))
            steps += 1

        # possibly return steps - 1 would work as well
        max_distance = -1
        for row in mapped_grid:
            max_distance = max(max_distance, max(row))

        return max_distance
