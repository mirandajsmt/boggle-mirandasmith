import typing
from typing import Optional, Dict
from collections.abc import Iterator

from py_boggle.boggle_dictionary import BoggleDictionary


class TrieNode:
    """
    Our TrieNode class. Feel free to add new properties/functions, but 
    DO NOT edit the names of the given properties (children and is_word).
    """
    def __init__(self):
        self.children : Dict[str, TrieNode] = {} # maps a child letter to its TrieNode class
        self.is_word = False # whether or not this Node is a valid word ending


class TrieDictionary(BoggleDictionary):
    """
    Your implementation of BoggleDictionary.
    Several functions have been filled in for you from our solution, but you are free to change their implementations.
    Do NOT change the name of self.root, as our autograder will manually traverse using self.root
    """

    def __init__(self):
        self.root : TrieNode = TrieNode()

    def load_dictionary(self, filename: str) -> None:
        # Remember to add every word to the trie, not just the words over some length.
        with open(filename) as wordsfile:
            for line in wordsfile:
                word = line.strip().upper()
                if not word:
                    continue # skip empty lines

                current_node = self.root # start at the root

                for letter in word:
                    if letter not in current_node.children:
                        current_node.children[letter] = TrieNode()
                    current_node = current_node.children[letter]

                current_node.is_word = True # mark the end of the word

    def traverse(self, prefix: str) -> Optional[TrieNode]:
        """
        Traverse will traverse the Trie down a given path of letters `prefix`.
        If there is ever a missing child node, then returns None.
        Otherwise, returns the TrieNode referenced by `prefix`.
        """
        current_node = self.root
        prefix = prefix.upper()
        for letter in prefix:
            if letter not in current_node.children:
                return None
            current_node = current_node.children[letter]
        return current_node

    def is_prefix(self, prefix: str) -> bool:
        if self.traverse(prefix.upper()) is not None:
            return True
        return False

    def contains(self, word: str) -> bool:
        node = self.traverse(word.upper())
        if node is not None and node.is_word:
            return True
        return False

    def __iter__(self) -> typing.Iterator[str]:
        """Returns an iterator that iterates through all words in the TrieDictionary in alphabetical order."""
        def dfs(node: TrieNode, prefix: str) -> Iterator[str]:
            if node.is_word:
                yield prefix
            for letter in sorted(node.children.keys()):
                yield from dfs(node.children[letter], prefix + letter)

        return dfs(self.root, "")