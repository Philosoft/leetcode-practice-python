"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every
element is distinct.

## Example 1

Input: nums = [1,2,3,1]
Output: true

## Example 2

Input: nums = [1,2,3,4]
Output: false

## Example 3

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

## Constraints

* 1 <= nums.length <= 10^5
* -10^9 <= nums[i] <= 10^9
"""
from typing import List, Set
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        self.assertTrue(self.containsDuplicate([1, 2, 3, 1]))

    def test_exmaple_2(self):
        self.assertFalse(self.containsDuplicate([1, 2, 3, 4]))

    def test_example_3(self):
        self.assertTrue(self.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))

    def containsDuplicate(self, nums: List[int]) -> bool:
        seen: Set[int] = set()

        for n in nums:
            if n in seen:
                return True
            seen.add(n)

        return False
