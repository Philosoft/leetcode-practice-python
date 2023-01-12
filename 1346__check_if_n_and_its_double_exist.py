import unittest
from collections import defaultdict
from typing import List

"""
Given an array arr of integers, check if there exist two indices i and j such that :

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]
 

Example 1:

Input: arr = [10,2,5,3]
Output: true
Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]

Example 2:

Input: arr = [3,1,7,11]
Output: false
Explanation: There is no i and j that satisfy the conditions.
 

Constraints:

2 <= arr.length <= 500
-10^3 <= arr[i] <= 10^3
"""


class Solution(unittest.TestCase):
    def test_example_1(self):
        self.assertTrue(self.checkIfExist([10, 2, 5, 3]))
        self.assertTrue(self.checkIfExistBrute([10, 2, 5, 3]))
        self.assertTrue(self.checkIfExistHash([10, 2, 5, 3]))

    def test_example_2(self):
        self.assertFalse(self.checkIfExist([3, 1, 7, 11]))
        self.assertFalse(self.checkIfExistBrute([3, 1, 7, 11]))
        self.assertFalse(self.checkIfExistHash([3, 1, 7, 11]))

    def test_my_example(self):
        self.assertFalse(self.checkIfExist([0, 1]))
        self.assertFalse(self.checkIfExistBrute([0, 1]))
        self.assertFalse(self.checkIfExistHash([0, 1]))

    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        for i in range(len(arr)):
            if self.search(arr, arr[i] * 2, i):
                return True

        return False

    def search(self, arr: List[int], target: int, ignore_index: int) -> bool:
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = left + (right - left) // 2

            if arr[mid] == target:
                if mid != ignore_index:
                    return True

                if (mid - 1 >= 0 and arr[mid - 1] == target) or (mid + 1 < len(arr) and arr[mid + 1] == target):
                    return True

                return False

            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return arr[mid] == target

    def checkIfExistHash(self, arr: List[int]) -> bool:
        lookup = defaultdict(set)
        for i in range(len(arr)):
            lookup[arr[i]].add(i)

        for i in range(len(arr)):
            target = arr[i] * 2
            if target in lookup:
                if len(lookup[target]) > 1 or i not in lookup[target]:
                    return True

        return False

    def checkIfExistBrute(self, arr: List[int]) -> bool:
        """
        brute force
        T: O(n ** 2), S: O(1)
        """
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] == 2 * arr[j] or arr[j] == 2 * arr[i]:
                    return True

        return False
