"""
Given a string s, partition s such that every substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.

## Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

## Example 2:

Input: s = "a"
Output: [["a"]]

## Constraints

* 1 <= s.length <= 16
* s contains only lowercase English letters.
"""
from functools import cache
from typing import List
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        expected = [["a", "a", "b"], ["aa", "b"]]
        expected.sort()
        answer = self.partition("aab")
        answer.sort()

        self.assertEqual(expected, answer)

    def test_example_2(self):
        self.assertEqual([["a"]], (self).partition("a"))

    def partition(self, s: str) -> List[List[str]]:
        result = []

        @cache
        def is_palindrome(word: str) -> bool:
            if len(word) == 1:
                return True

            left, right = 0, len(word) - 1
            while left < right:
                if word[left] != word[right]:
                    return False
                left += 1
                right -= 1
            return True

        option = []

        def bt(start: int):
            if start >= len(s):
                result.append(option.copy())
                return

            for end in range(start, len(s)):
                if is_palindrome(s[start:end + 1]):
                    option.append(s[start:end + 1])
                    bt(end + 1)
                    option.pop()

        bt(0)

        return result
