"""
LeetCode: https://leetcode.com/problems/maximum-width-of-binary-tree/
"""

from collections import deque
from typing import Deque, Tuple, Optional
from unittest import TestCase

from lib.TreeNode import TreeNode, build_tree


class Solution(TestCase):
    def test_example_1(self):
        root = build_tree([1, 3, 2, 5, 3, None, 9])
        self.assertEqual(4, self.widthOfBinaryTree(root))

    def test_example_2(self):
        root = build_tree([1, 3, 2, 5, None, None, 9, 6, None, 7])
        self.assertEqual(7, self.widthOfBinaryTree(root))

    def test_example_3(self):
        root = build_tree([1, 3, 2, 5])
        self.assertEqual(2, self.widthOfBinaryTree(root))

    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_width = 0
        q: Deque[Tuple[TreeNode, int]] = deque([(root, 1)])  # node, idx
        while q:
            left, right = q[0][1], q[-1][1]
            max_width = max(max_width, right - left + 1)
            for _ in range(len(q)):
                node, idx = q.popleft()
                if node.left:
                    q.append((node.left, idx * 2))
                if node.right:
                    q.append((node.right, idx * 2 + 1))

        return max_width

    def widthOfBinaryTreeFirstApproach(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.max = 0

        q: Deque[Tuple[Optional[TreeNode], int]] = deque([(root, 0)])
        lvl = 0
        while q:
            lvl += 1
            counter = 0
            left, right = None, None
            for node in q:
                if node[0]:
                    left = node
                    break

            for node in reversed(q):
                if node[0]:
                    right = node
                    break

            if left and right:
                self.max = max(self.max, right[1] - left[1] + 1)

            for _ in range(len(q)):
                node, idx = q.popleft()
                if not node:
                    counter += 1
                    counter += 1
                    continue

                q.append((node.left, counter))
                counter += 1
                q.append((node.right, counter))
                counter += 1

        return self.max
