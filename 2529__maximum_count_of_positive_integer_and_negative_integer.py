import unittest
from typing import List


class Solution(unittest.TestCase):
    def test(self):
        options = [
            ('negative and positive', [-2, -1, -1, 1, 2, 3], 3),
            ('everything with two zeroes', [-3, -2, -1, 0, 0, 1, 2], 3),
            ('all positive', [5, 20, 66, 1314], 4),
            ('all zeroes', [0, 0, 0, 0, 0, 0, 0], 0),
            ('1 negative + zero', [-1, 0], 1),
            ('all negative', [-1, -1, -1, -1, -1], 5),
        ]
        for name, nums, expected in options:
            with self.subTest(name):
                self.assertEqual(expected, self.maximumCount(nums))

    def maximumCount(self, nums: List[int]) -> int:
        """
        The best solution would be to use binary search to search for leftmost and rightmost 0
        then calculate counts from these indices and len(nums)
        but since max length of nums is 2000, brute force will do
        """
        neg, pos = 0, 0
        for n in nums:
            if n < 0:
                neg += 1
            if n > 0:
                pos += 1

        return max(neg, pos)
