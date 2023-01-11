from dataclasses import dataclass
from typing import Dict, Optional
from unittest import TestCase

"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to
the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

Constraints:

1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.
"""


class TestCache(TestCase):
    def test_example_1(self):
        actions = [("put", [1, 1]), ("put", [2, 2]), ("get", [1], 1), ("put", [3, 3]), ("get", [2], -1),
            ("put", [4, 4]), ("get", [1], -1), ("get", [3], 3), ("get", [4], 4), ]

        cache = LRUCache(2)
        for action in actions:
            if action[0] == "put":
                cache.put(*action[1])
            else:
                self.assertEqual(action[2], cache.get(*action[1]))


@dataclass
class CacheNode:
    val: int
    key: int
    left: Optional['CacheNode'] = None
    right: Optional['CacheNode'] = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.map: Dict[int, CacheNode] = {}
        self.tail: CacheNode = CacheNode(666, 999)
        self.head: CacheNode = CacheNode(666, 999)
        self.head.right, self.tail.left = self.tail, self.head

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1

        v = self.map[key].val
        self.remove(key)
        self.add(key, v)

        return v

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.remove(key)
            self.add(key, value)
        else:
            self.add(key, value)
            if len(self.map) > self.cap:
                self.remove(self.head.right.key)

    def remove(self, key: int) -> None:
        if key not in self.map:
            return

        node = self.map[key]
        node.left.right, node.right.left = node.right, node.left
        del node
        del self.map[key]

    def add(self, key: int, value: int) -> None:
        node = CacheNode(value, key)
        prev = self.tail.left
        prev.right = self.tail.left = node
        node.left, node.right = prev, self.tail

        self.map[key] = node
