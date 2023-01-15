"""
Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

 Example 1:

Input:
    low = 3
    high = 7
Output: 3
Explanation: The odd numbers between 3 and 7 are [3,5,7].

Example 2:

Input:
    low = 8
    high = 10
Output: 1
Explanation: The odd numbers between 8 and 10 are [9].

Constraints:

0 <= low <= high <= 10^9
"""
import unittest


class Solution(unittest.TestCase):
    def test(self):
        options = [(3, 3, 7), (1, 8, 10), (0, 0, 0), (1, 9, 10), (5555, 0, 11110), (500_000_000, 0, 10 ** 9), ]

        for expected, low, high in options:
            with self.subTest(f"[{low}, {high}]"):
                self.assertEqual(expected, self.countOdds(low, high))

    def countOdds(self, low: int, high: int) -> int:
        if low % 2 == 0:
            low += 1

        if high % 2 == 0:
            high -= 1

        return (high - low) // 2 + 1
