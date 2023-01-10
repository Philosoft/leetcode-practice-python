import unittest
from typing import List


class Solution(unittest.TestCase):
    def test(self):
        options = [
            (2, [3, 5]),
            (-1, [0, 0]),
            (3, [0, 4, 3, 0, 4])
        ]

        for expected, arr in options:
            with self.subTest():
                self.assertEqual(expected, self.specialArray(arr))

    def specialArray(self, nums: List[int]) -> int:
        left, right = 0, len(nums)
        while left <= right:
            mid = left + (right - left) // 2

            gte_count = 0
            for n in nums:
                if n >= mid:
                    gte_count += 1
                    if gte_count > mid:
                        break

            if gte_count == mid:
                return mid

            if gte_count > mid:
                left = mid + 1
            else:
                right = mid - 1

        return -1
