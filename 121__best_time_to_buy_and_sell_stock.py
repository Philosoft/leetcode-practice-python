"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future
to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation:
    Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
    Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:

* 1 <= prices.length <= 10^5
* 0 <= prices[i] <= 10^4
"""
from typing import List
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        self.assertEqual(5, self.maxProfit([7, 1, 5, 3, 6, 4]))

    def test_example_2(self):
        self.assertEqual(0, self.maxProfit([7, 6, 4, 3, 1]))

    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, len(prices) - 1
        left_min, right_max = None, None

        while left < right:
            if left_min is None or prices[left] < left_min:
                left_min = prices[left]

            left += 1

            if right_max is None or prices[right] > right_max:
                right_max = prices[right]

            right -= 1

        if left_min is not None and right_max is not None and left_min < right_max:
            return right_max - left_min

        return 0
