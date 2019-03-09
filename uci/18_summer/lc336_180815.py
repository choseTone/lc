__author__ = 'wangqc'

'''
336. Palindrome Pairs

Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, so that the concatenation of 
the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:
Input: ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]] 
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]

Example 2:
Input: ["bat","tab","cat"]
Output: [[0,1],[1,0]] 
Explanation: The palindromes are ["battab","tabbat"]
'''


import collections

class Solution:
    def palindromePairs(self, words):
        rev, ans = collections.defaultdict(int), []
        for i, word in enumerate(words):
            rev[word[::-1]] = i
        for i, word in enumerate(words):
            if word == "":
                for k, v in rev.items():
                    if k and k == k[::-1]:
                        ans.append([i, v])
            for j in range(len(word)):
                prefix, suffix = word[:j], word[j:]
                if prefix in rev and suffix == suffix[::-1] and i != rev[prefix]:
                    ans.append([i, rev[prefix]])
                if suffix in rev and prefix == prefix[::-1] and i != rev[suffix]:
                    ans.append([rev[suffix], i])
        return ans


if __name__ == '__main__':
    from time import time

    sol = Solution()

    t = time()
    ans = sol.palindromePairs(["abcd","dcba","lls","s","sssll"])
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))

