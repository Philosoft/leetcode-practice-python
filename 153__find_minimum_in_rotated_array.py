"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array
nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array
[a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

## Example 1

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

## Example 2

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

## Example 3

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times.

## Constraints

* n == nums.length
* 1 <= n <= 5000
* -5000 <= nums[i] <= 5000
* All the integers of nums are unique.
* nums is sorted and rotated between 1 and n times.
"""

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
