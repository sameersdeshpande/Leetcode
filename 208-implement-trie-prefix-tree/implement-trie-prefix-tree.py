class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.endOfWord = True
    def search(self, word: str) -> bool:
        node = self._search_node(word)
        return node is not None and node.endOfWord
    def startsWith(self, prefix: str) -> bool:
        node = self._search_node(prefix)
        return node is not None
    def _search_node(self,word:str) -> TrieNode:
        node = self.root
        for char in word:
            if char not in node.children:
                return None
            node = node.children[char]
        return node
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)