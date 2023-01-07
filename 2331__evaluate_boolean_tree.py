import unittest

from lib.TreeNode import TreeNode, build_tree


class Solution(unittest.TestCase):
    def test_example_1(self):
        root = build_tree([2, 1, 3, None, None, 0, 1])

        self.assertTrue(self.evaluateTree(root))

    def test_example_2(self):
        self.assertFalse(self.evaluateTree(build_tree([0])))

    def test_only_true(self):
        self.assertTrue(self.evaluateTree(build_tree([1])))

    def evaluateTree(self, root: TreeNode) -> bool:
        if root.left:
            # not a leaf node
            if root.val == 2:
                return self.evaluateTree(root.left) or self.evaluateTree(root.right)
            else:
                return self.evaluateTree(root.left) and self.evaluateTree(root.right)
        else:
            # leaf node
            return root.val == 1
