__author__ = 'wangqc'

# https://leetcode.com/problems/word-ladder/

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        words, N = set(wordList), len(beginWord)
        if endWord not in words:
            return 0

        def gen_nei_word(word):
            for i in range(N):
                for c in "qwertyuiopasdfghjklzxcvbnm":
                    if c != word[i]:
                        candidate = word[:i] + c + word[i + 1:]
                        if candidate in words:
                            yield candidate

        begins, ends, d, seen = {beginWord}, {endWord}, 2, {beginWord, endWord}
        while begins:
            if len(begins) > len(ends):
                begins, ends = ends, begins
            next_begins = set()
            for word in begins:
                for nei_word in gen_nei_word(word):
                    if nei_word in ends:
                        return d
                    if nei_word not in seen:
                        next_begins.add(nei_word)
                        seen.add(nei_word)
            begins, d = next_begins, d+1
        return 0


if __name__ == '__main__':
    sol = Solution()

    t1 = "hit", "cog", ["hot","dot","dog","lot","log","cog"],
    print(sol.ladderLength(*t1))

    t2 = "hit", "cog", ["hot","dot","dog","lot","log"],
    print(sol.ladderLength(*t2))