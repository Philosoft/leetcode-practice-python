"""
LeetCode: https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/description/
"""
from typing import Optional
from unittest import TestCase

from lib.TreeNode import TreeNode, build_tree


class Solution(TestCase):
    path: int = 0

    def test_example_1(self):
        root = build_tree([1, None, 1, 1, 1, None, None, 1, 1, None, 1, None, None, None, 1, None, 1])

        self.assertEqual(3, self.longestZigZag(root))
        self.assertEqual(3, self.longestZigZagSmart(root))

    def test_example_2(self):
        root = build_tree([1, 1, 1, None, 1, None, None, 1, 1, None, 1])

        self.assertEqual(4, self.longestZigZag(root))
        self.assertEqual(4, self.longestZigZagSmart(root))

    def test_example_3(self):
        root = TreeNode(1)

        self.assertEqual(0, self.longestZigZag(root))
        self.assertEqual(0, self.longestZigZagSmart(root))

    def longestZigZagSmart(self, root: Optional[TreeNode]) -> int:
        self.path = 0

        def dfs(node: Optional[TreeNode], left_path: int = 0, right_path: int = 0) -> int:
            if not node:
                return 0

            self.path = max(self.path, max(left_path, right_path))
            dfs(node.left, right_path + 1, 0)
            dfs(node.right, 0, left_path + 1)

        dfs(root)

        return self.path

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.path = 0
        LEFT, RIGHT = 0, 1

        def dfs(node: Optional[TreeNode], direction: int) -> int:
            if not node:
                return 0

            p: int = 0

            if direction == LEFT:
                p = dfs(node.left, RIGHT)
                dfs(node.left, LEFT)
            else:
                p = dfs(node.right, LEFT)
                dfs(node.right, RIGHT)

            self.path = max(self.path, p)

            return p + 1

        dfs(root, LEFT)
        dfs(root, RIGHT)

        return self.path
