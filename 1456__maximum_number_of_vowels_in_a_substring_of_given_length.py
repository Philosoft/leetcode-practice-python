"""
LeetCode: https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/
"""
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        self.assertEqual(3, self.maxVowels("abciiidef", 3))

    def test_example_2(self):
        self.assertEqual(2, self.maxVowels("aeiou", 2))

    def test_example_3(self):
        self.assertEqual(2, self.maxVowels("leetcode", 3))

    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        count = 0
        left, right = 0, 0
        vowel_count = 0
        while right < k:
            char = s[right]
            if char in vowels:
                vowel_count += 1

            right += 1

        count = max(count, vowel_count)
        while right < len(s):
            if s[left] in vowels:
                vowel_count -= 1

            if s[right] in vowels:
                vowel_count += 1
            count = max(count, vowel_count)

            left += 1
            right += 1

        return count
