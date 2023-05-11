"""
LeetCode: https://leetcode.com/problems/swim-in-rising-water/description/
"""
import heapq
from typing import List
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        self.assertEqual(3, self.swimInWater([[0, 2], [1, 3]]))

    def test_example_2(self):
        grid = [[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]
        self.assertEqual(16, self.swimInWater(grid))

    def swimInWater(self, grid: List[List[int]]) -> int:
        h = [(grid[0][0], 0, 0)]  # height, (row, col)
        visited = set()
        t = 0
        while h:
            cur_height, cur_row, cur_col = heapq.heappop(h)
            visited.add((cur_row, cur_col))

            if cur_height > t:
                t = cur_height

            if cur_row == len(grid) - 1 and cur_col == len(grid[cur_row]) - 1:
                return t

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_row, new_col = cur_row + dr, cur_col + dc

                if (
                    min(new_row, new_col) < 0
                    or new_row >= len(grid)
                    or new_col >= len(grid[new_row])
                    or (new_row, new_col) in visited
                ):
                    continue
                else:
                    visited.add((new_row, new_col))
                    heapq.heappush(h, (grid[new_row][new_col], new_row, new_col))

        return -1
