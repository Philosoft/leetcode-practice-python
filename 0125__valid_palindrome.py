"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all
non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers

Given a string s, return true if it is a palindrome, or false otherwise.

## Example 1

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

## Example 2

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

## Example 3

Input: s = " "
Output: true
Explanation:
    s is an empty string "" after removing non-alphanumeric characters.
    Since an empty string reads the same forward and backward, it is a palindrome.

## Constraints

* 1 <= s.length <= 2 * 10^5
* s consists only of printable ASCII characters.
"""
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        self.assertTrue(self.isPalindrome("A man, a plan, a canal: Panama"))

    def test_example_2(self):
        self.assertFalse(self.isPalindrome("race a car"))

    def test_example_3(self):
        self.assertTrue(self.isPalindrome(""))

    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalpha():
                left += 1

            while right > left and not s[right].isalpha():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
