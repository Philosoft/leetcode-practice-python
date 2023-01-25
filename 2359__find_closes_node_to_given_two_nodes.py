"""
You are given a directed graph of n nodes numbered from 0 to n - 1, where each node has at most one outgoing edge.
The graph is represented with a given 0-indexed array edges of size n, indicating that there is a directed edge from
node i to node edges[i]. If there is no outgoing edge from i, then edges[i] == -1.

You are also given two integers node1 and node2.

Return the index of the node that can be reached from both node1 and node2, such that the maximum between the distance
from node1 to that node, and from node2 to that node is minimized. If there are multiple answers, return the node with
the smallest index, and if no possible answer exists, return -1.

Note that edges may contain cycles.

## Example 1

Input:
    edges = [2,2,3,-1]
    node1 = 0
    node2 = 1
Output: 2
Explanation:
    The distance from node 0 to node 2 is 1, and the distance from node 1 to node 2 is 1.
    The maximum of those two distances is 1. It can be proven that we cannot get a node with a smaller maximum distance
    than 1, so we return node 2.


## Example 2:

Input:
    edges = [1,2,-1]
    node1 = 0
    node2 = 2
Output: 2
Explanation:
    The distance from node 0 to node 2 is 2, and the distance from node 2 to itself is 0.
    The maximum of those two distances is 2. It can be proven that we cannot get a node with a smaller maximum distance
    than 2, so we return node 2.

## Constraints:

* n == edges.length
* 2 <= n <= 10^5
* -1 <= edges[i] < n
* edges[i] != i
* 0 <= node1, node2 < n
"""
from math import inf
from typing import List, Set
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        self.assertEqual(2, self.closestMeetingNode([2, 2, 3, -1], 0, 1))

    def test_example_2(self):
        self.assertEqual(2, self.closestMeetingNode([1, 2, -1], 0, 2))

    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        distances_from_1: List[int | float] = [inf] * len(edges)
        distances_from_2: List[int | float] = distances_from_1.copy()

        def bfs(node: int, distances: List[int]) -> None:
            visited: Set[int] = set()
            steps = 0
            while node != -1:
                visited.add(node)
                distances[node] = steps

                if edges[node] not in visited:
                    node = edges[node]
                    steps += 1
                else:
                    node = -1

        bfs(node1, distances_from_1)
        bfs(node2, distances_from_2)

        answer = -1
        min_distance: float | int = inf
        for i in range(len(edges)):
            m = max(distances_from_1[i], distances_from_2[i])
            if m < min_distance:
                min_distance = m
                answer = i

        return answer
