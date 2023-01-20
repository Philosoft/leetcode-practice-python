"""
Given an integer array nums, return all the different possible non-decreasing subsequences of the given array with at
least two elements. You may return the answer in any order.

Example 1:

Input: nums = [4,6,7,7]
Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]

Example 2:

Input: nums = [4,4,3,2,1]
Output: [[4,4]]

Constraints:

* 1 <= nums.length <= 15
* -100 <= nums[i] <= 100
"""
from typing import List
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        expected = [[4, 6], [4, 6, 7], [4, 6, 7, 7], [4, 7], [4, 7, 7], [6, 7], [6, 7, 7], [7, 7]]
        answer = self.findSubsequencesBruteWithSet([4, 6, 7, 7])
        expected.sort()
        answer.sort()

        self.assertEqual(expected, answer)

    def test_example_2(self):
        expected = [[4, 4]]
        answer = self.findSubsequencesBruteWithSet([4, 4, 3, 2, 1])
        expected.sort()
        answer.sort()

        self.assertEqual(expected, answer)

    def test_all_the_same(self):
        expected = [[7, 7], [7, 7, 7]]
        answer = self.findSubsequencesBruteWithSet([7, 7, 7])

        expected.sort()
        answer.sort()

        self.assertEqual(expected, answer)

    def test_decreasing_seq(self):
        expected = [[4, 6]]
        answer = self.findSubsequencesBruteWithSet([4, 6, 1])

        self.assertEqual(expected, answer)

    def test_big_bitonic_input(self):
        expected = [[100, 100], [90, 90], [90, 90, 100], [90, 100], [80, 80], [80, 80, 90], [80, 80, 90, 100],
                    [80, 80, 100], [80, 90], [80, 90, 100], [80, 100], [70, 70], [70, 70, 80], [70, 70, 80, 90],
                    [70, 70, 80, 90, 100], [70, 70, 80, 100], [70, 70, 90], [70, 70, 90, 100], [70, 70, 100], [70, 80],
                    [70, 80, 90], [70, 80, 90, 100], [70, 80, 100], [70, 90], [70, 90, 100], [70, 100], [60, 60],
                    [60, 60, 70], [60, 60, 70, 80], [60, 60, 70, 80, 90], [60, 60, 70, 80, 90, 100],
                    [60, 60, 70, 80, 100], [60, 60, 70, 90], [60, 60, 70, 90, 100], [60, 60, 70, 100], [60, 60, 80],
                    [60, 60, 80, 90], [60, 60, 80, 90, 100], [60, 60, 80, 100], [60, 60, 90], [60, 60, 90, 100],
                    [60, 60, 100], [60, 70], [60, 70, 80], [60, 70, 80, 90], [60, 70, 80, 90, 100], [60, 70, 80, 100],
                    [60, 70, 90], [60, 70, 90, 100], [60, 70, 100], [60, 80], [60, 80, 90], [60, 80, 90, 100],
                    [60, 80, 100], [60, 90], [60, 90, 100], [60, 100], [50, 60], [50, 60, 70], [50, 60, 70, 80],
                    [50, 60, 70, 80, 90], [50, 60, 70, 80, 90, 100], [50, 60, 70, 80, 100], [50, 60, 70, 90],
                    [50, 60, 70, 90, 100], [50, 60, 70, 100], [50, 60, 80], [50, 60, 80, 90], [50, 60, 80, 90, 100],
                    [50, 60, 80, 100], [50, 60, 90], [50, 60, 90, 100], [50, 60, 100], [50, 70], [50, 70, 80],
                    [50, 70, 80, 90], [50, 70, 80, 90, 100], [50, 70, 80, 100], [50, 70, 90], [50, 70, 90, 100],
                    [50, 70, 100], [50, 80], [50, 80, 90], [50, 80, 90, 100], [50, 80, 100], [50, 90], [50, 90, 100],
                    [50, 100]]
        answer = self.findSubsequencesBruteWithSet([100, 90, 80, 70, 60, 50, 60, 70, 80, 90, 100])

        expected.sort()
        answer.sort()

        self.assertEqual(expected, answer)

    def test_small_bitonic_input(self):
        expected = [[2, 2], [1, 2]]
        expected.sort()
        answer = self.findSubsequencesBruteWithSet([2, 1, 2])
        answer.sort()

        self.assertEqual(expected, answer)

    def findSubsequencesBruteWithSet(self, nums: List[int]) -> List[List[int]]:
        result = set()
        arr = list(reversed(nums.copy()))
        option = []

        def pick(leftover: List[int]) -> None:
            if not leftover:
                if len(option) >= 2:
                    result.add(tuple(option))
                return

            n = leftover.pop()
            if option:
                if option[-1] <= n:
                    option.append(n)
                    pick(leftover.copy())
                    option.pop()
            else:
                option.append(n)
                pick(leftover.copy())
                option.pop()

            pick(leftover.copy())

        pick(arr)

        return list(map(list, result))
