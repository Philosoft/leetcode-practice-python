import unittest


class Solution(unittest.TestCase):
    def test_example_1(self):
        self.assertTrue(self.detectCapitalUse('USA'))

    def test_example_2(self):
        self.assertFalse(self.detectCapitalUse('FlaG'))

    def test_proper_word(self):
        self.assertTrue(self.detectCapitalUse('Flag'))

    def test_2000(self):
        self.assertFalse(self.detectCapitalUse('HeLlO'))

    def test_all_lowercase(self):
        self.assertTrue(self.detectCapitalUse('leetcode'))

    def test_last_capital(self):
        self.assertFalse(self.detectCapitalUse('abcdeF'))

    def test_one_lowercase_letter(self):
        self.assertTrue(self.detectCapitalUse('a'))

    def test_one_uppercase_letter(self):
        self.assertTrue(self.detectCapitalUse('A'))

    def detectCapitalUse(self, word: str) -> bool:
        capitals_found = 0
        for i in range(0, len(word)):
            if ord('A') <= ord(word[i]) <= ord('Z'):
                capitals_found += 1

        return capitals_found == len(word) \
            or (capitals_found == 1 and ord('A') <= ord(word[0]) <= ord('Z')) \
            or capitals_found == 0
