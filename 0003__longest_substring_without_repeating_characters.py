"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string s, find the length of the longest
substring without repeating characters.

## Example 1

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

## Example 2

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

## Example 3

Input: s = "pwwkew"
Output: 3
Explanation:
    The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

## Constraints

* 0 <= s.length <= 5 * 10^4
* s consists of English letters, digits, symbols and spaces.
"""
from typing import Set
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        self.assertEqual(3, self.lengthOfLongestSubstring("abcabcbb"))

    def test_example_2(self):
        self.assertEqual(1, self.lengthOfLongestSubstring("bbbbb"))

    def test_example_3(self):
        self.assertEqual(3, self.lengthOfLongestSubstring("pwwkew"))

    def lengthOfLongestSubstring(self, s: str) -> int:
        m = 0
        left, right = 0, 0
        window: Set[str] = set()
        current_length = 0
        while right < len(s):
            if s[right] not in window:
                window.add(s[right])
                current_length += 1
                m = max(m, current_length)
            else:
                while s[left] != s[right]:
                    window.remove(s[left])
                    left += 1
                    current_length -= 1
                left += 1
            right += 1

        return m
