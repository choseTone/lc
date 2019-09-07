__author__ = 'wangqc'

# https://leetcode.com/problems/word-break-ii/


class Solution:
    def wordBreak(self, s, wordDict):
        N = len(s)
        words, memo = set(wordDict), {N: [""]}
        def dfs(i):
            if i not in memo:
                memo[i] = [s[i:j] + (rest and " "+rest)
                           for j in range(i+1,N+1) if s[i:j] in words
                           for rest in dfs(j)]
            return memo[i]
        return dfs(0)


if __name__ == '__main__':
    sol = Solution()

    t1 = "catsanddog", ["cat", "cats", "and", "sand", "dog"],
    print(sol.wordBreak(*t1))

    t2 = "pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"],
    print(sol.wordBreak(*t2))