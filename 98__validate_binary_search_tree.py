"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

* The left subtree of a node contains only nodes with keys less than the node's key.
* The right subtree of a node contains only nodes with keys greater than the node's key.
* Both the left and right subtrees must also be binary search trees.

## Example 1:

  2
 / \
1   3

Input: root = [2,1,3]
Output: true

## Example 2:

  5
 / \
1   4
   / \
  3   6

Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

## Constraints:

* The number of nodes in the tree is in the range [1, 10^4].
* -2^31 <= Node.val <= 2^31 - 1
"""
from math import inf
from typing import Optional
from unittest import TestCase

from lib.TreeNode import TreeNode, build_tree


class Solution(TestCase):
    def test_example_1(self):
        self.assertTrue(self.isValidBST(build_tree([2, 1, 3])))

    def test_example_2(self):
        self.assertFalse(self.isValidBST(build_tree([5, 1, 4, None, None, 3, 6])))

    def test_just_root(self):
        self.assertTrue(self.isValidBST(build_tree([1])))

    def test_list(self):
        self.assertFalse(self.isValidBST(build_tree([3, None, 30, 10, None, None, 15, None, 45])))

    def test_forest(self):
        self.assertFalse(
            self.isValidBST(build_tree([120, 70, 140, 50, 100, 130, 160, 20, 55, 75, 110, 119, 135, 150, 200]))
        )

    def test_tricky(self):
        self.assertFalse(self.isValidBST(build_tree([10, 5, 15, None, None, 6, 20])))

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode], left: int | float, right: int | float) -> bool:
            if not node:
                return True

            if not (left < node.val < right):
                return False

            return dfs(node.left, left, node.val) and dfs(node.right, node.val, right)

        return dfs(root, -inf, inf)
