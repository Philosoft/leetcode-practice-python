"""
Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.
Return a list of all possible strings we could create. Return the output in any order.

## Example 1:

Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]

## Example 2:

Input: s = "3z4"
Output: ["3z4","3Z4"]

## Constraints:

* 1 <= s.length <= 12
* s consists of lowercase English letters, uppercase English letters, and digits.
"""
from typing import List
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        expected = ["a1b2", "a1B2", "A1b2", "A1B2"]
        expected.sort()
        answer = self.letterCasePermutation("a1b2")
        answer.sort()

        self.assertEqual(expected, answer)

    def test_example_2(self):
        expected = ["3z4", "3Z4"]
        expected.sort()
        answer = self.letterCasePermutation("3z4")
        answer.sort()

        self.assertEqual(expected, answer)

    def test_only_numbers(self):
        self.assertEqual(["12345"], self.letterCasePermutation("12345"))

    def test_only_1_number(self):
        self.assertEqual(["1"], self.letterCasePermutation("1"))

    def test_only_1_lower_case_letter(self):
        self.assertEqual(["a", "A"], self.letterCasePermutation("a"))

    def test_only_1_upper_case_letter(self):
        self.assertEqual(["A", "a"], self.letterCasePermutation("A"))

    def test_only_letters(self):
        expected = ["ab", "aB", "Ab", "AB"]
        expected.sort()
        answer = self.letterCasePermutation("ab")
        answer.sort()

        self.assertEqual(expected, answer)

    def letterCasePermutation(self, s: str) -> List[str]:
        result: List[str] = []
        perm: List[str] = []

        def backtrack(ptr: int) -> None:
            # no more string to process
            if ptr >= len(s):
                result.append("".join(perm))
                return

            # add numbers as is
            while ptr < len(s) and not s[ptr].isalpha():
                perm.append(s[ptr])
                ptr += 1

            # if it's the end of string - there is nothing to change
            # record permutation and return
            if ptr >= len(s):
                result.append("".join(perm))
                return

            # here we have a letter at s[ptr]
            # permute -> use as is, and build string further
            perm.append(s[ptr])
            l = len(perm)
            backtrack(ptr + 1)

            # permute -> change case and build string again
            while len(perm) > l:
                perm.pop()
            perm[-1] = perm[-1].upper() if perm[-1].islower() else perm[-1].lower()
            backtrack(ptr + 1)

        backtrack(0)

        return result
