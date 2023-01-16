"""
Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive
(i.e. nums[left] + nums[left + 1] + ... + nums[right]).


Example 1:

Input:
    ["NumArray", "sumRange", "sumRange", "sumRange"]
    [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output:
    [null, 1, -1, -3]
Explanation:
    NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
    numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
    numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
    numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3


Constraints:

* 1 <= nums.length <= 10^4
* -10^5 <= nums[i] <= 10^5
* 0 <= left <= right < nums.length
* At most 10^4 calls will be made to sumRange.
"""
from typing import List
from unittest import TestCase


class TestNumArray(TestCase):
    def test(self):
        arr = NumArray([-2, 0, 3, -5, 2, -1])
        self.assertEqual(1, arr.sumRange(0, 2))
        self.assertEqual(-1, arr.sumRange(2, 5))
        self.assertEqual(-3, arr.sumRange(0, 5))


class NumArray:
    def __init__(self, nums: List[int]):
        self.prefixes = [nums[0]]
        for i in range(1, len(nums)):
            self.prefixes.append(self.prefixes[i - 1] + nums[i])

    def sumRange(self, left: int, right: int) -> int:
        left = self.prefixes[left - 1] if left > 0 else 0
        right = self.prefixes[right]

        return right - left
