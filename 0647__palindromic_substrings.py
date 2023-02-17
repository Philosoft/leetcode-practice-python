"""
LeetCode: https://leetcode.com/problems/palindromic-substrings/

Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

## Example 1

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

## Example 2

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

## Constraints

* 1 <= s.length <= 1000
* s consists of lowercase English letters.
"""
from functools import cache
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        self.assertEqual(3, self.countSubstrings("abc"))
        self.assertEqual(3, self.countSubstringsDP("abc"))
        self.assertEqual(3, self.countSubstringsFirstApproach("abc"))

    def test_example_2(self):
        self.assertEqual(6, self.countSubstrings("aaa"))
        self.assertEqual(6, self.countSubstringsDP("aaa"))
        self.assertEqual(6, self.countSubstringsFirstApproach("aaa"))

    def countSubstringsDP(self, s: str) -> int:
        count = 0
        # dp[i, j] = is_palindrome(s[i:j])
        dp = [[False] * len(s) for _ in range(len(s))]

        # base case: 1 letter
        for i in range(len(s)):
            count += 1
            dp[i][i] = True

        # base case: 2 letters
        for i in range(len(s)):
            left, right = i, i + 1
            if right < len(s) and s[left] == s[right]:
                count += 1
                dp[left][right] = True

        # everything else
        for length in range(3, len(s) + 1):
            i = 0
            j = length - 1

            while j < len(s):
                dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
                if dp[i][j]:
                    count += 1

                i += 1
                j += 1

        return count

    def countSubstrings(self, s: str) -> int:
        count = 0

        for i in range(len(s)):
            # 1 character
            count += 1

            # odd length
            left, right = i - 1, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

            # even length
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

        return count

    def countSubstringsFirstApproach(self, s: str) -> int:
        def is_palindrome(string: str) -> bool:
            left, right = 0, len(string) - 1
            while left < right:
                if string[left] != string[right]:
                    return False

                left += 1
                right -= 1

            return True

        @cache
        def is_palindrome_cached(string: str) -> bool:
            if len(string) <= 1:
                return True

            return string[0] == string[-1] and is_palindrome_cached(string[1:-1])

        count = 0
        options = []
        for i in range(len(s) - 1, -1, -1):
            for idx, sub in enumerate(options):
                candidate = s[i] + sub
                if is_palindrome_cached(candidate):
                    count += 1
                options[idx] = candidate
            options.append(s[i])
            count += 1

        return count
