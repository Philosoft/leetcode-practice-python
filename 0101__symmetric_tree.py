from typing import Optional
from unittest import TestCase

from lib.TreeNode import TreeNode, build_tree


class Solution(TestCase):
    def test_example_1(self):
        self.assertTrue(self.isSymmetric(build_tree([1, 2, 2, 3, 4, 4, 3])))

    def test_example_2(self):
        self.assertFalse(self.isSymmetric(build_tree([1, 2, 2, None, 3, None, 3])))

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root or (not root.left and not root.right):
            return True

        if not root.left or not root.right:
            return False

        def helper(left: Optional[TreeNode], right: Optional[TreeNode]):
            if not left and not right:
                return True

            if not left or not right:
                return False

            if left.val != right.val:
                return False

            return helper(left.left, right.right) and helper(left.right, right.left)

        return helper(root.left, root.right)
