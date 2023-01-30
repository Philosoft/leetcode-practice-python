"""
Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their
lexicographical order.

## Example 1

Input:
    words = ["i","love","leetcode","i","love","coding"]
    k = 2
Output:
    ["i","love"]
Explanation:
    "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.

## Example 2

Input:
    words = ["the","day","is","sunny","the","the","the","sunny","is","is"]
    k = 4
Output:
    ["the","is","sunny","day"]
Explanation:
    "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.

## Constraints

* 1 <= words.length <= 500
* 1 <= words[i].length <= 10
* words[i] consists of lowercase English letters.
* k is in the range [1, The number of unique words[i]]


## Follow-up

Could you solve it in O(n log(k)) time and O(n) extra space?
"""
from collections import defaultdict, Counter
from heapq import heappop, heapify
from typing import List
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        words = ["i", "love", "leetcode", "i", "love", "coding"]

        self.assertEqual(["i", "love"], self.topKFrequentDumbWay(words, 2))
        self.assertEqual(["i", "love"], self.topKFrequentHeapWay(words, 2))

    def test_example_2(self):
        words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
        k = 4
        expected = ["the", "is", "sunny", "day"]

        self.assertEqual(expected, self.topKFrequentDumbWay(words, k))
        self.assertEqual(expected, self.topKFrequentHeapWay(words, k))

    def topKFrequentHeapWay(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        heap = [(-freq, word) for word, freq in counter.items()]
        heapify(heap)

        return [heappop(heap)[1] for _ in range(k)]

    def topKFrequentDumbWay(self, words: List[str], k: int) -> List[str]:
        words.sort()
        word_count = defaultdict(int)
        for word in words:
            word_count[word] += 1

        count_to_words = defaultdict(set)
        for w, cnt in word_count.items():
            count_to_words[cnt].add(w)

        freqs = list(count_to_words.keys())
        freqs.sort(reverse=True)
        result = []
        size = 0
        for freq in freqs:
            for w in sorted(count_to_words[freq]):
                result.append(w)
                size += 1
                if size == k:
                    break
            if size == k:
                break

        return result
