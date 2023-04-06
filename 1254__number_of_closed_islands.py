"""
LeetCode: https://leetcode.com/problems/number-of-closed-islands/
"""
import unittest
from typing import List, Set, Tuple
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        self.assertEqual(
            2,
            self.closedIsland(
                [
                    [1, 1, 1, 1, 1, 1, 1, 0],
                    [1, 0, 0, 0, 0, 1, 1, 0],
                    [1, 0, 1, 0, 1, 1, 1, 0],
                    [1, 0, 0, 0, 0, 1, 0, 1],
                    [1, 1, 1, 1, 1, 1, 1, 0]
                ]
            )
        )

    def test_example_2(self):
        self.assertEqual(1, self.closedIsland([[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]]))

    def test_example_3(self):
        self.assertEqual(
            2,
            self.closedIsland(
                [[1, 1, 1, 1, 1, 1, 1],
                 [1, 0, 0, 0, 0, 0, 1],
                 [1, 0, 1, 1, 1, 0, 1],
                 [1, 0, 1, 0, 1, 0, 1],
                 [1, 0, 1, 1, 1, 0, 1],
                 [1, 0, 0, 0, 0, 0, 1],
                 [1, 1, 1, 1, 1, 1, 1]]
            )
        )

    def test_case_25(self):
        self.assertEqual(
            5,
            self.closedIsland(
                [
                    [0, 0, 1, 1, 0, 1, 0, 0, 1, 0],
                    [1, 1, 0, 1, 1, 0, 1, 1, 1, 0],
                    [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
                    [0, 1, 1, 0, 0, 0, 0, 1, 0, 1],
                    [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
                    [0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
                    [1, 0, 1, 0, 1, 1, 0, 0, 0, 1],
                    [1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
                    [1, 1, 1, 0, 0, 1, 0, 1, 0, 1],
                    [1, 1, 1, 0, 1, 1, 0, 1, 1, 0],
                ]
            )
        )

    def test_case_34(self):
        self.assertEqual(
            4,
            self.closedIsland(
                [[1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
                 [0, 0, 1, 0, 0, 1, 0, 1, 1, 1],
                 [1, 0, 1, 0, 0, 0, 1, 0, 1, 0],
                 [1, 1, 1, 1, 1, 0, 0, 1, 0, 0],
                 [1, 0, 1, 0, 1, 1, 1, 1, 1, 0],
                 [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                 [1, 0, 1, 0, 0, 0, 0, 1, 1, 0],
                 [1, 1, 0, 0, 1, 1, 0, 0, 0, 0],
                 [0, 0, 0, 1, 1, 0, 1, 1, 1, 0],
                 [1, 1, 0, 1, 0, 1, 0, 0, 1, 0]]
            )
        )

    def closedIsland(self, grid: List[List[int]]) -> int:
        visited: Set[Tuple[int, int]] = set()
        num_of_islands = 0
        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
        ]

        def dfs(row: int, col: int) -> bool:
            if min(row, col) < 0 or row >= len(grid) or col >= len(grid[row]):
                return False

            if (row, col) in visited or grid[row][col] == 1:
                return True

            visited.add((row, col))
            acc = []
            for dr, dc in directions:
                acc.append(dfs(row + dr, col + dc))

            return all(acc)

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 0 and (row, col) not in visited and dfs(row, col):
                    num_of_islands += 1

        return num_of_islands


if __name__ == "__main__":
    unittest.main()
