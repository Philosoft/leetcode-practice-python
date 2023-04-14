"""
LeetCode: https://leetcode.com/problems/task-scheduler/

Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task.
Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete
either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter
in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.

## Example 1

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation:

A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.

## Example 2

Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation:

On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.

## Example 3

Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation:

One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A


## Constraints

* 1 <= task.length <= 10^4
* tasks[i] is upper-case English letter.
* The integer n is in the range [0, 100]
"""
from collections import Counter, deque
from heapq import heapify, heappop, heappush
from typing import List, Deque, Tuple
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        self.assertEqual(8, self.leastInterval(["A", "A", "A", "B", "B", "B"], 2))

    def test_example_2(self):
        self.assertEqual(6, self.leastInterval(["A", "A", "A", "B", "B", "B"], 0))

    def test_example_3(self):
        self.assertEqual(16, self.leastInterval(["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2))

    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)

        heap = [-freq for freq in Counter(tasks).values()]
        heapify(heap)
        q: Deque[Tuple[int, int]] = deque()  # elements in the form of Tuple[freq, time_when_it_is_possible_to_run]
        required_time = 0
        while heap or q:
            required_time += 1
            if heap:
                freq = heappop(heap)
                freq += 1
                if freq != 0:
                    # there are still tasks left
                    q.append((freq, required_time + n))
            if q and q[0][1] == required_time:
                heappush(heap, q.popleft()[0])

        return required_time
