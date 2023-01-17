"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements
Note that you must do this in-place without making a copy of the array.


Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:

Input: nums = [0]
Output: [0]

Constraints:

* 1 <= nums.length <= 10^4
* -231 <= nums[i] <= 231 - 1

Follow up: Could you minimize the total number of operations done?
"""
from typing import List
from unittest import TestCase


class Solution(TestCase):
    def test(self):
        options = [
            ('generic', [1, 3, 12, 0, 0], [0, 1, 0, 3, 12]),
            ('one zero', [0], [0]),
            ('one 1', [1], [1]),
            ('only zeroes', [0, 0, 0, 0], [0, 0, 0, 0]),
            ('complex case', [4, 2, 4, 3, 5, 1, 0, 0, 0, 0], [4, 2, 4, 0, 0, 3, 0, 5, 1, 0])
        ]

        for name, expected, nums in options:
            with self.subTest(name):
                orig_nums = nums.copy()
                self.moveZeroes(nums)
                self.assertEqual(expected, nums)

                nums = orig_nums.copy()
                self.moveZeroesSnowball(nums)
                self.assertEqual(expected, nums)

    def moveZeroesSnowball(self, nums: List[int]) -> None:
        snowball_size = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                snowball_size += 1
                continue
            else:
                nums[i], nums[i - snowball_size] = nums[i - snowball_size], nums[i]

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_ptr, non_zero_ptr = 0, 0
        while zero_ptr < len(nums) and non_zero_ptr < len(nums):
            while zero_ptr < len(nums) and nums[zero_ptr] != 0:
                zero_ptr += 1

            # zero_ptr is either out of bounds -> we are finished, or it's pointing to zero
            if zero_ptr >= len(nums):
                return

            non_zero_ptr = zero_ptr + 1
            while non_zero_ptr < len(nums) and nums[non_zero_ptr] == 0:
                non_zero_ptr += 1

            if non_zero_ptr >= len(nums):
                return

            nums[zero_ptr], nums[non_zero_ptr] = nums[non_zero_ptr], nums[zero_ptr]
