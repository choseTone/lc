__author__ = 'wangqc'

import time

'''
139. Word Break

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be 
segmented into a space-separated sequence of one or more dictionary words.

Note:
The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.

Example 1:
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".

Example 3:
Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
'''

class Solution:
    def wordBreak(self, s, wordDict):
        # update a dp bool list, each element's index i indicates whether s[:i] can be segmented by words in wordDict
        # dp[0] being True means s[:0](empty string) can be mapped in wordDict; convert wordDict to hash table
        dp, words, n = [True], set(wordDict), len(s)
        for i in range(1, n+1):
            # if s[j:i] can be founded in wordDict and dp[j] is True(s[:j] can be segmented), s[:i] can be segmented
            dp.append(any(s[j:i] in words and dp[j] for j in range(i)))
        # check whether s[:n] or whole s can be segmented
        return dp[n]

if __name__ == '__main__':
    sol = Solution()
    t = time.time()
    ans = sol.wordBreak("applepenapple", ["apple", "pen"])
    # ans = sol.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"])
    print('ans: %s\ntime: %.2fms' % (ans, ((time.time() - t)) * 1000))