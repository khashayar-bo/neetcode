class PrefixTree:

    def __init__(self):
        self.children = [None] * 26
        self.flag = False

    def insert(self, word: str) -> None:
        current_node = self
        for c in word:
            if not current_node.children[ord(c) - ord('a')]:
                current_node.children[ord(c) - ord('a')] = PrefixTree()
            current_node = current_node.children[ord(c) - ord('a')]
        
        current_node.flag = True

    def search(self, word: str) -> bool:
        current_node = self
        for c in word:
            alph_index = ord(c) - ord('a')
            if not current_node.children[alph_index]:
                return False
            current_node = current_node.children[alph_index]

        return current_node.flag

    def startsWith(self, prefix: str) -> bool:
        current_node = self
        for c in prefix:
            alph_index = ord(c) - ord('a')
            if not current_node.children[alph_index]:
                return False
            current_node = current_node.children[alph_index]

        return True
        