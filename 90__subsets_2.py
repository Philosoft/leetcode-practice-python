import unittest
from typing import List


class Solution(unittest.TestCase):
    def test_example_1(self):
        nums = [1, 2, 2]
        expected = [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
        expected.sort()
        answer = self.subsetsWithDup(nums)
        answer.sort()

        self.assertEqual(expected, answer)

    def test_example_2(self):
        nums = [0]
        expected = [[], [0]]
        expected.sort()
        answer = self.subsetsWithDup(nums)
        answer.sort()

        self.assertEqual(expected, answer)

    def test_simple(self):
        expected = [[], [1], [1, 2], [2]]
        expected.sort()
        answer = self.subsetsWithDup([1, 2])
        answer.sort()

        self.assertEqual(expected, answer)

    def test_absurd(self):
        nums = [4, 4, 4, 1, 4]
        expected = [[], [1], [1, 4], [1, 4, 4], [1, 4, 4, 4], [1, 4, 4, 4, 4], [4], [4, 4], [4, 4, 4], [4, 4, 4, 4]]
        expected.sort()

        answer = self.subsetsWithDup(nums)
        answer.sort()

        self.assertEqual(answer, expected)

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        answer = []
        stack = []
        nums.sort()

        def helper(ptr: int = 0):
            if ptr == len(nums):
                answer.append(stack.copy())
                return

            stack.append(nums[ptr])
            helper(ptr + 1)
            stack.pop()

            while ptr + 1 < len(nums) and nums[ptr] == nums[ptr + 1]:
                ptr += 1
            helper(ptr + 1)

        helper()

        return answer
