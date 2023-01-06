import unittest
from collections import deque
from typing import List


class Solution(unittest.TestCase):
    def test_example_1(self):
        grid = [
            [0, 1],
            [1, 0]
        ]
        expected = 2
        self.assertEqual(expected, self.shortestPathBinaryMatrix(grid))

    def test_example_2(self):
        grid = [
            [0, 0, 0],
            [1, 1, 0],
            [1, 1, 0]
        ]
        expected = 4
        self.assertEqual(expected, self.shortestPathBinaryMatrix(grid))

    def test_example_3(self):
        grid = [
            [1, 0, 0],
            [1, 1, 0],
            [1, 1, 0]]
        expected = -1
        self.assertEqual(expected, self.shortestPathBinaryMatrix(grid))

    def test_failing_test(self):
        grid = [
            [0, 1, 1, 0, 0, 0],
            [0, 1, 0, 1, 1, 0],
            [0, 1, 1, 0, 1, 0],
            [0, 0, 0, 1, 1, 0],
            [1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 0]
        ]
        expected = 14
        self.assertEqual(expected, self.shortestPathBinaryMatrix(grid))

    def test_maxi_grid(self):
        grid = [[0] * 100] * 100
        expected = 100
        self.assertEqual(expected, self.shortestPathBinaryMatrix(grid))

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        mapped_grid = []
        for _ in range(len(grid)):
            mapped_grid.append([-1] * len(grid))

        q = deque([(0, 0)])
        steps = 0
        while q:
            steps += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                if mapped_grid[r][c] != -1 or grid[r][c] == 1:
                    continue

                mapped_grid[r][c] = steps
                top_left, top, top_right = (r - 1, c - 1), (r - 1, c), (r - 1, c + 1)
                left, right = (r, c - 1), (r, c + 1)
                bottom_left, bottom, bottom_right = (r + 1, c - 1), (r + 1, c), (r + 1, c + 1)

                # top
                if r - 1 >= 0:
                    # left
                    if c - 1 >= 0 and mapped_grid[r - 1][c - 1] == -1 and grid[r - 1][c - 1] == 0:
                        q.append(top_left)

                    # center
                    if mapped_grid[r - 1][c] == -1 and grid[r - 1][c] == 0:
                        q.append(top)

                    # right
                    if c + 1 < len(grid) and mapped_grid[r - 1][c + 1] == -1 and grid[r - 1][c + 1] == 0:
                        q.append(top_right)

                # left
                if c - 1 >= 0 and mapped_grid[r][c - 1] == -1 and grid[r][c - 1] == 0:
                    q.append(left)

                # right
                if c + 1 < len(grid) and mapped_grid[r][c + 1] == -1 and grid[r][c + 1] == 0:
                    q.append(right)

                # bottom
                if r + 1 < len(grid):
                    # left
                    if c - 1 >= 0 and mapped_grid[r + 1][c - 1] == -1 and grid[r + 1][c - 1] == 0:
                        q.append(bottom_left)

                    # center
                    if mapped_grid[r + 1][c] == -1 and grid[r + 1][c] == 0:
                        q.append(bottom)

                    # right
                    if c + 1 < len(grid) and mapped_grid[r + 1][c + 1] == -1 and grid[r + 1][c + 1] == 0:
                        q.append(bottom_right)

        return mapped_grid[-1][-1]
