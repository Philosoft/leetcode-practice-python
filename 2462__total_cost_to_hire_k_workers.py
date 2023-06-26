"""
LeetCode: https://leetcode.com/problems/total-cost-to-hire-k-workers/
"""
from heapq import heappush, heappop, heapify
from typing import List
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        self.assertEqual(11, self.totalCostOneHeap([17, 12, 10, 2, 7, 2, 11, 20, 8], 3, 4))
        self.assertEqual(11, self.totalCost([17, 12, 10, 2, 7, 2, 11, 20, 8], 3, 4))

    def test_example_2(self):
        self.assertEqual(4, self.totalCostOneHeap([1, 2, 4, 1], 3, 3))
        self.assertEqual(4, self.totalCost([1, 2, 4, 1], 3, 3))

    def test_case_46(self):
        self.assertEqual(
            423,
            self.totalCostOneHeap([31, 25, 72, 79, 74, 65, 84, 91, 18, 59, 27, 9, 81, 33, 17, 58], 11, 2)
        )
        self.assertEqual(
            423,
            self.totalCost([31, 25, 72, 79, 74, 65, 84, 91, 18, 59, 27, 9, 81, 33, 17, 58], 11, 2)
        )

    def totalCost(self, costs: List[int], k: int, n: int) -> int:
        total_cost = 0
        head_next, tail_next = n, len(costs) - 1 - n

        head = costs[:n]
        heapify(head)

        tail = costs[max(n, len(costs) - n):]
        heapify(tail)

        for _ in range(k):
            if head and tail:
                h, t = heappop(head), heappop(tail)
                if h <= t:
                    total_cost += h
                    if head_next <= tail_next:
                        heappush(head, costs[head_next])
                        head_next += 1
                    heappush(tail, t)
                else:
                    total_cost += t
                    if head_next <= tail_next:
                        heappush(tail, costs[tail_next])
                        tail_next -= 1
                    heappush(head, h)
            else:
                if head:
                    total_cost += heappop(head)
                    if head_next <= tail_next:
                        heappush(head, costs[head_next])
                        head_next += 1
                else:
                    total_cost += heappop(tail)
                    if head_next <= tail_next:
                        heappush(tail, costs[tail_next])
                        tail_next -= 1

        return total_cost

    def totalCostOneHeap(self, costs: List[int], k: int, candidates: int) -> int:
        total_cost = 0

        for _ in range(k):
            heap = []
            for idx, c in enumerate(costs):
                if idx < candidates or idx >= len(costs) - candidates:
                    heappush(heap, (c, idx))

            c_cost, c_idx = heappop(heap)
            stack = [(c_cost, c_idx)]
            while heap:
                tmp = heappop(heap)
                if tmp[0] > c_cost:
                    heappush(heap, tmp)
                    break

            possible_indexes = [idx for _, idx in stack]
            c_idx = min(possible_indexes)
            for pair in stack:
                if pair[1] != c_idx:
                    heappush(pair)
            total_cost += c_cost
            del costs[c_idx]

        return total_cost
