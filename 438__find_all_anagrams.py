from collections import Counter
from typing import List
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        self.assertEqual([0, 6], self.findAnagrams("cbaebabacd", "abc"))

    def test_example_2(self):
        self.assertEqual([0, 1, 2], self.findAnagrams("abab", "ab"))

    def test_no_cigar(self):
        self.assertEqual([], self.findAnagrams("aa", "bb"))

    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        if len(s) == len(p):
            return [0] if Counter(s) == Counter(p) else []

        result = []
        window = Counter(s[:len(p)])
        target = Counter(p)
        left = 0
        right = len(p) - 1
        if window == target:
            result.append(0)
        while right < len(s) - 1:
            window[s[left]] -= 1
            left += 1

            right += 1
            if right < len(s):
                window[s[right]] += 1

                if window == target:
                    result.append(left)

        return result
