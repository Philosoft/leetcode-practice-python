"""
You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by
an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of
fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while
moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.

## Example 1

Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.

## Example 2

Input: fruits = [0,1,2,2]
Output: 3
Explanation:
    We can pick from trees [1,2,2].
    If we had started at the first tree, we would only pick from trees [0,1].

## Example 3

Input: fruits = [1,2,3,2,2]
Output: 4
Explanation:
    We can pick from trees [2,3,2,2].
    If we had started at the first tree, we would only pick from trees [1,2].

## Constraints

* 1 <= fruits.length <= 10^5
* 0 <= fruits[i] < fruits.length
"""

from collections import defaultdict
from typing import List
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        self.assertEqual(3, self.totalFruit([1, 2, 1]))

    def test_example_2(self):
        self.assertEqual(3, self.totalFruit([0, 1, 2, 2]))

    def totalFruit(self, fruits: List[int]) -> int:
        if len(fruits) <= 2:
            return len(fruits)

        m = 1
        window = defaultdict(int)
        window[fruits[0]] += 1
        left, right = 0, 1
        while right < len(fruits):
            while right < len(fruits) and (fruits[right] in window or len(window.keys()) < 2):
                window[fruits[right]] += 1
                right += 1
            # either array is over or we can't pick anymore
            # update max
            m = max(m, right - left)
            # shrink window, until only one type of fruits remain
            while left < right and len(window.keys()) == 2:
                window[fruits[left]] -= 1
                if window[fruits[left]] == 0:
                    del window[fruits[left]]
                left += 1

        return m
