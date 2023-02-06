"""
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure
and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree
tree could also be considered as a subtree of itself.

## Example 1

Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true

## Example 2

Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false

## Constraints

* The number of nodes in the root tree is in the range [1, 2000].
* The number of nodes in the subRoot tree is in the range [1, 1000].
* -10^4 <= root.val <= 10^4
* -10^4 <= subRoot.val <= 10^4
"""
from typing import Optional
from unittest import TestCase

from lib.TreeNode import TreeNode, build_tree


class Solution(TestCase):
    def test_example_1(self):
        search_root = build_tree([3, 4, 5, 1, 2])
        sub = build_tree([4, 1, 2])

        self.assertTrue(self.isSubtree(search_root, sub))
        self.assertTrue(self.isSubtreeRecursive(search_root, sub))

    def test_example_2(self):
        search_root = build_tree([3, 4, 5, 1, 2, None, None, None, None, 0, None])
        sub = build_tree([4, 1, 2])

        self.assertFalse(self.isSubtree(search_root, sub))
        self.assertFalse(self.isSubtreeRecursive(search_root, sub))

    def test_tricky(self):
        self.assertTrue(self.isSubtree(build_tree([1, 1, None]), build_tree([1])))
        self.assertTrue(self.isSubtreeRecursive(build_tree([1, 1, None]), build_tree([1])))

    def isSubtreeRecursive(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same(search: Optional[TreeNode], sub: Optional[TreeNode]) -> bool:
            if not search and not sub:
                return True
            if not search or not sub:
                return False

            return search.val == sub.val and same(search.left, sub.left) and same(search.right, sub.right)

        return (root and subRoot) and (
                same(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        )

    def isSubtree(self, root: Optional[TreeNode], sub: Optional[TreeNode]) -> bool:
        if not root or not sub:
            return False

        return self.transcribe(sub) in self.transcribe(root)

    def transcribe(self, root: Optional[TreeNode]) -> str:
        if not root:
            return '#'

        return "^" + str(root.val) + self.transcribe(root.left) + self.transcribe(root.right)
