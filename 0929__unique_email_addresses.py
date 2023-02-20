"""
LeetCode: https://leetcode.com/problems/unique-email-addresses/description/

Every valid email consists of a local name and a domain name, separated by the '@' sign. Besides lowercase letters, the
 email may contain one or more '.' or '+'.

For example, in "alice@leetcode.com", "alice" is the local name, and "leetcode.com" is the domain name.
If you add periods '.' between some characters in the local name part of an email address, mail sent there will be
forwarded to the same address without dots in the local name. Note that this rule does not apply to domain names.

For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.
If you add a plus '+' in the local name, everything after the first plus sign will be ignored. This allows certain
emails to be filtered. Note that this rule does not apply to domain names.

For example, "m.y+name@email.com" will be forwarded to "my@email.com".
It is possible to use both of these rules at the same time.

Given an array of strings emails where we send one email to each emails[i], return the number of different addresses
that actually receive mails.

## Example 1

Input: emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
Output: 2
Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails.

## Example 2

Input: emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
Output: 3

## Constraints

* 1 <= emails.length <= 100
* 1 <= emails[i].length <= 100
* emails[i] consist of lowercase English letters, '+', '.' and '@'.
* Each emails[i] contains exactly one '@' character.
* All local and domain names are non-empty.
* Local names do not start with a '+' character.
* Domain names end with the ".com" suffix.
"""
from typing import List
from unittest import TestCase


class State:
    LOCAL: str = 'local'
    SKIP_UNTIL_DOMAIN: str = 'local-skip'
    DOMAIN: str = 'domain'


class Solution(TestCase):
    def test_example_1(self):
        emails = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]

        self.assertEqual(2, self.numUniqueEmails(emails))

    def test_example_2(self):
        self.assertEqual(3, self.numUniqueEmails(["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]))

    def test_more(self):
        self.assertEqual(1, self.numUniqueEmails(["test.email+alex@leetcode.com", "test.email@leetcode.com"]))

    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        for email in emails:
            buf = []
            state = State.LOCAL
            for char in email:
                if state == State.LOCAL:
                    if char == ".":
                        pass
                    elif char == "+":
                        state = State.SKIP_UNTIL_DOMAIN
                    elif char == "@":
                        buf.append(char)
                        state = State.DOMAIN
                    else:
                        buf.append(char)
                elif state == State.SKIP_UNTIL_DOMAIN:
                    if char == "@":
                        state = State.DOMAIN
                        buf.append("@")
                if state == State.DOMAIN:
                    buf.append(char)

            unique.add("".join(buf))

        return len(unique)
