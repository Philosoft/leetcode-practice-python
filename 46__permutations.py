import unittest
from typing import List


class Solution(unittest.TestCase):
    def test_example_1(self):
        nums = [1, 2, 3]
        expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        expected.sort()
        answer = self.permute(nums)
        answer.sort()

        self.assertEqual(answer, expected)

    def test_example_2(self):
        nums = [0, 1]
        expected = [[0, 1], [1, 0]]
        expected.sort()
        answer = self.permute(nums)
        answer.sort()

        self.assertEqual(answer, expected)

    def test_example_3(self):
        nums = [1]
        expected = [[1]]
        expected.sort()
        answer = self.permute(nums)
        answer.sort()

        self.assertEqual(answer, expected)

    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        stack = []

        def helper(remainder: List[int]) -> None:
            if not remainder:
                answer.append(stack.copy())
                return

            for i in range(len(remainder)):
                pick, head, tail = remainder[i], remainder[:i], remainder[i + 1:]
                stack.append(pick)
                helper(head + tail)
                stack.pop()

        helper(nums)

        return answer
