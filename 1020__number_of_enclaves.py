"""
LeetCode: https://leetcode.com/problems/number-of-enclaves/
"""
from typing import List, Set, Tuple
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        self.assertEqual(3, self.numEnclaves([[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]))

    def test_example_2(self):
        self.assertEqual(0, self.numEnclaves([[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]))

    def numEnclaves(self, grid: List[List[int]]) -> int:
        enclaves = 0
        visited: Set[Tuple[int, int]] = set()
        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
        ]

        def is_enclave(r: int, c: int) -> bool:
            if min(r, c) < 0 or r >= len(grid) or c >= len(grid[r]):
                # of bounds - not enclave
                return False

            if (r, c) in visited or grid[r][c] == 0:
                return True

            visited.add((r, c))

            acc: List[bool] = []
            if r == 0 or c == 0 or r == len(grid) - 1 or c == len(grid[r]) - 1:
                # touching boundary - not an enclave,
                # but we still need to explore whole island
                acc.append(False)

            for dr, dc in directions:
                acc.append(is_enclave(r + dr, c + dc))

            return all(acc)

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1 and (row, col) not in visited:
                    before = len(visited)
                    if is_enclave(row, col):
                        enclaves += len(visited) - before

        return enclaves
