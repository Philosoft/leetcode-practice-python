"""
LeetCode: https://leetcode.com/problems/path-sum-iii
"""

from collections import defaultdict
from typing import Optional, Dict
from unittest import TestCase

from lib.TreeNode import TreeNode, build_tree


class Solution(TestCase):
    # def test_example_1(self):
    #     self.assertEqual(3, self.pathSum(build_tree([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]), 8))
    #
    # def test_example_2(self):
    #     self.assertEqual(3, self.pathSum(build_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]), 22))

    def test_case_100(self):
        self.assertEqual(2, self.pathSum(build_tree([1, None, 2, None, 3, None, 4, None, 5]), 3))

    def test_case_101(self):
        self.assertEqual(1, self.pathSum(build_tree([1, -2, -3]), -1))

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0

        self.number_of_paths = 0
        self.hashmap: Dict[int, int] = defaultdict(int)

        def dfs(node: TreeNode, cur_sum: int) -> None:
            if not node:
                return

            cur_sum += node.val
            if cur_sum == targetSum:
                self.number_of_paths += 1

            self.number_of_paths += self.hashmap[cur_sum - targetSum]
            self.hashmap[cur_sum] += 1
            dfs(node.left, cur_sum)
            dfs(node.right, cur_sum)

            self.hashmap[cur_sum] -= 1

        dfs(root, 0)

        return self.number_of_paths
