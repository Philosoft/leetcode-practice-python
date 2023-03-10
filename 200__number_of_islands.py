import unittest
from collections import deque
from typing import List


class Solution(unittest.TestCase):
    def test_smallest_island(self):
        self.assertEqual(1, self.numIslands([['1']]))
        self.assertEqual(1, self.numIslandsDFS([['1']]))

    def test_no_islands_min(self):
        self.assertEqual(0, self.numIslands([['0']]))
        self.assertEqual(0, self.numIslandsDFS([['0']]))

    def test_no_islands_big(self):
        self.assertEqual(0, self.numIslands([['0'] * 300] * 300))
        self.assertEqual(0, self.numIslandsDFS([['0'] * 300] * 300))

    def test_one_gigantic_island(self):
        self.assertEqual(1, self.numIslands([['1'] * 300] * 300))
        self.assertEqual(1, self.numIslandsDFS([['1'] * 300] * 300))

    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()

        def explore_island(start_row: int, start_column: int) -> int:
            q = deque([(start_row, start_column)])
            is_new_island = False
            while q:
                r, c = q.popleft()
                if grid[r][c] != '1' or (r, c) in visited:
                    continue

                is_new_island = True
                visited.add((r, c))
                top, bottom, left, right = (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)

                if top not in visited and top[0] >= 0:
                    q.append(top)

                if bottom not in visited and bottom[0] < len(grid):
                    q.append(bottom)

                if left not in visited and left[1] >= 0:
                    q.append(left)

                if right not in visited and right[1] < len(grid[r]):
                    q.append(right)

            return 1 if is_new_island else 0

        island_counter = 0
        for row in range(len(grid)):
            for column in range(len(grid[row])):
                if grid[row][column] == '1':
                    island_counter += explore_island(row, column)

        return island_counter

    def numIslandsDFS(self, grid: List[List[str]]) -> int:
        count = 0

        def trace_island(row, cell):
            if row < 0 or cell < 0 or row >= len(grid) or cell >= len(grid[row]) or grid[row][cell] != "1":
                return

            grid[row][cell] = "2"

            trace_island(row + 1, cell)
            trace_island(row - 1, cell)
            trace_island(row, cell + 1)
            trace_island(row, cell - 1)

        for row in range(len(grid)):
            for cell in range(len(grid[row])):
                if grid[row][cell] == "1":
                    count += 1
                    trace_island(row, cell)

        for row in range(len(grid)):
            for cell in range(len(grid[row])):
                if grid[row][cell] == "2":
                    grid[row][cell] = "1"

        return count
