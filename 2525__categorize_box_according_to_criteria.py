import unittest


class Solution(unittest.TestCase):
    """
    Example 1:

Input: length = 1000, width = 35, height = 700, mass = 300
Output: "Heavy"
Explanation:
None of the dimensions of the box is greater or equal to 104.
Its volume = 24500000 <= 109. So it cannot be categorized as "Bulky".
However mass >= 100, so the box is "Heavy".
Since the box is not "Bulky" but "Heavy", we return "Heavy".
Example 2:

Input: length = 200, width = 50, height = 800, mass = 50
Output: "Neither"
Explanation:
None of the dimensions of the box is greater or equal to 104.
Its volume = 8 * 106 <= 109. So it cannot be categorized as "Bulky".
Its mass is also less than 100, so it cannot be categorized as "Heavy" either.
Since its neither of the two above categories, we return "Neither".
    """
    def test_example_1(self):
        self.assertEqual('Heavy', self.categorizeBox(1000, 35, 700, 300))

    def test_example_2(self):
        self.assertEqual('Neither', self.categorizeBox(200, 50, 800, 50))

    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        is_bulky, is_heavy = False, False
        if length >= 10 ** 4 or width >= 10 ** 4 or height >= 10 ** 4 or length * width * height >= 10 ** 9:
            is_bulky = True

        if mass >= 100:
            is_heavy = True

        if is_bulky and is_heavy:
            return 'Both'

        if not is_bulky and not is_heavy:
            return 'Neither'

        return 'Bulky' if is_bulky else 'Heavy'
"""
The box is "Bulky" if:
    Any of the dimensions of the box is greater or equal to 104.
    Or, the volume of the box is greater or equal to 109.
    
If the mass of the box is greater or equal to 100, it is "Heavy".

If the box is both "Bulky" and "Heavy", then its category is "Both".
If the box is neither "Bulky" nor "Heavy", then its category is "Neither".

If the box is "Bulky" but not "Heavy", then its category is "Bulky".
If the box is "Heavy" but not "Bulky", then its category is "Heavy".
"""
