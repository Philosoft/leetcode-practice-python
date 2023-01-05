import unittest
from collections import Counter


class Solution(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(7, self.longestPalindrome("abccccdd"))

    def test_example_2(self):
        self.assertEqual(1, self.longestPalindrome('a'))

    def test_simple_long(self):
        self.assertEqual(5000, self.longestPalindrome('a' * 5000))

    def longestPalindrome(self, s: str) -> int:
        if len(s) == 1:
            return 1

        counter = Counter(s)
        length = 0
        for char, count in counter.items():
            if count >= 2:
                l = counter[char] // 2 * 2
                counter[char] -= l
                length += l

        for char, count in counter.items():
            if count == 1:
                return length + 1

        return length
