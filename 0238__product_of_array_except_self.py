"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of
nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

## Example 1

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

## Example 2

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

## Constraints

* 2 <= nums.length <= 10^5
* -30 <= nums[i] <= 30
* The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

## Follow up

Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space
complexity analysis.)
"""
import operator
from functools import reduce
from typing import List
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        self.assertEqual([24, 12, 8, 6], self.productExceptSelf([1, 2, 3, 4]))

    def test_example_2(self):
        self.assertEqual([0, 0, 9, 0, 0], self.productExceptSelf([-1, 1, 0, -3, 3]))

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = nums.copy()

        prefix = [1] * len(nums)
        product = 1
        for i in range(1, len(nums)):
            product *= nums[i - 1]
            prefix[i] = product

        postfix = [1] * len(nums)
        product = 1
        for i in range(len(nums) - 2, -1, -1):
            product *= nums[i + 1]
            postfix[i] = product

        for i in range(len(result)):
            result[i] = prefix[i] * postfix[i]

        return result
