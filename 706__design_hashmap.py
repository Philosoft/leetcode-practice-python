import unittest
from dataclasses import dataclass
from typing import List

"""
Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

MyHashMap() initializes the object with an empty map.
void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map,
update the corresponding value.
int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping
for the key.
void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.
 

Example 1:

Input
    ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
    [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
Output
    [null, null, null, 1, -1, null, 1, null, -1]

Explanation
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // The map is now [[1,1]]
myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]
 

Constraints:

0 <= key, value <= 10^6
At most 10^4 calls will be made to put, get, and remove.
"""


class TestHashMap(unittest.TestCase):
    def test_example_1(self):
        myHashMap = MyHashMap()
        myHashMap.put(1, 1)  # The map is now [[1,1]]
        myHashMap.put(2, 2)  # The map is now [[1,1], [2,2]]
        self.assertEqual(1, myHashMap.get(1))  # return 1, The map is now [[1,1], [2,2]]
        self.assertEqual(-1, myHashMap.get(3))  # return -1 (i.e., not found), The map is now [[1,1], [2,2]]
        myHashMap.put(2, 1)  # The map is now [[1,1], [2,1]] (i.e., update the existing value)
        self.assertEqual(1, myHashMap.get(2))  # return 1, The map is now [[1,1], [2,1]]
        myHashMap.remove(2)  # remove the mapping for 2, The map is now [[1,1]]
        self.assertEqual(-1, myHashMap.get(2))  # return -1 (i.e., not found), The map is now [[1,1]]

    def test_big_map(self):
        m = MyHashMap()
        for i in range(1000):
            m.put(i, i)

        for i in range(1000):
            self.assertEqual(i, m.get(i))

    def test_chaining(self):
        m = MyHashMap()
        for i in range(1, 16 * 16, 16):
            m.put(i, i)

        for i in range(1, 10 * 16, 16):
            self.assertEqual(i, m.get(i))

    def test_remove_head_in_chain(self):
        m = MyHashMap()
        m.put(1, 1)
        m.put(17, 171)
        m.remove(1)

        self.assertEqual(-1, m.get(1))
        self.assertEqual(171, m.get(17))


@dataclass
class Value:
    key: int
    val: int


# hashmap with very lousy chaining
# better would be with double linked list, but ... oh well
class MyHashMap:
    def __init__(self):
        self.cap = 16
        self.size = 0
        self.map: List[List[Value]] = []
        for _ in range(self.cap):
            self.map.append([])

    def put(self, key: int, value: int) -> None:
        idx = self.hash(key)
        row = self.map[idx]

        # search for existing value
        was_updated = False
        for v in row:
            if v.key == key:
                v.val = value
                was_updated = True
                break

        if not was_updated:
            row.append(Value(key, value))

        self.size += 1
        if self.size >= self.cap // 2:
            self.rehash()

    def get(self, key: int) -> int:
        idx = self.hash(key)
        for v in self.map[idx]:
            if v.key == key:
                return v.val

        return -1

    def remove(self, key: int) -> None:
        idx = self.hash(key)
        for i in range(len(self.map[idx])):
            if self.map[idx][i].key == key:
                del self.map[idx][i]
                self.size -= 1
                return

    def hash(self, key: int) -> int:
        return key % self.cap

    def rehash(self) -> None:
        self.size = 0
        self.cap *= 2
        old_map = self.map
        self.map = []
        for _ in range(self.cap):
            self.map.append([])

        for row in old_map:
            for v in row:
                self.put(v.key, v.val)
