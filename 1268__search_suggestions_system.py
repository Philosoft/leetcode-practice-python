"""
You are given an array of strings products and a string searchWord.
Design a system that suggests at most three product names from products after each character of searchWord is typed.
Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix
return the three lexicographically minimums products.
Return a list of lists of the suggested products after each character of searchWord is typed.

## Example 1:

Input:
    products = ["mobile","mouse","moneypot","monitor","mousepad"]
    searchWord = "mouse"
Output:
    [
        ["mobile","moneypot","monitor"],
        ["mobile","moneypot","monitor"],
        ["mouse","mousepad"],
        ["mouse","mousepad"],
        ["mouse","mousepad"],
    ]
Explanation:
    products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"].
    After typing m and mo all products match and we show user ["mobile","moneypot","monitor"].
    After typing mou, mous and mouse the system suggests ["mouse","mousepad"].

## Example 2:

Input:
    products = ["havana"]
    searchWord = "havana"
Output:
    [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
Explanation:
    The only word "havana" will be always suggested while typing the search word.

## Constraints:

* 1 <= products.length <= 1000
* 1 <= products[i].length <= 3000
* 1 <= sum(products[i].length) <= 2 * 10^4
* All the strings of products are unique.
* products[i] consists of lowercase English letters.
* 1 <= searchWord.length <= 1000
* searchWord consists of lowercase English letters.
"""
from typing import List
from unittest import TestCase

from lib.Trie import Trie, TrieNode


class Solution(TestCase):
    def test_example_1(self):
        products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
        search_term = "mouse"
        expected = [
            ["mobile", "moneypot", "monitor"],
            ["mobile", "moneypot", "monitor"],
            ["mouse", "mousepad"],
            ["mouse", "mousepad"],
            ["mouse", "mousepad"],
        ]

        self.assertEqual(expected, self.suggestedProducts(products, search_term))
        self.assertEqual(expected, self.suggestedProductsTwoPointers(products, search_term))

    def test_example_2(self):
        products = ["havana"]
        search_term = "havana"
        expected = [["havana"], ["havana"], ["havana"], ["havana"], ["havana"], ["havana"]]

        self.assertEqual(expected, self.suggestedProducts(products, search_term))
        self.assertEqual(expected, self.suggestedProductsTwoPointers(products, search_term))

    def test_leetcode_8(self):
        products = ["bags","baggage","banner","box","cloths"]
        expected = [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]

        self.assertEqual(expected, self.suggestedProducts(products, "bags"))
        self.assertEqual(expected, self.suggestedProductsTwoPointers(products, "bags"))

    def suggestedProductsTwoPointers(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        left, right = 0, len(products) - 1
        results = []
        for ptr in range(len(searchWord)):
            while left <= right and (len(products[left]) <= ptr or products[left][ptr] != searchWord[ptr]):
                left += 1
            while left <= right and (len(products[right]) <= ptr or products[right][ptr] != searchWord[ptr]):
                right -= 1

            match = []
            for i in range(left, left + 3):
                if i < len(products) and i <= right:
                    match.append(products[i])

            results.append(match)

        return results

    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for product in sorted(products):
            trie.insert(product)

        subset: List[str] = []
        traced_word: List[str] = []

        def dfs(node: TrieNode, remaining_prefix: List[str]) -> None:
            if len(subset) == 3:
                return

            if not remaining_prefix:
                # nothing left to search - start collecting words
                if node.is_word:
                    subset.append("".join(traced_word))

                for child_char, child in node.children.items():
                    traced_word.append(child_char)
                    dfs(child, [])
                    traced_word.pop()

                return

            char = remaining_prefix[0]
            if char not in node.children:
                return

            traced_word.append(char)
            dfs(node.children[char], remaining_prefix[1:])
            traced_word.pop()

        result = []
        prefix = []
        for idx, char in enumerate(searchWord):
            prefix.append(char)
            subset = []
            dfs(trie.root, prefix)
            result.append(subset)
            if not subset:
                # that means there will be no more matches if we increase prefix
                for i in range(idx + 1, len(searchWord)):
                    result.append([])
                break

        return result
