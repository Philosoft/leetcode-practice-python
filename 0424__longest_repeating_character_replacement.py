"""
LeetCode link https://leetcode.com/problems/longest-repeating-character-replacement/

You are given a string s and an integer k. You can choose any character of the string and change it to any other
uppercase English character. You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:

Input:
    s = "ABAB"
    k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:

Input:
    s = "AABABBA"
    k = 1
Output: 4
Explanation:
    Replace the one 'A' in the middle with 'B' and form "AABBBBA".
    The substring "BBBB" has the longest repeating letters, which is 4.

Constraints:

* 1 <= s.length <= 10^5
* s consists of only uppercase English letters.
* 0 <= k <= s.length
"""
from collections import Counter
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        self.assertEqual(4, self.characterReplacement("ABAB", 2))

    def test_example_2(self):
        self.assertEqual(4, self.characterReplacement("AABABBA", 1))

    def test_no_replaces_available(self):
        self.assertEqual(3, self.characterReplacement("AAAB", 0))

    def test_leetcode_13(self):
        self.assertEqual(2, self.characterReplacement("ABCDE", 1))

    def test_leetcode_23(self):
        self.assertEqual(4, self.characterReplacement("ABBB", 2))

    def characterReplacement(self, s: str, k: int) -> int:
        counter = Counter()
        l, r = 0, 0
        counter[s[0]] = counter.get(s[0], 0) + 1
        max_length = 1
        window_size = 1
        while r + 1 < len(s):
            r += 1
            window_size += 1
            counter[s[r]] = counter.get(s[r], 0) + 1
            most_freq = counter.most_common(1)[0][1]
            if window_size - most_freq <= k:
                max_length = max(max_length, window_size)
            else:
                counter[s[l]] -= 1
                window_size -= 1
                l += 1

        return max_length
