"""
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and
initial word order.

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Example 2:

Input: s = "God Ding"
Output: "doG gniD"

Constraints:

* 1 <= s.length <= 5 * 10^4
* s contains printable ASCII characters.
* s does not contain any leading or trailing spaces.
* There is at least one word in s.
* All the words in s are separated by a single space.
"""
from unittest import TestCase


class Solution(TestCase):
    def test_example_2(self):
        self.assertEqual("s'teL ekat edoCteeL tsetnoc", "Let's take LeetCode contest")

    def test_example_2(self):
        self.assertEqual("doG gniD", self.reverseWords("God Ding"))

    def reverseWords(self, s: str) -> str:
        string = list(s)
        left = 0
        for right, char in enumerate(s):
            if char == " ":
                # word from left to right - 1
                l, r = left, right - 1
                while l < r:
                    string[l], string[r] = string[r], string[l]
                    l += 1
                    r -= 1
                left = right + 1
            right += 1

        if string[-1] != " ":
            l, r = left, len(string) - 1
            while l < r:
                string[l], string[r] = string[r], string[l]
                l += 1
                r -= 1

        return "".join(string)
