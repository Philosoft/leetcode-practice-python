import unittest
from collections import deque
from typing import List, Optional

from TreeNode import TreeNode, build_tree


class Solution(unittest.TestCase):
    def test_example_1(self):
        root = build_tree([3, 9, 20, None, None, 15, 7])
        expected = [[3], [9, 20], [15, 7]]

        self.assertEquals(self.levelOrder(root), expected)

    def test_example_2(self):
        root = build_tree([1])
        expected = [[1]]

        self.assertEquals(self.levelOrder(root), expected)

    def test_example_3(self):
        self.assertEquals(self.levelOrder(build_tree([])), [])

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        q = deque([root])
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                if not node:
                    continue

                level.append(node.val)
                q.append(node.left)
                q.append(node.right)

            if level:
                result.append(level)

        return result
