import unittest
from typing import List


class Solution(unittest.TestCase):
    def test_example_1(self):
        self.assertEquals(self.subsets([1, 2, 3]), [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]])

    def test_example_2(self):
        self.assertEquals(self.subsets([0]), [[], [0]])

    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []

        for option in range(2 ** len(nums)):
            mutation = []
            for ptr in range(len(nums)):
                if (option >> ptr) & 1 == 1:
                    mutation.append(nums[ptr])
            results.append(mutation)

        return results
