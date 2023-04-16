"""
LeetCode: https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/
"""
from functools import cache
from typing import List
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        self.assertEqual(101, self.maxValueOfCoins([[1, 100, 3], [7, 8, 9]], 2))

    def test_example_2(self):
        self.assertEqual(706,
                         self.maxValueOfCoins([[100], [100], [100], [100], [100], [100], [1, 1, 1, 1, 1, 1, 700]], 7))

    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        N = len(piles)

        @cache
        def dfs(pile: int, coins_allowed: int) -> int:
            if pile == N:
                # out of bounds
                return 0

            # skip current pile
            option = dfs(pile + 1, coins_allowed)

            # current pile
            current_pile_sum = 0
            for ptr in range(min(coins_allowed, len(piles[pile]))):
                current_pile_sum += piles[pile][ptr]
                option = max(option, current_pile_sum + dfs(pile + 1, coins_allowed - ptr - 1))

            return option

        return dfs(0, k)
