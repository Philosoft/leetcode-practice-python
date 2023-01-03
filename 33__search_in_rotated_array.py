import unittest
from typing import List


class Solution(unittest.TestCase):
    def test_single_element_list(self):
        self.assertEqual(self.search([1], 1), 0)

    def test_not_in_single_element_list(self):
        self.assertEqual(self.search([1], 2), -1)

    def test_non_rotated_list_end(self):
        self.assertEqual(self.search([1, 2, 3, 4], 4), 3)

    def test_non_rotated_list_beginning(self):
        self.assertEqual(self.search([1, 2, 3, 4], 1), 0)

    def test_simple(self):
        self.assertEqual(self.search([4, 5, 6, 7, 0, 1, 2], 0), 4)

    def test_example_1(self):
        self.assertEqual(self.search([4, 5, 6, 7, 0, 1, 2], 0), 4)

    def test_example_2(self):
        self.assertEqual(self.search([4, 5, 6, 7, 0, 1, 2], 3), -1)

    def test_example_3(self):
        self.assertEqual(self.search([1], 0), -1)

    def test_half_rotate(self):
        self.assertEqual(self.search([3, 5, 1], 3), 0)

    def test_somthing(self):
        self.assertEqual(self.search([5, 1, 3], 3), 2)

    def test_edge(self):
        self.assertEqual(self.search([5, 1, 3], 5), 0)

    def test_target_on_the_right_of_pivot(self):
        self.assertEqual(self.search([3, 4, 5, 6, 1, 2], 2), 5)

    def test_sms(self):
        self.assertEqual(self.search([3, 4, 5, 6, 7, 1, 2], 4), 1)

    def test_aaaa(self):
        self.assertEqual(self.search([6, 7, 1, 2, 3, 4, 5], 6), 0)

    @staticmethod
    def search(nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            m = left + (right - left) // 2

            if nums[m] == target:
                return m

            if nums[left] <= nums[right]:
                # there is no pivot in this interval, proceed as usual
                if nums[m] < target:
                    left = m + 1
                else:
                    right = m - 1
            else:
                # there is a pivot inside interval
                # check if we hit max
                if m + 1 < len(nums) and nums[m + 1] < nums[m]:
                    # then everything else is smaller
                    # check intervals, choose accordingly and proceed as usual
                    if nums[left] <= target < nums[m]:
                        right = m - 1
                    else:
                        left = m + 1
                # check if we hit min
                elif m > 0 and nums[m - 1] > nums[m]:
                    # then everything else is bigger
                    # check intervals and choose accordingly
                    if nums[left] <= target <= nums[m - 1]:
                        right = m - 1
                    else:
                        left = m + 1
                else:
                    # then pivot is either to the left or to the right from here
                    if nums[left] < nums[m]:
                        # no pivot on the left
                        if nums[left] <= target < nums[m]:
                            # proceed without care in the world
                            right = m - 1
                        else:
                            left = m + 1
                    elif nums[m] < nums[right]:
                        # no pivot on the right
                        if nums[m] < target <= nums[right]:
                            # proceed without care in the world
                            left = m + 1
                        else:
                            right = m - 1

        return -1


print(Solution.search([5, 1, 3], 5))
