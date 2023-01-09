import unittest
from typing import Optional, List

from lib.TreeNode import TreeNode, build_tree


class Solution(unittest.TestCase):
    def test_example_1(self):
        root = build_tree([1, None, 2, None, 3])
        expected = [1, 2, 3]

        self.assertEqual(expected, self.preorderTraversal(root))

    def test_empty_tree(self):
        self.assertEqual([], self.preorderTraversal(None))

    def test_only_root(self):
        self.assertEqual([1], self.preorderTraversal(TreeNode(1)))

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []

        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                return

            stack.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return stack
