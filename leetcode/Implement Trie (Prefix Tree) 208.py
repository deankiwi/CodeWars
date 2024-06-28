
import bisect


import bisect


class Trie:

    def __init__(self):
        self.words = set()
        self.ordered = []

    def insert(self, word: str) -> None:
        if word not in self.words:
            self.words.add(word)
            self.ordered.append(word)
            self.ordered.sort()

    def search(self, word: str) -> bool:
        if word in self.words:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        if self.ordered:
            i = bisect.bisect_left(self.ordered, prefix)
            print(f'{i = }')
            word_left = self.ordered[min(i, len(self.ordered) - 1)]
            word_right = self.ordered[min(i + 1, len(self.ordered) - 1)]

            if word_left.startswith(prefix) or word_right.startswith(prefix):
                return True
        return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


'''
Faster solution. 

have a tree which starts with the letter of word then have connecting letters
note isEnd to show it is the end of work

class TrieNode:
    def __init__(self):
        # Stores children nodes and whether node is the end of a word
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        # Insert character by character into trie
        for c in word:
            # if character path does not exist, create it
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isEnd = True
        

    def search(self, word: str) -> bool:
        cur = self.root
        # Search character by character in trie
        for c in word:
            # if character path does not exist, return False
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.isEnd
        

    def startsWith(self, prefix: str) -> bool:
        # Same as search, except there is no isEnd condition at final return
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
'''

