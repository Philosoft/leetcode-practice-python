import collections
import unittest
from typing import Set


class Solution(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual("makkek", self.smallestEquivalentStringFirstSolution("parker", "morris", "parser"))

    def test_example_2(self):
        self.assertEqual("hdld", self.smallestEquivalentStringFirstSolution("hello", "world", "hold"))

    def test_example_3(self):
        self.assertEqual("aauaaaaada", self.smallestEquivalentStringFirstSolution("leetcode", "programs", "sourcecode"))

    def smallestEquivalentStringFirstSolution(self, s1: str, s2: str, baseStr: str) -> str:
        equiv_map = collections.defaultdict(set)
        for a, b in zip(s1, s2):
            equiv_map[a].add(b)
            equiv_map[b].add(a)

        def organize(char: str, visited: Set[str]) -> Set[str]:
            if char in visited:
                return set()

            nonlocal equiv_map
            visited.add(char)
            additional_chars: Set[str] = {char}
            for equiv_char in equiv_map[char]:
                additional_chars = additional_chars.union(organize(equiv_char, visited))

            return additional_chars

        for k in set(s1 + s2):
            visited = set()
            equiv_map[k] = equiv_map[k].union(organize(k, visited))
            del visited

        result = ""
        for char in baseStr:
            if char not in equiv_map:
                result += char
            else:
                options = list(equiv_map[char] | {char})
                options.sort()
                result += options[0]

        return result
