__author__ = 'wangqc'

'''
208. Implement Trie (Prefix Tree)

Implement a trie with insert, search, and startsWith methods.

Example:
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true

Note:
You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
'''


class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word):
        node = self.root
        for c in word:
            node = node.setdefault(c, {})
        node['$'] = None


    def search(self, word):
        node = self.root
        for c in word:
            node = node.get(c)
            if not node: return False
        return '$' in node


    def startsWith(self, prefix):
        node = self.root
        for c in prefix:
            node = node.get(c)
            if not node: return False
        return True


if __name__ == '__main__':

    obj = Trie()
    print(obj.insert("apple"))
    print(obj.search("apple"))
    print(obj.search("app"))
    print(obj.startsWith("app"))
    print(obj.insert("app"))
    print(obj.search("app"))

