"""
You are playing the Bulls and Cows game with your friend.
You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you
provide a hint with the following info:

The number of "bulls", which are digits in the guess that are in the correct position.
The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position
Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both
secret and guess may contain duplicate digits.

## Example 1:

Input: secret = "1807", guess = "7810"
Output: "1A3B"
Explanation:

Buls: 8 (at index 1)
Cows: 7 (at index 0; should be at index 2), 1 (at index 2; should be at index 0) and 0 (at index 3; should be at 2)

## Example 2:

Input: secret = "1123", guess = "0111"
Output: "1A1B"

Note that only one of the two unmatched 1s is counted as a cow since the non-bull digits can only be rearranged to allow
one 1 to be a bull.

## Constraints:

* 1 <= secret.length, guess.length <= 1000
* secret.length == guess.length
* secret and guess consist of digits only.
"""
from collections import Counter
from typing import List
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        self.assertEqual("1A3B", self.getHint("1807", "7810"))

    def test_example_2(self):
        self.assertEqual("1A1B", self.getHint("1123", "0111"))

    def test_no_bulls(self):
        self.assertEqual("0A3B", self.getHint("1122", "2011"))

    def test_no_space_for_cows(self):
        self.assertEqual("2A0B", self.getHint("1122", "1111"))

    def getHint(self, secret: str, guess: str) -> str:
        correct_positions = 0
        incorrect_positions = 0

        counter = Counter(secret)
        probably_wrong_position: List[str] = []
        for i in range(len(secret)):
            if guess[i] == secret[i]:
                correct_positions += 1
                counter[guess[i]] -= 1
            elif guess[i] in counter:
                probably_wrong_position.append(guess[i])

        for letter in probably_wrong_position:
            if counter[letter] > 0:
                counter[letter] -= 1
                incorrect_positions += 1

        return f"{correct_positions}A{incorrect_positions}B"
