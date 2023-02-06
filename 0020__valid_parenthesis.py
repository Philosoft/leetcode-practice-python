"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

* Open brackets must be closed by the same type of brackets.
* Open brackets must be closed in the correct order.
* Every close bracket has a corresponding open bracket of the same type.

## Example 1

Input: s = "()"
Output: true

## Example 2

Input: s = "()[]{}"
Output: true

## Example 3

Input: s = "(]"
Output: false

## Constraints

* 1 <= s.length <= 10^4
* s consists of parentheses only '()[]{}'.
"""
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        self.assertTrue(self.isValid("()"))

    def test_example_2(self):
        self.assertTrue(self.isValid("()[]{}"))

    def test_example_3(self):
        self.assertFalse(self.isValid("(]"))

    def test_tricky(self):
        self.assertFalse(self.isValid("(([{}{]))"))

    def isValid(self, s: str) -> bool:
        pairs = {")": "(", "]": "[", "}": "{"}

        stack = []
        for char in s:
            if char not in pairs:
                stack.append(char)
            else:
                if not stack or stack[-1] != pairs[char]:
                    return False
                stack.pop()

        return len(stack) == 0
