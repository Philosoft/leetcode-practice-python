"""
Given an array of integers arr and two integers k and threshold, return the number of sub-arrays of size k and average
greater than or equal to threshold.

Example 1:

Input:
    arr = [2,2,2,2,5,5,5,8]
    k = 3
    threshold = 4
Output:
    3
Explanation:
    Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively.
    All other sub-arrays of size 3 have averages less than 4 (the threshold).

Example 2:

Input:
    arr = [11,13,17,23,29,31,7,5,2,3]
    k = 3
    threshold = 5
Output:
    6
Explanation:
    The first 6 sub-arrays of size 3 have averages greater than 5. Note that averages are not integers.

Constraints:

* 1 <= arr.length <= 10^5
* 1 <= arr[i] <= 10^4
* 1 <= k <= arr.length
* 0 <= threshold <= 10^4
"""
from typing import List
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        self.assertEqual(3, self.numOfSubarrays([2, 2, 2, 2, 5, 5, 5, 8], 3, 4))

    def test_example_2(self):
        self.assertEqual(6, self.numOfSubarrays([11, 13, 17, 23, 29, 31, 7, 5, 2, 3], 3, 5))

    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        if len(arr) < k:
            return 0

        count = 0
        sliding_sum = sum(arr[:k])
        if sliding_sum / k >= threshold:
            count += 1

        for i in range(k, len(arr)):
            sliding_sum = sliding_sum - arr[i - k] + arr[i]
            if sliding_sum / k >= threshold:
                count += 1

        return count
