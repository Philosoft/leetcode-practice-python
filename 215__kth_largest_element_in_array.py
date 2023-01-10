import unittest
from heapq import heapify, heappop
from typing import List

"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

You must solve it in O(n) time complexity.


Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
"""


class Solution(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(5, self.findKthLargest([3, 2, 1, 5, 6, 4], 2))

    def test_example_2(self):
        self.assertEqual(4, self.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))

    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = -nums[i]

        heapify(nums)
        while k > 1:
            heappop(nums)
            k -= 1

        return -heappop(nums)
