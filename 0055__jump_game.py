"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the
array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

## Example 1

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

## Example 2

Input: nums = [3,2,1,0,4]
Output: false
Explanation:

    You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible
    to reach the last index.


Constraints:

1 <= nums.length <= 10^4
0 <= nums[i] <= 10^5
"""
from typing import List
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        self.assertTrue(self.canJump([2, 3, 1, 1, 4]))

    def test_example_2(self):
        self.assertFalse(self.canJump([3, 2, 1, 0, 4]))

    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[-1] = True

        for i in range(len(nums) - 2, -1, -1):
            res = False
            for jump in range(i + 1, min(i + nums[i] + 1, len(dp))):
                if dp[jump]:
                    res = True
                    break
            dp[i] = res

        return dp[0]
