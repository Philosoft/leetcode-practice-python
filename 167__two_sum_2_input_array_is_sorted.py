import unittest
from typing import List


class Solution(unittest.TestCase):
    def test_example_1(self):
        numbers = [2, 7, 11, 15]
        target = 9
        expected = [1, 2]

        self.assertEqual(expected, self.twoSum(numbers, target))

    def test_example_2(self):
        numbers = [2, 3, 4]
        target = 6
        expected = [1, 3]

        self.assertEqual(expected, self.twoSum(numbers, target))

    def test_example_3(self):
        numbers = [-1, 0]
        target = -1
        expected = [1, 2]

        self.assertEqual(expected, self.twoSum(numbers, target))

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_bound = 0
        while left_bound < len(numbers):
            left, right = left_bound + 1, len(numbers) - 1
            local_target = target - numbers[left_bound]

            while left <= right:
                mid = left + (right - left) // 2

                if numbers[mid] == local_target:
                    return [left_bound + 1, mid + 1]

                if numbers[mid] < local_target:
                    left = mid + 1
                else:
                    right = mid - 1

            left_bound += 1

        return [-1, -1]

    def twoSumTwoPointers(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            local_target = numbers[left] + numbers[right]

            if local_target == target:
                return [left + 1, right + 1]

            if local_target > target:
                right -= 1
            else:
                left += 1

        return [-1, -1]
