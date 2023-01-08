import unittest


class Solution(unittest.TestCase):
    def test_example(self):
        options = [(5, 2), (8, 3), (1, 1), (2, 1), (3, 2), (99, 13), (99999, 446), ]

        for coins, expected_lines in options:
            with self.subTest(f'{coins} coins'):
                self.assertEqual(expected_lines, self.arrangeCoins(coins))

    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n
        lines = 1
        while left <= right:
            mid = left + (right - left) // 2

            need_coins = (mid * (mid + 1)) // 2

            if need_coins <= n:
                lines = mid
                left = mid + 1
            else:
                right = mid - 1

        return lines
