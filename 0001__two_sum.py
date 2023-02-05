"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

## Example 1

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

## Example 2

Input: nums = [3,2,4], target = 6
Output: [1,2]

## Example 3

Input: nums = [3,3], target = 6
Output: [0,1]

## Constraints

* 2 <= nums.length <= 10^4
* -10^9 <= nums[i] <= 10^9
* -10^9 <= target <= 10^9
* Only one valid answer exists.

## Follow-up

Can you come up with an algorithm that is less than O(n2) time complexity?
"""
from typing import List, Dict
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        self.assertEqual([0, 1], sorted(self.twoSum([2, 7, 11, 15], 9)))

    def test_example_2(self):
        self.assertEqual([1, 2], sorted(self.twoSum([3, 2, 4], 6)))

    def test_example_3(self):
        self.assertEqual([0, 1], sorted(self.twoSum([3, 3], 6)))

    # The real solution. Speed: O(n), Space O(2n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap: Dict[int, int] = {}
        for i, first in enumerate(nums):
            t = target - first
            if t in hashmap:
                return [i, hashmap[t]]
            else:
                hashmap[first] = i
