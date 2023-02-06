"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

## Example 1

Input: n = 2
Output: 2
Explanation:
    There are two ways to climb to the top.
        1. 1 step + 1 step
        2. 2 steps

## Example 2

Input: n = 3
Output: 3
Explanation:
    There are three ways to climb to the top.
        1. 1 step + 1 step + 1 step
        2. 1 step + 2 steps
        3. 2 steps + 1 step

## Constraints

* 1 <= n <= 45
"""
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        self.assertEqual(2, self.climbStairs(2))

    def test_example_2(self):
        self.assertEqual(3, self.climbStairs(3))

    def test_maxi_case(self):
        self.assertEqual(1836311903, self.climbStairs(45))

    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 2)
        dp[n] = 1
        for i in range(n - 1, -1, -1):
            dp[i] = dp[i + 1] + dp[i + 2]

        return dp[0]
