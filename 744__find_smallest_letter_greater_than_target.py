import unittest
from typing import List


class Solution(unittest.TestCase):
    def test_example_1(self):
        letters = ["c", "f", "j"]
        target = "a"
        expected = "c"

        self.assertEqual(expected, self.nextGreatestLetter(letters, target))

    def test_example_2(self):
        letters = ["c", "f", "j"]
        target = "c"
        expected = "f"

        self.assertEqual(expected, self.nextGreatestLetter(letters, target))

    def test_example_3(self):
        letters = ["x", "x", "y", "y"]
        target = "z"
        expected = "x"

        self.assertEqual(expected, self.nextGreatestLetter(letters, target))

    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) - 1
        result = letters[0]
        while left <= right:
            mid = left + (right - left) // 2

            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
                result = letters[mid]

        return result
