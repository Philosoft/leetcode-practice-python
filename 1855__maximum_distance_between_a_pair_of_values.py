"""
You are given two non-increasing 0-indexed integer arrays nums1 and nums2.
A pair of indices (i, j), where 0 <= i < nums1.length and 0 <= j < nums2.length, is valid if both
    i <= j
    and nums1[i] <= nums2[j].
The distance of the pair is j - i.
Return the maximum distance of any valid pair (i, j). If there are no valid pairs, return 0.
An array arr is non-increasing if arr[i-1] >= arr[i] for every 1 <= i < arr.length.


Example 1:

Input:
    nums1 = [55,30,5,4,2]
    nums2 = [100,20,10,10,5]
Output: 2
Explanation:
    The valid pairs are (0,0), (2,2), (2,3), (2,4), (3,3), (3,4), and (4,4).
    The maximum distance is 2 with pair (2,4).

Example 2:

Input:
    nums1 = [2,2,2],
    nums2 = [10,10,1]
Output: 1
Explanation:
    The valid pairs are (0,0), (0,1), and (1,1).
    The maximum distance is 1 with pair (0,1).

Example 3:

Input:
    nums1 = [30,29,19,5]
    nums2 = [25,25,25,25,25]
Output: 2
Explanation:
    The valid pairs are (2,2), (2,3), (2,4), (3,3), and (3,4).
    The maximum distance is 2 with pair (2,4).
"""
import unittest
from typing import List


class Solution(unittest.TestCase):
    def test_examples(self):
        options = [
            (2, [55, 30, 5, 4, 2], [100, 20, 10, 10, 5]),
            (1, [2, 2, 2], [10, 10, 1]),
            (2, [30, 29, 19, 5], [25, 25, 25, 25, 25]),
        ]

        for expected, n1, n2 in options:
            with self.subTest():
                self.assertEqual(expected, self.maxDistance(n1, n2))

    def test_maxi_lists(self):
        n1 = [1] * 100_000
        n2 = [0] * 100_000

        self.assertEqual(0, self.maxDistance(n1, n2))

    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        m = 0
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                # pair is established, let's search for rightmost option
                left, right = j, len(nums2) - 1
                rightmost = j
                while left <= right:
                    mid = left + (right - left) // 2

                    if nums2[mid] >= nums1[i]:
                        # mada - mada
                        rightmost = mid
                        left = mid + 1
                    else:
                        right = mid - 1

                if nums1[i] <= nums2[rightmost]:
                    m = max(m, rightmost - i)
                    j = rightmost + 1
                    i += 1
                else:
                    i += 1
            else:
                i += 1

        return m

    def maxDistanceBrute(self, nums1: List[int], nums2: List[int]) -> int:
        m = 0
        left, right = 0, 0
        while left < len(nums1) and right < len(nums2):
            while right + 1 < len(nums2) and nums1[left] <= nums2[right + 1]:
                right += 1

            if nums1[left] <= nums2[right]:
                m = max(m, right - left)
            left += 1

        return m
