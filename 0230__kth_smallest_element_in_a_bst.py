from typing import Optional
from unittest import TestCase

from lib.TreeNode import TreeNode, build_tree


class Solution(TestCase):
    def test_example_1(self):
        root = build_tree([3, 1, 4, None, 2])

        self.assertEqual(1, self.kthSmallest(root, 1))

    def test_example_2(self):
        root = build_tree([5, 3, 6, 2, 4, None, None, 1, None])

        self.assertTrue(3, self.kthSmallest(root, 3))

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal k
            if not node:
                return -1

            # go as deep left as we can
            res = dfs(node.left)
            if res >= 0:
                return res
            k -= 1
            if k == 0:
                return node.val

            # node.val
            return dfs(node.right)

        return dfs(root)
