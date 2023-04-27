"""
LeetCode: https://leetcode.com/problems/asteroid-collision/

We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning
right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both
are the same size, both will explode. Two asteroids moving in the same direction will never meet.

## Example 1

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

## Example 2

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.

## Example 3

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.

## Constraints

* 2 <= asteroids.length <= 10^4
* -1000 <= asteroids[i] <= 1000
* asteroids[i] != 0
"""
from typing import List
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        self.assertEqual([5, 10], self.asteroidCollision([5, 10, -5]))

    def test_example_2(self):
        self.assertEqual([], self.asteroidCollision([8, -8]))

    def test_example_3(self):
        self.assertEqual([10], self.asteroidCollision([10, 2, -5]))

    def test_case_143(self):
        self.assertEqual([-2, -1, 1, 2], self.asteroidCollision([-2, -1, 1, 2]))

    def test_case_249(self):
        self.assertEqual([-2, -2, -2], self.asteroidCollision([-2, -2, 1, -2]))

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result = []
        for a in asteroids:
            if not result:
                result.append(a)
            else:
                if (result[-1] < 0 and a < 0) or (result[-1] > 0 and a > 0) or (result[-1] < 0 < a):
                    result.append(a)
                # collision
                else:
                    new_one = a
                    while result and (result[-1] * new_one < 0):
                        if abs(result[-1]) < abs(new_one):
                            result.pop()
                        elif abs(result[-1]) > abs(new_one):
                            new_one = 0
                        else:
                            new_one = 0
                            result.pop()
                    if new_one != 0:
                        result.append(new_one)

        return result
