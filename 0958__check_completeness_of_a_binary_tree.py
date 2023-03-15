"""
LeetCode: https://leetcode.com/problems/check-completeness-of-a-binary-tree/
"""
from collections import deque
from typing import Optional
from unittest import TestCase

from lib.TreeNode import TreeNode, build_tree


class Solution(TestCase):
    def test_example_1(self):
        self.assertTrue(self.isCompleteTree(build_tree([1, 2, 3, 4, 5, 6, None])))

    def test_example_2(self):
        self.assertFalse(self.isCompleteTree(build_tree([1, 2, 3, 4, 5, None, 7])))

    def test_skewed_to_right_tree(self):
        self.assertFalse(self.isCompleteTree(build_tree([1, 2, 3, None, None, 7, 8])))

    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        seen_null = False
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if seen_null and node:
                    return False

                if node:
                    q.append(node.left)
                    q.append(node.right)
                else:
                    seen_null = True

        return True
