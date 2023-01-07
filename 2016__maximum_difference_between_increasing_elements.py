import unittest
from typing import List


class Solution(unittest.TestCase):
    def test_example_1(self):
        nums = [7, 1, 5, 4]
        expected = 4
        self.assertEqual(expected, self.maximumDifference(nums))

    def test_example_2(self):
        nums = [9, 4, 3, 2]
        expected = -1
        self.assertEqual(expected, self.maximumDifference(nums))

    def test_example_3(self):
        nums = [1, 5, 2, 10]
        expected = 9
        self.assertEqual(expected, self.maximumDifference(nums))

    def test_a(self):
        nums = [999, 997, 980, 976, 948, 940, 938, 928, 924, 917, 907, 907, 881, 878, 864, 862, 859, 857, 848, 840, 824,
                824, 824, 805, 802, 798, 788, 777, 775, 766, 755, 748, 735, 732, 727, 705, 700, 697, 693, 679, 676, 644,
                634, 624, 599, 596, 588, 583, 562, 558, 553, 539, 537, 536, 509, 491, 485, 483, 454, 449, 438, 425, 403,
                368, 345, 327, 287, 285, 270, 263, 255, 248, 235, 234, 224, 221, 201, 189, 187, 183, 179, 168, 155, 153,
                150, 144, 107, 102, 102, 87, 80, 57, 55, 49, 48, 45, 26, 26, 23, 15]
        self.assertEqual(-1, self.maximumDifference(nums))

    def maximumDifference(self, nums: List[int]) -> int:
        left = nums[0]
        max_diff = 0
        for i in range(1, len(nums)):
            max_diff = max(max_diff, nums[i] - left)
            left = min(left, nums[i])

        return -1 if max_diff == 0 else max_diff

    def maximumDifferenceSliding(self, nums: List[int]) -> int:
        left, right = 0, 1
        max_diff = 0
        while left < right < len(nums):
            if nums[left] >= nums[right]:
                left += 1
            else:
                d = nums[right] - nums[left]
                if d > max_diff:
                    max_diff = d
                right += 1

            if left == right:
                right += 1

        return -1 if max_diff == 0 else max_diff

    def maximumDifferenceBrute(self, nums: List[int]) -> int:
        """
        brute force solution
        O(N ** 2)
        """
        diff = -1
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                d = nums[j] - nums[i]
                if d > 0 and d > diff:
                    diff = d

        return diff
