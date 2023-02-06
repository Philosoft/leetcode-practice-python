from typing import Optional
from unittest import TestCase

from lib.TreeNode import TreeNode, build_tree


class Solution(TestCase):
    def test_example_3(self):
        root = self.invertTree(build_tree([4, 2, 7, 1, 3, 6, 9]))
        left, right = root.left, root.right

        self.assertEqual(7, left.val)
        self.assertEqual(2, right.val)

        self.assertEqual(9, left.left.val)
        self.assertEqual(1, right.right.val)

    def test_example_2(self):
        root = build_tree([2, 1, 3])
        root = self.invertTree(root)

        self.assertEqual(3, root.left.val)
        self.assertEqual(1, root.right.val)

    def test_example_3(self):
        self.assertIsNone(self.invertTree(None))

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

        return root
