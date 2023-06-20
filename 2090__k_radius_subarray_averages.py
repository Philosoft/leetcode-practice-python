"""
LeetCode: https://leetcode.com/problems/k-radius-subarray-averages/description/
"""
from typing import List
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        self.assertEqual([-1, -1, -1, 5, 4, 4, -1, -1, -1], self.getAverages([7, 4, 3, 9, 1, 8, 5, 2, 6], 3))

    def test_example_2(self):
        self.assertEqual([100000], self.getAverages([100000], 0))

    def test_example_3(self):
        self.assertEqual([-1], self.getAverages([8], 10000))

    def test_k_is_zero(self):
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], self.getAverages([1, 2, 3, 4, 5, 6, 7, 8, 9], 0))

    def test_k_is_to_large(self):
        self.assertEqual([-1, -1, -1], self.getAverages([1, 2, 3], 10))

    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums

        window = 0
        size = k * 2 + 1 # k to the left and right + middle
        if size > len(nums):
            return [-1] * len(nums)

        for i in range(size):
            window += nums[i]

        avg = [-1] * k
        for i in range(k, len(nums) - k):
            avg.append(window // size)
            if i + k + 1 < len(nums):
                window = window - nums[i - k] + nums[i + k + 1]

        for _ in range(len(nums) - k, len(nums)):
            avg.append(-1)

        return avg
