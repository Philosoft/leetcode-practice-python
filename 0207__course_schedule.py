"""
LeetCode: https://leetcode.com/problems/course-schedule/description/

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array
prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take
course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

## Example 1

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation:
    There are a total of 2 courses to take.
    To take course 1 you should have finished course 0. So it is possible.

## Example 2

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation:
    There are a total of 2 courses to take.
    To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1.
    So it is impossible.

## Constraints

* 1 <= numCourses <= 2000
* 0 <= prerequisites.length <= 5000
* prerequisites[i].length == 2
* 0 <= ai, bi < numCourses
* All the pairs prerequisites[i] are unique.
"""
from collections import deque
from typing import List, Dict, Set
from unittest import TestCase


class Solution(TestCase):
    def test_it(self):
        self.assertTrue(self.canFinish(5, [[1, 4], [2, 4], [3, 1], [3, 2]]))
        self.assertTrue(self.canFinish(5, [[1, 4], [2, 4], [3, 1], [3, 2]]))
        self.assertFalse(self.canFinish(3, [[0, 1], [0, 2], [1, 0]]))
        self.assertTrue(self.canFinish(3, [[0, 1], [0, 2], [1, 2]]))

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True

        adj: Dict[int, Set[int]] = {}
        for n in range(numCourses):
            adj[n] = set()

        for target, pre in prerequisites:
            adj[target].add(pre)

        can_finish: Dict[int, bool] = {}

        def dfs(node: int, visited) -> bool:
            if node in can_finish:
                return can_finish[node]

            if node in visited:
                # cycle
                return False

            visited.add(node)
            for nei in adj[node]:
                if not dfs(nei, visited):
                    can_finish[node] = False
                    return False
            can_finish[node] = True
            return True

        return all([dfs(n, set()) for n in range(numCourses)])
