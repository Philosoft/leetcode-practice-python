import unittest
from typing import List


class Solution(unittest.TestCase):
    def test_example_1(self):
        costs = [1, 3, 2, 4, 1]
        coins = 7
        self.assertEqual(4, self.maxIceCream(costs, coins))

    def test_example_2(self):
        costs = [10, 6, 8, 7, 7, 8]
        coins = 5
        self.assertEqual(0, self.maxIceCream(costs, coins))

    def test_example_3(self):
        costs = [1, 6, 3, 1, 2, 5]
        coins = 20
        self.assertEqual(6, self.maxIceCream(costs, coins))

    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        bought = 0
        for c in costs:
            if c <= coins:
                coins -= c
                bought += 1
            else:
                break

        return bought
