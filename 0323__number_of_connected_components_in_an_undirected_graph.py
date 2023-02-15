from typing import List
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        self.assertEqual(2, self.countComponents(5, [[0, 1], [1, 2], [3, 4]]))

    def test_example_2(self):
        self.assertEqual(1, self.countComponents(5, [[0, 1], [1, 2], [2, 3], [3, 4]]))

    def test_cycle(self):
        self.assertEqual(2, self.countComponents(4, [[2, 3], [1, 2], [1, 3]]))

    def test_cycle_two(self):
        self.assertEqual(2, self.countComponents(4, [[0, 1], [0, 2], [1, 2]]))

    def test_one_line_stitched(self):
        self.assertEqual(1, self.countComponents(4, [[0, 1], [2, 3], [1, 2]]))

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = {}

        def find(x: int) -> int:
            if x not in uf:
                uf[x] = x

            if x != uf[x]:
                uf[x] = find(uf[x])

            return uf[x]

        def union(x: int, y: int) -> int:
            xroot, yroot = find(x), find(y)

            if xroot == yroot:
                return 0

            if xroot < yroot:
                uf[yroot] = xroot
            else:
                uf[xroot] = yroot

            return 1

        for i in range(n):
            uf[i] = i

        subgraphs = n
        for a, b in edges:
            subgraphs -= union(a, b)

        return subgraphs
