"""
LeetCode premium: https://leetcode.com/problems/number-of-islands-ii/
"""
from typing import List, Tuple
from unittest import TestCase


class Solution(TestCase):
    def test_it(self):
        expected = [1, 2, 2, 2, 2, 2, 2, 1]
        positions = [[0, 0], [2, 0], [0, 1], [2, 1], [0, 2], [2, 2], [0, 1], [1, 2]]

        self.assertEqual(expected, self.numIslands2(3, 3, positions))

    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        uf = {}

        def find(p: Tuple[int, int]) -> Tuple[int, int]:
            if p not in uf:
                uf[p] = p

            if p != uf[p]:
                uf[p] = find(uf[p])

            return uf[p]

        def union_around(p: Tuple[int, int]) -> int:
            find(p)
            connections = 0

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_row, new_col = p[0] + dr, p[1] + dc
                new_p = (new_row, new_col)

                if (
                    new_row < 0 or new_row >= m
                    or new_col < 0 or new_col >= n
                    or new_p not in uf
                ):
                    continue

                connections += union(p, new_p)

            return connections

        def union(p1: Tuple[int, int], p2: Tuple[int, int]) -> int:
            p1root, p2root = find(p1), find(p2)
            if p1root == p2root:
                return 0

            # @todo: optimize by rank
            uf[p1root] = p2root

            return 1

        count = 0
        result = []
        for p in positions:
            p = tuple(p)
            if p not in uf:
                count += 1 - union_around(p)

            result.append(count)

        return result
