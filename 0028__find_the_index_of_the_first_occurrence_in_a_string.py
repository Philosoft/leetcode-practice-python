"""
LeetCode: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle
is not part of haystack.

## Example 1

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation:
    "sad" occurs at index 0 and 6.
    The first occurrence is at index 0, so we return 0.

## Example 2

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

## Constraints

* 1 <= haystack.length, needle.length <= 10^4
* haystack and needle consist of only lowercase English characters.
"""
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        self.assertEqual(0, self.strStr("sadbutsad", "sad"))

    def test_example_2(self):
        self.assertEqual(-1, self.strStr("leetcode", "leeto"))

    def test_case_73(self):
        self.assertEqual(4, self.strStr("mississippi", "issip"))

    def strStr(self, haystack: str, needle: str) -> int:
        left = 0
        while left < len(haystack):
            right = 0
            while left < len(haystack) and haystack[left] != needle[right]:
                left += 1

            pos = left
            while left < len(haystack) and right < len(needle) and haystack[left] == needle[right]:
                left += 1
                right += 1

            if right == len(needle):
                return pos
            left = pos + 1

        return -1
