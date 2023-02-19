"""
LeetCode: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to
right, then right to left for the next level and alternate between).

## Example 1

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

## Example 2:

Input: root = [1]
Output: [[1]]

## Example 3:

Input: root = []
Output: []

## Constraints

* The number of nodes in the tree is in the range [0, 2000].
* -100 <= Node.val <= 100
"""
from collections import deque
from typing import Optional, List
from unittest import TestCase

from lib.TreeNode import TreeNode, build_tree


class Solution(TestCase):
    def test_example_1(self):
        root = build_tree([3, 9, 20, None, None, 15, 7])
        expected = [[3], [20, 9], [15, 7]]

        self.assertEqual(expected, self.zigzagLevelOrder(root))

    def test_example_2(self):
        self.assertEqual([[1]], self.zigzagLevelOrder(build_tree([1])))

    def test_example_3(self):
        self.assertEqual([], self.zigzagLevelOrder(None))

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque([root])
        result = []
        reverse = False
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if reverse:
                level = level[::-1]
            reverse = not reverse
            result.append(level)

        return result
