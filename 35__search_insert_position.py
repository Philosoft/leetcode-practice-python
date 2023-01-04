import unittest
from typing import List


class Solution(unittest.TestCase):
    def test_example_1(self):
        nums = [1, 3, 5, 6]
        target = 5
        expected = 2

        self.assertEqual(expected, self.searchInsert(nums, target))

    def test_example_2(self):
        nums = [1, 3, 5, 6]
        target = 2
        expected = 1

        self.assertEqual(expected, self.searchInsert(nums, target))

    def test_example_3(self):
        nums = [1, 3, 5, 6]
        target = 7
        expected = 4

        self.assertEqual(expected, self.searchInsert(nums, target))

    def test_empty(self):
        self.assertEqual(self.searchInsert([], 5), 0)

    def test_one_after(self):
        self.assertEqual(self.searchInsert([1], 2), 1)

    def test_one_before(self):
        self.assertEqual(self.searchInsert([2], 1), 0)

    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if target == nums[mid]:
                return mid

            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return left
