import unittest
from typing import List


class Solution(unittest.TestCase):
    def test_example_1(self):
        self.assertEquals(self.minDeletionSize(["cba", "daf", "ghi"]), 1)

    def test_example_2(self):
        self.assertEquals(self.minDeletionSize(['a', 'b']), 0)

    def test_example_3(self):
        self.assertEquals(self.minDeletionSize(["zyx", "wvu", "tsr"]), 3)

    def minDeletionSize(self, strs: List[str]) -> int:
        deleted = 0
        for column in range(len(strs[0])):
            prev = 'a'
            for row in range(len(strs)):
                char = strs[row][column]
                if ord(char) < ord(prev):
                    deleted += 1
                    break
                prev = char

        return deleted
