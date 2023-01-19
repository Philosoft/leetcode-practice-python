"""
Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

Constraints:

* 1 <= s.length <= 10^5
* s[i] is a printable ascii character.
"""
from typing import List
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        expected = ["o", "l", "l", "e", "h"]
        s = ["h", "e", "l", "l", "o"]
        self.reverseString(s)

        self.assertEqual(expected, s)

    def test_example_2(self):
        expected = ["h", "a", "n", "n", "a", "H"]
        s = ["H", "a", "n", "n", "a", "h"]

        self.reverseString(s)
        self.assertEqual(expected, s)

    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
