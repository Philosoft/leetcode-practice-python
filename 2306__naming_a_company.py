"""
LeetCode link https://leetcode.com/problems/naming-a-company/

You are given an array of strings ideas that represents a list of names to be used in the process of naming a company.
The process of naming a company is as follows:

* Choose 2 distinct names from ideas, call them ideaA and ideaB.
* Swap the first letters of ideaA and ideaB with each other.
* If both of the new names are not found in the original ideas, then the name ideaA ideaB (the concatenation of ideaA and ideaB, separated by a space) is a valid company name.
* Otherwise, it is not a valid name.
* Return the number of distinct valid names for the company.

## Example 1

Input:
```
ideas = ["coffee","donuts","time","toffee"]
```

Output:
```6```

Explanation:

The following selections are valid:
- ("coffee", "donuts"): The company name created is "doffee conuts".
- ("donuts", "coffee"): The company name created is "conuts doffee".
- ("donuts", "time"): The company name created is "tonuts dime".
- ("donuts", "toffee"): The company name created is "tonuts doffee".
- ("time", "donuts"): The company name created is "dime tonuts".
- ("toffee", "donuts"): The company name created is "doffee tonuts".

Therefore, there are a total of 6 distinct company names.

The following are some examples of invalid selections:

- ("coffee", "time"): The name "toffee" formed after swapping already exists in the original array.
- ("time", "toffee"): Both names are still the same after swapping and exist in the original array.
- ("coffee", "toffee"): Both names formed after swapping already exist in the original array.

## Example 2

Input:
```ideas = ["lack","back"]```

Output: ```0```

Explanation: There are no valid selections. Therefore, 0 is returned.

## Constraints

* 2 <= ideas.length <= 5 * 10^4
* 1 <= ideas[i].length <= 10
* ideas[i] consists of lowercase English letters.
* All the strings in ideas are unique.
"""
from collections import defaultdict
from typing import List
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        self.assertEqual(6, self.distinctNames(["coffee", "donuts", "time", "toffee"]))

    def test_example_2(self):
        self.assertEqual(0, self.distinctNames(["lack", "back"]))

    def distinctNames(self, ideas: List[str]) -> int:
        letter_to_suffix = defaultdict(set)
        for idea in ideas:
            letter_to_suffix[idea[0]].add(idea[1:])

        result = 0
        for lchar, lsuf in letter_to_suffix.items():
            for rchar, rsuf in letter_to_suffix.items():
                if rchar == lchar:
                    continue

                same = len(lsuf & rsuf)
                # I by myself was to stupid to come up with this instead of real word concat
                # and result hashset 🤦‍♂️
                result += (len(lsuf) - same) * (len(rsuf) - same)

        return result
