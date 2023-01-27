from dataclasses import dataclass, field
from typing import Dict
from unittest import TestCase


@dataclass
class TrieNode:
    children: Dict[str, 'TrieNode'] = field(default_factory=dict)
    is_word: bool = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        ptr = self.root
        for char in word:
            if char not in ptr.children:
                ptr.children[char] = TrieNode()
            ptr = ptr.children[char]
        ptr.is_word = True

    def search(self, word: str) -> bool:
        ptr = self.root
        for char in word:
            if char not in ptr.children:
                return False
            ptr = ptr.children[char]
        return ptr.is_word

    def startsWith(self, prefix: str) -> bool:
        ptr = self.root
        for char in prefix:
            if char not in ptr.children:
                return False
            ptr = ptr.children[char]
        return True


class TestTrie(TestCase):
    def test_it(self):
        trie = Trie()
        trie.insert("apple")
        self.assertTrue(trie.search("apple"))
        self.assertFalse(trie.search("app"))
        self.assertTrue(trie.startsWith("app"))
        trie.insert("app")
        self.assertTrue(trie.search("app"))
