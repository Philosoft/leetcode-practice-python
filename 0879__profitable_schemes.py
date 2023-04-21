"""
LeetCode: https://leetcode.com/problems/profitable-schemes/
"""
from functools import cache
from typing import List
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        self.assertEqual(2, self.profitableSchemes(5, 3, [2, 2], [2, 3]))

    def test_example_2(self):
        self.assertEqual(7, self.profitableSchemes(10, 5, [2, 3, 5], [6, 7, 8]))

    def test_case_40(self):
        self.assertEqual(2, self.profitableSchemes(64, 0, [80, 40], [88, 88]))

    def test_case_41(self):
        self.assertEqual(
            653387801,
            self.profitableSchemes(
                100,
                100,
                [24, 23, 7, 4, 26, 3, 7, 11, 1, 7, 1, 3, 5, 26, 26, 1, 13, 12, 2, 1, 7, 4, 1, 27, 13, 16, 26, 18, 6, 1,
                 1, 7, 16, 1, 6, 2, 5, 9, 19, 28, 1, 23, 2, 1, 3, 4, 4, 3, 22, 1, 1, 3, 5, 34, 2, 1, 22, 16, 8, 5, 3,
                 21, 1, 8, 14, 2, 1, 3, 8, 12, 40, 6, 4, 2, 2, 14, 1, 11, 9, 1, 7, 1, 1, 1, 6, 6, 4, 1, 1, 7, 8, 10, 20,
                 2, 14, 31, 1, 13, 1, 9],
                [5, 2, 38, 25, 4, 17, 5, 1, 4, 0, 0, 8, 13, 0, 20, 0, 28, 1, 22, 7, 10, 32, 6, 37, 0, 11, 6, 11, 23, 20,
                 13, 13, 6, 2, 36, 1, 0, 9, 4, 5, 6, 14, 20, 1, 13, 6, 33, 0, 22, 1, 17, 12, 10, 1, 19, 13, 8, 1, 0, 17,
                 20, 9, 8, 6, 2, 2, 1, 4, 22, 11, 3, 2, 6, 0, 40, 0, 0, 7, 1, 0, 25, 5, 12, 7, 19, 4, 12, 7, 4, 4, 1,
                 15, 33, 14, 2, 1, 1, 61, 4, 5]
            )
        )

    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = 10 ** 9 + 7

        @cache
        def plan(ptr: int, currentProfit: int, remainingCrew: int) -> int:
            if ptr == len(group):
                return 1 if currentProfit >= minProfit else 0

            # option 1 - skip the job
            ways = plan(ptr + 1, currentProfit, remainingCrew)

            # option 2 - take it
            if remainingCrew >= group[ptr]:
                ways += plan(ptr + 1, min(minProfit, currentProfit + profit[ptr]), remainingCrew - group[ptr])

            return ways % MOD

        return plan(0, 0, n)
