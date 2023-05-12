"""
LeetCode: https://leetcode.com/problems/solving-questions-with-brainpower/description/
"""

from functools import cache
from typing import List
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        self.assertEqual(5, self.mostPoints([[3, 2], [4, 3], [4, 4], [2, 5]]))

    def test_example_2(self):
        self.assertEqual(7, self.mostPoints([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]))

    def mostPoints(self, questions: List[List[int]]) -> int:
        @cache
        def dfs(ptr: int) -> int:
            if ptr >= len(questions):
                return 0

            reward, brainpower = questions[ptr]

            return max(
                # option 1 - take and skip
                reward + dfs(ptr + brainpower + 1),
                # option 2 - skip
                dfs(ptr + 1)
            )

        return dfs(0)
