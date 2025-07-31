class WordDictionary:

    def __init__(self):
        self.trie = {}
        

    def addWord(self, word: str) -> None:
        node = self.trie  # Start from the root of the Trie
        for char in word:
            if char not in node:
                node[char] = {}  # Create a new dictionary if the character is not present
            node = node[char]  # Move to the next level in the Trie
        node['#'] = True

    def search(self, word: str) -> bool:
         return self._search_in_node(word, self.trie)
    def _search_in_node(self, word: str, node: dict) -> bool:
        for i, char in enumerate(word):
            if char == '.':
                # If the character is a dot, try all possible branches
                for child in node.values():
                    if isinstance(child, dict):  # Ensure we're iterating over a dictionary node
                        if self._search_in_node(word[i+1:], child):
                            return True
                return False  # No valid match found for any child
            else:
                # If it's a regular character, check if it exists in the current node
                if char not in node:
                    return False
                node = node[char]  # Move to the next level in the Trie
        return '#' in node 
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)