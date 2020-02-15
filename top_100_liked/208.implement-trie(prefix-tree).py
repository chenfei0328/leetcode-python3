class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur_node = self.root
        for s in word:
            if s not in cur_node:
                cur_node[s] = {}
            cur_node = cur_node[s]
        cur_node['*'] = {}

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur_node = self.root
        for s in word:
            if s not in cur_node:
                return False
            cur_node = cur_node[s]
        return '*' in cur_node 

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur_node = self.root
        for s in prefix:
            if s not in cur_node:
                return False
            cur_node = cur_node[s]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)