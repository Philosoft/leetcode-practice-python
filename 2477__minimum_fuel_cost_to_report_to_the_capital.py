from collections import defaultdict
from math import ceil
from typing import List
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        self.assertEqual(3, self.minimumFuelCost([[0, 1], [0, 2], [0, 3]], 5))

    def test_example_2(self):
        self.assertEqual(7, self.minimumFuelCost([[3, 1], [3, 2], [1, 0], [0, 4], [0, 5], [4, 6]], 2))

    def test_example_3(self):
        self.assertEqual(0, self.minimumFuelCost([], 1))

    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        adj = defaultdict(set)
        for src, dst in roads:
            adj[src].add(dst)
            adj[dst].add(src)

        total_fuel = 0

        def dfs(city: int, prev_city: int) -> int:
            nonlocal total_fuel

            passengers = 0
            for next_city in adj[city]:
                if next_city != prev_city:
                    passengers_from_children = dfs(next_city, city)
                    passengers += passengers_from_children
                    total_fuel += int(ceil(passengers_from_children / seats))
            return passengers + 1

        dfs(0, -1)
        return total_fuel
