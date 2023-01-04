import unittest
from typing import Optional, List

from lib.TreeNode import build_tree, TreeNode


class Solution(unittest.TestCase):
    def test_example_1(self):
        root = build_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])
        self.assertTrue(self.hasPathSum(root, 22))

    def test_example_2(self):
        self.assertFalse(self.hasPathSum(build_tree([1, 2, 3]), 5))

    def test_example_3(self):
        self.assertFalse(self.hasPathSum(build_tree([]), 0))

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.is_path_found = False

        def dfs(node: Optional[TreeNode], path: List[int]):
            if self.is_path_found or not node:
                return

            path.append(node.val)
            if not node.left and not node.right:
                # leaf
                if sum(path) == targetSum:
                    self.is_path_found = True
                path.pop()
                return

            dfs(node.left, path)
            dfs(node.right, path)
            path.pop()

        dfs(root, [])

        return self.is_path_found

