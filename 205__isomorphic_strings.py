"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character, but a character may map to itself.


Example 1:

Input:
    s = "egg"
    t = "add"
Output:
    true

Example 2:

Input:
    s = "foo"
    t = "bar"
Output:
    false

Example 3:

Input:
    s = "paper"
    t = "title"
Output:
    true

Constraints:

* 1 <= s.length <= 5 * 10^4
* t.length == s.length
* s and t consist of any valid ascii character.
"""
from typing import Dict, Set
from unittest import TestCase


class Solution(TestCase):
    def test(self):
        options = [
            (True, "egg", "add"),
            (False, "foo", "bar"),
            (True, "paper", "title"),
            (False, "badc", "baba"),
        ]

        for expected, left, right in options:
            with self.subTest(f'{left} {"==" if expected else "!="} {right}'):
                self.assertEqual(expected, self.isIsomorphic(left, right))

    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmap: Dict[str, str] = {}
        already_mapped: Set[str] = set()
        for left, right in zip(s, t):
            if left not in hashmap:
                if right in already_mapped:
                    return False
                hashmap[left] = right
                already_mapped.add(right)
            elif hashmap[left] != right:
                return False
        return True
