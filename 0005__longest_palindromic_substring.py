"""
LeetCode: https://leetcode.com/problems/longest-palindromic-substring/

[[Blind75]]

Given a string s, return the longest palindromic substring in s.

## Example 1

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

## Example 2

Input: s = "cbbd"
Output: "bb"

## Constraints

* 1 <= s.length <= 1000
* s consist of only digits and English letters.
"""
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        self.assertEqual("bab", self.longestPalindrome("babad"))

    def longestPalindrome(self, s: str) -> str:
        longest = s[0]

        for i in range(len(s)):
            # odd length
            left, right = i - 1, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > len(longest):
                    longest = s[left:right + 1]
                left -= 1
                right += 1

            # even length
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > len(longest):
                    longest = s[left:right + 1]
                left -= 1
                right += 1

        return longest
