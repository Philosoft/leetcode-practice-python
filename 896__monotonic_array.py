import unittest
from typing import List


class Solution(unittest.TestCase):
    def test_example_1(self):
        self.assertTrue(self.isMonotonic([1, 2, 2, 3]))

    def test_example_2(self):
        self.assertTrue(self.isMonotonic([6, 5, 4, 4]))

    def test_example_3(self):
        self.assertFalse(self.isMonotonic([1, 3, 2]))

    def test_one_element(self):
        self.assertTrue(self.isMonotonic([0]))

    def test_same_elements(self):
        self.assertTrue(self.isMonotonic([1, 1, 1, 1]))

    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        is_inc, is_dec = True, True
        i = 0
        while i + 1 < len(nums) and is_inc and is_dec:
            if nums[i] > nums[i + 1]:
                is_inc = False
            if nums[i] < nums[i + 1]:
                is_dec = False
            i += 1

        for ptr in range(i + 1, len(nums)):
            if is_inc and nums[ptr - 1] > nums[ptr]:
                is_inc = False
                break
            if is_dec and nums[ptr - 1] < nums[ptr]:
                is_dec = False
                break

        return is_inc or is_dec
