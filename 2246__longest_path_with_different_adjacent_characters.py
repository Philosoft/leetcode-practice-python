"""
You are given a tree (i.e. a connected, undirected graph that has no cycles) rooted at node 0 consisting of n nodes
numbered from 0 to n - 1. The tree is represented by a 0-indexed array parent of size n, where parent[i] is the parent
of node i. Since node 0 is the root, parent[0] == -1.

You are also given a string s of length n, where s[i] is the character assigned to node i.

Return the length of the longest path in the tree such that no pair of adjacent nodes on the path have the same
character assigned to them.


Example 1:

Input:
    parent = [-1,0,0,1,1,2]
    s = "abacbe"
Output: 3
Explanation:
    The longest path where each two adjacent nodes have different characters in the tree is the path: 0 -> 1 -> 3.
    The length of this path is 3, so 3 is returned.
    It can be proven that there is no longer path that satisfies the conditions.

Example 2:

Input:
    parent = [-1,0,0,0]
    s = "aabc"
Output: 3
Explanation:
    The longest path where each two adjacent nodes have different characters is the path: 2 -> 0 -> 3.
    The length of this path is 3, so 3 is returned.

Constraints:

* n == parent.length == s.length
* 1 <= n <= 10^5
* 0 <= parent[i] <= n - 1 for all i >= 1
* parent[0] == -1
* parent represents a valid tree.
* s consists of only lowercase English letters.
"""
import unittest
from collections import defaultdict, deque
from typing import List, Dict, Set, Deque


