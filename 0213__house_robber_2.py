"""
LeetCode: https://leetcode.com/problems/house-robber-ii/description/

[[Blind75]]

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed.
All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one.
Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two
adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can
rob tonight without alerting the police.

## Example 1

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

## Example 2

Input: nums = [1,2,3,1]
Output: 4
Explanation:
    Rob house 1 (money = 1) and then rob house 3 (money = 3).
    Total amount you can rob = 1 + 3 = 4.

## Example 3

Input: nums = [1,2,3]
Output: 3

## Constraints

* 1 <= nums.length <= 100
* 0 <= nums[i] <= 1000
"""
from typing import List
from unittest import TestCase


class Solution(TestCase):
    def test_it(self):
        options = [
            (3, [2,3,2]),
            (4, [1,2,3,1]),
            (3, [1,2,3]),
            (1, [1]),
            (1, [1, 1]),
            (2, [1, 2]),
        ]

        for expected, houses in options:
            with self.subTest():
                self.assertEqual(expected, self.rob(houses))

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums)

        return max(self.rob_basic(nums[:-1]), self.rob_basic(nums[1:]))

    def rob_basic(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums) if len(nums) > 0 else 0

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[-1]
