"""
There are n cars going to the same destination along a one-lane road. The destination is target miles away.

You are given two integer array position and speed, both of length n, where position[i] is the position of the ith car
and speed[i] is the speed of the ith car (in miles per hour).

A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper at the same speed.
The faster car will slow down to match the slower car's speed. The distance between these two cars is ignored (i.e.,
they are assumed to have the same position).

A car fleet is some non-empty set of cars driving at the same position and same speed. Note that a single car is also a
car fleet.

If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.

Return the number of car fleets that will arrive at the destination.

## Example 1

Input:
    target = 12
    position = [10,8,0,5,3]
    speed = [2,4,1,1,3]
Output: 3
Explanation:
    The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12.
    The car starting at 0 does not catch up to any other car, so it is a fleet by itself.
    The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6. The fleet moves at speed
    1 until it reaches target.
    Note that no other cars meet these fleets before the destination, so the answer is 3.

## Example 2

Input:
    target = 10
    position = [3]
    speed = [3]
Output: 1
Explanation: There is only one car, hence there is only one fleet.

## Example 3

Input:
    target = 100
    position = [0,2,4]
    speed = [4,2,1]
Output: 1
Explanation:
    The cars starting at 0 (speed 4) and 2 (speed 2) become a fleet, meeting each other at 4. The fleet moves at speed 2
    Then, the fleet (speed 2) and the car starting at 4 (speed 1) become one fleet, meeting each other at 6. The fleet
    moves at speed 1 until it reaches target.

## Constraints

* n == position.length == speed.length
* 1 <= n <= 10^5
* 0 < target <= 10^6
* 0 <= position[i] < target
* All the values of position are unique.
* 0 < speed[i] <= 10^6
"""

from dataclasses import dataclass
from typing import List
from unittest import TestCase


@dataclass
class Car:
    position: int
    speed: int

    def __lt__(self, other):
        return self.position < other.position

    def __gt__(self, other):
        return self.position > other.position

    def __eq__(self, other):
        return self.position == other.position


class Solution(TestCase):
    def test_example_1(self):
        target = 12
        position = [10, 8, 0, 5, 3]
        speed = [2, 4, 1, 1, 3]

        self.assertEqual(3, self.carFleet(target, position, speed))

    def test_example_2(self):
        target = 10
        position = [3]
        speed = [3]

        self.assertEqual(1, self.carFleet(target, position, speed))

    def test_example_3(self):
        target = 100
        position = [0, 2, 4]
        speed = [4, 2, 1]

        self.assertEqual(1, self.carFleet(target, position, speed))

    def test_same_speed(self):
        position = [8, 3, 7, 4, 6, 5]
        speed = [4, 4, 4, 4, 4, 4]
        target = 10

        self.assertEqual(6, self.carFleet(target, position, speed))

    def test_leetcode_34(self):
        position = [5, 26, 18, 25, 29, 21, 22, 12, 19, 6]
        speed = [7, 6, 6, 4, 3, 4, 9, 7, 6, 4]
        target = 31

        self.assertEqual(6, self.carFleet(target, position, speed))

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[pos, spd] for pos, spd in zip(position, speed)]
        stack = []
        for car in reversed(sorted(pairs)):
            time_to_target = (target - car[0]) / car[1] # (destination - position) / speed
            stack.append(time_to_target)
            if len(stack) > 1:
                if stack[-1] <= stack[-2]:
                    stack.pop()

        return len(stack)

    def carFleetSimulation(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        ⚠️ does not pass test case #34
        """
        cars: List[Car] = []

        for i in range(len(position)):
            cars.append(Car(position[i], speed[i]))

        # sort cars by position -> create implicit stack
        cars.sort()

        fleet_count = 0
        while cars:
            # simulate passage of 1 unit of time
            # move cars towards the target to min(cur.pos + cur.speed, next.pos)
            car_in_front = Car(cars[-1].position + 1 + cars[-1].speed, 0)
            for ptr in range(len(cars) - 1, -1, -1):
                current_car = cars[ptr]

                current_car.position = min(current_car.position + current_car.speed, car_in_front.position)
                car_in_front = current_car

            # remove fleet, that reached the target at this time
            prev_position = cars[-1].position + 1
            if cars[-1].position >= target:
                while cars and cars[-1].position >= target:
                    if cars[-1].position != prev_position:
                        fleet_count += 1
                    prev_position = cars[-1].position
                    cars.pop()

        return fleet_count
