__author__ = 'wangqc'

'''
127. Word Ladder

Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation 
sequence from beginWord to endWord, such that:
Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.

Example 1:
Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Example 2:
Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
'''


class Solution:
    # use a begin set and a end set to build the word ladder from both sides
    # always build from the shorter set to save time for iteration
    def ladderLength(self, beginWord, endWord, wordList):
        lower_letters = 'abcdefghijklmnopqrstuvwxyz'
        wordList = set(wordList)
        if endWord not in wordList: return 0
        ans, word_size, bset, eset = 2, len(beginWord), {beginWord}, {endWord}
        while bset and eset:
            if len(bset) > len(eset):
                bset, eset = eset, bset
            cache = set()
            for word in bset:
                for i in range(word_size):
                    for c in lower_letters:
                        new_word = word[:i] + c + word[i+1:]
                        if new_word in eset:
                            return ans
                        if new_word in wordList:
                            wordList.remove(new_word)
                            cache.add(new_word)
            bset = cache
            ans += 1
        return ans


if __name__ == '__main__':
    from time import time

    sol = Solution()
    t = time()
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    ans = sol.ladderLength("hit", "cog", wordList)
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))