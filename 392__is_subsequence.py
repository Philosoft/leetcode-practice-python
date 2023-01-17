"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the
characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of
"abcde" while "aec" is not).


Example 1:

Input:
    s = "abc"
    t = "ahbgdc"
Output: true

Example 2:

Input:
    s = "axc"
    t = "ahbgdc"
Output: false

Constraints:

* 0 <= s.length <= 100
* 0 <= t.length <= 10^4
* s and t consist only of lowercase English letters.

Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one
to see if t has its subsequence. In this scenario, how would you change your code?
"""
from unittest import TestCase


class Solution(TestCase):
    def test(self):
        options = [
            (True, "abc", "ahbgdc"),
            (False, "axc", "ahbgdc"),
        ]

        for expected, a, b in options:
            with self.subTest(a):
                self.assertEqual(expected, self.isSubsequence(a, b))

    def isSubsequence(self, s: str, t: str) -> bool:
        left, right = 0, 0
        while left < len(s) and right < len(t):
            while right < len(t) and s[left] != t[right]:
                right += 1
            if right < len(t) and s[left] == t[right]:
                left += 1
                right += 1

        return left == len(s)
