"""
LeetCode: https://leetcode.com/problems/maximal-square/description/
"""
from typing import List, Dict, Tuple
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        matrix = [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"],
        ]

        self.assertEqual(4, self.maximalSquareTopDown(matrix))
        self.assertEqual(4, self.maximalSquareBottomUp(matrix))

    def test_example_2(self):
        self.assertEqual(1, self.maximalSquareTopDown([["0", "1"], ["1", "0"]]))
        self.assertEqual(1, self.maximalSquareBottomUp([["0", "1"], ["1", "0"]]))

    def test_example_3(self):
        self.assertEqual(0, self.maximalSquareTopDown([["0"]]))
        self.assertEqual(0, self.maximalSquareBottomUp([["0"]]))

    def test_case_65(self):
        matrix = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "1", "1", "0"],
            ["1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["0", "0", "1", "1", "1"],
        ]

        self.assertEqual(16, self.maximalSquareTopDown(matrix))
        self.assertEqual(16, self.maximalSquareBottomUp(matrix))

    def maximalSquareBottomUp(self, matrix: List[List[str]]) -> int:
        cache = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        max_sq = 0

        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == "1":
                    cache[row][col] = 1 + min(cache[row][col - 1], cache[row - 1][col], cache[row - 1][col - 1])
                    max_sq = max(max_sq, cache[row][col])

        return max_sq ** 2

    def maximalSquareTopDown(self, matrix: List[List[str]]) -> int:
        max_sq = 0
        cache: Dict[Tuple[int, int], int] = {}

        def explore(start_row: int, start_column: int) -> int:
            if min(start_row, start_column) < 0 or start_row >= len(matrix) or start_column >= len(matrix[start_row]):
                return 0

            if matrix[start_row][start_column] == "0":
                return 0

            key = (start_row, start_column)
            if key in cache:
                return cache[key]

            sq = 1
            if start_row + 1 < len(matrix) and start_column + 1 < len(matrix[start_row + 1]):
                sq += min(
                    explore(start_row + 1, start_column + 1),
                    explore(start_row + 1, start_column),
                    explore(start_row, start_column + 1),
                )

            cache[key] = sq

            return cache[key]

        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == "1":
                    max_sq = max(max_sq, explore(row, col))

        return max_sq ** 2
