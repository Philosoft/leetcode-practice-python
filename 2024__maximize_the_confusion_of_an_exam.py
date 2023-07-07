"""
LeetCode: https://leetcode.com/problems/maximize-the-confusion-of-an-exam/
"""
from collections import Counter
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        self.assertEqual(4, self.maxConsecutiveAnswers("TTFF", 2))

    def test_example_2(self):
        self.assertEqual(3, self.maxConsecutiveAnswers("TFFT", 1))

    def test_example_3(self):
        self.assertEqual(5, self.maxConsecutiveAnswers("TTFTTFTT", 1))

    def test_case_73(self):
        self.assertEqual(1, self.maxConsecutiveAnswers("F", 1))

    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        window = Counter({'T': 0, 'F': 0})
        max_len = 0
        left, right = 0, 0
        while right < len(answerKey):
            # grow
            while right < len(answerKey) and min(window.values()) <= k:
                window[answerKey[right]] += 1
                if min(window.values()) <= k:
                    max_len = max(max_len, sum(window.values()))
                else:
                    max_len = max(max_len, sum(window.values()) - 1)
                right += 1

            # shrink
            while left < right and min(window.values()) > k:
                window[answerKey[left]] -= 1
                left += 1

        return max_len