class Solution(unittest.TestCase):
    def test_example_1(self):
        parent = [-1, 0, 0, 1, 1, 2]
        s = "abacbe"

        self.assertEqual(3, self.longestPath(parent, s))
        self.assertEqual(3, self.longestPathBFS(parent, s))

    def test_example_2(self):
        parent = [-1, 0, 0, 0]
        s = "aabc"

        self.assertEqual(3, self.longestPath(parent, s))
        self.assertEqual(3, self.longestPathBFS(parent, s))

    def test_askew_tree(self):
        parent = [-1, 0, 0, 1, 3, 4, 5]
        s = "abcdefj"

        self.assertEqual(7, self.longestPath(parent, s))
        self.assertEqual(7, self.longestPathBFS(parent, s))

    def test_askew_tree_cut_off(self):
        parent = [-1, 0, 0, 1, 3, 4, 5]
        s = "aacdefj"

        self.assertEqual(5, self.longestPath(parent, s))
        self.assertEqual(5, self.longestPathBFS(parent, s))

    def test_tricky_one(self):
        parent = [-1, 0, 1]
        s = "aab"

        self.assertEqual(2, self.longestPath(parent, s))
        self.assertEqual(2, self.longestPathBFS(parent, s))

    def test_case_11(self):
        parent = [-1, 0, 1, 2, 3, 4]
        s = "zzabab"

        self.assertEqual(5, self.longestPath(parent, s))
        self.assertEqual(5, self.longestPathBFS(parent, s))

    def test_case_14(self):
        parent = [-1, 137, 65, 60, 73, 138, 81, 17, 45, 163, 145, 99, 29, 162, 19, 20, 132, 132, 13, 60, 21, 18, 155,
                  65, 13, 163, 125, 102, 96, 60, 50, 101, 100, 86, 162, 42, 162, 94, 21, 56, 45, 56, 13, 23, 101, 76,
                  57, 89,
                  4, 161, 16, 139, 29, 60, 44, 127, 19, 68, 71, 55, 13, 36, 148, 129, 75, 41, 107, 91, 52, 42, 93, 85,
                  125,
                  89, 132, 13, 141, 21, 152, 21, 79, 160, 130, 103, 46, 65, 71, 33, 129, 0, 19, 148, 65, 125, 41, 38,
                  104,
                  115, 130, 164, 138, 108, 65, 31, 13, 60, 29, 116, 26, 58, 118, 10, 138, 14, 28, 91, 60, 47, 2, 149,
                  99, 28,
                  154, 71, 96, 60, 106, 79, 129, 83, 42, 102, 34, 41, 55, 31, 154, 26, 34, 127, 42, 133, 113, 125, 113,
                  13,
                  54, 132, 13, 56, 13, 42, 102, 135, 130, 75, 25, 80, 159, 39, 29, 41, 89, 85, 19, ]

        s = "ajunvefrdrpgxltugqqrwisyfwwtldxjgaxsbbkhvuqeoigqssefoyngykgtthpzvsxgxrqedntvsjcpdnupvqtroxmbpsdwoswxfarnixkvcimzgvrevxnxtkkovwxcjmtgqrrsqyshxbfxptuvqrytctujnzzydhpal"

        self.assertEqual(17, self.longestPath(parent, s))
        self.assertEqual(17, self.longestPathBFS(parent, s))

    def test_maxi_tree(self):
        parent = []
        s = []
        prev = "b"
        for i in range(100_000):
            parent.append(i - 1)
            s.append("a" if prev == "b" else "b")
            prev = "a" if prev == "b" else "b"

        s = "".join(s)

        self.assertEqual(len(parent), self.longestPathBFS(parent, s))

        import sys
        import resource

        prev_recursion_limit = sys.getrecursionlimit()
        prev_stack_limit = resource.getrlimit(resource.RLIMIT_STACK)
        sys.setrecursionlimit(2 * len(parent))
        resource.setrlimit(resource.RLIMIT_STACK, (len(parent) * 512, resource.RLIM_INFINITY))

        self.assertEqual(len(parent), self.longestPath(parent, s))

        sys.setrecursionlimit(prev_recursion_limit)
        resource.setrlimit(resource.RLIMIT_STACK, prev_stack_limit)

    def longestPathBFS(self, parent: List[int], s: str) -> int:
        """
        Context info: longest path through a node in a tree is sum of 2 longest paths + 1

        Idea is to go from the bottom up.
        Start with leaves.
        For each leaf calculate two lengthiest paths. Since it's leaf it'll be [0, 0]
        If path parent -> child is correct, update maximum paths of parent
            Current max paths of parents are [0, 0]
            Update it with max(max paths of current node) + 1
                ^ max_paths_of_current_node = [0, 0], since it's leaf
                ^ +1 since we need to count node itself
            New max_paths of parent is [0, 1]
            If it was last unprocessed child of this parent, add parent to queue
        Update global result regardless result = max(result, sum(max_cur_paths) + 1)

        Repeat the process while queue is not empty
        """
        result = 0
        tree: Dict[int, Set[int]] = defaultdict(set)
        for i in range(1, len(parent)):
            tree[parent[i]].add(i)

        q: Deque[int] = deque([])
        longest_paths = []
        # 👇 this will be used to start processing parent nodes AFTER processing all the children
        unprocessed_children = [0] * len(parent)
        for i in range(len(parent)):
            longest_paths.append([0, 0])
            if len(tree[i]) == 0:
                # no children => leaf
                q.append(i)
            else:
                unprocessed_children[i] = len(tree[i])

        while q:
            node = q.popleft()
            parent_node = parent[node]
            current_node_longest_path = max(longest_paths[node]) + 1
            result = max(result, sum(longest_paths[node]) + 1)

            if parent_node != -1:
                unprocessed_children[parent_node] -= 1
                if unprocessed_children[parent_node] == 0:
                    q.append(parent_node)

                # parent -> child is a valid path
                # update parent's longest path
                if s[node] != s[parent_node]:
                    parent_paths = longest_paths[parent_node]
                    longest_paths[parent_node] = [max(parent_paths), max(min(parent_paths), current_node_longest_path)]

        return result

    def longestPath(self, parent: List[int], s: str) -> int:
        tree: Dict[int, Set[int]] = defaultdict(set)
        for i in range(1, len(parent)):
            tree[parent[i]].add(i)

        result = 0

        def dfs_with_two_paths(starting_node: int) -> int:
            nonlocal result
            max_paths = [0, 0]
            for nei in tree[starting_node]:
                local_max = dfs_with_two_paths(nei)
                if s[nei] != s[starting_node]:
                    max_paths = [max(max_paths), max(min(max_paths), local_max)]

            current_max = sum(max_paths) + 1
            result = max(result, current_max)

            return max(max_paths) + 1

        dfs_with_two_paths(0)

        return result
