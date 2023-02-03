"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display
 his pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);


## Example 1

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

## Example 2

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I

## Example 3

Input: s = "A", numRows = 1
Output: "A"

## Constraints

* 1 <= s.length <= 1000
* s consists of English letters (lower-case and upper-case), ',' and '.'.
* 1 <= numRows <= 1000
"""
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        self.assertEqual("PAHNAPLSIIGYIR", self.convert("PAYPALISHIRING", 3))

    def convert(self, s: str, numRows: int) -> str:
        """
        to hell with this task
        """
        transform = []
        for _ in range(numRows):
            transform.append([""] * len(s))
        str_ptr = 0
        row, col = 0, 0
        while str_ptr < len(s):
            # row top -> bottom
            row = 0
            while row < numRows and str_ptr < len(s):
                transform[row][col] = s[str_ptr]
                row += 1
                str_ptr += 1

            # diagonal bottom -> top
            col += 1
            row -= 2
            while row > 0 and str_ptr < len(s):
                transform[row][col] = s[str_ptr]

                str_ptr += 1
                col += 1
                row -= 1

        result = []
        for row in transform:
            print(row)
            result.append("".join(row))

        return "".join(result)
