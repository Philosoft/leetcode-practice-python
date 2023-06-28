"""
LeetCode: https://leetcode.com/problems/path-with-maximum-probability/
"""
from collections import defaultdict
from heapq import heappop, heappush
from typing import List, Dict, Set, Tuple
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        self.assertEqual(0.25, self.maxProbability(3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.2], 0, 2))

    def test_example_2(self):
        self.assertEqual(0.3, self.maxProbability(3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.3], 0, 2))

    def test_example_3(self):
        self.assertEqual(0.0, self.maxProbability(3, [[0, 1]], [0.5], 0, 2))

    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adj: Dict[int, List[Tuple[int, float]]] = defaultdict(list)
        for idx, (src, dst) in enumerate(edges):
            adj[src].append((dst, succProb[idx]))
            adj[dst].append((src, succProb[idx]))

        visited: Set[int] = set()
        q = [(-1.0, start)]
        result = 0.0
        while q:
            p, node = heappop(q)
            if node == end:
                # there can be more than 1 answer
                result = max(result, -p)

            if node in visited:
                continue
            visited.add(node)

            for nei, prob_of_success in adj[node]:
                if nei not in visited:
                    heappush(q, (p * prob_of_success, nei))

        return result
