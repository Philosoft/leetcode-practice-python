"""
LeetCode: https://leetcode.com/problems/longest-common-subsequence/description/

Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common
subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted
without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

## Example 1

Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.

## Example 2

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

## Example 3

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

## Constraints

* 1 <= text1.length, text2.length <= 1000
* text1 and text2 consist of only lowercase English characters.
"""
from typing import Dict, Tuple
from unittest import TestCase


class Solution(TestCase):
    def test_it(self):
        options = [
            ('example 1', 3, 'abcde', 'ace'),
            ('example 2', 3, 'abc', 'abc'),
            ('example 3', 0, 'abc', 'def'),
            ('tricky example', 1, 'bl', 'yby'),
        ]

        for name, expected, txt1, txt2 in options:
            with self.subTest(name):
                self.assertEqual(expected, self.longestCommonSubsequenceBottomUp(txt1, txt2))
                self.assertEqual(expected, self.longestCommonSubsequenceTopDown(txt1, txt2))
                self.assertEqual(expected, self.longestCommonSubsequenceTopDownReverse(txt1, txt2))
                self.assertEqual(expected, self.longestCommonSubsequenceBottomUpMyOwn(txt1, txt2))

    def longestCommonSubsequenceBottomUpMyOwn(self, text1: str, text2: str) -> int:
        cache = []
        for i in range(len(text1) + 1):
            cache.append([0] * (len(text2) + 1))

        for left in range(len(text1) - 1, -1, -1):
            for right in range(len(text2) - 1, -1, -1):
                if text1[left] == text2[right]:
                    cache[left][right] = 1 + cache[left + 1][right + 1]
                else:
                    cache[left][right] = max(cache[left + 1][right], cache[left][right + 1])

        return cache[0][0]

    def longestCommonSubsequenceTopDownReverse(self, text1: str, text2: str) -> int:
        cache: Dict[Tuple[int, int], int] = {}

        def dfs(left: int, right: int) -> int:
            if left < 0 or right < 0:
                return 0

            key = (left, right)
            if key in cache:
                return cache[key]

            max_length_up_to_here = 0
            if text1[left] == text2[right]:
                max_length_up_to_here = 1 + dfs(left - 1, right - 1)
            else:
                max_length_up_to_here = max(dfs(left - 1, right), dfs(left, right - 1))

            cache[key] = max_length_up_to_here

            return cache[key]

        return dfs(len(text1) - 1, len(text2) - 1)

    def longestCommonSubsequenceTopDown(self, text1: str, text2: str) -> int:
        cache: Dict[Tuple[int, int], int] = {}

        def dfs(left: int, right: int) -> int:
            if left >= len(text1) or right >= len(text2):
                return 0

            key = (left, right)
            if key in cache:
                return cache[key]

            max_length_up_to_here = 0
            if text1[left] == text2[right]:
                max_length_up_to_here = max(
                    1 + dfs(left + 1, right + 1),  # take this
                    dfs(left + 1, right)  # ignore
                )
            else:
                max_length_up_to_here = max(
                    dfs(left + 1, right),
                    dfs(left + 1, right + 1),
                    dfs(left, right + 1)
                )

            cache[key] = max_length_up_to_here

            return cache[key]

        return dfs(0, 0)

    def longestCommonSubsequenceBottomUp(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

        return dp[0][0]
