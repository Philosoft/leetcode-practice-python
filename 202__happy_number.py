import unittest


class Solution(unittest.TestCase):
    def test_example_1(self):
        self.assertTrue(self.isHappy(19))

    def test_example_2(self):
        self.assertFalse(self.isHappy(2))

    def isHappy(self, n: int) -> bool:
        visited = set()
        while True:
            if n in visited:
                return False
            visited.add(n)
            new_number = 0
            while n > 0:
                new_number += (n % 10) ** 2
                n = (n - (n % 10)) // 10
            n = new_number
            if n == 1:
                return True
