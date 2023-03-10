"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and
it will automatically contact the police if two adjacent houses were broken into on the same night.
Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can
rob tonight without alerting the police.

## Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation:
    Rob house 1 (money = 1) and then rob house 3 (money = 3).
    Total amount you can rob = 1 + 3 = 4.

## Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation:
    Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
    Total amount you can rob = 2 + 9 + 1 = 12.

## Constraints:

* 1 <= nums.length <= 100
* 0 <= nums[i] <= 400
"""
from typing import List
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        self.assertEqual(4, self.rob([1, 2, 3, 1]))

    def test_example_2(self):
        self.assertEqual(12, self.rob([2, 7, 9, 3, 1]))

    def test_single_home(self):
        self.assertEqual(1, self.rob([1]))

    def test_two_homes(self):
        self.assertEqual(2, self.rob([1, 2]))

    def simple_inc(self):
        self.assertEqual(25, self.rob([1, 2, 3, 4, 5, 6, 7, 8, 9]))

    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        dp = [0] * len(nums)
        dp[0], dp[1] = nums[0], max(nums[:2])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[-1]
