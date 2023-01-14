import collections
import unittest
from typing import Set, List


class Solution(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual("makkek", self.smallestEquivalentStringFirstSolution("parker", "morris", "parser"))
        self.assertEqual("makkek", self.smallestEquivalentStringDisjointSet("parker", "morris", "parser"))
        self.assertEqual("makkek", self.smallestEquivalentStringUF("parker", "morris", "parser"))

    def test_example_2(self):
        self.assertEqual("hdld", self.smallestEquivalentStringFirstSolution("hello", "world", "hold"))
        self.assertEqual("hdld", self.smallestEquivalentStringDisjointSet("hello", "world", "hold"))
        self.assertEqual("hdld", self.smallestEquivalentStringUF("hello", "world", "hold"))

    def test_example_3(self):
        self.assertEqual("aauaaaaada", self.smallestEquivalentStringFirstSolution("leetcode", "programs", "sourcecode"))
        self.assertEqual("aauaaaaada", self.smallestEquivalentStringDisjointSet("leetcode", "programs", "sourcecode"))
        self.assertEqual("aauaaaaada", self.smallestEquivalentStringUF("leetcode", "programs", "sourcecode"))

    def smallestEquivalentStringUF(self, s1: str, s2: str, baseStr: str) -> str:
        # Union find version
        uf = {}

        def find(char: str) -> str:
            if char not in uf:
                uf[char] = char

            if uf[char] == char:
                return char

            return find(uf[char])

        def union(left: str, right: str) -> None:
            root1, root2 = find(left), find(right)

            if root1 > root2:
                root1, root2 = root2, root1

            uf[root2] = root1

        for a, b in zip(s1, s2):
            union(a, b)

        return "".join([find(char) for char in baseStr])


    def smallestEquivalentStringDisjointSet(self, s1: str, s2: str, baseString: str) -> str:
        """
        Idea. Construct disjoint set. Always lexicographically smaller letter as root.
        Then go through base string taking roots

        @todo: rewrite with hashset instead of array
        """
        dis_set: List[int] = [i for i in range(26)]

        def union(left: str, right: str) -> None:
            root1, root2 = find(left), find(right)
            if root1 == root2:
                return

            if root1 > root2:
                root1, root2 = root2, root1

            dis_set[ord(root2) - ord("a")] = ord(root1) - ord('a')

        def find(target: str) -> str:
            t = ord(target) - ord("a")
            if dis_set[t] == t:
                return target

            return find(chr(dis_set[t] + ord("a")))

        for a, b in zip(s1, s2):
            union(a, b)

        return "".join([min(x, find(x)) for x in baseString])

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
