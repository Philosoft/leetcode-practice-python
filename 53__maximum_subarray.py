"""
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

Constraints:

* 1 <= nums.length <= 10^5
* -10^4 <= nums[i] <= 10^4

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach,
 which is more subtle.
"""
from typing import List
from unittest import TestCase


class Solution(TestCase):
    def test(self):
        options = [
            (6, [-2, 1, -3, 4, -1, 2, 1, -5, 4]),
            (1, [1]),
            (23, [5, 4, -1, 7, 8]),
        ]

        for expected, nums in options:
            with self.subTest():
                self.assertEqual(expected, self.maxSubArray(nums))

    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's algo
        max_sum = nums[0]
        cur_sum = 0

        for n in nums:
            cur_sum = max(cur_sum, 0) + n
            max_sum = max(max_sum, cur_sum)

        return max_sum
