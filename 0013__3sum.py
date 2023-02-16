"""
LeetCode: https://leetcode.com/problems/3sum/

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

## Example 1

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
    nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
    nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
    nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
    The distinct triplets are [-1,0,1] and [-1,-1,2].
    Notice that the order of the output and the order of the triplets does not matter.

## Example 2

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

## Example 3

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

## Constraints

* 3 <= nums.length <= 3000
* -10^5 <= nums[i] <= 10^5
"""
from typing import List
from unittest import TestCase


class Solution(TestCase):
    def test_it(self):
        options = [
            ('example 1', [[-1, -1, 2], [-1, 0, 1]], [-1, 0, 1, 2, -1, -4]),
            ('example 2', [], [0, 1, 1]),
            ('example 3', [[0, 0, 0]], [0, 0, 0]),
            ('test 79 (4 zeroes)', [[0, 0, 0]], [0, 0, 0, 0]),
        ]

        for name, expected, nums in options:
            with self.subTest(name):
                expected.sort()
                answer = self.threeSum(nums)
                answer.sort()

                self.assertEqual(expected, answer)

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        i = 0
        while i < len(nums) - 2:
            if nums[i] > 0:
                break

            left, right = i + 1, len(nums) - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left - 1] == nums[left]:
                        left += 1
                elif s < 0:
                    left += 1
                else:
                    right -= 1

            i += 1
            while i < len(nums) - 2 and nums[i - 1] == nums[i]:
                i += 1

        return result
