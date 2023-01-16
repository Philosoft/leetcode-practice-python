"""
Given an integer number n, return the difference between the product of its digits and the sum of its digits.


Example 1:

Input: n = 234
Output: 15
Explanation:
Product of digits = 2 * 3 * 4 = 24
Sum of digits = 2 + 3 + 4 = 9
Result = 24 - 9 = 15

Example 2:

Input: n = 4421
Output: 21
Explanation:
Product of digits = 4 * 4 * 2 * 1 = 32
Sum of digits = 4 + 4 + 2 + 1 = 11
Result = 32 - 11 = 21


Constraints:

1 <= n <= 10^5
"""
from unittest import TestCase


class Solution(TestCase):
    def test(self):
        options = [
            (15, 234),
            (21, 4421),
        ]

        for expected, n in options:
            with self.subTest(str(n)):
                self.assertEqual(expected, self.subtractProductAndSumStringManipulation(n))
                self.assertEqual(expected, self.subtractProductAndSum(n))

    def subtractProductAndSum(self, n: int) -> int:
        p, s = 1, 0
        while n > 0:
            digit = n % 10
            p *= digit
            s += digit
            n //= 10

        return p - s

    def subtractProductAndSumStringManipulation(self, n: int) -> int:
        product = 1
        s = 0

        for char in str(n):
            s += int(char)
            product *= int(char)

        return product - s
