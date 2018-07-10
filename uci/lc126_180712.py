__author__ = 'wangqc'

'''
126. Word Ladder II

Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from
beginWord to endWord, such that:
Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.

Note:
Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.

Example 1:
Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]
Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]

Example 2:
Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
Output: []
Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
'''
import collections
import string


class Solution:
    # use a begin set and a end set to build the word ladder from both sides
    # always build from the shorter set to save time for iteration
    def findLadders(self, beginWord, endWord, wordList):
        self.lower_letters = 'abcdefghijklmnopqrstuvwxyz'
        wordList, bset, eset, ladder, word_size = \
            set(wordList), {beginWord}, {endWord}, collections.defaultdict(list), len(beginWord)
        return self.construct(beginWord, endWord, ladder)\
            if endWord in wordList and self.search(bset, eset, ladder, True, wordList, word_size) else []

    def search(self, bset, eset, ladder, forward, wordList, word_size):
        if not bset: return False
        if len(bset) > len(eset):
            return self.search(eset, bset, ladder, not forward, wordList, word_size)
        found, cache, wordList = False, set(), set([i for i in wordList if i not in bset and i not in eset])
        for word in bset:
            for i in range(word_size):
                for c in self.lower_letters:
                    new_word = word[:i] + c + word[i+1:]
                    if new_word in eset:
                        found = True
                        self.add_path(ladder, word, new_word, forward)
                    elif new_word in wordList:
                        cache.add(new_word)
                        self.add_path(ladder, word, new_word, forward)
        return found or self.search(cache, eset, ladder, forward, wordList, word_size)

    def add_path(self, ladder, word, new_word, forward):
        return ladder[word].append(new_word) if forward else ladder[new_word].append(word)

    def construct(self, begin, end, ladder):
        return [[begin]] if begin == end \
            else [[begin] + rest for new in ladder[begin] for rest in self.construct(new, end, ladder)]


if __name__ == '__main__':
    from time import time

    sol = Solution()
    t = time()
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    ans = sol.findLadders("hit", "cog", wordList)
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))