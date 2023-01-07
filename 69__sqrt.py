import unittest


class Solution(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(2, self.mySqrt(4))

    def test_example_2(self):
        self.assertEqual(2, self.mySqrt(8))

    def test_zero(self):
        self.assertEqual(0, self.mySqrt(0))

    def test_one(self):
        self.assertEqual(1, self.mySqrt(1))

    def test_ones(self):
        self.assertEqual(105, self.mySqrt(11111))

    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x

        left, right = 0, x
        result = 0
        while left <= right:
            mid = left + (right - left) // 2

            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid

            if mid * mid < x:
                left = mid + 1
                result = mid
            else:
                right = mid - 1

        return result
