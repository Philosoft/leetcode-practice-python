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
        self.assertEqual(5, self.findKthLargestHeap([3, 2, 1, 5, 6, 4], 2))

    def test_example_2(self):
        self.assertEqual(4, self.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
        self.assertEqual(4, self.findKthLargestHeap([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))

    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        quick select algo
        """
        k = len(nums) - k

        def quick_select(left: int, right: int) -> int:
            swap_ptr = left
            pivot = nums[right]
            for i in range(left, right):
                if nums[i] <= pivot:
                    nums[swap_ptr], nums[i] = nums[i], nums[swap_ptr]
                    swap_ptr += 1
            nums[swap_ptr], nums[right] = nums[right], nums[swap_ptr]

            if swap_ptr < k:
                # target is on the right
                return quick_select(swap_ptr + 1, right)
            elif swap_ptr > k:
                return quick_select(left, swap_ptr - 1)
            else:
                return nums[swap_ptr]

        return quick_select(0, len(nums) - 1)

    def findKthLargestHeap(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = -nums[i]

        heapify(nums)
        while k > 1:
            heappop(nums)
            k -= 1

        return -heappop(nums)
