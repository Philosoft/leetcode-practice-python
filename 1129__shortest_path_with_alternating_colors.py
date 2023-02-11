from collections import deque
from typing import List
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        self.assertEqual([0, 1, -1], self.shortestAlternatingPaths(3, [[0, 1], [1, 2]], []))

    def test_example_2(self):
        self.assertEqual([0, 1, -1], self.shortestAlternatingPaths(3, [[0, 1]], [[2, 1]]))

    def test_from_discussion(self):
        red = [[0, 1], [1, 2], [2, 3], [3, 4]]
        blue = [[1, 2], [2, 3], [3, 1]]
        self.assertEqual([0, 1, 2, 3, 7], self.shortestAlternatingPaths(5, red, blue))

    def test_first_fail(self):
        red = [[2, 2], [0, 1], [0, 3], [0, 0], [0, 4], [2, 1], [2, 0], [1, 4], [3, 4]]
        blue = [[1, 3], [0, 0], [0, 3], [4, 2], [1, 0]]

        self.assertEqual([0, 1, 2, 1, 1], self.shortestAlternatingPaths(5, red, blue))

    def test_case_22(self):
        red = [[4, 1], [3, 5], [5, 2], [1, 4], [4, 2], [0, 0], [2, 0], [1, 1]]
        blue = [[5, 5], [5, 0], [4, 4], [0, 3], [1, 0]]

        self.assertEqual([0, -1, 4, 1, -1, 2], self.shortestAlternatingPaths(6, red, blue))

    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        adj = {}
        for a, b in redEdges:
            if a not in adj:
                adj[a] = {}
            if 'red' not in adj[a]:
                adj[a]['red'] = set()

            adj[a]['red'].add(b)

        for a, b in blueEdges:
            if a not in adj:
                adj[a] = {}
            if 'blue' not in adj[a]:
                adj[a]['blue'] = set()

            adj[a]['blue'].add(b)

        paths_len = []

        def find_shortest_alt_path(target: int, edge_color: str):
            q = deque([(0, edge_color, -1)])
            visited = set()

            steps = 0
            while q:
                for _ in range(len(q)):
                    node, color, prev_node = q.popleft()
                    if node == target:
                        return steps

                    if node not in adj or color not in adj[node]:
                        continue

                    if (node, color, prev_node) in visited:
                        # cycle
                        continue

                    visited.add((node, color, prev_node))

                    next_color = 'blue' if color == 'red' else 'red'
                    for nei in adj[node][color]:
                        if nei != prev_node:
                            q.append((nei, next_color, node))
                steps += 1
            return -1

        result = [-2] * n
        for target_node in range(n):
            path_red = find_shortest_alt_path(target_node, 'red')
            path_blue = find_shortest_alt_path(target_node, 'blue')
            if path_red >= 0 and path_blue >= 0:
                result[target_node] = min(path_red, path_blue)
            elif path_red == -1 and path_blue == -1:
                result[target_node] = -1
            else:
                result[target_node] = max(path_red, path_blue)

        return result
