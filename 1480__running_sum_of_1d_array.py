"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.


Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

Example 3:

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]

Constraints:

* 1 <= nums.length <= 1000
* -10^6 <= nums[i] <= 10^6
"""
from typing import List
from unittest import TestCase


class Solution(TestCase):
    def test(self):
        options = [
            ([1, 3, 6, 10], [1, 2, 3, 4]),
            ([1, 2, 3, 4, 5], [1, 1, 1, 1, 1]),
            ([3, 4, 6, 16, 17], [3, 1, 2, 10, 1]),
        ]

        for expected, nums in options:
            with self.subTest():
                self.assertEqual(expected, self.runningSum(nums))

    def runningSum(self, nums: List[int]) -> List[int]:
        s = [nums[0]]
        for i in range(1, len(nums)):
            s.append(nums[i] + s[-1])

        return s
