__author__ = 'wangqc'

'''
72. Edit Distance

Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.
You have the following 3 operations permitted on a word:
Insert a character
Delete a character
Replace a character

Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
'''


class Solution:
    def minDistance(self, word1, word2):
        l1, l2 = len(word1), len(word2)
        if not l1 or not l2: return l1 or l2
        d = [[-1] * l2 for _ in range(l1)]
        def bt(i, j):
            if i < 0: return j + 1
            if j < 0: return i + 1
            if d[i][j] == -1:
                d[i][j] = bt(i-1, j-1) if word1[i] == word2[j] else min(bt(i-1, j-1), bt(i, j-1), bt(i-1, j)) + 1
            return d[i][j]
        return bt(l1-1, l2-1)


if __name__ == '__main__':
    from time import time

    sol = Solution()

    t = time()
    ans = sol.minDistance("horse", "ros")
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))

