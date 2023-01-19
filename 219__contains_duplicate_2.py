"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such
that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false

Constraints:

* 1 <= nums.length <= 10^5
* -10^9 <= nums[i] <= 10^9
* 0 <= k <= 10^5
"""
from typing import List
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        self.assertTrue(self.containsNearbyDuplicate([1, 2, 3, 1], 3))

    def test_example_2(self):
        self.assertTrue(self.containsNearbyDuplicate([1, 0, 1, 1], 1))

    def test_example_3(self):
        self.assertFalse(self.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))

    def test_leetcode_100(self):
        self.assertFalse(self.containsNearbyDuplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 15))

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set(nums[:k])
        if len(window) < min(len(nums), k):
            return True

        for i in range(k, len(nums)):
            n = nums[i]
            if n in window:
                return True

            window.add(n)
            window.remove(nums[i - k])
        return False
