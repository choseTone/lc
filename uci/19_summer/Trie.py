class Trie:

    def __init__(self):
        self.T = [[0] * 27]

    def insert(self, word: str) -> None:
        i = 0
        for c in word:
            if not self.T[i][ord(c) - 97]:
                self.T[i][ord(c) - 97] = len(self.T)
                self.T.append([0] * 27)
            i = self.T[i][ord(c) - 97]
        self.T[i][26] = 1

    def match(self, word, prefix) -> bool:
        i = 0
        for c in word:
            if not (i := self.T[i][ord(c) - 97]):
                return False
        return prefix or bool(self.T[i][26])

    def search(self, word: str) -> bool:
        return self.match(word, False)

    def startsWith(self, prefix: str) -> bool:
        return self.match(prefix, True)



if __name__ == '__main__':
    trie = Trie()
    print(trie.insert("apple"))
    print(trie.search("apple"))
    print(trie.search("app"))
    print(trie.startsWith("app"))
    print(trie.insert("app"))
    print(trie.search("app"))