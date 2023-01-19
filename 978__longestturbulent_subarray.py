"""
Given an integer array arr, return the length of a maximum size turbulent subarray of arr.

A subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

More formally, a subarray [arr[i], arr[i + 1], ..., arr[j]] of arr is said to be turbulent if and only if:

For i <= k < j:
* arr[k] > arr[k + 1] when k is odd, and
* arr[k] < arr[k + 1] when k is even.
Or, for i <= k < j:
* arr[k] > arr[k + 1] when k is even, and
* arr[k] < arr[k + 1] when k is odd.

Example 1:

Input: arr = [9,4,2,10,7,8,8,1,9]
Output: 5
Explanation: arr[1] > arr[2] < arr[3] > arr[4] < arr[5]

Example 2:

Input: arr = [4,8,12,16]
Output: 2

Example 3:

Input: arr = [100]
Output: 1

Constraints:

* 1 <= arr.length <= 4 * 10^4
* 0 <= arr[i] <= 10^9
"""
from typing import List
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        self.assertEqual(5, self.maxTurbulenceSize([9, 4, 2, 10, 7, 8, 8, 1, 9]))

    def test_example_2(self):
        self.assertEqual(2, self.maxTurbulenceSize([4, 8, 12, 16]))

    def test_Example_3(self):
        self.assertEqual(1, self.maxTurbulenceSize([100]))

    def test_leetcode_100(self):
        self.assertEqual(5, self.maxTurbulenceSize([0, 1, 1, 0, 1, 0, 1, 1, 0, 0]))

    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1

        max_len = 1
        should_be_greater = arr[0] > arr[1]
        length_so_far = 1
        for right in range(0, len(arr) - 1):
            if should_be_greater:
                if arr[right] > arr[right + 1]:
                    length_so_far += 1
                    max_len = max(max_len, length_so_far)
                    should_be_greater = False
                else:
                    if arr[right] == arr[right + 1]:
                        length_so_far = 1
                    else:
                        length_so_far = 2
            else:
                if arr[right] < arr[right + 1]:
                    length_so_far += 1
                    max_len = max(max_len, length_so_far)
                    should_be_greater = True
                else:
                    if arr[right] == arr[right + 1]:
                        length_so_far = 1
                    else:
                        length_so_far = 2

        return max_len
