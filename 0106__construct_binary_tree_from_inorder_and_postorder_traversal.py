"""
LeetCode: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
"""
from typing import List, Optional
from unittest import TestCase

from lib.TreeNode import TreeNode


class Solution(TestCase):
    def test_example_1(self):
        root = self.buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])

        self.assertEqual(3, root.val)
        self.assertEqual(9, root.left.val)
        self.assertEqual(20, root.right.val)

    def test_case_6(self):
        root = self.buildTree([2, 3, 1], [3, 2, 1])

        self.assertEqual(1, root.val)
        self.assertEqual(2, root.left.val)

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None

        root_val = postorder[-1]
        root = TreeNode(root_val)

        if len(inorder) == 1:
            return root

        root_val_in_idx = inorder.index(root_val)
        left_inorder = inorder[:root_val_in_idx]
        right_inorder = inorder[root_val_in_idx + 1:]

        right_postorder = postorder[-len(right_inorder) - 1:-1]
        left_postorder = postorder[:-len(right_inorder) - 1]

        root.left = self.buildTree(left_inorder, left_postorder)
        root.right = self.buildTree(right_inorder, right_postorder)

        return root
