"""
A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the
same.
Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise,
return false.


Example 1:

Input:
    arr = [3,5,1]
Output:
    true
Explanation:
    We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, between each consecutive
    elements.
Example 2:

Input:
    arr = [1,2,4]
Output:
    false
Explanation:
    There is no way to reorder the elements to obtain an arithmetic progression.

Constraints:

* 2 <= arr.length <= 1000
* -10^6 <= arr[i] <= 10^6
"""
from typing import List
from unittest import TestCase


class Solution(TestCase):
    def test(self):
        options = [
            (True, [3, 5, 1]),
            (False, [1, 2, 4]),
            (True, [1, 1, 1, 1, 1]),
            (True, [0, 0, 0, 0, 0]),
        ]

        for expected, arr in options:
            with self.subTest():
                self.assertEqual(expected, self.canMakeArithmeticProgression(arr))

    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        """
        Since max length of list is 1k according to constrains O(n log n) is quite an acceptable complexity
        Idea for a better solution (kudos to community)
            * find min and max
            * find diff between them
            * divide diff by len(arr) - 1 - that must be delta between sorted elements
            * sort array / check for existing values using that arr[i] must be min + i * delta
        """
        arr.sort()
        diff = arr[0] - arr[1]
        for i in range(len(arr) - 1):
            if arr[i] - arr[i + 1] != diff:
                return False

        return True
