"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the
original letters exactly once.

## Example 1

Input: s = "anagram", t = "nagaram"
Output: true

## Example 2

Input: s = "rat", t = "car"
Output: false

## Constraints

* 1 <= s.length, t.length <= 5 * 10^4
* s and t consist of lowercase English letters.

## Follow up

What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""
from collections import defaultdict
from typing import Dict
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        self.assertTrue(self.isAnagram("anagram", "nagaram"))

    def test_example_2(self):
        self.assertFalse(self.isAnagram("rat", "car"))

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        alphabet: Dict[str, int] = defaultdict(int)
        for char_s, char_t in zip(s, t):
            alphabet[char_s] += 1
            alphabet[char_t] -= 1

        for char in s:
            if alphabet[char] != 0:
                return False

        return True
