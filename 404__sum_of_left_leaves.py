"""
Given the root of a binary tree, return the sum of all left leaves.
A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.

## Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.

## Example 2:

Input: root = [1]
Output: 0

## Constraints:

* The number of nodes in the tree is in the range [1, 1000].
* -1000 <= Node.val <= 1000
"""
from typing import Optional
from unittest import TestCase

from lib.TreeNode import TreeNode, build_tree


class Solution(TestCase):
    def test_example_1(self):
        self.assertEqual(24, self.sumOfLeftLeaves(build_tree([3, 9, 20, None, None, 15, 7])))

    def test_example_2(self):
        self.assertEqual(0, self.sumOfLeftLeaves(build_tree([0])))

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        s = 0

        def dfs(node: Optional[TreeNode]):
            nonlocal s
            if not node:
                return

            if node.left and not node.left.left and not node.left.right:
                s += node.left.val

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return s
