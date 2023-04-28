"""
LeetCode: https://leetcode.com/problems/number-of-provinces/
"""
from collections import defaultdict
from typing import List, Dict, Set
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        self.assertEqual(2, self.findCircleNumUnionFind([[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
        self.assertEqual(2, self.findCircleNumDFS([[1, 1, 0], [1, 1, 0], [0, 0, 1]]))

    def test_example_2(self):
        self.assertEqual(3, self.findCircleNumUnionFind([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
        self.assertEqual(3, self.findCircleNumDFS([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))

    def test_case_96(self):
        connection_matrix = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                             [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                             [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                             [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                             [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
                             [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                             [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                             [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                             [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]
        self.assertEqual(8, self.findCircleNumUnionFind(connection_matrix))
        self.assertEqual(8, self.findCircleNumDFS(connection_matrix))

    def findCircleNumDFS(self, is_connected: List[List[int]]) -> int:
        provinces = 0
        visited: Set[int] = set()

        def dfs(p: int) -> None:
            visited.add(p)
            for province_idx, has_connection in enumerate(is_connected[p]):
                if has_connection == 1 and province_idx not in visited:
                    dfs(province_idx)

        for province in range(len(is_connected)):
            if province not in visited:
                provinces += 1
                dfs(province)

        return provinces

    def findCircleNumUnionFind(self, isConnected: List[List[int]]) -> int:
        number_of_provinces = len(isConnected)
        adj: Dict[int, Set[int]] = defaultdict(set)
        for src, connections in enumerate(isConnected):
            for dst, flag in enumerate(connections):
                if flag == 1:
                    adj[src].add(dst)

        uf: Dict[int, int] = {}

        def find(x: int) -> int:
            if x not in uf:
                uf[x] = x
                return uf[x]

            if x != uf[x]:
                uf[x] = find(uf[x])

            return uf[x]

        def connect(x: int, y: int) -> int:
            xroot, yroot = find(x), find(y)
            if xroot == yroot:
                return 0

            uf[xroot] = yroot
            return 1

        for src, dst_list in adj.items():
            for dst in dst_list:
                if connect(src, dst) != 0:
                    number_of_provinces -= 1

        return number_of_provinces
