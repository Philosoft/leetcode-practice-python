"""
LeetCode: https://leetcode.com/problems/optimal-partition-of-string/

Solution idea
=============

One word: greedy

* start at the begining
* greedily chunk up as much as you can
* chomp it of
* repeat until the end
"""
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        self.assertEqual(4, self.partitionString("abacaba"))

    def test_example_2(self):
        self.assertEqual(6, self.partitionString("ssssss"))

    def test_random_string(self):
        self.assertEqual(97, self.partitionString(
            "alsjdfhlasdfoqgewriqyewgfyusdbchjgfolhdsachdosagfoiudsfhadlkjfalkdsfaksdgflksagflkagfhagfggggggggggggalsjdfhlasdfoqgewriqyewgfyusdbchjgfolhdsachdosagfoiudsfhadlkjfalkdsfaksdgflksagflkagfhagfggggggggggggalsjdfhlasdfoqgewriqyewgfyusdbchjgfolhdsachdosagfoiudsfhadlkjfalkdsfaksdgflksagflkagfhagfggggggggggggalsjdfhlasdfoqgewriqyewgfyusdbchjgfolhdsachdosagfoiudsfhadlkjfalkdsfaksdgflksagflkagfhagfgggggggggggg"))

    def partitionString(self, s: str) -> int:
        ptr = 0
        substr_count = 0
        window = set()
        while ptr < len(s):
            while ptr < len(s) and s[ptr] not in window:
                window.add(s[ptr])
                ptr += 1

            substr_count += 1
            window = set()

        return substr_count
