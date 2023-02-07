"""
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise.
word may contain dots '.' where dots can be matched with any letter.

## Example:

Input:
    ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
    [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
    [null,null,null,null,false,true,true,true]

## Explanation
    WordDictionary wordDictionary = new WordDictionary();
    wordDictionary.addWord("bad");
    wordDictionary.addWord("dad");
    wordDictionary.addWord("mad");
    wordDictionary.search("pad"); // return False
    wordDictionary.search("bad"); // return True
    wordDictionary.search(".ad"); // return True
    wordDictionary.search("b.."); // return True

## Constraints:

* 1 <= word.length <= 25
* word in addWord consists of lowercase English letters.
* word in search consist of '.' or lowercase English letters.
* There will be at most 3 dots in word for search queries.
* At most 10^4 calls will be made to addWord and search.
"""

from dataclasses import dataclass, field
from typing import Dict, List
from unittest import TestCase


@dataclass
class TrieNode:
    children: Dict[str, 'TrieNode'] = field(default_factory=dict)
    is_word: bool = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        ptr = self.root
        for char in word:
            if char not in ptr.children:
                ptr.children[char] = TrieNode()
            ptr = ptr.children[char]
        ptr.is_word = True

    def search(self, word: str) -> bool:
        def dfs(node: TrieNode, remainder: List[str]):
            if not remainder:
                return node.is_word

            char = remainder[0]
            if char != '.':
                if char not in node.children:
                    return False
                return dfs(node.children[char], remainder[1:])

            for child in node.children.values():
                result = dfs(child, remainder[1:])
                if result:
                    return True
            return False

        return dfs(self.root, list(word))

    def startsWith(self, prefix: str) -> bool:
        ptr = self.root
        for char in prefix:
            if char not in ptr.children:
                return False
            ptr = ptr.children[char]
        return True


class TestDictionary(TestCase):
    def test_it(self):
        wd = WordDictionary()
        wd.addWord("bad")
        wd.addWord("dad")
        wd.addWord("mad")
        self.assertFalse(wd.search("pad"))
        self.assertTrue(wd.search("bad"))
        self.assertTrue(wd.search(".ad"))
        self.assertTrue(wd.search("b.."))

    def test_further(self):
        wd = WordDictionary()

        wd.addWord("a")
        wd.addWord("ab")

        self.assertTrue(wd.search("a"))
        self.assertTrue(wd.search("a."))
        self.assertTrue(wd.search("ab"))

        self.assertFalse(wd.search(".a"))
        self.assertTrue(wd.search(".b"))
        self.assertFalse(wd.search("ab."))
        self.assertTrue(wd.search("."))
        self.assertTrue(wd.search(".."))
