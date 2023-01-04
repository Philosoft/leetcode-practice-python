import unittest
from typing import List


class Solution(unittest.TestCase):
    def test_example_1(self):
        arr = [0, 1, 0]
        expected = 1

        self.assertEqual(expected, self.peakIndexInMountainArray(arr))

    def test_example_2(self):
        arr = [0, 2, 1, 0]
        expected = 1

        self.assertEqual(expected, self.peakIndexInMountainArray(arr))

    def test_example_3(self):
        arr = [0, 10, 5, 2]
        expected = 1

        self.assertEqual(expected, self.peakIndexInMountainArray(arr))

    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 1, len(arr) - 2

        while left <= right:
            m = left + (right - left) // 2

            # peak
            if arr[m - 1] < arr[m] > arr[m + 1]:
                return m

            # to the left of peak
            if arr[m] < arr[m + 1] > arr[m + 2]:
                return m + 1

            # to the right of peak
            if arr[m] < arr[m - 1] < arr[m + 1]:
                return m - 1

            # slope
            if arr[m - 1] < arr[m]:
                left = m + 1
            else:
                right = m

        return -1
