from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.best_index = -1
        self.best_length = float("inf")

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        root = TrieNode()

        # Initialize root with the globally best candidate
        for i, word in enumerate(wordsContainer):
            if len(word) < root.best_length or (
                len(word) == root.best_length and i < root.best_index
            ):
                root.best_length = len(word)
                root.best_index = i

        # Insert reversed words into Trie
        for i, word in enumerate(wordsContainer):
            node = root
            rev = word[::-1]
            for ch in rev:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
                # Update best candidate at this node
                if len(word) < node.best_length or (
                    len(word) == node.best_length and i < node.best_index
                ):
                    node.best_length = len(word)
                    node.best_index = i

        # Query processing
        ans = []
        for query in wordsQuery:
            node = root
            rev = query[::-1]
            best = root.best_index  # fallback to root's best
            for ch in rev:
                if ch not in node.children:
                    break
                node = node.children[ch]
                best = node.best_index
            ans.append(best)
        return ans
