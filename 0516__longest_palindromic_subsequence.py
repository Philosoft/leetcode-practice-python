"""
LeetCode: https://leetcode.com/problems/longest-palindromic-subsequence/

Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing
the order of the remaining elements.

## Example 1

Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".

## Example 2

Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".

## Constraints

* 1 <= s.length <= 1000
* s consists only of lowercase English letters.
"""
from functools import cache
from unittest import TestCase


def defaultlist(param):
    pass


class Solution(TestCase):
    def test_example_1(self):
        self.assertEqual(4, self.longestPalindromeSubseq("bbbab"))

    def test_example_2(self):
        self.assertEqual(2, self.longestPalindromeSubseq("cbbd"))

    def test_only_one_letter(self):
        self.assertEqual(1, self.longestPalindromeSubseq("a"))

    def test_all_different_letters(self):
        self.assertEqual(1, self.longestPalindromeSubseq("abcdefghjklmnopqrstuwxyz"))

    def test_case_61(self):
        self.assertEqual(159, self.longestPalindromeSubseq(
            "euazbipzncptldueeuechubrcourfpftcebikrxhybkymimgvldiwqvkszfycvqyvtiwfckexmowcxztkfyzqovbtmzpxojfofbvwnnc"
            + "ajvrvdbvjhcrameamcfmcoxryjukhpljwszknhiypvyskmsujkuggpztltpgoczafmfelahqwjbhxtjmebnymdyxoeodqmvkxittxjnl"
            + "ltmoobsgzdfhismogqfpfhvqnxeuosjqqalvwhsidgiavcatjjgeztrjuoixxxoznklcxolgpuktirmduxdywwlbikaqkqajzbsjvdgj"
            + "cnbtfksqhquiwnwflkldgdrqrnwmshdpykicozfowmumzeuznolmgjlltypyufpzjpuvucmesnnrwppheizkapovoloneaxpfinaontw"
            + "tdqsdvzmqlgkdxlbeguackbdkftzbnynmcejtwudocemcfnuzbttcoew"
        ))

    def longestPalindromeSubseq(self, s: str) -> int:
        @cache
        def dfs(left: int, right: int) -> int:
            if left > right:
                return 0
            if left == right:
                return 1

            if s[left] == s[right]:
                return 2 + dfs(left + 1, right - 1)

            return max(dfs(left + 1, right), dfs(left, right - 1))

        return dfs(0, len(s) - 1)
