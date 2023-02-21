"""
LeetCode: https://leetcode.com/problems/single-element-in-a-sorted-array/

You are given a sorted array consisting of only integers where every element appears exactly twice, except for one
element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.

## Example 1

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2

## Example 2

Input: nums = [3,3,7,7,10,11,11]
Output: 10

** Constraints

* 1 <= nums.length <= 10^5
* 0 <= nums[i] <= 10^5
"""
from typing import List
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        self.assertEqual(2, self.singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]))
        self.assertEqual(2, self.singleNonDuplicateBinarySearch([1, 1, 2, 3, 3, 4, 4, 8, 8]))

    def test_example_2(self):
        self.assertEqual(10, self.singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]))
        self.assertEqual(10, self.singleNonDuplicateBinarySearch([3, 3, 7, 7, 10, 11, 11]))

    def test_example_3(self):
        self.assertEqual(1, self.singleNonDuplicate([1, 2, 2, 3, 3, 4, 4, 8, 8]))
        self.assertEqual(1, self.singleNonDuplicateBinarySearch([1, 2, 2, 3, 3, 4, 4, 8, 8]))

    def singleNonDuplicateBinarySearch(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2

            halves_are_even = (right - mid) % 2 == 0
            if nums[mid + 1] == nums[mid]:
                if halves_are_even:
                    left = mid + 2
                else:
                    right = mid - 1
            elif nums[mid - 1] == nums[mid]:
                if halves_are_even:
                    right = mid - 2
                else:
                    left = mid + 1
            else:
                return nums[mid]

        return nums[left]

    def singleNonDuplicate(self, nums: List[int]) -> int:
        result = 0
        for n in nums:
            result ^= n

        return result
