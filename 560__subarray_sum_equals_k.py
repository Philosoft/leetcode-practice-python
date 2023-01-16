"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.


Example 1:

Input: nums = [1,1,1], k = 2
Output: 2

Example 2:

Input: nums = [1,2,3], k = 3
Output: 2

Constraints:

* 1 <= nums.length <= 2 * 10^4
* -1000 <= nums[i] <= 1000
* -10^7 <= k <= 10^7
"""
from typing import List
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        self.assertEqual(2, self.subarraySum([1, 1, 1], 2))

    def test_example_2(self):
        self.assertEqual(2, self.subarraySum([1, 2, 3], 3))

    def test_single_element_ok(self):
        self.assertEqual(1, self.subarraySum([0], 0))

    def test_simple_element_not_ok(self):
        self.assertEqual(0, self.subarraySum([0], 11))

    def test_edge(self):
        self.assertEqual(2, self.subarraySum([2, 2], 2))

    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sums = {0: 1}
        current_sum = 0
        for n in nums:
            current_sum += n
            diff = current_sum - k

            count += prefix_sums.get(diff, 0)
            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1

        return count
