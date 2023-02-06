"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf
node.

## Example 1

Input: root = [3,9,20,null,null,15,7]
Output: 3

## Example 2

Input: root = [1,null,2]
Output: 2

## Constraints

* The number of nodes in the tree is in the range [0, 10^4].
* -100 <= Node.val <= 100
"""
from typing import Optional
from unittest import TestCase

from lib.TreeNode import TreeNode, build_tree


class Solution(TestCase):
    def test_example_1(self):
        self.assertEqual(3, self.maxDepth(build_tree([3, 9, 20, None, None, 15, 7])))

    def test_example_2(self):
        self.assertEqual(2, self.maxDepth(build_tree([1, None, 2])))

    def test_empty_tree(self):
        self.assertEqual(0, self.maxDepth(None))

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
