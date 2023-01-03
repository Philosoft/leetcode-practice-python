from typing import List
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        answer = self.combinationSum([2, 3, 6, 7], 7)
        answer.sort()
        expected = [[2, 2, 3], [7]]
        expected.sort()

        self.assertEqual(answer, expected)

    def test_example_2(self):
        answer = self.combinationSum([2, 3, 5], 8)
        answer.sort()
        expected = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
        expected.sort()

        self.assertEqual(answer, expected)

    def test_example_3(self):
        answer = self.combinationSum([2], 1)
        answer.sort()
        expected = []
        expected.sort()

        self.assertEqual(answer, expected)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []

        def dfs(start_at: int, option: List[int], current_sum: int = 0):
            if current_sum > target or start_at >= len(candidates):
                return

            if current_sum == target:
                results.append(option.copy())
                return

            option.append(candidates[start_at])
            dfs(start_at, option, current_sum + candidates[start_at])

            option.pop()
            dfs(start_at + 1, option, current_sum)

        dfs(0, [], 0)

        return results
