import unittest
from typing import List


class Solution(unittest.TestCase):
    def test_example_1(self):
        expected = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
        result = self.subsets([1, 2, 3])

        expected.sort()
        result.sort()

        self.assertEqual(result, expected)

    def test_example_2(self):
        expected = [[], [0]]
        result = self.subsets([0])

        expected.sort()
        result.sort()

        self.assertEqual(result, expected)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []

        for option in range(2 ** len(nums)):
            mutation = []
            for ptr in range(len(nums)):
                if (option >> ptr) & 1 == 1:
                    mutation.append(nums[ptr])
            results.append(mutation)

        return results

    def subsetsRecursive(self, nums: List[int]) -> List[List[int]]:
        results = []

        def helper(ptr: int, mutation: List[int]):
            if ptr == len(nums):
                results.append(mutation.copy())
                return

            mutation.append(nums[ptr])
            helper(ptr + 1, mutation)
            mutation.pop()
            helper(ptr + 1, mutation)

        helper(0, [])

        return results
