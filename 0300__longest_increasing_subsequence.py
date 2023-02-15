"""
LeetCode: https://leetcode.com/problems/longest-increasing-subsequence/

Given an integer array nums, return the length of the longest strictly increasing
subsequence

## Example 1

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

## Example 2

Input: nums = [0,1,0,3,2,3]
Output: 4

## Example 3

Input: nums = [7,7,7,7,7,7,7]
Output: 1

## Constraints

* 1 <= nums.length <= 2500
* -10^4 <= nums[i] <= 10^4

## Follow up

Can you come up with an algorithm that runs in O(n log(n)) time complexity?
"""
from typing import List
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        self.assertEqual(4, self.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))

    def test_example_2(self):
        self.assertEqual(4, self.lengthOfLIS([0, 1, 0, 3, 2, 3]))

    def test_example_3(self):
        self.assertEqual(1, self.lengthOfLIS([7] * 10))

    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for left in range(len(nums) - 1, -1, -1):
            for right in range(left + 1, len(nums)):
                if nums[left] < nums[right]:
                    dp[left] = max(dp[left], 1 + dp[right])

        return max(dp)
