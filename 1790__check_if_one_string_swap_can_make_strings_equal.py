"""
You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a
string (not necessarily different) and swap the characters at these indices.
Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the
strings. Otherwise, return false.


Example 1:

Input:
    s1 = "bank"
    s2 = "kanb"
Output:
    true
Explanation:
    For example, swap the first character with the last character of s2 to make "bank".

Example 2:

Input:
    s1 = "attack"
    s2 = "defend"
Output:
    false
Explanation:
    It is impossible to make them equal with one string swap.

Example 3:

Input:
    s1 = "kelb"
    s2 = "kelb"
Output:
    true
Explanation:
    The two strings are already equal, so no string swap operation is required.


Constraints:

* 1 <= s1.length, s2.length <= 100
* s1.length == s2.length
* s1 and s2 consist of only lowercase English letters.
"""
from collections import Counter
from unittest import TestCase


class Solution(TestCase):
    def test(self):
        options = [
            ('1 letter diff', True, "bank", "kanb"),
            ('totally different', False, "attack", "defend"),
            ('the same', True, "kelb", "kelb"),
            ('impossible 1 letter diff', False, "aa", "ac"),
        ]

        for name, expected, s1, s2 in options:
            with self.subTest(name):
                self.assertEqual(expected, self.areAlmostEqualBrute(s1, s2))
                self.assertEqual(expected, self.areAlmostEqualSmart(s1, s2))

    def areAlmostEqualSmart(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        if len(s1) != len(s2):
            return False

        diff_at_idx = []
        for (idx, left), right in zip(enumerate(s1), s2):
            if left != right:
                diff_at_idx.append(idx)
                if len(diff_at_idx) > 2:
                    return False

        if len(diff_at_idx) != 2:
            return False

        variant = list(s1)
        swap_a, swap_b = diff_at_idx
        variant[swap_a], variant[swap_b] = variant[swap_b], variant[swap_a]

        return "".join(variant) == s2

    def areAlmostEqualBrute(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        if Counter(s1) != Counter(s2):
            return False

        for i in range(len(s1)):
            for j in range(len(s1)):
                variant = list(s1)
                variant[i], variant[j] = variant[j], variant[i]

                if "".join(variant) == s2:
                    return True

        return False
