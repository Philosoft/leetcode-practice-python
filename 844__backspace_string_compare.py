import unittest


class Solution(unittest.TestCase):
    def test_example_1(self):
        self.assertTrue(self.backspaceCompare("ab#c", "ad#c"))

    def test_example_2(self):
        self.assertTrue(self.backspaceCompare("ab##", "c#d#"))

    def test_example_3(self):
        self.assertFalse(self.backspaceCompare("a#c", "b"))

    def test_something(self):
        self.assertTrue(self.backspaceCompare("a##c", "#a#c"))

    def test_strange_case(self):
        self.assertTrue(self.backspaceCompare("xywrrmp", "xywrrmu#p"))

    def test_empty(self):
        self.assertTrue(self.backspaceCompare('',  ''))

    def test_backspace_only(self):
        self.assertTrue(self.backspaceCompare('###', '##########'))

    def test_another_failed_case(self):
        self.assertTrue(self.backspaceCompare("bxj##tw", "bxo#j##tw"))

    def test_backspaces_in_the_beginning(self):
        self.assertTrue(self.backspaceCompare('###abc', 'abc'))

    def backspaceCompare(self, s: str, t: str) -> bool:
        left, right = len(s) - 1, len(t) - 1

        def handle_backspace(text: str, ptr: int) -> int:
            while ptr >= 0 and text[ptr] == '#':
                backspace = 0
                while ptr >= 0 and text[ptr] == '#':
                    ptr -= 1
                    backspace += 1
                while backspace > 0 and ptr >= 0:
                    if text[ptr] == '#':
                        backspace += 1
                    else:
                        backspace -= 1
                    ptr -= 1

            return ptr

        while left >= 0 and right >= 0:
            left = handle_backspace(s, left)
            right = handle_backspace(t, right)

            if left >= 0 and right >= 0:
                if s[left] != t[right]:
                    return False
                left -= 1
                right -= 1

        left = handle_backspace(s, left)
        right = handle_backspace(t, right)

        return left < 0 and right < 0


    def backspaceCompareStacks(self, s: str, t: str) -> bool:
        left_stack = []
        for c in s:
            if c == '#':
                if left_stack:
                    left_stack.pop()
            else:
                left_stack.append(c)

        right_stack = []
        for c in t:
            if c == '#':
                if right_stack:
                    right_stack.pop()
            else:
                right_stack.append(c)

        return left_stack == right_stack

