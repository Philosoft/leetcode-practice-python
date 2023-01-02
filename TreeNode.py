import unittest
from dataclasses import dataclass
from typing import Optional, List


@dataclass
class TreeNode:
    val: int = 0
    left: Optional['TreeNode'] = None
    right: Optional['TreeNode'] = None


# [3, 9, 20, None, None, 15, 7]
#   3
#  / \
# 9  20
#    /\
#   15 7
def build_tree(node_values: List[Optional[int]]) -> Optional[TreeNode]:
    if not node_values:
        return None

    nodes = [TreeNode(node_values.pop(0))]
    ptr = -1
    while node_values:
        ptr += 1
        left, right = node_values.pop(0), node_values.pop(0)

        root = nodes[ptr]
        if left:
            root.left = TreeNode(left)
            nodes.append(root.left)
        if right:
            root.right = TreeNode(right)
            nodes.append(root.right)

    return nodes[0]


class TestTreeBuilding(unittest.TestCase):
    def test_empty_tree(self):
        self.assertIsNone(build_tree([]))

    def test_only_root(self):
        root = build_tree([0])
        self.assertIsNone(root.left)
        self.assertIsNone(root.right)
        self.assertEquals(root.val, 0)

    def test_only_left_leaf(self):
        root = build_tree([0, 1, None])

        self.assertEquals(root.val, 0)

        self.assertIsNotNone(root.left)
        self.assertIsInstance(root.left, TreeNode)
        self.assertEquals(root.left.val, 1)

        self.assertIsNone(root.right)

    def test_only_right(self):
        root = build_tree([0, None, 2])

        self.assertEquals(root.val, 0)

        self.assertIsNone(root.left)

        self.assertIsNotNone(root.right)
        self.assertIsInstance(root.right, TreeNode)
        self.assertEquals(root.right.val, 2)

    def test_basic(self):
        data = [3, 9, 20, None, None, 15, 7]
        root = build_tree(data)

        self.assertEquals(root.right.val, 20)
        self.assertEquals(root.right.right.val, 7)
