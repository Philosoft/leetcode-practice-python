import unittest
from typing import List


class Solution(unittest.TestCase):
    def test_example_1(self):
        digits = "23"
        expected = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        expected.sort()

        self.assertEqual(self.letterCombinations(digits), expected)

    def test_example_2(self):
        self.assertEqual(self.letterCombinations(''), [])

    def test_example_3(self):
        digits = "2"
        expected = ["a", "b", "c"]
        expected.sort()

        self.assertEqual(self.letterCombinations(digits), expected)

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        dictionary = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        answer = []
        stack = []

        def helper(remaining_string: str) -> None:
            if not remaining_string:
                answer.append(''.join(stack))
                return

            head, tail = remaining_string[0], remaining_string[1:]
            for char in dictionary[head]:
                stack.append(char)
                helper(tail)
                stack.pop()

        helper(digits)

        return answer
