"""
LeetCode: https://leetcode.com/problems/minimum-window-substring/

Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every
character in t (including duplicates) is included in the window. If there is no such substring, return the empty
string "".

The testcases will be generated such that the answer is unique.

## Example 1

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

## Example 2

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

## Example 3

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

## Constraints

* m == s.length
* n == t.length
* 1 <= m, n <= 105
* s and t consist of uppercase and lowercase English letters.

## Follow up

Could you find an algorithm that runs in O(m + n) time?
"""
from collections import Counter
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        self.assertEqual("BANC", self.minWindow("ADOBECODEBANC", "ABC"))

    def test_example_2(self):
        self.assertEqual("a", self.minWindow("a", "a"))

    def test_leetcode_211(self):
        self.assertEqual("a", self.minWindow("ab", "a"))

    def test_leetcode_249(self):
        self.assertEqual("b", self.minWindow("ab", "b"))

    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        target_cnt = Counter(t)
        window_counter = target_cnt.copy()
        for char in target_cnt.keys():
            window_counter[char] = 0

        minsub = None

        left, right = 0, 0
        while right < len(s):
            if s[right] in window_counter:
                window_counter[s[right]] += 1

                if window_counter >= target_cnt:
                    # found it
                    # now, minimize
                    if s[left] in window_counter:
                        window_counter[s[left]] -= 1
                    left += 1
                    while window_counter >= target_cnt and left <= right:
                        if s[left] in window_counter:
                            window_counter[s[left]] -= 1
                        left += 1

                    possible_min = s[left - 1:right + 1]
                    if minsub is None:
                        minsub = possible_min
                    elif len(possible_min) < len(minsub):
                        minsub = possible_min

            right += 1

        return minsub if minsub else ""
