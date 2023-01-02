import unittest
from typing import List, Optional

from TreeNode import TreeNode


class Solution(unittest.TestCase):
    @staticmethod
    def tree_to_array(root: TreeNode) -> List[int]:
        result = []
        q = [root]
        while q:
            for _ in range(len(q)):
                node = q.pop(0)
                if not node:
                    continue

                q.append(node.left)
                q.append(node.right)

                result.append(node.val)

        return result

    def test_example_1(self):
        tree = self.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
        expected = [3, 9, 20, 15, 7]

        self.assertEquals(self.tree_to_array(tree), expected)

    def test_example_2(self):
        tree = self.buildTree([-1], [-1])
        expected = [-1]

        self.assertEquals(self.tree_to_array(tree), expected)

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        nodes_count = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:nodes_count + 1], inorder[:nodes_count])
        root.right = self.buildTree(preorder[nodes_count + 1:], inorder[nodes_count + 1:])

        return root
