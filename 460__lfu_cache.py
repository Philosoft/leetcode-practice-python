from collections import defaultdict
from dataclasses import dataclass
from typing import Dict


@dataclass
class CacheNode:
    key: int
    val: int
    count: int


class LFUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.key_to_node: Dict[int, CacheNode] = {}
        self.count_to_nodes: Dict[int, Dict[int, CacheNode]] = defaultdict(dict)  # count -> [key -> node]
        self.min_count = 0

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1

        node = self.key_to_node[key]
        del self.count_to_nodes[node.count][key]

        node.count += 1
        self.count_to_nodes[node.count][key] = node
        if not self.count_to_nodes[self.min_count]:
            self.min_count += 1

        return node.val

    def put(self, key: int, val: int) -> None:
        if self.cap == 0:
            return

        if key in self.key_to_node:
            self.key_to_node[key].val = val
            self.get(key)  # to update usage count and reorder stuff
            return

        if len(self.key_to_node) == self.cap:
            lru_key = -1
            for k in self.count_to_nodes[self.min_count].keys():
                lru_key = k
                break
            del self.count_to_nodes[self.min_count][lru_key]
            del self.key_to_node[lru_key]

        self.count_to_nodes[1][key] = self.key_to_node[key] = CacheNode(key, val, 1)
        self.min_count = 1
