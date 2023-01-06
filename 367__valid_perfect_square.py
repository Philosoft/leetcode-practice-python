import unittest


class Solution(unittest.TestCase):
    def test_example_1(self):
        self.assertTrue(self.isPerfectSquare(16))

    def test_example_2(self):
        self.assertFalse(self.isPerfectSquare(14))

    def isPerfectSquare(self, num: int) -> bool:
        left, right = 1, num

        while left <= right:
            m = left + (right - left) // 2

            if m ** 2 == num:
                return True

            if num > m ** 2:
                left = m + 1
            else:
                right = m - 1

        return left ** 2 == num
