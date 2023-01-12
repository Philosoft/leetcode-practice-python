import unittest
from collections import deque
from typing import List, Deque, Tuple


class Solution(unittest.TestCase):
    def test_example_1(self):
        grid = [
            [2, 1, 1],
            [1, 1, 0],
            [0, 1, 1],
        ]

        self.assertEqual(4, self.orangesRotting(grid))

    def test_example_2(self):
        grid = [
            [2, 1, 1],
            [0, 1, 1],
            [1, 0, 1],
        ]

        self.assertEqual(-1, self.orangesRotting(grid))

    def test_example_3(self):
        grid = [[0, 2]]

        self.assertEqual(0, self.orangesRotting(grid))

    def test_no_oranges_min(self):
        self.assertEqual(0, self.orangesRotting([[0]]))

    def test_no_oranges_maxi(self):
        self.assertEqual(0, self.orangesRotting([[0] * 100] * 100))

    def test_only_normal_oranges_min(self):
        self.assertEqual(-1, self.orangesRotting([[1]]))

    def test_only_normal_oranges_maxi(self):
        self.assertEqual(-1, self.orangesRotting([[1] * 100] * 100))

    def test_only_rotten(self):
        self.assertEqual(0, self.orangesRotting([[0, 2, 2]]))

    def test_another(self):
        grid = [
            [2, 2],
            [1, 1],
            [0, 0],
            [2, 0],
        ]

        self.assertEqual(1, self.orangesRotting(grid))

    def orangesRotting(self, grid: List[List[int]]) -> int:
        q: Deque[Tuple[int, int]] = deque([])
        fresh = 0
        for row in range(len(grid)):
            for column in range(len(grid[row])):
                if grid[row][column] == 2:
                    q.append((row, column))
                elif grid[row][column] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        time = 0
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()

                grid[r][c] = 2
                is_top_available = r - 1 >= 0
                is_bottom_available = r + 1 < len(grid)
                is_left_available = c - 1 >= 0
                is_right_available = c + 1 < len(grid[r])

                if is_bottom_available and grid[r + 1][c] == 1 and (r + 1, c) not in q:
                    q.append((r + 1, c))
                    fresh -= 1

                if is_left_available and grid[r][c - 1] == 1 and (r, c - 1) not in q:
                    q.append((r, c - 1))
                    fresh -= 1

                if is_right_available and grid[r][c + 1] == 1 and (r, c + 1) not in q:
                    q.append((r, c + 1))
                    fresh -= 1

                if is_top_available and grid[r - 1][c] == 1 and (r - 1, c) not in q:
                    q.append((r - 1, c))
                    fresh -= 1

            if q:
                time += 1

        return -1 if fresh > 0 else time
