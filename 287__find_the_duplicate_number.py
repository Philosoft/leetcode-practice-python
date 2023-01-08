import unittest
from typing import List


class Solution(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(2, self.findDuplicate([1, 3, 4, 2, 2]))

    def test_example_2(self):
        self.assertEqual(3, self.findDuplicate([3, 1, 3, 4, 2]))

    def test_example_3(self):
        self.assertEqual(4, self.findDuplicate([4, 3, 1, 4, 2]))

    def test_example_4(self):
        self.assertEqual(9, self.findDuplicate([2, 5, 9, 6, 9, 3, 8, 9, 7, 1]))

    def findDuplicate(self, nums: List[int]) -> int:
        fast, slow = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if fast == slow:
                break

        slow2 = 0
        while slow != slow2:
            slow2 = nums[slow2]
            slow = nums[slow]

        return slow
