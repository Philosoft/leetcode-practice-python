"""
Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.
A subarray is a contiguous part of an array.

Example 1:

Input:
    nums = [4,5,0,-2,-3,1]
    k = 5
Output:
    7
Explanation:
    There are 7 subarrays with a sum divisible by k = 5:
    [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

Example 2:

Input:
    nums = [5]
    k = 9
Output: 0

Constraints:

* 1 <= nums.length <= 3 * 10^4
* -10^4 <= nums[i] <= 10^4
* 2 <= k <= 10^4
"""
from typing import List
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        self.assertEqual(7, self.subarraysDivByK([4, 5, 0, -2, -3, 1], 5))

    def test_example_2(self):
        self.assertEqual(0, self.subarraysDivByK([5], 9))

    def test_maxi_list(self):
        self.assertEqual(0, self.subarraysDivByK([1] * 10_000, 100_000))

    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        """
        brute force solution works ~5s for extreme test case (maxi list)
        """
        count, prefix_mod = 0, 0
        mod_groups = [0] * k
        mod_groups[0] = 1
        for n in nums:
            prefix_mod = (prefix_mod + n) % k
            count += mod_groups[prefix_mod]
            mod_groups[prefix_mod] += 1

        return count
