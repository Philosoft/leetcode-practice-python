"""
Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:

void add(key) Inserts the value key into the HashSet.
bool contains(key) Returns whether the value key exists in the HashSet or not.
void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.


Example 1:

Input
    ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
    [[], [1], [2], [1], [3], [2], [2], [2], [2]]
Output
    [null, null, null, true, false, null, true, null, false]

Explanation
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // return True
myHashSet.contains(3); // return False, (not found)
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // return True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // return False, (already removed)


Constraints:

0 <= key <= 10^6
At most 10^4 calls will be made to add, remove, and contains.
"""
import unittest
from typing import List


class TestHashSet(unittest.TestCase):
    def test(self):
        hs = MyHashSet()
        hs.add(1)  # set = [1]
        hs.add(2)  # set = [1, 2]
        self.assertTrue(hs.contains(1))  # return True
        self.assertFalse(hs.contains(3))  # return False, (not found)
        hs.add(2)  # set = [1, 2]
        self.assertTrue(hs.contains(2))  # return True
        hs.remove(2)  # set = [1]
        self.assertFalse(hs.contains(2))  # return False, (already removed)

    def test_collision(self):
        hs = MyHashSet()
        hs.add(1)
        hs.add(17)

        self.assertTrue(hs.contains(1))
        self.assertTrue(hs.contains(17))

        hs.remove(1)
        self.assertFalse(hs.contains(1))
        self.assertTrue(hs.contains(17))

    def test_rehash(self):
        hs = MyHashSet()

        for i in range(1, 16 * 16 + 1, 16):
            hs.add(i)

        for i in range(1, 16 * 16 + 1, 16):
            self.assertTrue(hs.contains(i))

class MyHashSet:
    def __init__(self):
        self.cap = 16
        self.size = 0
        self.data: List[List[int]] = []
        for _ in range(self.cap):
            self.data.append([])

    def hash(self, key: int) -> int:
        return key % self.cap

    def add(self, key: int) -> None:
        if not self.contains(key):
            idx = self.hash(key)
            self.data[idx].append(key)
            self.size += 1

            if self.size >= self.cap // 2:
                self.rehash()

    def rehash(self):
        self.cap *= 2
        self.size = 0
        old_set = self.data
        self.data = []
        for _ in range(self.cap):
            self.data.append([])

        for row in old_set:
            for val in row:
                self.add(val)

    def remove(self, key: int) -> None:
        idx = self.hash(key)
        for i in range(len(self.data[idx])):
            if self.data[idx][i] == key:
                self.data[idx][i], self.data[idx][-1] = self.data[idx][-1], self.data[idx][i]
                self.data[idx].pop()
                return

    def contains(self, key: int) -> bool:
        idx = self.hash(key)
        for v in self.data[idx]:
            if v == key:
                return True

        return False
