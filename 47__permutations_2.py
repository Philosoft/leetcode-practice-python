"""
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order

## Example 1:

Input: nums = [1,1,2]
Output:
    [[1,1,2],
    [1,2,1],
    [2,1,1]]

## Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

## Constraints:

* 1 <= nums.length <= 8
* -10 <= nums[i] <= 10
"""
from collections import Counter
from typing import List
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        expected = [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
        answer = self.permuteUnique([1, 1, 2])
        answer.sort()

        self.assertEqual(expected, answer)

    def test_example_2(self):
        expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        expected.sort()
        answer = self.permuteUnique([1, 2, 3])
        answer.sort()

        self.assertEqual(expected, answer)

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        counter = Counter(nums)
        perm = []

        def helper() -> None:
            if len(perm) == len(nums):
                result.append(perm.copy())
                return

            for n in counter.keys():
                if counter[n] > 0:
                    perm.append(n)
                    counter[n] -= 1

                    helper()

                    perm.pop()
                    counter[n] += 1

        helper()

        return result
