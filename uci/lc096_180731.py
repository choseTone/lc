__author__ = 'wangqc'

'''
96. Unique Binary Search Trees

Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:
Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''


class Solution:
    # dp[n] = dp[0]*dp[n-1](0 as root) + dp[1]*dp[n-2](1 as root) + ... + dp[n-1]*dp[0](n as root)
    def numTrees(self, n):
        dp = [1, 1] + [0] * (n-1)
        for i in range(1, n):
            for j in range(i+1):
                dp[i+1] += dp[j] * dp[i-j]
        return dp[n]



if __name__ == '__main__':
    from time import time

    sol = Solution()
    t = time()
    ans = sol.numTrees(3)
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))
