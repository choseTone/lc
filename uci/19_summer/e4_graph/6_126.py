__author__ = 'wangqc'

# https://leetcode.com/problems/word-ladder-ii/


from collections import defaultdict

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        tree, words, N = defaultdict(set), set(wordList), len(beginWord)
        if endWord not in words:
            return []

        def gen_nei_word(word):
            for i in range(len(word)):
                for c in "qwertyuiopasdfghjklzxcvbnm":
                    if c != word[i]:
                        candidate = word[:i] + c + word[i + 1:]
                        if candidate in words:
                            yield candidate

        begins, ends, done, rev = {beginWord}, {endWord}, False, False
        while begins and not done:
            if len(begins) > len(ends):
                begins, ends, rev = ends, begins, not rev
            words -= begins
            next_begins = set()
            for word in begins:
                for nei_word in gen_nei_word(word):
                    if nei_word in ends:
                        done = True
                    else:
                        next_begins.add(nei_word)
                    tree[nei_word].add(word) if rev else tree[word].add(nei_word)
            begins = next_begins

        def backtrack(word):
            return [[word]] if word==endWord else [[word]+rest for nei_word in tree[word] for rest in backtrack(nei_word)]

        return backtrack(beginWord)


if __name__ == '__main__':
    sol = Solution()

    t1 = "hit", "cog", ["hot","dot","dog","lot","log","cog"],
    print(sol.findLadders(*t1))

    t2 = "a", "c", ["a","b","c"],
    print(sol.findLadders(*t2))