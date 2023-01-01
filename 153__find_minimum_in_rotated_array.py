import unittest
from typing import List


class Solution(unittest.TestCase):
    def test_edge(self):
        self.assertEqual(self.findMin([0]), 0, "Should be 0")

    def test_simple_right(self):
        self.assertEqual(self.findMin([3, 4, 5, 1, 2]), 1)

    def test_simple_left(self):
        self.assertEqual(self.findMin([5, 1, 2, 3, 4]), 1)

    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            m = left + (right - left) // 2

            if m + 1 < len(nums) and nums[m] > nums[m + 1]:
                return nums[m + 1]

            if m > 0 and nums[m] < nums[m - 1]:
                return nums[m]

            if nums[right] > nums[m]:
                right = m - 1
            else:
                left = m + 1

        return nums[left]
