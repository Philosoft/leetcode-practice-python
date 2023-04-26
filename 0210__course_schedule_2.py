"""
LeetCode: https://leetcode.com/problems/course-schedule-ii/
"""
from collections import defaultdict
from typing import List, Dict, Set
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        self.assertEqual([0, 1], self.findOrder(2, [[1, 0]]))

    def test_example_2(self):
        self.assertTrue(
            self.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]) in [
                [0, 2, 1, 3],
                [0, 1, 2, 3]
            ]
        )

    def test_example_3(self):
        self.assertEqual([0], self.findOrder(1, []))

    def test_case_40(self):
        self.assertEqual([2, 1, 0], self.findOrder(3, [[0, 1], [0, 2], [1, 2]]))

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj: Dict[int, Set[int]] = defaultdict(set)
        for src, dst in prerequisites:
            adj[src].add(dst)

        visited: Set[int] = set()
        cycle: Set[int] = set()
        result: List[int] = []

        def dfs(course: int) -> bool:
            if course in visited:
                return True

            if course in cycle:
                return False

            cycle.add(course)
            for nei in adj[course]:
                if not dfs(nei):
                    return False

            visited.add(course)
            result.append(course)
            return True

        for n in range(numCourses):
            cycle.clear()
            if n not in visited and not dfs(n):
                return []

        return result
