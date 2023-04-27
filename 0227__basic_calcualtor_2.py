"""
LeetCode: https://leetcode.com/problems/basic-calculator-ii/description/
"""

from operator import add, mul, floordiv, sub
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        self.assertEqual(7, self.calculate("3+2*2"))

    def test_example_2(self):
        self.assertEqual(1, self.calculate(" 3/2 "))

    def test_example_3(self):
        self.assertEqual(5, self.calculate(" 3+5 / 2 "))

    def test_case_77(self):
        self.assertEqual(0, self.calculate("1-1"))

    def test_case_103(self):
        self.assertEqual(13, self.calculate("14-3/2"))

    def calculate(self, s: str) -> int:
        op_map = {
            '+': add,
            '*': mul,
            '/': floordiv,
            '-': sub,
        }

        stack = []
        buf = []
        ptr = 0
        op = '+'
        while ptr < len(s):
            while ptr < len(s) and s[ptr] not in op_map.keys():
                if s[ptr].isdigit():
                    buf.append(s[ptr])
                ptr += 1
            num = int("".join(buf))
            buf = []
            if op == '*':
                num = stack.pop() * num
            elif op == '/':
                num = int(stack.pop() / num)

            if op == '-':
                stack.append(-num)
            else:
                stack.append(num)

            while ptr < len(s) and s[ptr] == ' ':
                ptr += 1

            if ptr < len(s):
                op = s[ptr]
                ptr += 1

        while len(stack) > 1:
            stack.append(stack.pop() + stack.pop())

        return stack[-1]
