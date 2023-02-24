# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
from typing import Optional
from unittest import TestCase

from lib.TreeNode import TreeNode, build_tree


class TestCodec(TestCase):
    def test_example_1(self):
        root = build_tree([1, 2, 3, None, None, 4, 5])
        codec = Codec()

        new_tree = codec.deserialize(codec.serialize(root))

        result = []

        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                return

            result.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        original = result.copy()
        result = []
        dfs(new_tree)
        new = result.copy()

        self.assertEqual(original, new)

    def test_empty_tree(self):
        codec = Codec()

        self.assertEqual("#", codec.serialize(None))
        self.assertIsNone(codec.deserialize("#"))


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return '#'

        result = []
        q = deque([root])
        while q:
            buf = []
            for _ in range(len(q)):
                node = q.popleft()

                if not node:
                    buf.append("#")
                    continue

                buf.append("^" + str(node.val))

                q.append(node.left)
                q.append(node.right)

            if buf:
                result.extend(buf)

        return "".join(result)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if len(data) == 1:
            if data[0] == "#":
                return None
            else:
                raise Exception("Incorrect format")

        nodes = []
        data_ptr = 0
        while data_ptr < len(data):
            if data[data_ptr] == "#":
                nodes.append(None)
                data_ptr += 1
                continue

            if data[data_ptr] == "^":
                data_ptr += 1
                buf = []
                while data_ptr < len(data) and data[data_ptr] not in ["#", "^"]:
                    buf.append(data[data_ptr])
                    data_ptr += 1

                nodes.append(TreeNode(int("".join(buf))))
                continue

        root = nodes[0]
        linked_nodes = [root]
        node_ptr = 0
        process = deque(nodes)
        process.popleft()
        while process:
            parent = linked_nodes[node_ptr]
            left, right = process.popleft(), process.popleft()

            if left:
                parent.left = left
                linked_nodes.append(left)

            if right:
                parent.right = right
                linked_nodes.append(right)
            node_ptr += 1

        return root
