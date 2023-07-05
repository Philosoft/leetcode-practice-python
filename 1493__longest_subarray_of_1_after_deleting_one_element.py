"""
LeetCode: https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/
"""
from typing import List
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        self.assertEqual(3, self.longestSubarray([1, 1, 0, 1]))

    def test_example_2(self):
        self.assertEqual(5, self.longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]))

    def test_example_3(self):
        self.assertEqual(2, self.longestSubarray([1, 1, 1]))

    def test_case_x(self):
        self.assertEqual(11, self.longestSubarray([1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1]))

    def test_case_74(self):
        self.assertEqual(1, self.longestSubarray([0, 1, 0]))

    def longestSubarray(self, nums: List[int]) -> int:
        longest = 0
        left, right = 0, 0
        while left < len(nums):
            while left < len(nums) and nums[left] == 0:
                left += 1

            if left >= len(nums):
                break

            # left is at the first possible one
            right = left
            while right < len(nums) and nums[right] == 1:
                right += 1

            # that's the longest concequitive ones
            # right points to either the end of the array or zero
            next_stop = right

            # option #1 - take it as is and delete 1 number from it
            longest = max(longest, right - left - 1)

            # option #2 if there is at least one more zero to the right or left - take all ones
            if (
                (right + 1 < len(nums) and nums[right + 1] == 0)
                or (left - 1 > 0 and nums[left - 1] == 0)
                or (right < len(nums) and nums[right] == 0)
            ):
                longest = max(longest, right - left)

            # option #3 - skip one zero and continue building
            if right + 1 < len(nums) and nums[right + 1] == 1:
                right += 1
                while right < len(nums) and nums[right] == 1:
                    right += 1

                # right at the end or points to another zero
                longest = max(longest, right - left - 1)

            left = next_stop

        return longest
