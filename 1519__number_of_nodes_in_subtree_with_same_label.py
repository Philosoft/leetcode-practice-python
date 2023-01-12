import collections
import unittest
from collections import defaultdict
from typing import List, Counter

"""
You are given a tree (i.e. a connected, undirected graph that has no cycles) consisting of n nodes numbered from 0 to n - 1 and exactly n - 1 edges. The root of the tree is the node 0, and each node of the tree has a label which is a lower-case character given in the string labels (i.e. The node with the number i has the label labels[i]).

The edges array is given on the form edges[i] = [ai, bi], which means there is an edge between nodes ai and bi in the tree.

Return an array of size n where ans[i] is the number of nodes in the subtree of the ith node which have the same label as node i.

A subtree of a tree T is the tree consisting of a node in T and all of its descendant nodes.

 
Example 1:

Input:
    n = 7,
    edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]],
    labels = "abaedcd"
Output:
    [2,1,1,1,1,1,1]

Explanation:
Node 0 has label 'a' and its sub-tree has node 2 with label 'a' as well, thus the answer is 2. Notice that any node is part of its sub-tree.
Node 1 has a label 'b'. The sub-tree of node 1 contains nodes 1,4 and 5, as nodes 4 and 5 have different labels than node 1, the answer is just 1 (the node itself).

Example 2:

Input:
    n = 4,
    edges = [[0,1],[1,2],[0,3]],
    labels = "bbbb"
Output:
    [4,2,1,1]

Explanation:
The sub-tree of node 2 contains only node 2, so the answer is 1.
The sub-tree of node 3 contains only node 3, so the answer is 1.
The sub-tree of node 1 contains nodes 1 and 2, both have label 'b', thus the answer is 2.
The sub-tree of node 0 contains nodes 0, 1, 2 and 3, all with label 'b', thus the answer is 4.

Example 3:

Input:
    n = 5,
    edges = [[0,1],[0,2],[1,3],[0,4]],
    labels = "aabab"
Output:
    [3,2,1,1,1]
 

Constraints:

* 1 <= n <= 10^5
* edges.length == n - 1
* edges[i].length == 2
* 0 <= ai, bi < n
* ai != bi
* labels.length == n
* labels is consisting of only of lowercase English letters.
"""


class Solution(unittest.TestCase):
    def test_example_1(self):
        n = 7
        edges = [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]]
        labels = "abaedcd"
        expected = [2, 1, 1, 1, 1, 1, 1]

        self.assertEqual(expected, self.countSubTrees(n, edges, labels))

    def test_example_2(self):
        n = 4
        edges = [[0, 1], [1, 2], [0, 3]]
        labels = "bbbb"

        self.assertEqual([4, 2, 1, 1], self.countSubTrees(n, edges, labels))

    def test_example_3(self):
        n = 5
        edges = [[0, 1], [0, 2], [1, 3], [0, 4]]
        labels = "aabab"

        self.assertEqual([3, 2, 1, 1, 1], self.countSubTrees(n, edges, labels))

    def test_off_root_node(self):
        n = 4
        edges = [[0, 2], [0, 3], [1, 2]]
        labels = "aeed"

        self.assertEqual([1, 1, 2, 1], self.countSubTrees(n, edges, labels))

    def test_big_shallow_graph(self):
        n = 100_000
        edges = []
        for i in range(1, 100_000):
            edges.append([0, i])
        labels = "a" * 100_000
        expected = [1] * 100_000
        expected[0] = 100_000

        self.assertEqual(expected, self.countSubTrees(n, edges, labels))

    def test_deep_and_narrow_graph(self):
        n = 800
        edges = []
        for i in range(1, 800):
            edges.append([i - 1, i])

        labels = "a" * 800
        expected = [0] * 800
        cnt = 1
        for i in range(800 - 1, -1, -1):
            expected[i] = cnt
            cnt += 1

        self.assertEqual(expected, self.countSubTrees(n, edges, labels))

    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        adj = defaultdict(set)
        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)

        result = [0] * n

        def dfs(node: int, parent: int) -> Counter:
            cnt = collections.Counter()

            for neighbour in adj[node]:
                if neighbour != parent:
                    cnt += dfs(neighbour, node)

            cnt[labels[node]] += 1
            result[node] = cnt[labels[node]]

            return cnt

        dfs(0, -1)

        return result
