"""
A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255
(inclusive) and cannot have leading zeros.

For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and
"192.168@1.1" are invalid IP addresses.
Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots
into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.

## Example 1:

Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]

## Example 2:

Input: s = "0000"
Output: ["0.0.0.0"]

## Example 3:

Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]

## Constraints:

* 1 <= s.length <= 20
* s consists of digits only.
"""
import ipaddress
from typing import List
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        expected = ["255.255.11.135", "255.255.111.35"]
        expected.sort()
        answer = self.restoreIpAddresses("25525511135")
        answer.sort()

        self.assertEqual(expected, answer)

    def test_tiny(self):
        self.assertEqual(["1.2.3.4"], self.restoreIpAddresses("1234"))

    def tet_example_2(self):
        self.assertEqual(["0.0.0.0"], self.restoreIpAddresses("0000"))

    def test_example_3(self):
        expected = ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]
        expected.sort()
        answer = self.restoreIpAddresses("101023")
        answer.sort()

        self.assertEqual(expected, answer)

    def test_empty_answer(self):
        for i in range(1, 4):
            with self.subTest(i):
                self.assertEqual([], self.restoreIpAddresses("1" * i))

    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) < 4:
            return []

        result = []

        option = []

        def is_correct_ip(ip: List[str]) -> bool:
            ipstring = "".join(ip)
            if ipstring.count(".") != 3:
                return False

            def is_octet_correct(octet: str):
                if len(octet) < 1 or len(octet) > 3:
                    return False

                if str(int(octet)) != octet:
                    return False

                if int(octet) > 255:
                    return False

                return True

            return all(map(is_octet_correct, ipstring.split(".")))

        def gen(ptr: int, dots_used: int):
            if ptr >= len(s):
                if is_correct_ip(option):
                    result.append("".join(option))
                return

            option.append(s[ptr])
            ptr += 1
            if dots_used < 3:
                option.append(".")
                gen(ptr, dots_used + 1)
                option.pop()
            gen(ptr, dots_used)
            option.pop()

        gen(0, 0)

        return result
