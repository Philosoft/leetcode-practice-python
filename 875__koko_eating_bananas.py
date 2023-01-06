import unittest
from math import ceil
from typing import List


class Solution(unittest.TestCase):
    def test_example_1(self):
        piles = [3, 6, 7, 11]
        h = 8
        self.assertEqual(4, self.minEatingSpeed(piles, h))

    def test_example_2(self):
        piles = [30, 11, 23, 4, 20]
        h = 5
        self.assertEqual(30, self.minEatingSpeed(piles, h))

    def test_example_3(self):
        piles = [30, 11, 23, 4, 20]
        h = 6
        self.assertEqual(23, self.minEatingSpeed(piles, h))

    def test_huge_pile(self):
        self.assertEqual(2, self.minEatingSpeed([312884470], 312884469))

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = 1

        while left <= right:
            mid = left + (right - left) // 2

            hours = 0
            for p in piles:
                hours += ceil(p / mid)
                if hours > h:
                    break

            if hours <= h:
                res = mid
                right = mid - 1
            elif hours > h:
                left = mid + 1
            else:
                right = mid - 1

        return res
