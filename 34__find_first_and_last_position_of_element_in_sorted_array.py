import unittest
from typing import List


class Solution(unittest.TestCase):
    def test_example_1(self):
        nums = [5, 7, 7, 8, 8, 10]
        target = 8
        expected = [3, 4]

        self.assertEqual(expected, self.searchRange(nums, target))

    def test_example_2(self):
        nums = [5, 7, 7, 8, 8, 10]
        target = 6
        expected = [-1, -1]

        self.assertEqual(expected, self.searchRange(nums, target))

    def test_example_3(self):
        nums = []
        target = 0
        expected = [-1, -1]

        self.assertEqual(expected, self.searchRange(nums, target))

    def test_uniform_list(self):
        nums = [1] * 1000
        target = 1
        expected = [0, 999]

        self.assertEqual(expected, self.searchRange(nums, target))

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        # search right edge
        left, right = 0, len(nums) - 1
        right_ptr = - 1
        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] <= target:
                left = mid + 1
                right_ptr = mid
            else:
                right = mid - 1

        if nums[right_ptr] != target:
            return [-1, -1]

        answer = [-1, right_ptr]

        # search left edge
        left, right = 0, right_ptr
        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] >= target:
                right = mid - 1
                left_ptr = mid
            else:
                left = mid + 1

        answer[0] = left

        return answer
