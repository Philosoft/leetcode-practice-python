"""
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
You may return the answer in any order.

## Example 1:

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation:
    There are 4 choose 2 = 6 total combinations.
    Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

## Example 2:

Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.

## Constraints:

* 1 <= n <= 20
* 1 <= k <= n
"""
from typing import List
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        expected = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
        expected.sort()
        answer = self.combine(4, 2)
        answer.sort()
        answer_optimized = self.combine_optimized(4, 2)
        answer_optimized.sort()

        self.assertEqual(expected, answer)
        self.assertEqual(expected, answer_optimized)

    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        option = []

        def helper(num: int) -> None:
            if len(option) == k:
                result.append(option.copy())
                return

            if num > n:
                return

            option.append(num)
            helper(num + 1)
            option.pop()
            helper(num + 1)

        helper(1)

        return result

    def combine_optimized(self, n: int, k: int) -> List[List[int]]:
        result = []

        option = []

        def helper(num: int) -> None:
            if len(option) == k:
                result.append(option.copy())
                return

            for i in range(num, n + 1):
                option.append(i)
                helper(i + 1)
                option.pop()

        helper(1)

        return result
