import unittest
from collections import deque
from typing import List


class Solution(unittest.TestCase):
    def test_example_1(self):
        grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
        self.assertEqual(6, self.maxAreaOfIsland(grid))

    def test_example_2(self):
        grid = [[0, 0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(0, self.maxAreaOfIsland(grid))

    def test_single_island(self):
        grid = [[0, 0, 1, 0, 0]]
        self.assertEqual(1, self.maxAreaOfIsland(grid))

    def test_square_island(self):
        grid = [[1, 1], [1, 1], ]
        self.assertEqual(4, self.maxAreaOfIsland(grid))

    def test_max_island(self):
        grid = [[1] * 50] * 50
        self.assertEqual(sum([sum(x) for x in grid]), self.maxAreaOfIsland(grid))

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        answer = 0
        visited = set()

        def area_of_island(start_row: int, start_column: int) -> int:
            q = deque([(start_row, start_column)])
            area = 0
            while q:
                r, c = q.popleft()
                if grid[r][c] != 1 or (r, c) in visited:
                    continue

                area += 1
                visited.add((r, c))

                if r > 0 and (r - 1, c) not in visited:
                    q.append((r - 1, c))

                if r + 1 < len(grid) and (r + 1, c) not in visited:
                    q.append((r + 1, c))

                if c > 0 and (r, c - 1) not in visited:
                    q.append((r, c - 1))

                if c + 1 < len(grid[r]) and (r, c + 1) not in visited:
                    q.append((r, c + 1))

            return area

        for row in range(len(grid)):
            for column in range(len(grid[row])):
                if grid[row][column] == 1:
                    answer = max(answer, area_of_island(row, column))

        return answer
