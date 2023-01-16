"""
There is a tree (i.e. a connected, undirected graph with no cycles) consisting of n nodes numbered from 0 to n - 1 and
exactly n - 1 edges.

You are given a 0-indexed integer array vals of length n where vals[i] denotes the value of the ith node. You are also
given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting nodes
ai and bi.

A good path is a simple path that satisfies the following conditions:

* The starting node and the ending node have the same value.
* All nodes between the starting node and the ending node have values less than or equal to the starting node
    (i.e. the starting node's value should be the maximum value along the path).

Return the number of distinct good paths.

Note that a path and its reverse are counted as the same path. For example, 0 -> 1 is considered to be the same as
1 -> 0. A single node is also considered as a valid path.

Example 1:

Input:
    vals = [1,3,2,1,3]
    edges = [[0,1],[0,2],[2,3],[2,4]]
Output: 6
Explanation:
    There are 5 good paths consisting of a single node.
    There is 1 additional good path: 1 -> 0 -> 2 -> 4.
    (The reverse path 4 -> 2 -> 0 -> 1 is treated as the same as 1 -> 0 -> 2 -> 4.)
    Note that 0 -> 2 -> 3 is not a good path because vals[2] > vals[0].

Example 2:

Input:
    vals = [1,1,2,2,3]
    edges = [[0,1],[1,2],[2,3],[2,4]]
Output: 7
Explanation:
    There are 5 good paths consisting of a single node.
    There are 2 additional good paths: 0 -> 1 and 2 -> 3.

Example 3:

Input:
    vals = [1]
    edges = []
Output: 1
Explanation:
    The tree consists of only one node, so there is one good path.


Constraints:

* n == vals.length
* 1 <= n <= 3 * 10^4
* 0 <= vals[i] <= 10^5
* edges.length == n - 1
* edges[i].length == 2
* 0 <= ai, bi < n
* ai != bi
* edges represents a valid tree.
"""
import unittest
from collections import defaultdict
from dataclasses import dataclass, field
from typing import List, Set


@dataclass
class UnionFind:
    parents: dict[int, int] = field(default_factory=dict)
    ranks: dict[int, int] = field(default_factory=lambda: defaultdict(int))

    def find(self, x: int) -> int:
        if x not in self.parents:
            self.parents[x] = x

        if self.parents[x] != x:
            # path compression ftw
            self.parents[x] = self.find(self.parents[x])

        return self.parents[x]

    def union(self, x: int, y: int) -> None:
        rootx, rooty = self.find(x), self.find(y)
        if rootx == rooty:
            return

        if self.ranks[rootx] < self.ranks[rooty]:
            self.parents[rootx] = rooty
        elif self.ranks[rootx] > self.ranks[rooty]:
            self.parents[rooty] = rootx
        else:
            self.parents[rooty] = rootx
            self.ranks[rootx] += 1


class Solution(unittest.TestCase):
    def test(self):
        options = [
            ('first leetcode example', 6, [1, 3, 2, 1, 3], [[0, 1], [0, 2], [2, 3], [2, 4]]),
            ('only two real path (+ 5 1-node ones)', 7, [1, 1, 2, 2, 3], [[0, 1], [1, 2], [2, 3], [2, 4]]),
            ('one node tree', 1, [1], []),
        ]

        for name, expected, vals, edges in options:
            with self.subTest(name):
                self.assertEqual(expected, self.numberOfGoodPaths(vals, edges))

    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        """
        my own idea was to use bruuuute force - dfs on every node to find all valid paths from that node. too long
        second idea was to use union-find to somehow simplify process. turned out to be another brute force
        third was to use union-find to built trees from the lowest values to biggest and then check for paths, failed to
        produce  decent algorithm that wouldn't involve brute-force dfs on ever-growing trees (with less node to check
            on a first glance, but eventually it was exactly the same as first one, since in first implementation
            I stop exploring paths at the moment of next_node_val > started_node_val

        And then I gave up and went for solutions
        """
        result = 0
        adj: dict[int, Set[int]] = defaultdict(set)
        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)
        values_to_nodes_tmp: dict[int, Set[int]] = defaultdict(set)
        values_to_nodes: dict[int, Set[int]] = defaultdict(set)

        for i in range(len(vals)):
            values_to_nodes_tmp[vals[i]].add(i)

        for v in sorted(values_to_nodes_tmp.keys()):
            values_to_nodes[v] = values_to_nodes_tmp[v]
        del values_to_nodes_tmp

        uf = UnionFind()

        # showtime
        # go from 0 -> n in values
        for val, nodes in values_to_nodes.items():
            # consider each node
            for node in nodes:
                # consider each neighbour of each node
                for nei in adj[node]:
                    # if value is "correct" - we can construct a good path
                    # can construct a good path? add to subgraph via union
                    # specific path doesn't matter, because we are interested only in number of good paths
                    # and for that we only need number of nodes in a correct subtree
                    if vals[node] >= vals[nei]:
                        uf.union(node, nei)
            # group[i] -> c
            # where
            #   i - is a common root
            #   c - number of nodes in subtree
            group: dict[int, int] = defaultdict(int)
            for node in nodes:
                group[uf.find(node)] += 1

            # mathematical mad skillz (kudos goes to ... not me)
            # originally here I resorted to dfs from each root ... 🤦‍♂️
            for _, number_of_nodes in group.items():
                result += number_of_nodes * (number_of_nodes + 1) // 2

        return result
