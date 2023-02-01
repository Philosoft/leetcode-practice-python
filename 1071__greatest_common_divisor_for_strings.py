"""
For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one
or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

## Example 1

Input:
    str1 = "ABCABC"
    str2 = "ABC"
Output:
    "ABC"

## Example 2

Input:
    str1 = "ABABAB"
    str2 = "ABAB"
Output:
    "AB"

## Example 3

Input:
    str1 = "LEET"
    str2 = "CODE"
Output:
    ""

## Constraints

* 1 <= str1.length, str2.length <= 1000
* str1 and str2 consist of English uppercase letters.
"""
from collections import Counter
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        self.assertEqual("ABC", self.gcdOfStrings("ABCABC", "ABC"))

    def test_example_2(self):
        self.assertEqual("AB", self.gcdOfStrings("ABABAB", "ABAB"))

    def test_example_3(self):
        self.assertEqual("", self.gcdOfStrings("LEET", "CODE"))

    def test_tricky(self):
        self.assertEqual("TAUXX", self.gcdOfStrings("TAUXXTAUXXTAUXXTAUXXTAUXX",
                                                    "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"))

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 == str2:
            return str1

        if len(str1) > len(str2):
            big, small = str1, str2
        else:
            big, small = str2, str1

        def is_divisible(option: str) -> bool:
            length = len(option)
            if len(str1) % length != 0 or len(str2) % length != 0:
                return False
            return str1 == option * (len(str1) // len(option)) and str2 == option * (len(str2) // len(option))

        candidate = small
        while candidate:
            if is_divisible(candidate):
                return candidate

            candidate = candidate[:-1]

        return ""
