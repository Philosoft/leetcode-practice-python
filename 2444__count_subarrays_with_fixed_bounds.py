"""
LeetCode: https://leetcode.com/problems/count-subarrays-with-fixed-bounds/description/

You are given an integer array nums and two integers minK and maxK.

A fixed-bound subarray of nums is a subarray that satisfies the following conditions:

* The minimum value in the subarray is equal to minK.
* The maximum value in the subarray is equal to maxK.
* Return the number of fixed-bound subarrays.

A subarray is a contiguous part of an array.

## Example 1

Input: nums = [1,3,5,2,7,5], minK = 1, maxK = 5
Output: 2
Explanation: The fixed-bound subarrays are [1,3,5] and [1,3,5,2].

## Example 2

Input: nums = [1,1,1,1], minK = 1, maxK = 1
Output: 10
Explanation: Every subarray of nums is a fixed-bound subarray. There are 10 possible subarrays.

## Constraints

* 2 <= nums.length <= 10^5
* 1 <= nums[i], minK, maxK <= 10^6
"""
from typing import List
from unittest import TestCase


class Solution(TestCase):
    def test_it(self):
        options = [
            ('example 1', 2, [1, 3, 5, 2, 7, 5], 1, 5),
            ('example 1, tweaked', 1, [1, 3, 5], 1, 5),
            # ('example 2', 10, [1, 1, 1, 1], 1, 1),
            # ('test case 45', 50005000, [1] * (10 ** 4), 1, 1),
        ]

        for name, expected, nums, min_k, max_k in options:
            with self.subTest(name):
                self.assertEqual(expected, self.countSubarrays(nums, min_k, max_k))

    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        count = 0
        out_of_window = max_pos = min_pos = -1
        for i in range(len(nums)):
            if not minK <= nums[i] <= maxK:
                out_of_window = i

            if nums[i] == minK:
                min_pos = i
            if nums[i] == maxK:
                max_pos = i

            if out_of_window < min_pos and out_of_window < max_pos:
                count += min(max_pos, min_pos) - out_of_window

        return count

    def countSubarraysBrute(self, nums: List[int], minK: int, maxK: int) -> int:
        count = 0
        left = 0
        while left < len(nums):
            # find a start of a window
            while left < len(nums) and not minK <= nums[left] <= maxK:
                left += 1

            if left == len(nums):
                break

            # left is a start of a *possible* window (at least size 1)
            # find a right end of a window.
            right = left
            found_min = found_max = nums[left] == minK == maxK
            while right < len(nums) and minK <= nums[right] <= maxK:
                if not found_min and nums[right] == minK:
                    found_min = True

                if not found_max and nums[right] == maxK:
                    found_max = True

                right += 1
                if found_min and found_max:
                    count += 1  # each step gives us a new subarray

            left += 1

        return count
