__author__ = 'wangqc'

import collections, itertools


class Solution(object):
    def wordBreak(self, s, wordDict):
        n, wset = len(s), set(wordDict)
        dp = [True] + [False] * n
        for j in range(1, n+1):
            for i in range(j):
                if dp[i] and s[i:j] in wset:
                    dp[j] = True
                    break
        return dp[-1]




