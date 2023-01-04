import unittest
from typing import Optional, List

from TreeNode import TreeNode, build_tree


class Solution(unittest.TestCase):
    def test_example_1(self):
        root = build_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
        answer = self.pathSum(root, 22)
        answer.sort()

        expected = [[5, 4, 11, 2], [5, 8, 4, 5]]
        expected.sort()

        self.assertEqual(answer, expected)

    def test_example_2(self):
        self.assertEqual(self.pathSum(build_tree([1, 2, 3]), 5), [])

    def test_example_3(self):
        self.assertEqual(self.pathSum(build_tree([1, 2, None]), 0), [])

    def test_empty_tree(self):
        self.assertEqual(self.pathSum(None, 11), [])

    def test_negative_sum(self):
        root = build_tree([-2, None, -3])
        self.assertEqual(self.pathSum(root, -5), [[-2, -3]])

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []

        paths = []
        path = []

        def dfs(node: TreeNode, current_sum: int = 0):
            if not node.left and not node.right:
                if current_sum + node.val == targetSum:
                    path.append(node.val)
                    paths.append(path.copy())
                    path.pop()
                return

            current_sum += node.val
            path.append(node.val)
            if node.left:
                dfs(node.left, current_sum)
            if node.right:
                dfs(node.right, current_sum)

            path.pop()

        dfs(root)

        return paths
